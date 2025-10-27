from django.shortcuts import render, redirect
from .models import Automovil
from .forms import AutomovilModelForm

def lista_automoviles(request):
    autos = Automovil.objects.all()
    return render(request, "lista.html", {"autos": autos})

def crear_automovil(request):
    """
    Vista para crear un nuevo automóvil desde un formulario.
    Maneja tanto la presentación del formulario como el procesamiento de datos.
    """
    if request.method == 'POST':
        form = AutomovilModelForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo automóvil en la base de datos
            return redirect('lista_automoviles')  # Redirige a la lista de autos
    else:
        form = AutomovilModelForm()  # Formulario vacío para GET

    return render(request, 'crear_automovil.html', {'form': form})
