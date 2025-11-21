from django.contrib import admin
from .models import Categoria, Producto, Etiqueta, DetalleProducto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

admin.site.register(Categoria, CategoriaAdmin)


class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color')
    search_fields = ('nombre',)
    list_per_page = 20

admin.site.register(Etiqueta, EtiquetaAdmin)


class DetalleProductoInline(admin.StackedInline):
    model = DetalleProducto
    extra = 0
    can_delete = True


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'disponible', 'mostrar_etiquetas')
    list_filter = ('disponible', 'categoria', 'etiquetas')
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('etiquetas',)
    inlines = [DetalleProductoInline]
    
    def mostrar_etiquetas(self, obj):
        return ", ".join([etiqueta.nombre for etiqueta in obj.etiquetas.all()])
    mostrar_etiquetas.short_description = 'Etiquetas'

admin.site.register(Producto, ProductoAdmin)


class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'peso', 'dimensiones_completas', 'material', 'fabricante')
    search_fields = ('producto__nombre', 'material', 'fabricante')
    list_filter = ('pais_origen',)

admin.site.register(DetalleProducto, DetalleProductoAdmin)