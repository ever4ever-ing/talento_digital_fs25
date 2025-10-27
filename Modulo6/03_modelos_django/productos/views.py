from django.shortcuts import render
from .models import Producto

# Create your views here.
def lista_productos(request):
    # Crear datos de ejemplo de productos
    productos = [
        {"nombre": "Producto A", "precio": 100.50, "disponible": True},
        {"nombre": "Producto B", "precio": 200.75, "disponible": False},
        {"nombre": "Producto C", "precio": 50.99, "disponible": True},
    ]
    # Para obtener productos desde la base de datos, descomenta la línea siguiente:
    productos_bd = Producto.objects.all()
    
    # extender la lista con productos de la base de datos
    productos.extend(productos_bd)
    
    # Pasar los productos a la plantilla
    return render(request, 'lista.html', {'productos': productos})