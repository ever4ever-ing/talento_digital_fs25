from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AutomovilForm
from .models import Automovil

def lista_automoviles(request):
    #recuperar autos desde la base de datos
    autos = Automovil.objects.all()
    contexto = {
        'autos': autos
    }
    return render(request, 'lista.html', contexto)

def crear_automovil(request):
    """
    Vista para crear un nuevo automóvil desde un formulario.
    Maneja tanto la presentación del formulario como el procesamiento de datos.
    """
    if request.method == 'POST':
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo automóvil en la base de datos
            return redirect('lista_automoviles')  # Redirige a la lista de autos
    else:
        form = AutomovilForm()  # Formulario vacío para GET
    
    return render(request, 'crear_automovil.html', {'form': form})