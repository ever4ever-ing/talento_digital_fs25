# 🚀 Guía Rápida: Carrito de Compras

## ⚡ Inicio Rápido

### 1. Iniciar el servidor
```bash
python manage.py runserver
```

### 2. URLs principales
- **Catálogo**: http://localhost:8000/
- **Carrito**: http://localhost:8000/carrito/
- **Mis Órdenes**: http://localhost:8000/mis-ordenes/ (requiere login)

---

## 🛒 Funcionalidades del Carrito

### ✅ Lo que PUEDES hacer SIN login:
- Ver el catálogo de bicicletas
- Agregar productos al carrito
- Ver tu carrito
- Actualizar cantidades
- Eliminar productos del carrito

### 🔐 Lo que REQUIERE login:
- Crear una orden desde el carrito
- Ver tus órdenes anteriores

---

## 📝 Flujo de Compra

### Paso 1: Agregar al Carrito
1. Navega al catálogo: http://localhost:8000/
2. Encuentra una bicicleta disponible
3. Click en "🛒 Agregar al Carrito"
4. Verás un mensaje de confirmación
5. El badge del carrito se actualiza

### Paso 2: Ver y Gestionar el Carrito
1. Click en "🛒 Carrito" en la navbar
2. Verás todos los productos agregados
3. Puedes:
   - Cambiar la cantidad (1-10)
   - Eliminar productos
   - Ver el total

### Paso 3: Crear Orden
1. En el carrito, click en "✅ Crear Orden"
2. Si no estás logueado, te redirige a login
3. Después de login, la orden se crea automáticamente
4. El carrito se limpia
5. Eres redirigido a "Mis Órdenes"

### Paso 4: Ver Órdenes
1. Click en "Mis Órdenes" en la navbar
2. Verás todas tus órdenes con:
   - Número de orden
   - Fecha y hora
   - Estado (Pendiente/Pagada/Cancelada)
   - Productos y cantidades
   - Total

---

## 🎯 Características Clave

### 💾 Persistencia de Sesión
- El carrito se guarda en la sesión del navegador
- Se mantiene aunque cierres pestañas
- Se limpia al crear la orden

### 🔢 Gestión de Cantidades
- Rango: 1-10 unidades por producto
- Actualización en tiempo real
- Recalculo automático de totales

### 👤 Cliente Automático
- Si no tienes perfil de Cliente, se crea automáticamente
- Usa tu nombre y email de usuario
- No necesitas configuración adicional

### 📊 Estados de Orden
- **Pendiente**: Orden creada, esperando pago
- **Pagada**: Orden pagada (cambio manual por admin)
- **Cancelada**: Orden cancelada

---

## 🧪 Prueba Rápida (5 minutos)

### Test 1: Carrito sin login
```
1. Abre navegador de incógnito
2. Ve a http://localhost:8000/
3. Agrega 2-3 bicicletas al carrito
4. Ve al carrito
5. Actualiza cantidad de una
6. Elimina otra
7. Intenta crear orden → Te pide login ✓
```

### Test 2: Crear orden con login
```
1. Inicia sesión con tu usuario
2. Agrega productos al carrito
3. Ve al carrito
4. Click "Crear Orden"
5. Verifica mensaje de éxito ✓
6. Ve a "Mis Órdenes"
7. Verifica que aparece la orden ✓
```

### Test 3: Badge del carrito
```
1. Carrito vacío → Sin badge
2. Agrega 1 producto → Badge muestra "1"
3. Agrega 2 más → Badge muestra "3"
4. Crea orden → Badge desaparece ✓
```

---

## 🐛 Solución de Problemas

### Problema: "No aparece el badge del carrito"
**Solución**: 
- Verifica que `{% load carrito_tags %}` está al inicio del template
- Asegúrate que `app_carrito` está en `INSTALLED_APPS`

### Problema: "Error al crear orden"
**Posibles causas**:
1. No estás logueado → Inicia sesión
2. Carrito vacío → Agrega productos primero
3. No existe modelo Cliente → Se crea automáticamente

### Problema: "La cantidad no se actualiza"
**Solución**:
- Usa el selector de cantidad
- Click en botón "🔄 Actualizar"
- No modifiques manualmente el input

### Problema: "El carrito se mantiene después de crear orden"
**Solución**: Eso es un bug. El carrito debe limpiarse. Verifica que `carrito.limpiar()` se llama en la vista.

---

## 💻 Código de Ejemplo

### Agregar producto al carrito (plantilla)
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

### Mostrar badge del carrito
```html
{% load carrito_tags %}
<a href="{% url 'carrito_detalle' %}">
    🛒 Carrito
    {% cantidad_total_carrito request as total_items %}
    {% if total_items > 0 %}
        <span class="badge bg-danger">{{ total_items }}</span>
    {% endif %}
</a>
```

### Iterar sobre items del carrito
```python
carrito = Carrito(request)
for item in carrito:
    print(item['bicicleta'].marca)
    print(item['cantidad'])
    print(item['precio'])
    print(item['total_precio'])
```

---

## 📋 Checklist de Verificación

Antes de considerar completado:

- [ ] Badge del carrito se muestra correctamente
- [ ] Puedes agregar productos sin login
- [ ] El contador del badge es correcto
- [ ] Puedes actualizar cantidades
- [ ] Puedes eliminar productos
- [ ] El total se calcula correctamente
- [ ] Crear orden requiere login
- [ ] Se crea perfil Cliente automático si no existe
- [ ] La orden se crea con todos los detalles
- [ ] El carrito se limpia después de crear orden
- [ ] "Mis Órdenes" muestra las órdenes correctamente

---

## 🎨 Personalización

### Cambiar rango de cantidades (actualmente 1-10)
```python
# app_carrito/forms.py
CANTIDAD_CHOICES = [(i, str(i)) for i in range(1, 21)]  # Cambia a 1-20
```

### Cambiar ID de sesión del carrito
```python
# bikeshop/settings.py
CART_SESSION_ID = 'mi_carrito'  # Cambia el nombre
```

### Agregar validación de stock
```python
# app_carrito/views.py en carrito_agregar
if bicicleta.disponible:
    carrito.agregar(...)
else:
    messages.error(request, 'Producto no disponible')
```

---

## 📚 Documentación Completa

Para más detalles, consulta: `doc/CARRITO_README.md`

---

**¡Listo para empezar! 🚀**
