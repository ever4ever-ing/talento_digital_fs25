from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import Automovil
from .forms import AutomovilForm

@login_required
def lista_automoviles(request):
    #recuperar autos desde la base de datos
    autos = Automovil.objects.all()
    contexto = {
        'autos': autos
    }
    return render(request, 'lista.html', contexto)

@login_required
@permission_required('concesionaria.add_auto', raise_exception=True)
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


def login_view(request):
    """
    Vista para autenticar usuarios.
    Esta vista se agrega porque antes no existía funcionalidad de login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige al listado de autos tras login exitoso
            return redirect('lista_automoviles')
    # Si GET o credenciales incorrectas, se muestra formulario de login
    return render(request, 'login.html')

@login_required
def logout_view(request):
    """
    Vista para cerrar sesión.
    Se agrega porque anteriormente no existía forma de salir de la sesión.
    """
    logout(request)
    # Tras logout, vuelve al login
    return redirect('login')

