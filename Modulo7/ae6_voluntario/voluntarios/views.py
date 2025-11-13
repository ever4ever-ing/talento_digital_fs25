from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Voluntario, Evento


# ==================== VISTAS PRINCIPALES ====================

def index(request):
    """Vista principal que muestra el dashboard"""
    voluntarios = Voluntario.objects.all()
    eventos = Evento.objects.all()
    
    context = {
        'total_voluntarios': voluntarios.count(),
        'total_eventos': eventos.count(),
        'voluntarios_recientes': voluntarios[:5],
        'proximos_eventos': eventos[:5],
    }
    return render(request, 'index.html', context)


# ==================== VISTAS DE VOLUNTARIOS ====================

def lista_voluntarios(request):
    """Lista todos los voluntarios registrados"""
    voluntarios = Voluntario.objects.all()
    return render(request, 'voluntarios/lista.html', {'voluntarios': voluntarios})


def detalle_voluntario(request, pk):
    """Muestra el detalle de un voluntario específico"""
    voluntario = get_object_or_404(Voluntario, pk=pk)
    return render(request, 'voluntarios/detalle.html', {'voluntario': voluntario})


def crear_voluntario(request):
    """Crea un nuevo voluntario"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono', '')
        
        try:
            Voluntario.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono
            )
            messages.success(request, f'Voluntario {nombre} creado exitosamente.')
            return redirect('lista_voluntarios')
        except Exception as e:
            messages.error(request, f'Error al crear voluntario: {str(e)}')
    
    return render(request, 'voluntarios/crear.html')


def editar_voluntario(request, pk):
    """Edita un voluntario existente"""
    voluntario = get_object_or_404(Voluntario, pk=pk)
    
    if request.method == 'POST':
        voluntario.nombre = request.POST.get('nombre')
        voluntario.email = request.POST.get('email')
        voluntario.telefono = request.POST.get('telefono', '')
        
        try:
            voluntario.save()
            messages.success(request, f'Voluntario {voluntario.nombre} actualizado exitosamente.')
            return redirect('detalle_voluntario', pk=voluntario.pk)
        except Exception as e:
            messages.error(request, f'Error al actualizar voluntario: {str(e)}')
    
    return render(request, 'voluntarios/editar.html', {'voluntario': voluntario})


def eliminar_voluntario(request, pk):
    """Elimina un voluntario"""
    voluntario = get_object_or_404(Voluntario, pk=pk)
    
    if request.method == 'POST':
        nombre = voluntario.nombre
        voluntario.delete()
        messages.success(request, f'Voluntario {nombre} eliminado exitosamente.')
        return redirect('lista_voluntarios')
    
    return render(request, 'voluntarios/eliminar.html', {'voluntario': voluntario})


# ==================== VISTAS DE EVENTOS ====================

def lista_eventos(request):
    """Lista todos los eventos"""
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista.html', {'eventos': eventos})


def detalle_evento(request, pk):
    """Muestra el detalle de un evento específico"""
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/detalle.html', {'evento': evento})


def crear_evento(request):
    """Crea un nuevo evento"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        
        try:
            evento = Evento.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha=fecha
            )
            messages.success(request, f'Evento "{titulo}" creado exitosamente.')
            return redirect('detalle_evento', pk=evento.pk)
        except Exception as e:
            messages.error(request, f'Error al crear evento: {str(e)}')
    
    return render(request, 'eventos/crear.html')


def editar_evento(request, pk):
    """Edita un evento existente"""
    evento = get_object_or_404(Evento, pk=pk)
    
    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.descripcion = request.POST.get('descripcion')
        evento.fecha = request.POST.get('fecha')
        
        try:
            evento.save()
            messages.success(request, f'Evento "{evento.titulo}" actualizado exitosamente.')
            return redirect('detalle_evento', pk=evento.pk)
        except Exception as e:
            messages.error(request, f'Error al actualizar evento: {str(e)}')
    
    return render(request, 'eventos/editar.html', {'evento': evento})


def eliminar_evento(request, pk):
    """Elimina un evento"""
    evento = get_object_or_404(Evento, pk=pk)
    
    if request.method == 'POST':
        titulo = evento.titulo
        evento.delete()
        messages.success(request, f'Evento "{titulo}" eliminado exitosamente.')
        return redirect('lista_eventos')
    
    return render(request, 'eventos/eliminar.html', {'evento': evento})


# ==================== ASIGNACIÓN DE VOLUNTARIOS A EVENTOS ====================

def asignar_voluntario(request, evento_pk):
    """Asigna voluntarios a un evento"""
    evento = get_object_or_404(Evento, pk=evento_pk)
    
    if request.method == 'POST':
        voluntario_ids = request.POST.getlist('voluntarios')
        evento.voluntarios.set(voluntario_ids)
        messages.success(request, f'Voluntarios asignados al evento "{evento.titulo}" exitosamente.')
        return redirect('detalle_evento', pk=evento.pk)
    
    voluntarios = Voluntario.objects.all()
    voluntarios_asignados = evento.voluntarios.all()
    
    context = {
        'evento': evento,
        'voluntarios': voluntarios,
        'voluntarios_asignados': voluntarios_asignados,
    }
    return render(request, 'eventos/asignar_voluntarios.html', context)
