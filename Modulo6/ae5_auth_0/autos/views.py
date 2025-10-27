from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AutomovilForm
from django.shortcuts import render, redirect
from .forms import AutomovilForm
from .models import Automovil

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def crear_auto(request):
    if request.method == 'POST':
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autos')
    else:
        form = AutomovilForm()
    return render(request, 'crear_auto.html', {'form': form})


@login_required(login_url='login')
def lista_autos(request):
    autos = Automovil.objects.all()
    return render(request, 'home.html', {'autos': autos})


def home(request):
    autos = Automovil.objects.all()
    return render(request, 'home.html', {'autos': autos})