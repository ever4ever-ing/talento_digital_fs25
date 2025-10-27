from django.contrib import admin
from .models import Producto

# Registrar el modelo Producto en el administrador de Django
# Es necesario para gestionar los productos desde el panel de administración
# Se debe hacer migraciones después de registrar el modelo
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')