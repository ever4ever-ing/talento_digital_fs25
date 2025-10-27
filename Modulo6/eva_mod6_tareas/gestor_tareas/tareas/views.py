from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import TareaForm, TareaModelForm
from .models import Tarea
from django.contrib.auth import logout

@login_required
def lista_tareas(request):
    """Vista para mostrar todas las tareas del usuario autenticado"""
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, tarea_id):
    """Vista para mostrar los detalles de una tarea específica"""
    try:
        tarea = Tarea.objects.get(pk=tarea_id, usuario=request.user)
    except Tarea.DoesNotExist:
        raise Http404("La tarea no existe")

    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

@login_required
def agregar_tarea(request):
    """Vista para agregar una nueva tarea"""
    if request.method == 'POST':
        form = TareaModelForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            messages.success(request, 'Tarea agregada exitosamente.')
            return redirect('tareas:lista_tareas')
    else:
        form = TareaModelForm()

    return render(request, 'tareas/agregar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    """Vista para eliminar una tarea existente"""
    try:
        tarea = Tarea.objects.get(pk=tarea_id, usuario=request.user)
        tarea.delete()
        messages.success(request, 'Tarea eliminada exitosamente.')
    except Tarea.DoesNotExist:
        messages.error(request, 'No se pudo eliminar la tarea.')

    return redirect('tareas:lista_tareas')

def registro(request):
    """Vista para registrar nuevos usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('tareas:lista_tareas')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def cerrar_sesion(request):
    """Cerrar la sesión del usuario y redirigir al formulario de login."""
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('login')