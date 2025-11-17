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
    productos = Producto.objects.all()  # Los más nuevos primero
    return render(request, 'productos/lista_productos.html', {'productos': productos})


