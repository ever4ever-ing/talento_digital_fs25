from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import AutomovilForm
from .models import Automovil


# -----------------------
# VISTA DE LOGIN
# -----------------------
def login_view(request):
    """
    Vista para autenticar usuarios.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_automoviles')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')


# -----------------------
# VISTA DE LOGOUT
# -----------------------
@login_required
def logout_view(request):
    """
    Cierra la sesión y redirige al login.
    """
    logout(request)
    return redirect('login')


# -----------------------
# LISTADO DE AUTOS (protegido)
# -----------------------
@login_required
def lista_automoviles(request):
    # recuperar autos desde la base de datos
    autos = Automovil.objects.all()
    contexto = {
        'autos': autos
    }
    return render(request, 'lista.html', contexto)


# -----------------------
# CREAR AUTOMOVIL (protegido con permiso)
# -----------------------
@login_required
@permission_required('app_autos.add_automovil', raise_exception=True)
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