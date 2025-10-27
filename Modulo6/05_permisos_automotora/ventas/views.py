from django.shortcuts import render, redirect
from .forms import AutomovilForm
from .models import Automovil  # Importar el modelo aquí para evitar problemas circulares
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('ventas.add_automovil', raise_exception=True)
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

@login_required
def lista_automoviles(request):
    """
    Vista para listar todos los automóviles disponibles.
    Recupera los datos de la base de datos y los pasa al template.
    """
    automoviles = Automovil.objects.all()  # Recupera todos los automóviles
    
    return render(request, 'index.html', {'automoviles': automoviles})
