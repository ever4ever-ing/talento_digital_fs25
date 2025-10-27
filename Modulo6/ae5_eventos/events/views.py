from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.contrib.auth.views import LoginView
from .models import Event
from .forms import EventForm
from django.db.models import Q
from django.contrib.auth import logout
from django.conf import settings
from django.views.decorators.http import require_POST
import logging

logger = logging.getLogger(__name__)

class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'events/list.html'

    def get_queryset(self):
        qs = Event.objects.all()
        # asistentes no ven eventos privados a menos que sean owner
        if not self.request.user.is_staff:
            qs = qs.filter(Q(is_private=False) | Q(owner=self.request.user))
        return qs


class EventCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/form.html'
    permission_required = 'events.add_event'
    success_url = reverse_lazy('events:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Evento creado.')
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/form.html'
    permission_required = 'events.change_event'
    success_url = reverse_lazy('events:list')

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para editar este evento.')
        return redirect('events:list')


class EventDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Event
    template_name = 'events/confirm_delete.html'
    success_url = reverse_lazy('events:list')
    permission_required = 'events.delete_event'

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para eliminar este evento.')
        return redirect('events:list')


def access_denied(request):
    messages.error(request, 'Acceso denegado: no tienes permisos suficientes.')
    return render(request, 'access_denied.html')


@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect(settings.LOGOUT_REDIRECT_URL)


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        # Mensaje genérico para intentos fallidos (no revelar detalles)
        messages.error(self.request, 'Usuario o contraseña inválidos.')
        return super().form_invalid(form)

