from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Count
from app_bicicletas.models import Bicicleta
from .models import Resena
from .forms import ResenaForm


def detalle_bicicleta_con_resenas(request, pk):
    """
    Vista para ver el detalle de una bicicleta con sus reseñas
    """
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    resenas = bicicleta.resenas.all()
    
    # Calcular estadísticas
    stats = bicicleta.resenas.aggregate(
        promedio=Avg('puntuacion'),
        total=Count('id')
    )
    
    # Verificar si el usuario ya dejó reseña
    usuario_ya_reseno = False
    resena_usuario = None
    if request.user.is_authenticated:
        try:
            resena_usuario = Resena.objects.get(bicicleta=bicicleta, usuario=request.user)
            usuario_ya_reseno = True
        except Resena.DoesNotExist:
            pass
    
    context = {
        'bicicleta': bicicleta,
        'resenas': resenas,
        'promedio': stats['promedio'],
        'total_resenas': stats['total'],
        'usuario_ya_reseno': usuario_ya_reseno,
        'resena_usuario': resena_usuario
    }
    
    return render(request, 'resenas/detalle_bicicleta.html', context)


@login_required(login_url='login')
def crear_resena(request, bicicleta_id):
    """
    Vista para crear una nueva reseña
    Solo usuarios autenticados pueden crear reseñas
    """
    bicicleta = get_object_or_404(Bicicleta, pk=bicicleta_id)
    
    # Verificar si el usuario ya dejó una reseña
    if Resena.objects.filter(bicicleta=bicicleta, usuario=request.user).exists():
        messages.warning(request, 'Ya has dejado una reseña para esta bicicleta.')
        return redirect('detalle_bicicleta', pk=bicicleta_id)
    
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.bicicleta = bicicleta
            resena.usuario = request.user
            resena.save()
            messages.success(request, '¡Gracias por tu reseña! 🌟')
            return redirect('detalle_bicicleta', pk=bicicleta_id)
    else:
        form = ResenaForm()
    
    return render(request, 'resenas/crear_resena.html', {
        'form': form,
        'bicicleta': bicicleta
    })


@login_required(login_url='login')
def editar_resena(request, pk):
    """
    Vista para editar una reseña existente
    Solo el autor puede editar su propia reseña
    """
    resena = get_object_or_404(Resena, pk=pk)
    
    # Verificar que el usuario sea el autor
    if resena.usuario != request.user:
        messages.error(request, 'No puedes editar una reseña que no es tuya.')
        return redirect('detalle_bicicleta', pk=resena.bicicleta.pk)
    
    if request.method == 'POST':
        form = ResenaForm(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reseña actualizada correctamente.')
            return redirect('detalle_bicicleta', pk=resena.bicicleta.pk)
    else:
        form = ResenaForm(instance=resena)
    
    return render(request, 'resenas/editar_resena.html', {
        'form': form,
        'resena': resena,
        'bicicleta': resena.bicicleta
    })


@login_required(login_url='login')
def eliminar_resena(request, pk):
    """
    Vista para eliminar una reseña
    Solo el autor puede eliminar su propia reseña
    """
    resena = get_object_or_404(Resena, pk=pk)
    
    # Verificar que el usuario sea el autor
    if resena.usuario != request.user:
        messages.error(request, 'No puedes eliminar una reseña que no es tuya.')
        return redirect('detalle_bicicleta', pk=resena.bicicleta.pk)
    
    bicicleta_id = resena.bicicleta.pk
    resena.delete()
    messages.success(request, 'Reseña eliminada correctamente.')
    return redirect('detalle_bicicleta', pk=bicicleta_id)


def mis_resenas(request):
    """
    Vista para ver todas las reseñas del usuario autenticado
    """
    if not request.user.is_authenticated:
        return redirect('login')
    
    resenas = Resena.objects.filter(usuario=request.user)
    
    return render(request, 'resenas/mis_resenas.html', {
        'resenas': resenas
    })
