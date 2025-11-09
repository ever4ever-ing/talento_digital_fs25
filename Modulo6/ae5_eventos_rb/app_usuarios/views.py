from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import RegistroForm, PerfilForm


class RegistroView(CreateView):
    """
    Vista para registro de nuevos usuarios.
    Usa el formulario RegistroForm que extiende UserCreationForm.
    
    Funcionalidad:
    - Valida datos del formulario
    - Crea nuevo usuario en la base de datos
    - Inicia sesión automáticamente después del registro
    - Redirige al listado de eventos
    """
    form_class = RegistroForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('lista_eventos')

    def form_valid(self, form):
        """
        Guarda el usuario y lo autentica automáticamente.
        """
        response = super().form_valid(form)
        # Autenticar al usuario recién registrado
        login(self.request, self.object)
        messages.success(
            self.request, 
            f'¡Bienvenido {self.object.username}! Tu cuenta ha sido creada exitosamente.'
        )
        return response

    def form_invalid(self, form):
        """
        Muestra mensaje de error si el formulario no es válido.
        """
        messages.error(
            self.request,
            'Por favor corrige los errores en el formulario.'
        )
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        """
        Redirige a la lista de eventos si el usuario ya está autenticado.
        """
        if request.user.is_authenticated:
            messages.info(request, 'Ya tienes una sesión activa.')
            return redirect('lista_eventos')
        return super().dispatch(request, *args, **kwargs)


class LoginView(DjangoLoginView):
    """
    Vista de inicio de sesión personalizada.
    Hereda de la vista de login de Django y añade mensajes personalizados.
    """
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        """
        Redirige al usuario después del login exitoso.
        Prioriza: next parameter > eventos
        """
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('lista_eventos')

    def form_valid(self, form):
        """
        Muestra mensaje de bienvenida al iniciar sesión.
        """
        messages.success(
            self.request,
            f'¡Bienvenido de nuevo, {form.get_user().username}!'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Muestra mensaje de error en credenciales inválidas.
        """
        messages.error(
            self.request,
            'Usuario o contraseña incorrectos. Por favor intenta nuevamente.'
        )
        return super().form_invalid(form)


class LogoutView(LoginRequiredMixin, TemplateView):
    """
    Vista para cerrar sesión del usuario.
    Requiere autenticación y muestra mensaje de confirmación.
    """
    template_name = 'usuarios/logout.html'

    def get(self, request, *args, **kwargs):
        """
        Cierra la sesión del usuario y redirige al login.
        """
        username = request.user.username
        logout(request)
        messages.success(request, f'Hasta pronto, {username}. Has cerrado sesión exitosamente.')
        return redirect('login')


class PerfilView(LoginRequiredMixin, UpdateView):
    """
    Vista para ver y editar el perfil del usuario autenticado.
    Permite modificar información personal excepto username.
    
    Funcionalidad:
    - Muestra información actual del usuario
    - Permite editar: email, nombre, apellido
    - No permite cambiar: username (por seguridad)
    - Valida que el email no esté en uso
    """
    form_class = PerfilForm
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        """
        Retorna el usuario autenticado actual.
        """
        return self.request.user

    def form_valid(self, form):
        """
        Guarda los cambios y muestra mensaje de éxito.
        """
        messages.success(
            self.request,
            'Tu perfil ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Muestra mensaje de error si la validación falla.
        """
        messages.error(
            self.request,
            'No se pudo actualizar tu perfil. Verifica los errores.'
        )
        return super().form_invalid(form)


class InfoUsuarioView(LoginRequiredMixin, TemplateView):
    """
    Vista de información del usuario.
    Muestra estadísticas y datos relevantes del usuario autenticado.
    
    Información mostrada:
    - Datos personales
    - Eventos creados
    - Eventos en los que participa
    - Estadísticas generales
    """
    template_name = 'usuarios/info_usuario.html'

    def get_context_data(self, **kwargs):
        """
        Añade información del usuario al contexto.
        """
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Eventos creados por el usuario
        context['eventos_creados'] = user.evento_set.all().order_by('-fecha_inicio')
        context['total_eventos_creados'] = user.evento_set.count()
        
        # Eventos en los que participa
        context['eventos_participando'] = user.eventos_participando.all().order_by('-fecha_inicio')
        context['total_eventos_participando'] = user.eventos_participando.count()
        
        return context
