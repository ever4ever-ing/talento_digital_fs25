# 🛒 Sistema de Carrito de Compras - BikeShop

## 📋 Descripción General

El sistema de carrito de compras permite a los usuarios agregar bicicletas, gestionar cantidades, y crear órdenes de compra. Utiliza sesiones de Django para mantener el estado del carrito sin necesidad de autenticación hasta el momento de crear la orden.

---

## 🏗️ Arquitectura

### Componentes Principales:

1. **Clase Carrito** (`app_carrito/carrito.py`)
   - Maneja la lógica del carrito usando sesiones
   - Operaciones: agregar, eliminar, limpiar, calcular totales

2. **Vistas** (`app_carrito/views.py`)
   - `carrito_detalle`: Muestra el contenido del carrito
   - `carrito_agregar`: Agrega productos al carrito
   - `carrito_eliminar`: Elimina productos del carrito
   - `crear_orden_desde_carrito`: Convierte el carrito en una orden
   - `mis_ordenes`: Lista las órdenes del usuario

3. **Template Tags** (`app_carrito/templatetags/carrito_tags.py`)
   - `cantidad_total_carrito`: Muestra el número de items
   - `total_carrito`: Muestra el precio total

---

## 🔧 Configuración

### settings.py
```python
INSTALLED_APPS = [
    # ...
    'app_carrito',
]

# ID de sesión para el carrito
CART_SESSION_ID = 'carrito'
```

### urls.py
```python
urlpatterns = [
    # ...
    path('', include('app_carrito.urls')),
]
```

---

## 💾 Estructura de Datos (Sesión)

El carrito se guarda en `request.session['carrito']`:

```python
{
    'bicicleta_id': {
        'cantidad': 2,
        'precio': '299.99'
    },
    'otro_id': {
        'cantidad': 1,
        'precio': '499.99'
    }
}
```

**Características:**
- ✅ No requiere base de datos
- ✅ Funciona sin autenticación
- ✅ Persiste entre requests
- ✅ Se limpia al crear la orden
- ✅ Los precios se guardan como string (serialización JSON)

---

## 📌 Flujo de Uso

### 1. Agregar al Carrito (Sin Login Requerido)

**Formulario en plantilla:**
```html
<form action="{% url 'carrito_agregar' bicicleta.id %}" method="post">
    {% csrf_token %}
    <input type="hidden" name="cantidad" value="1">
    <input type="hidden" name="actualizar" value="False">
    <button type="submit" class="btn btn-success">
        🛒 Agregar al Carrito
    </button>
</form>
```

**Vista:**
```python
@require_POST
def carrito_agregar(request, bicicleta_id):
    carrito = Carrito(request)
    bicicleta = get_object_or_404(Bicicleta, id=bicicleta_id)
    form = CarritoAgregarBicicletaForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        carrito.agregar(
            bicicleta=bicicleta,
            cantidad=cd['cantidad'],
            actualizar_cantidad=cd['actualizar']
        )
    
    return redirect('carrito_detalle')
```

### 2. Ver Carrito

**URL:** `/carrito/`

Muestra todos los items con:
- Imagen de la bicicleta
- Precio unitario y total
- Selector de cantidad
- Botón para actualizar cantidad
- Botón para eliminar
- Resumen con total general
- Botón para crear orden (requiere login)

### 3. Actualizar Cantidad

El usuario puede cambiar la cantidad usando un select (1-10) y hacer clic en "🔄 Actualizar".

### 4. Eliminar del Carrito

```python
@require_POST
def carrito_eliminar(request, bicicleta_id):
    carrito = Carrito(request)
    bicicleta = get_object_or_404(Bicicleta, id=bicicleta_id)
    carrito.eliminar(bicicleta)
    return redirect('carrito_detalle')
```

### 5. Crear Orden (Login Requerido)

**Vista:**
```python
@login_required
def crear_orden_desde_carrito(request):
    carrito = Carrito(request)
    
    # Verificar cliente
    cliente = Cliente.objects.get_or_create(
        user=request.user,
        defaults={
            'nombre': request.user.get_full_name(),
            'email': request.user.email
        }
    )[0]
    
    # Crear orden
    orden = Orden.objects.create(cliente=cliente, estado='pendiente')
    
    # Crear detalles
    for item in carrito:
        DetalleOrden.objects.create(
            orden=orden,
            bicicleta=item['bicicleta'],
            precio_unitario=item['precio'],
            cantidad=item['cantidad']
        )
    
    # Calcular total
    orden.calcular_total()
    
    # Limpiar carrito
    carrito.limpiar()
    
    return redirect('mis_ordenes')
```

### 6. Ver Mis Órdenes

**URL:** `/mis-ordenes/`

Muestra todas las órdenes del usuario con:
- Número de orden
- Fecha y hora
- Estado (Pendiente/Pagada/Cancelada)
- Lista de productos
- Total de la orden

---

## 🎨 Template Tags

### Uso en plantillas:

```html
{% load carrito_tags %}

<!-- Mostrar cantidad de items -->
{% cantidad_total_carrito request as total_items %}
<span class="badge">{{ total_items }}</span>

<!-- Mostrar total del carrito -->
{% total_carrito request as total %}
${{ total }}
```

### En la navbar:

```html
<a href="{% url 'carrito_detalle' %}" class="btn btn-warning">
    🛒 Carrito
    {% cantidad_total_carrito request as total_items %}
    {% if total_items > 0 %}
        <span class="badge bg-danger">{{ total_items }}</span>
    {% endif %}
</a>
```

---

## 🔐 Seguridad y Validaciones

### ✅ Validaciones Implementadas:

1. **Carrito vacío**: No permite crear órdenes sin items
2. **Usuario autenticado**: Solo usuarios con login pueden crear órdenes
3. **Cliente automático**: Si no existe Cliente, se crea automáticamente
4. **CSRF protection**: Todos los formularios usan `{% csrf_token %}`
5. **@require_POST**: Agregar/eliminar solo por POST
6. **@login_required**: Crear orden y ver órdenes requiere login

---

## 📊 Integración con Modelos Existentes

### Relación con `app_ordenes`:

```python
# app_ordenes/models.py
class Orden(models.Model):
    cliente = ForeignKey(Cliente)
    fecha = DateTimeField(auto_now_add=True)
    total = DecimalField()
    estado = CharField(choices=[...])
    bicicletas = ManyToManyField(Bicicleta, through='DetalleOrden')

class DetalleOrden(models.Model):
    orden = ForeignKey(Orden)
    bicicleta = ForeignKey(Bicicleta)
    cantidad = PositiveIntegerField()
    precio_unitario = DecimalField()
```

**El carrito convierte sesión → Orden + DetalleOrden**

---

## 🎯 URLs Disponibles

| URL | Nombre | Método | Auth | Descripción |
|-----|--------|--------|------|-------------|
| `/carrito/` | `carrito_detalle` | GET | No | Ver carrito |
| `/carrito/agregar/<id>/` | `carrito_agregar` | POST | No | Agregar al carrito |
| `/carrito/eliminar/<id>/` | `carrito_eliminar` | POST | No | Eliminar del carrito |
| `/carrito/crear-orden/` | `crear_orden_desde_carrito` | POST | **Sí** | Crear orden |
| `/mis-ordenes/` | `mis_ordenes` | GET | **Sí** | Ver mis órdenes |

---

## 💡 Casos de Uso

### Caso 1: Usuario Anónimo
1. Navega el catálogo
2. Agrega bicicletas al carrito (sin login)
3. Ve su carrito
4. Intenta crear orden → Redirigido a login
5. Después de login → Crea la orden exitosamente

### Caso 2: Usuario Registrado
1. Ya está logueado
2. Agrega productos al carrito
3. Crea orden inmediatamente
4. Ve sus órdenes en "Mis Órdenes"

### Caso 3: Actualizar Cantidades
1. Usuario tiene 1 bicicleta en el carrito
2. Cambia cantidad a 3
3. Click en "Actualizar"
4. El total se recalcula automáticamente

---

## 🧪 Ejemplo de Prueba Manual

### Prueba Completa:

1. **Agregar productos**:
   - Ve al catálogo: http://localhost:8000/
   - Click en "🛒 Agregar al Carrito" en 2-3 bicicletas
   - Verifica badge del carrito en navbar

2. **Ver carrito**:
   - Click en botón "🛒 Carrito"
   - Verifica que aparecen los productos
   - Cambia cantidad de uno
   - Click "Eliminar" en otro

3. **Crear orden**:
   - Si no estás logueado, haz login
   - Click en "✅ Crear Orden"
   - Verifica mensaje de éxito

4. **Ver órdenes**:
   - Click en "Mis Órdenes"
   - Verifica que aparece la orden
   - Verifica estado, productos y total

---

## 🚀 Mejoras Futuras (Opcionales)

- [ ] Cupones de descuento
- [ ] Envío y cálculo de costos
- [ ] Checkout con múltiples pasos
- [ ] Integración con pasarelas de pago
- [ ] Notificaciones por email
- [ ] Carrito persistente en base de datos
- [ ] Wishlist / Lista de deseos
- [ ] Stock y control de inventario
- [ ] Historial de precios

---

## 📝 Notas Importantes

1. **Sesiones**: El carrito usa sesiones de Django, asegúrate que `SessionMiddleware` esté activo
2. **CART_SESSION_ID**: Configurado en settings.py como 'carrito'
3. **Cliente automático**: Se crea automáticamente si el usuario no tiene perfil Cliente
4. **Decimales**: Los precios se convierten a string para JSON, luego a Decimal
5. **Limpieza**: El carrito se limpia automáticamente al crear la orden

---

## ✅ Checklist de Integración

- [x] Crear app_carrito
- [x] Clase Carrito con gestión de sesiones
- [x] Vistas para CRUD del carrito
- [x] Template tags para mostrar info
- [x] Plantillas con Bootstrap
- [x] Integración con navbar
- [x] Botones en catálogo y detalle
- [x] Crear órdenes desde carrito
- [x] Vista de mis órdenes
- [x] Documentación completa

---

**¡El sistema de carrito está listo para usar! 🎉**
