from django.contrib import admin
from .models import Resena


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ['bicicleta', 'usuario', 'puntuacion', 'fecha_creacion']
    list_filter = ['puntuacion', 'fecha_creacion']
    search_fields = ['bicicleta__marca', 'bicicleta__modelo', 'usuario__email', 'comentario']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    ordering = ['-fecha_creacion']
