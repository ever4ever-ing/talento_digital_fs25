from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .models import Evento

# Create your views here.

class LoginView(View):
    def get(self, request):
        # Si ya está autenticado, redirigir a la lista de eventos
        if request.user.is_authenticated:
            return redirect('lista_eventos')
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'✓ ¡Bienvenido, {user.username}!')
            # Redirigir a la página que intentaba acceder o a la lista de eventos
            next_url = request.GET.get('next', 'lista_eventos')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, '✓ Has cerrado sesión exitosamente.')
        return redirect('lista_eventos')

class ListaEventos(ListView):
    model = Evento
    template_name = 'list_eventos.html'
    context_object_name = 'eventos'
    
class MisEventos(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'mis_eventos.html'
    context_object_name = 'eventos'
    login_url = '/login/'  # URL personalizada de login
    redirect_field_name = 'next'  # Parámetro para redirigir después del login
    
    def dispatch(self, request, *args, **kwargs):
        # Verificar si el usuario no está autenticado
        if not request.user.is_authenticated:
            messages.warning(request, '⚠️ Debes iniciar sesión para ver tus eventos.')
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        # Solo muestra eventos del usuario logueado
        return Evento.objects.filter(autor=self.request.user)