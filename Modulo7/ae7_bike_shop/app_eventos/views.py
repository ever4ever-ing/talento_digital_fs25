from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Evento, Inscripcion
from app_clientes.models import Cliente


def lista_eventos(request):
    """
    Mostrar todos los eventos activos y disponibles.
    """
    # Filtrar eventos activos y futuros
    eventos = Evento.objects.filter(
        activo=True,
        fecha_hora__gte=timezone.now()
    ).order_by('fecha_hora')
    
    # Filtros opcionales
    tipo_filter = request.GET.get('tipo')
    dificultad_filter = request.GET.get('dificultad')
    
    if tipo_filter:
        eventos = eventos.filter(tipo_evento=tipo_filter)
    
    if dificultad_filter:
        eventos = eventos.filter(dificultad=dificultad_filter)
    
    context = {
        'eventos': eventos,
        'tipo_filter': tipo_filter,
        'dificultad_filter': dificultad_filter,
    }
    return render(request, 'eventos/lista_eventos.html', context)


def detalle_evento(request, evento_id):
    """
    Mostrar detalles de un evento específico.
    """
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Verificar si el usuario ya está inscrito
    ya_inscrito = False
    if request.user.is_authenticated:
        try:
            cliente = Cliente.objects.get(email=request.user.email)
            ya_inscrito = Inscripcion.objects.filter(
                evento=evento,
                cliente=cliente
            ).exclude(estado='cancelada').exists()
        except Cliente.DoesNotExist:
            pass
    
    context = {
        'evento': evento,
        'ya_inscrito': ya_inscrito,
    }
    return render(request, 'eventos/detalle_evento.html', context)


@login_required
def inscribirse_evento(request, evento_id):
    """
    Inscribir al usuario en un evento.
    """
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Verificar que el evento esté disponible
    if not evento.puede_inscribirse():
        messages.error(request, '⚠️ Este evento no está disponible para inscripción.')
        return redirect('detalle_evento', evento_id=evento_id)
    
    # Obtener o crear cliente
    try:
        cliente = Cliente.objects.get(email=request.user.email)
    except Cliente.DoesNotExist:
        cliente = Cliente.objects.create(
            nombre=request.user.get_full_name() or request.user.username,
            email=request.user.email
        )
    
    # Verificar si ya está inscrito
    if Inscripcion.objects.filter(evento=evento, cliente=cliente).exclude(estado='cancelada').exists():
        messages.warning(request, '⚠️ Ya estás inscrito en este evento.')
        return redirect('detalle_evento', evento_id=evento_id)
    
    if request.method == 'POST':
        num_personas = int(request.POST.get('num_personas', 1))
        contacto_emergencia = request.POST.get('contacto_emergencia', '')
        telefono_emergencia = request.POST.get('telefono_emergencia', '')
        observaciones = request.POST.get('observaciones', '')
        
        # Verificar cupos disponibles
        if evento.cupo_disponible < num_personas:
            messages.error(
                request,
                f'⚠️ No hay suficientes cupos. Solo quedan {evento.cupo_disponible} cupos disponibles.'
            )
            return redirect('detalle_evento', evento_id=evento_id)
        
        # Crear inscripción
        total = evento.precio * num_personas
        inscripcion = Inscripcion.objects.create(
            evento=evento,
            cliente=cliente,
            num_personas=num_personas,
            contacto_emergencia=contacto_emergencia,
            telefono_emergencia=telefono_emergencia,
            observaciones=observaciones,
            estado='confirmada',
            total_pagado=total
        )
        
        messages.success(
            request,
            f'✅ ¡Inscripción exitosa! Te esperamos en {evento.nombre}. Total: ${total}'
        )
        return redirect('mis_inscripciones')
    
    context = {
        'evento': evento,
    }
    return render(request, 'eventos/inscribirse.html', context)


@login_required
def mis_inscripciones(request):
    """
    Mostrar las inscripciones del usuario actual.
    """
    try:
        cliente = Cliente.objects.get(email=request.user.email)
        inscripciones = Inscripcion.objects.filter(
            cliente=cliente
        ).select_related('evento').order_by('-fecha_inscripcion')
    except Cliente.DoesNotExist:
        inscripciones = []
        messages.info(request, 'ℹ️ Aún no tienes inscripciones a eventos.')
    
    context = {
        'inscripciones': inscripciones,
    }
    return render(request, 'eventos/mis_inscripciones.html', context)


@login_required
def cancelar_inscripcion(request, inscripcion_id):
    """
    Cancelar una inscripción.
    """
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    
    # Verificar que sea del usuario actual
    if inscripcion.cliente.email != request.user.email:
        messages.error(request, '⚠️ No tienes permiso para cancelar esta inscripción.')
        return redirect('mis_inscripciones')
    
    # Verificar que no sea un evento pasado
    if inscripcion.evento.evento_pasado():
        messages.error(request, '⚠️ No puedes cancelar un evento que ya pasó.')
        return redirect('mis_inscripciones')
    
    if inscripcion.estado != 'cancelada':
        inscripcion.cancelar()
        messages.success(
            request,
            f'✅ Inscripción a {inscripcion.evento.nombre} cancelada. Los cupos han sido liberados.'
        )
    else:
        messages.info(request, 'ℹ️ Esta inscripción ya estaba cancelada.')
    
    return redirect('mis_inscripciones')
