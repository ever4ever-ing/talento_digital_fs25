from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto, Categoria, Etiqueta, DetalleProducto
from .forms import ProductoForm

# ============== VISTAS DE PRODUCTOS ==============

def index(request):
    """Página de bienvenida"""
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    total_etiquetas = Etiqueta.objects.count()
    productos_disponibles = Producto.objects.filter(disponible=True).count()
    
    context = {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_etiquetas': total_etiquetas,
        'productos_disponibles': productos_disponibles,
    }
    return render(request, 'index.html', context)

def lista_productos(request):
    """Lista todos los productos con sus relaciones"""
    productos = Producto.objects.select_related('categoria').prefetch_related('etiquetas').all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def crear_producto(request):
    """Crea un nuevo producto"""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            
            # Guardar etiquetas si se seleccionaron
            if 'etiquetas' in request.POST:
                etiquetas_ids = request.POST.getlist('etiquetas')
                producto.etiquetas.set(etiquetas_ids)
            
            messages.success(request, f'Producto "{producto.nombre}" creado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    etiquetas = Etiqueta.objects.all()
    return render(request, 'productos/crear_producto.html', {'form': form, 'etiquetas': etiquetas})

def detalle_producto(request, id):
    """Muestra el detalle completo de un producto"""
    producto = get_object_or_404(Producto, id=id)
    try:
        detalle = producto.detalle
    except DetalleProducto.DoesNotExist:
        detalle = None
    
    context = {
        'producto': producto,
        'detalle': detalle,
    }
    return render(request, 'productos/detalle_producto.html', context)

def editar_producto(request, id):
    """Edita un producto existente"""
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            
            # Actualizar etiquetas
            if 'etiquetas' in request.POST:
                etiquetas_ids = request.POST.getlist('etiquetas')
                producto.etiquetas.set(etiquetas_ids)
            
            messages.success(request, f'Producto "{producto.nombre}" actualizado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    
    etiquetas = Etiqueta.objects.all()
    etiquetas_seleccionadas = producto.etiquetas.all().values_list('id', flat=True)
    
    context = {
        'form': form,
        'producto': producto,
        'etiquetas': etiquetas,
        'etiquetas_seleccionadas': list(etiquetas_seleccionadas),
    }
    return render(request, 'productos/editar_producto.html', context)

def eliminar_producto(request, id):
    """Elimina un producto"""
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado exitosamente.')
        return redirect('lista_productos')
    
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

# ============== VISTAS DE CATEGORÍAS ==============

def lista_categorias(request):
    """Lista todas las categorías"""
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    """Crea una nueva categoría"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        
        if nombre:
            Categoria.objects.create(nombre=nombre, descripcion=descripcion)
            messages.success(request, f'Categoría "{nombre}" creada exitosamente.')
            return redirect('lista_categorias')
        else:
            messages.error(request, 'El nombre es obligatorio.')
    
    return render(request, 'categorias/formulario_categoria.html')

def editar_categoria(request, id):
    """Edita una categoría existente"""
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        
        if nombre:
            categoria.nombre = nombre
            categoria.descripcion = descripcion
            categoria.save()
            messages.success(request, f'Categoría "{nombre}" actualizada exitosamente.')
            return redirect('lista_categorias')
        else:
            messages.error(request, 'El nombre es obligatorio.')
    
    return render(request, 'categorias/formulario_categoria.html', {'categoria': categoria})

def eliminar_categoria(request, id):
    """Elimina una categoría"""
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        nombre = categoria.nombre
        categoria.delete()
        messages.success(request, f'Categoría "{nombre}" eliminada exitosamente.')
        return redirect('lista_categorias')
    
    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})

# ============== VISTAS DE ETIQUETAS ==============

def lista_etiquetas(request):
    """Lista todas las etiquetas"""
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista_etiquetas.html', {'etiquetas': etiquetas})

def crear_etiqueta(request):
    """Crea una nueva etiqueta"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        color = request.POST.get('color', '#007bff')
        
        if nombre:
            Etiqueta.objects.create(nombre=nombre, color=color)
            messages.success(request, f'Etiqueta "{nombre}" creada exitosamente.')
            return redirect('lista_etiquetas')
        else:
            messages.error(request, 'El nombre es obligatorio.')
    
    return render(request, 'etiquetas/formulario_etiqueta.html')

def editar_etiqueta(request, id):
    """Edita una etiqueta existente"""
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        color = request.POST.get('color', '#007bff')
        
        if nombre:
            etiqueta.nombre = nombre
            etiqueta.color = color
            etiqueta.save()
            messages.success(request, f'Etiqueta "{nombre}" actualizada exitosamente.')
            return redirect('lista_etiquetas')
        else:
            messages.error(request, 'El nombre es obligatorio.')
    
    return render(request, 'etiquetas/formulario_etiqueta.html', {'etiqueta': etiqueta})

def eliminar_etiqueta(request, id):
    """Elimina una etiqueta"""
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        nombre = etiqueta.nombre
        etiqueta.delete()
        messages.success(request, f'Etiqueta "{nombre}" eliminada exitosamente.')
        return redirect('lista_etiquetas')
    
    return render(request, 'etiquetas/eliminar_etiqueta.html', {'etiqueta': etiqueta})