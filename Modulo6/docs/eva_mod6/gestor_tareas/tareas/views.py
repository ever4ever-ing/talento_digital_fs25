from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import TareaForm

# Almacenamiento en memoria - Diccionario por usuario
tareas_por_usuario = {}
contador_id = 0

def obtener_tareas_usuario(user_id):
    """Obtiene las tareas del usuario o crea una lista vacía si no existe"""
    if user_id not in tareas_por_usuario:
        tareas_por_usuario[user_id] = []
    return tareas_por_usuario[user_id]

@login_required
def lista_tareas(request):
    """Vista para mostrar todas las tareas del usuario autenticado"""
    tareas = obtener_tareas_usuario(request.user.id)
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, tarea_id):
    """Vista para mostrar los detalles de una tarea específica"""
    tareas = obtener_tareas_usuario(request.user.id)
    
    # Buscar la tarea por ID
    tarea = None
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    
    if not tarea:
        raise Http404("La tarea no existe")
    
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

@login_required
def agregar_tarea(request):
    """Vista para agregar una nueva tarea"""
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            global contador_id
            contador_id += 1
            
            nueva_tarea = {
                'id': contador_id,
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'usuario_id': request.user.id
            }
            
            tareas = obtener_tareas_usuario(request.user.id)
            tareas.append(nueva_tarea)
            
            messages.success(request, 'Tarea agregada exitosamente.')
            return redirect('tareas:lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'tareas/agregar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    """Vista para eliminar una tarea existente"""
    tareas = obtener_tareas_usuario(request.user.id)
    
    # Buscar y eliminar la tarea
    tarea_eliminada = False
    for i, tarea in enumerate(tareas):
        if tarea['id'] == tarea_id:
            del tareas[i]
            tarea_eliminada = True
            break
    
    if tarea_eliminada:
        messages.success(request, 'Tarea eliminada exitosamente.')
    else:
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
