from django.contrib import admin

from .models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Evento
    """
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin', 'ubicacion', 'autor')
    list_filter = ('fecha_inicio', 'ubicacion', 'autor')
    ordering = ('-fecha_inicio',)
