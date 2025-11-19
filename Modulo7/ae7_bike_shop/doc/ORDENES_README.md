# 📦 Documentación: App Órdenes - BikeShop

## Fecha: 9 de noviembre de 2025

---

## Resumen

Se creó la aplicación `ordenes` que permite gestionar órdenes de compra de bicicletas con una relación **ManyToMany** entre Bicicletas y Órdenes a través de una tabla intermedia (`DetalleOrden`).

---

## 🎯 Características Implementadas

### Modelos Creados

#### 1. **Modelo Orden**
```python
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ordenes')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    estado = models.CharField(max_length=20, choices=[...], default='pendiente')
    bicicletas = models.ManyToManyField(Bicicleta, through='DetalleOrden', related_name='ordenes')
```

**Campos:**
- `cliente`: Relación ForeignKey con Cliente
- `fecha`: Fecha y hora de creación (automática)
- `total`: Total de la orden en pesos
- `estado`: Estado de la orden (pendiente, pagada, cancelada)
- `bicicletas`: Relación ManyToMany con Bicicleta (a través de DetalleOrden)

**Métodos:**
- `calcular_total()`: Calcula y actualiza el total automáticamente

#### 2. **Modelo DetalleOrden** (Tabla Intermedia)
```python
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='detalles')
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
```

**Campos:**
- `orden`: Relación con la orden
- `bicicleta`: Relación con la bicicleta
- `cantidad`: Cantidad de bicicletas de este tipo en la orden
- `precio_unitario`: Precio de la bicicleta al momento de la orden

**Métodos:**
- `subtotal()`: Calcula el subtotal (cantidad × precio_unitario)

---

## 🔗 Relaciones Entre Modelos

### Diagrama de Relaciones

```
Cliente (1) ──────► (N) Orden
                       ↓
                    (N) DetalleOrden (tabla intermedia)
                       ↓
Bicicleta (N) ◄─────(N) Orden
```

### Tipos de Relaciones

1. **Cliente ↔ Orden**: OneToMany (ForeignKey)
   - Un cliente puede tener muchas órdenes
   - Una orden pertenece a un solo cliente

2. **Orden ↔ Bicicleta**: ManyToMany (through DetalleOrden)
   - Una orden puede tener muchas bicicletas
   - Una bicicleta puede estar en muchas órdenes

3. **DetalleOrden**: Tabla intermedia
   - Conecta Orden con Bicicleta
   - Almacena información adicional (cantidad, precio_unitario)

---

## 🚀 Cómo Usar

### Paso 1: Aplicar Migraciones

```bash
python manage.py makemigrations ordenes
python manage.py migrate
```

### Paso 2: Ejecutar el Script de Ejemplo

**Opción A: Desde el shell de Django**
```bash
python manage.py shell
```
Luego copiar y pegar el contenido de `ejemplo_ordenes.py`

**Opción B: Ejecutar directamente (si está configurado)**
```bash
python manage.py shell < ejemplo_ordenes.py
```

### Paso 3: Crear Órdenes Manualmente

```python
from clientes.models import Cliente
from bicicletas.models import Bicicleta
from ordenes.models import Orden, DetalleOrden

# 1. Crear cliente
cliente = Cliente.objects.create(
    nombre="Laura Gómez",
    email="laura@example.com"
)

# 2. Obtener bicicletas existentes
mtb = Bicicleta.objects.get(marca="Trek", modelo="Marlin 7")
ruta = Bicicleta.objects.get(marca="Giant", modelo="TCR Advanced")

# 3. Crear orden
orden = Orden.objects.create(
    cliente=cliente,
    estado='pendiente'
)

# 4. Agregar detalles a la orden
DetalleOrden.objects.create(
    orden=orden,
    bicicleta=mtb,
    cantidad=2,
    precio_unitario=mtb.precio
)

DetalleOrden.objects.create(
    orden=orden,
    bicicleta=ruta,
    cantidad=1,
    precio_unitario=ruta.precio
)

# 5. Calcular total
orden.calcular_total()
print(f"Total: ${orden.total:,.0f}")
```

---

## 📊 Consultas Útiles

### Obtener todas las órdenes de un cliente
```python
cliente = Cliente.objects.get(email="laura@example.com")
ordenes = cliente.ordenes.all()
```

### Obtener todas las bicicletas de una orden
```python
orden = Orden.objects.get(id=1)
bicicletas = orden.bicicletas.all()
```

### Obtener los detalles de una orden
```python
orden = Orden.objects.get(id=1)
detalles = orden.detalles.all()
for detalle in detalles:
    print(f"{detalle.cantidad} x {detalle.bicicleta} = ${detalle.subtotal()}")
```

### Obtener todas las órdenes que incluyen una bicicleta
```python
bici = Bicicleta.objects.get(marca="Trek")
ordenes = bici.ordenes.all()
```

### Filtrar órdenes por estado
```python
# Órdenes pendientes
pendientes = Orden.objects.filter(estado='pendiente')

# Órdenes pagadas
pagadas = Orden.objects.filter(estado='pagada')

# Órdenes canceladas
canceladas = Orden.objects.filter(estado='cancelada')
```

### Calcular ventas totales
```python
from django.db.models import Sum

# Total de ventas pagadas
ventas = Orden.objects.filter(estado='pagada').aggregate(
    total=Sum('total')
)['total']
print(f"Ventas totales: ${ventas:,.0f}")
```

### Bicicleta más vendida
```python
from django.db.models import Sum

ventas_por_bici = DetalleOrden.objects.values(
    'bicicleta__marca',
    'bicicleta__modelo'
).annotate(
    total_vendido=Sum('cantidad')
).order_by('-total_vendido')

top = ventas_por_bici.first()
print(f"Más vendida: {top['bicicleta__marca']} {top['bicicleta__modelo']}")
```

---

## 🔧 Operaciones Comunes

### Cambiar estado de una orden
```python
orden = Orden.objects.get(id=1)
orden.estado = 'pagada'
orden.save()
```

### Agregar más productos a una orden existente
```python
orden = Orden.objects.get(id=1)
bici = Bicicleta.objects.get(id=5)

DetalleOrden.objects.create(
    orden=orden,
    bicicleta=bici,
    cantidad=1,
    precio_unitario=bici.precio
)

# Recalcular total
orden.calcular_total()
```

### Eliminar un producto de una orden
```python
detalle = DetalleOrden.objects.get(id=1)
detalle.delete()

# Recalcular total
orden.calcular_total()
```

### Obtener el subtotal de cada detalle
```python
orden = Orden.objects.get(id=1)
for detalle in orden.detalles.all():
    print(f"{detalle}: ${detalle.subtotal():,.0f}")
```

---

## 📁 Estructura de la Base de Datos

### Tabla: ordenes_orden
| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | BigInt | PRIMARY KEY, AUTO_INCREMENT |
| cliente_id | BigInt | FOREIGN KEY → clientes_cliente(id) |
| fecha | DateTime | NOT NULL |
| total | Decimal(10,2) | DEFAULT 0.0 |
| estado | VARCHAR(20) | DEFAULT 'pendiente' |

### Tabla: ordenes_detalleorden
| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | BigInt | PRIMARY KEY, AUTO_INCREMENT |
| orden_id | BigInt | FOREIGN KEY → ordenes_orden(id) |
| bicicleta_id | BigInt | FOREIGN KEY → bicicletas_bicicleta(id) |
| cantidad | Integer | NOT NULL, >= 1 |
| precio_unitario | Decimal(10,2) | NOT NULL |

---

## 💡 Ventajas de la Relación ManyToMany con Tabla Intermedia

### Sin Tabla Intermedia (ManyToMany simple)
```python
# Solo permite relacionar órdenes con bicicletas
orden.bicicletas.add(bici1, bici2)
```

### Con Tabla Intermedia (through)
```python
# Permite almacenar información adicional
DetalleOrden.objects.create(
    orden=orden,
    bicicleta=bici1,
    cantidad=5,           # ← Información extra
    precio_unitario=1000  # ← Información extra
)
```

**Beneficios:**
- ✅ Guardar cantidad de cada producto
- ✅ Guardar precio al momento de la compra (histórico)
- ✅ Calcular subtotales
- ✅ Más flexibilidad para reportes

---

## 🎨 Próximas Mejoras (Opcionales)

### 1. Admin de Django
```python
# ordenes/admin.py
from django.contrib import admin
from .models import Orden, DetalleOrden

class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 1

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha', 'total', 'estado']
    list_filter = ['estado', 'fecha']
    search_fields = ['cliente__nombre']
    inlines = [DetalleOrdenInline]
```

### 2. Métodos Adicionales
```python
# En el modelo Orden
def obtener_cantidad_productos(self):
    return sum(d.cantidad for d in self.detalles.all())

def puede_cancelarse(self):
    return self.estado == 'pendiente'
```

### 3. Validaciones
```python
from django.core.exceptions import ValidationError

# En el modelo DetalleOrden
def clean(self):
    if self.cantidad <= 0:
        raise ValidationError("La cantidad debe ser mayor a 0")
    if self.precio_unitario <= 0:
        raise ValidationError("El precio debe ser mayor a 0")
```

### 4. Signals (Automatización)
```python
# ordenes/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import DetalleOrden

@receiver([post_save, post_delete], sender=DetalleOrden)
def actualizar_total_orden(sender, instance, **kwargs):
    instance.orden.calcular_total()
```

### 5. Vistas y Templates
- Lista de órdenes
- Detalle de orden
- Crear nueva orden
- Carrito de compras

---

## 🐛 Solución de Problemas

### Error: "AttributeError: 'Bicicleta' object has no attribute 'nombre'"
**Causa**: El modelo Bicicleta no tiene campo `nombre`, tiene `marca` y `modelo`.

**Solución**: Usar `bicicleta.marca` y `bicicleta.modelo` en lugar de `bicicleta.nombre`.

### Error: "RelatedObjectDoesNotExist: Orden has no detalles"
**Causa**: Intentar acceder a detalles de una orden sin detalles.

**Solución**: 
```python
if orden.detalles.exists():
    for detalle in orden.detalles.all():
        print(detalle)
```

### Total no se actualiza automáticamente
**Causa**: Hay que llamar manualmente a `calcular_total()`.

**Solución**: Usar signals (ver sección "Próximas Mejoras") o llamar manualmente:
```python
orden.calcular_total()
```

---

## 📝 Notas Importantes

1. ✅ **Precio Histórico**: El `precio_unitario` guarda el precio al momento de la compra, no el precio actual
2. ✅ **Estado de la Orden**: Usar 'pendiente', 'pagada', 'cancelada'
3. ✅ **Calcular Total**: Llamar a `orden.calcular_total()` después de modificar detalles
4. ✅ **Disponibilidad**: Considera validar que `bicicleta.disponible == True` antes de agregar a orden
5. ✅ **Stock**: Considera implementar un sistema de stock en el futuro

---

## 📚 Archivos Creados/Modificados

1. ✅ `ordenes/models.py` - Modelos Orden y DetalleOrden
2. ✅ `ordenes/migrations/0001_initial.py` - Migración inicial
3. ✅ `ejemplo_ordenes.py` - Script de ejemplo completo
4. ✅ `ORDENES_README.md` - Esta documentación

---

## ✨ Ejemplo Rápido

```python
# Importar modelos
from clientes.models import Cliente
from bicicletas.models import Bicicleta
from ordenes.models import Orden, DetalleOrden

# Crear cliente y bicicletas
c = Cliente.objects.create(nombre="Laura", email="laura@example.com")
b1 = Bicicleta.objects.create(marca="Trek", modelo="X", tipo="MTB", precio=500000, anio=2024)
b2 = Bicicleta.objects.create(marca="Giant", modelo="Y", tipo="Ruta", precio=800000, anio=2024)

# Crear orden
o = Orden.objects.create(cliente=c)

# Agregar bicicletas
DetalleOrden.objects.create(orden=o, bicicleta=b1, cantidad=2, precio_unitario=500000)
DetalleOrden.objects.create(orden=o, bicicleta=b2, cantidad=1, precio_unitario=800000)

# Calcular total
o.calcular_total()
print(f"Total: ${o.total:,.0f}")  # Total: $1.800.000

# Consultar
print(o.bicicletas.all())  # Bicicletas en la orden
print(b1.ordenes.all())    # Órdenes que incluyen b1
```

---

*Documentación generada - 9 de noviembre de 2025*
