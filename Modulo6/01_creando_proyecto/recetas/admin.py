from django.contrib import admin
from .models import Receta

# Register your models here.

#Decorador que registra el modelo Receta en el admin de Django
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):  # Clase que personaliza cómo se muestra y maneja el modelo en el admin
    list_display = ('nombre', 'tiempo_preparacion', 'porciones')#Muestra estas columnas en la lista de recetas en el admin
    search_fields = ('nombre',)#Agrega un filtro lateral en el admin
    list_filter = ('tiempo_preparacion',) #Agrega un cuadro de búsqueda en la parte superior del admin