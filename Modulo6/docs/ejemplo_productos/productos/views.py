# productos/views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from datetime import datetime
from .models import Producto
from .forms import ProductoForm


def lista_productos(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')  # Los más nuevos primero
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def filtrar_productos(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')  # Inicializar productos
    categoria_seleccionada = request.GET.get('categoria')
    precio_min_seleccionado = request.GET.get('precio_min')
    precio_max_seleccionado = request.GET.get('precio_max')

    if categoria_seleccionada:
        productos = productos.filter(categoria=categoria_seleccionada)

    if precio_min_seleccionado:
        try:
            precio_min = Decimal(precio_min_seleccionado)
            productos = productos.filter(precio__gte=precio_min)
        except (InvalidOperation, ValueError):
            messages.error(request, "Precio mínimo inválido.")

    if precio_max_seleccionado:
        try:
            precio_max = Decimal(precio_max_seleccionado)
            productos = productos.filter(precio__lte=precio_max)
        except (InvalidOperation, ValueError):
            messages.error(request, "Precio máximo inválido.")

    return render(request, 'productos/lista_productos.html', {'productos': productos})


def registrar_producto(request):
    """
    Vista para registrar un nuevo producto usando un formulario.
    """
    if request.method == 'POST':
        # Si el formulario ha sido enviado (es una petición POST)
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            # Redirige a la lista de productos con namespace
            return redirect('productos:lista_productos')
    else:
        # Si es la primera vez que se carga la página (petición GET)
        form = ProductoForm()

    # Renderiza la plantilla con el formulario
    return render(request, 'productos/registrar_producto.html', {'form': form})
