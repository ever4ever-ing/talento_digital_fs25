# Guía de Filtros en Django - Query Parameters

## 📋 Resumen de Implementación

Esta guía muestra cómo implementar filtros por categoría usando Query Parameters en Django.

## 🔧 Pasos Implementados

### 1. Modificar la Vista (views.py)

```python
def lista_productos(request):
    """
    Vista para mostrar la lista de productos con múltiples filtros.
    """
    # Obtener parámetros de filtro de la URL
    categoria_filtro = request.GET.get('categoria')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    
    # Comenzar con todos los productos
    productos = Producto.objects.all()
    
    # Aplicar filtros uno por uno
    if categoria_filtro:
        productos = productos.filter(categoria=categoria_filtro)
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
    
    # Ordenar por fecha de creación
    productos = productos.order_by('-fecha_creacion')
    
    # Obtener todas las categorías disponibles
    categorias = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
    
    return render(request, 'productos/lista_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_filtro,
        'precio_min_seleccionado': precio_min,
        'precio_max_seleccionado': precio_max
    })
```

### 2. Modificar el Template (lista_productos.html)

```html
<!-- Filtros múltiples -->
<div style="margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
    <h3>Filtros</h3>
    
    <form method="get" style="display: flex; gap: 15px; align-items: center; flex-wrap: wrap;">
        <!-- Filtro por categoría -->
        <div>
            <label for="categoria">Categoría:</label>
            <select name="categoria" id="categoria">
                <option value="">Todas</option>
                {% for categoria in categorias %}
                    <option value="{{ categoria }}" 
                        {% if categoria == categoria_seleccionada %}selected{% endif %}>
                        {{ categoria }}
                    </option>
                {% endfor %}
            </select>
        </div>
        
        <!-- Filtro por precio mínimo -->
        <div>
            <label for="precio_min">Precio mín:</label>
            <input type="number" name="precio_min" id="precio_min" 
                   value="{{ precio_min_seleccionado|default:'' }}" 
                   placeholder="0" step="0.01" min="0">
        </div>
        
        <!-- Filtro por precio máximo -->
        <div>
            <label for="precio_max">Precio máx:</label>
            <input type="number" name="precio_max" id="precio_max" 
                   value="{{ precio_max_seleccionado|default:'' }}" 
                   placeholder="9999" step="0.01" min="0">
        </div>
        
        <!-- Botones -->
        <div>
            <button type="submit">Filtrar</button>
            <a href="{% url 'productos:lista_productos' %}">Limpiar</a>
        </div>
    </form>
    
    <!-- Mostrar filtros activos -->
    {% if categoria_seleccionada or precio_min_seleccionado or precio_max_seleccionado %}
        <div style="margin-top: 15px;">
            <strong>Filtros activos:</strong>
            {% if categoria_seleccionada %}
                <span>Categoría: {{ categoria_seleccionada }}</span>
            {% endif %}
            {% if precio_min_seleccionado %}
                <span>Precio mín: ${{ precio_min_seleccionado }}</span>
            {% endif %}
            {% if precio_max_seleccionado %}
                <span>Precio máx: ${{ precio_max_seleccionado }}</span>
            {% endif %}
        </div>
    {% endif %}
</div>
```

## 🚀 Cómo Funciona

1. **Query Parameters**: Los filtros se envían como parámetros GET en la URL
   - Sin filtro: `/productos/`
   - Con filtro: `/productos/?categoria=Electrónicos`

2. **request.GET.get()**: Obtiene el valor del parámetro de forma segura
   - Retorna `None` si no existe el parámetro

3. **Filtro Condicional**: Solo aplica el filtro si hay un valor
   - Con filtro: `Producto.objects.filter(categoria=categoria_filtro)`
   - Sin filtro: `Producto.objects.all()`

4. **Select Dinámico**: Las opciones del select se generan desde la base de datos
   - `values_list('categoria', flat=True).distinct()` obtiene valores únicos

## 📝 Ventajas de Query Parameters

✅ **Simple de implementar**
✅ **URLs amigables y compartibles**
✅ **Funciona con navegador (botón atrás)**
✅ **SEO friendly**
✅ **Fácil de extender con más filtros**

## 🔄 Extensiones Posibles

### Múltiples Filtros
```python
categoria_filtro = request.GET.get('categoria')
precio_min = request.GET.get('precio_min')
precio_max = request.GET.get('precio_max')

productos = Producto.objects.all()

if categoria_filtro:
    productos = productos.filter(categoria=categoria_filtro)
if precio_min:
    productos = productos.filter(precio__gte=precio_min)
if precio_max:
    productos = productos.filter(precio__lte=precio_max)
```

### Búsqueda por Texto
```python
busqueda = request.GET.get('q')
if busqueda:
    productos = productos.filter(
        Q(nombre__icontains=busqueda) | 
        Q(descripcion__icontains=busqueda)
    )
```

### Ordenamiento
```python
orden = request.GET.get('orden', '-fecha_creacion')
productos = productos.order_by(orden)
```

## 🌐 URLs de Ejemplo

- **Todos los productos**: `/productos/`
- **Filtro por categoría**: `/productos/?categoria=Electrónicos`
- **Filtro por precio mínimo**: `/productos/?precio_min=50`
- **Filtro por precio máximo**: `/productos/?precio_max=200`
- **Múltiples filtros**: `/productos/?categoria=Ropa&precio_min=50&precio_max=200`
- **Filtros combinados**: `/productos/?categoria=Libros&precio_min=10&precio_max=100`

## 🎯 Consejos

1. **Siempre validar parámetros** para evitar errores
2. **Usar `.distinct()`** para evitar categorías duplicadas
3. **Mantener estado del filtro** mostrando la selección actual
4. **Proporcionar forma de limpiar filtros** (enlace "Limpiar")
5. **Ordenar resultados** para consistencia

## 🚀 Para Probar

1. Ejecutar servidor: `python manage.py runserver`
2. Ir a: `http://127.0.0.1:8000/productos/`
3. Usar el select para filtrar por categoría
4. Observar cómo cambia la URL y los resultados

---
*Creado el 16 de agosto de 2025*
