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
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    productos = Producto.objects.all()
    if precio_min:
        productos = productos.filter(precio__gte=int(precio_min))
    if precio_max:
        productos = productos.filter(precio__lte=int(precio_max))
    contexto = {
        'productos': productos,
        'precio_min': precio_min or '', # Mantener el valor en el campo del formulario
        'precio_max': precio_max or '',
    }
    return render(request, 'productos/lista_productos.html', contexto)


