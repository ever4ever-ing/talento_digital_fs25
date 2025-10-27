from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Producto
from django.shortcuts import redirect

def index(request):
    cliente1 = Cliente(nombre="Everardo Alvarado", email="ever@gmail.com", fecha_registro="2023-10-01 10:00:00")
    cliente2 = Cliente(nombre="Natalia Peña", email="npena@gmail.com", fecha_registro="2023-10-02 11:00:00")
    return render(request, "index_cliente.html", {"cliente1": cliente1, "cliente2": cliente2})

def lista_productos(request):
    # Crear datos de ejemplo de productos
    productos = [
        {"nombre": "Producto A", "precio": 100.50, "disponible": True},
        {"nombre": "Producto B", "precio": 200.75, "disponible": False},
        {"nombre": "Producto C", "precio": 50.99, "disponible": True},
    ]
    
    producto = Producto(nombre="Producto D", precio=150.00, descripcion="Descripción del Producto D")
    productos.append(producto)
    producto = Producto(nombre="Producto E", precio=300.00, descripcion="Descripción del Producto E")
    productos.append(producto)
     
    # Pasar los productos a la plantilla
    return render(request, 'productos.html', {'productos': productos})

def ir_a_productos(request):
    # Redirige automáticamente a la página de productos
    return redirect('productos')


