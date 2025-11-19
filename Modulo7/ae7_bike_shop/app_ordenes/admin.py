from django.contrib import admin
from .models import Orden, DetalleOrden

# Inline para la tabla intermedia DetalleOrden
class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 1  # Número de filas extra vacías para agregar rápido
    min_num = 1
    can_delete = True
    verbose_name = "Detalle de la Orden"
    verbose_name_plural = "Detalles de la Orden"
    fields = ['bicicleta', 'cantidad', 'precio_unitario', 'get_subtotal']
    readonly_fields = ['get_subtotal']
    
    def get_subtotal(self, obj):
        if obj.id:
            return f"${obj.subtotal():,.0f}".replace(",", ".")
        return "-"
    get_subtotal.short_description = "Subtotal"


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha', 'get_total', 'estado', 'cantidad_productos']
    list_filter = ['estado', 'fecha']
    search_fields = ['cliente__nombre', 'cliente__email']
    date_hierarchy = 'fecha'
    inlines = [DetalleOrdenInline]
    readonly_fields = ['fecha', 'get_total']
    
    fieldsets = (
        ('Información de la Orden', {
            'fields': ('cliente', 'estado')
        }),
        ('Detalles', {
            'fields': ('fecha', 'get_total')
        }),
    )
    
    def get_total(self, obj):
        return f"${obj.total:,.0f}".replace(",", ".")
    get_total.short_description = "Total"
    get_total.admin_order_field = 'total'
    
    def cantidad_productos(self, obj):
        return obj.detalles.count()
    cantidad_productos.short_description = "Productos"
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.calcular_total()


@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'orden', 'bicicleta', 'cantidad', 'precio_unitario', 'get_subtotal']
    list_filter = ['orden__estado']
    search_fields = ['orden__id', 'bicicleta__marca', 'bicicleta__modelo']
    
    def get_subtotal(self, obj):
        return f"${obj.subtotal():,.0f}".replace(",", ".")
    get_subtotal.short_description = "Subtotal"
