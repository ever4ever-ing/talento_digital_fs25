from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from .models import Evento
from .forms import EventoForm

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


class CrearEvento(LoginRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'crear_evento.html'
    success_url = reverse_lazy('mis_eventos')
    login_url = '/login/'
    
    def form_valid(self, form):
        # Asignar automáticamente el usuario actual como autor del evento
        form.instance.autor = self.request.user
        
        # Mensaje de éxito
        messages.success(self.request, f'✓ Evento "{form.instance.titulo}" creado exitosamente.')
        
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        # Mensaje informativo si el usuario no está autenticado
        if not request.user.is_authenticated:
            messages.warning(request, '⚠️ Debes iniciar sesión para crear eventos.')
        return super().dispatch(request, *args, **kwargs)
    

class EditarEvento(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'editar_evento.html'
    permission_required = 'app_eventos.change_evento'
    success_url = reverse_lazy('mis_eventos')
    login_url = '/login/'
    context_object_name = 'evento'
    
    def get_queryset(self):
        # Solo permite editar eventos del usuario autenticado
        return Evento.objects.filter(autor=self.request.user)
    
    def form_valid(self, form):
        # Mensaje de éxito
        messages.success(self.request, '✓ Evento actualizado exitosamente.')
        return super().form_valid(form)


class EliminarEvento(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Evento
    template_name = 'eliminar_evento.html'
    permission_required = 'app_eventos.delete_evento'
    success_url = reverse_lazy('mis_eventos')
    login_url = '/login/'
    context_object_name = 'evento'
    
    def get_queryset(self):
        # Solo permite eliminar eventos del usuario autenticado
        return Evento.objects.filter(autor=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        # Guardar el título del evento antes de eliminarlo
        evento = self.get_object()
        titulo_evento = evento.titulo
        
        # Mensaje de éxito
        messages.success(request, f'✓ El evento "{titulo_evento}" ha sido eliminado exitosamente.')
        
        return super().delete(request, *args, **kwargs)