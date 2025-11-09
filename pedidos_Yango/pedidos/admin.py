from django.contrib import admin
from .models import Producto, Pedido, PedidoProducto, Direccion

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_pedido', 'total')

@admin.register(PedidoProducto)
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calle', 'numero', 'ciudad')
