
from django.contrib import admin
from .models import Bicicleta

@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'tipo', 'precio', 'disponible', 'anio', 'tiene_imagen']
    list_filter = ['tipo', 'disponible']
    search_fields = ['marca', 'modelo']
    fields = ['marca', 'modelo', 'tipo', 'precio', 'disponible', 'anio', 'imagen']
    
    def tiene_imagen(self, obj):
        return "✓" if obj.imagen else "✗"
    tiene_imagen.short_description = 'Imagen'