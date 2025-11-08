from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Evento
from .forms import EventoForm

# Create your views here.

# Mixin personalizado para verificar que el usuario es el autor del evento
class AutorRequeridoMixin(UserPassesTestMixin):
    """
    Mixin que verifica que el usuario autenticado sea el autor del evento.
    Maneja correctamente el caso cuando el evento no existe.
    """
    raise_exception = False  # Para poder redirigir en lugar de mostrar 403/404
    
    def test_func(self):
        """
        Verifica que el evento existe y pertenece al usuario actual.
        """
        try:
            evento = self.get_object()
            return evento.autor == self.request.user
        except Exception:
            return False
    
    def handle_no_permission(self):
        """
        Maneja cuando el evento no existe o no pertenece al usuario.
        """
        try:
            evento = self.get_object()
            messages.error(self.request, '🚫 No tienes permiso para realizar esta acción en este evento.')
        except Exception:
            messages.error(self.request, '🚫 El evento que buscas no existe o no tienes acceso a él.')
        
        return redirect('acceso_denegado')


# Mixin personalizado para manejo de permisos con mensajes
class PermissionDeniedMixin:
    """
    Mixin para manejar errores de permisos con mensajes personalizados
    """
    permission_denied_message = "No tienes permisos para realizar esta acción."
    
    def handle_no_permission(self):
        """
        Maneja el caso cuando el usuario no tiene permisos
        """
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request, f'🚫 {self.permission_denied_message}')
            return redirect('acceso_denegado')
        
        messages.warning(self.request, '⚠️ Debes iniciar sesión para acceder a esta página.')
        return redirect(f"{self.get_login_url()}?next={self.request.path}")


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


class AccesoDenegadoView(TemplateView):
    template_name = '403.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = self.request.GET.get('mensaje', 'No tienes permisos suficientes.')
        return context


def custom_permission_denied_view(request, exception=None):
    """
    Vista personalizada para manejar errores 403 (Permiso Denegado)
    """
    from django.shortcuts import render
    messages.error(request, '🚫 Acceso denegado. No tienes permisos para acceder a este recurso.')
    return render(request, '403.html', status=403)


def custom_page_not_found_view(request, exception=None):
    """
    Vista personalizada para manejar errores 404 (Página no encontrada)
    """
    from django.shortcuts import render
    messages.warning(request, '⚠️ La página o evento que buscas no fue encontrado.')
    return render(request, '404.html', status=404)


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
    

class EditarEvento(AutorRequeridoMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'editar_evento.html'
    permission_required = 'app_eventos.change_evento'
    success_url = reverse_lazy('mis_eventos')
    login_url = '/login/'
    context_object_name = 'evento'
    raise_exception = False  # Para que redirija en lugar de lanzar excepción 403
    
    def handle_no_permission(self):
        """
        Maneja cuando el usuario no tiene permisos.
        Se llama por LoginRequiredMixin o PermissionRequiredMixin.
        """
        if not self.request.user.is_authenticated:
            messages.warning(self.request, '⚠️ Debes iniciar sesión para editar eventos.')
            return redirect(f"{self.login_url}?next={self.request.path}")
        
        messages.error(self.request, '🚫 No tienes los permisos necesarios para editar eventos.')
        return redirect('acceso_denegado')
    
    def form_valid(self, form):
        messages.success(self.request, '✓ Evento actualizado exitosamente.')
        return super().form_valid(form)


class EliminarEvento(AutorRequeridoMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Evento
    template_name = 'eliminar_evento.html'
    permission_required = 'app_eventos.delete_evento'
    success_url = reverse_lazy('mis_eventos')
    login_url = '/login/'
    context_object_name = 'evento'
    raise_exception = False  # Para que redirija en lugar de lanzar excepción 403
    
    def handle_no_permission(self):
        """
        Maneja cuando el usuario no tiene permisos.
        Se llama por LoginRequiredMixin o PermissionRequiredMixin.
        """
        if not self.request.user.is_authenticated:
            messages.warning(self.request, '⚠️ Debes iniciar sesión para eliminar eventos.')
            return redirect(f"{self.login_url}?next={self.request.path}")
        
        messages.error(self.request, '🚫 No tienes los permisos necesarios para eliminar eventos.')
        return redirect('acceso_denegado')
    
    def delete(self, request, *args, **kwargs):
        evento = self.get_object()
        titulo_evento = evento.titulo
        messages.success(request, f'✓ El evento "{titulo_evento}" ha sido eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class UnirseEventoView(LoginRequiredMixin, View):
    """
    Vista para unirse o salirse de un evento
    """
    login_url = '/login/'
    
    def post(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        
        if request.user in evento.participantes.all():
            # El usuario ya está inscrito, lo removemos
            evento.participantes.remove(request.user)
            messages.success(request, f'✓ Te has retirado del evento "{evento.titulo}".')
        else:
            # El usuario no está inscrito, lo agregamos
            evento.participantes.add(request.user)
            messages.success(request, f'✓ Te has unido al evento "{evento.titulo}"!')
        
        # Redirigir a la página anterior o a la lista de eventos
        return redirect(request.META.get('HTTP_REFERER', 'lista_eventos'))


class ParticipantesEventoView(LoginRequiredMixin, TemplateView):
    """
    Vista para mostrar todos los participantes de un evento
    """
    template_name = 'participantes_evento.html'
    login_url = '/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evento_id = self.kwargs.get('pk')
        evento = get_object_or_404(Evento, pk=evento_id)
        
        # Verificar que el usuario sea el autor del evento
        if evento.autor != self.request.user:
            messages.warning(self.request, '⚠️ Solo el autor puede ver la lista completa de participantes.')
            return redirect('lista_eventos')
        
        context['evento'] = evento
        context['participantes'] = evento.participantes.all()
        return context


class UnirseEvento(LoginRequiredMixin, View):
    """
    Vista para que un usuario se una o salga de un evento.
    Toggle: si está participando lo remueve, si no está lo agrega.
    """
    login_url = '/login/'
    
    def post(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        user = request.user
        
        if evento.esta_participando(user):
            # El usuario ya está participando, lo removemos
            evento.participantes.remove(user)
            messages.success(request, f'✓ Ya no participas en "{evento.titulo}".')
        else:
            # El usuario no está participando, lo agregamos
            evento.participantes.add(user)
            messages.success(request, f'✓ ¡Te has unido a "{evento.titulo}"!')
        
        # Redirigir a la página anterior o a la lista de eventos
        return redirect(request.META.get('HTTP_REFERER', 'lista_eventos'))


class UnirseEventoView(LoginRequiredMixin, View):
    """
    Vista para que un usuario se una a un evento
    """
    login_url = '/login/'
    
    def post(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        
        # Verificar que el usuario no sea el autor
        if evento.autor == request.user:
            messages.warning(request, '⚠️ Eres el organizador de este evento.')
            return redirect('lista_eventos')
        
        # Verificar si ya está participando
        if evento.esta_participando(request.user):
            messages.info(request, 'ℹ️ Ya estás participando en este evento.')
        else:
            evento.participantes.add(request.user)
            messages.success(request, f'✓ Te has unido al evento "{evento.titulo}" exitosamente.')
        
        return redirect('lista_eventos')


class SalirseEventoView(LoginRequiredMixin, View):
    """
    Vista para que un usuario se salga de un evento
    """
    login_url = '/login/'
    
    def post(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        
        # Verificar si está participando
        if evento.esta_participando(request.user):
            evento.participantes.remove(request.user)
            messages.success(request, f'✓ Te has salido del evento "{evento.titulo}".')
        else:
            messages.warning(request, '⚠️ No estás participando en este evento.')
        
        return redirect('lista_eventos')


class ParticipantesEventoView(TemplateView):
    """
    Vista para mostrar la lista de participantes de un evento
    """
    template_name = 'participantes_evento.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evento = get_object_or_404(Evento, pk=self.kwargs['pk'])
        context['evento'] = evento
        context['participantes'] = evento.participantes.all().order_by('username')
        return context