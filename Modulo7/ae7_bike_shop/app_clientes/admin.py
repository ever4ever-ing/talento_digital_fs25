from django.contrib import admin
from .models import Cliente, PerfilCliente


class PerfilClienteInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name = "Perfil del Cliente"
    verbose_name_plural = "Perfil del Cliente"


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'created_at', 'tiene_perfil']
    search_fields = ['nombre', 'email']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    inlines = [PerfilClienteInline]
    
    def tiene_perfil(self, obj):
        return "✓" if hasattr(obj, 'perfil') else "✗"
    tiene_perfil.short_description = 'Perfil'


@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'telefono', 'fecha_nacimiento']
    search_fields = ['cliente__nombre', 'telefono']