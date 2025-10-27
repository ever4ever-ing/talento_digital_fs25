from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Receta
from .forms import ContactoForm

def inicio(request):
    """Vista para la página de inicio con las últimas 6 recetas"""
    recetas = Receta.objects.all()[:6]
    context = {
        'recetas': recetas
    }
    return render(request, 'inicio.html', context)

def lista_recetas(request):
    """Vista para mostrar todas las recetas"""
    recetas = Receta.objects.all()
    context = {
        'recetas': recetas
    }
    return render(request, 'lista_recetas.html', context)

def detalle_receta(request, pk):
    """Vista para mostrar el detalle de una receta individual"""
    try:
        receta = get_object_or_404(Receta, pk=pk)
        context = {
            'receta': receta
        }
        return render(request, 'detalle_receta.html', context)
    except:
        # Si la receta no existe, mostrar página 404
        return render(request, '404.html', status=404)

def contacto(request):
    """Vista para el formulario de contacto"""
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Aquí podrías procesar el formulario (enviar email, guardar en BD, etc.)
            # Por ahora solo redirigimos a la página de confirmación
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('recetas:confirmacion_contacto')
        else:
            messages.warning(request, 'Por favor, completa todos los campos correctamente.')
    else:
        form = ContactoForm()
    
    context = {
        'form': form
    }
    return render(request, 'contacto.html', context)

def confirmacion_contacto(request):
    """Vista para la página de confirmación después de enviar el contacto"""
    return render(request, 'confirmacion_contacto.html')

# Vista personalizada para errores 404
def handler404(request, exception):
    return render(request, '404.html', status=404)
