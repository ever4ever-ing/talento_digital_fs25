---
marp: true
theme: default
class: lead
---
# Consultas y Filtros Avanzados en Django ORM

---
## Modelo Producto

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField(default=True)
```

---
## Recuperar todos los registros

```python
from productos.models import Producto
productos = Producto.objects.all()
print(productos)
```

---
## Filtros básicos

**Precio mayor a 50:**
```python
productos_precio_mayor_50 = Producto.objects.filter(precio__gt=50)
for producto in productos_precio_mayor_50:
    print(producto.nombre, producto.precio)
```

**Nombre empieza con "A":**
```python
productos_nombre_a = Producto.objects.filter(nombre__startswith="A")
for producto in productos_nombre_a:
    print(producto.nombre)
```

**Productos disponibles:**
```python
productos_disponibles = Producto.objects.filter(disponible=True)
for producto in productos_disponibles:
    print(producto.nombre, producto.disponible)
```

---
## Consulta SQL con raw()

**Productos con precio menor a 100:**
```python
productos_menor_100 = Producto.objects.raw('SELECT * FROM productos WHERE precio < 1000')
for producto in productos_menor_100:
    print(producto.nombre, producto.precio)
```

---
## Consulta SQL con parámetros

```python
precio_limite = 100
productos_param = Producto.objects.raw('SELECT * FROM productos WHERE precio < %s', [precio_limite])
for producto in productos_param:
    print(producto.nombre, producto.precio)
```

---
## Consulta SQL personalizada y mapeo

```python
productos_custom = Producto.objects.raw('SELECT * FROM productos WHERE categoria = %s', ['General'])
for producto in productos_custom:
    print(producto.nombre, producto.categoria)
```

---
## Índices en Django

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    # ...otros campos...
```

---
## Excluir campo disponible

```python
productos_sin_disponible = Producto.objects.values('id', 'nombre', 'descripcion', 'precio', 'categoria', 'fecha_creacion')
for producto in productos_sin_disponible:
    print(producto)
```

---
## Anotación: precio con impuesto

```python
from django.db.models import F, ExpressionWrapper, DecimalField
productos_con_impuesto = Producto.objects.annotate(
    precio_con_impuesto=ExpressionWrapper(F('precio') * 1.16, output_field=DecimalField())
)
for producto in productos_con_impuesto:
    print(producto.nombre, producto.precio_con_impuesto)
```

---
## SQL personalizado (UPDATE)

```python
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("UPDATE productos_producto SET precio = precio * 1.10 WHERE precio < %s", [100])
    print("Precios actualizados")
```

---
## Conexión manual y recuperación

```python
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT nombre, precio FROM productos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```

---
## Crear procedimiento almacenado (MySQL)

```sql
DELIMITER //
CREATE PROCEDURE productos_baratos(IN precio_max DECIMAL(5,0))
BEGIN
    SELECT * FROM productos_producto WHERE precio < precio_max;
END //
DELIMITER ;
```

---
## Invocación a procedimiento almacenado

```python
from django.db import connection
with connection.cursor() as cursor:
    cursor.callproc('nombre_del_procedimiento', [param1, param2])
    results = cursor.fetchall()
    for result in results:
        print(result)
```

---
## Notas
- Para el filtro de productos disponibles, agrega `disponible = models.BooleanField(default=True)` al modelo.
- Para crear el índice, agrega `db_index=True` en el campo nombre del modelo.
- Los procedimientos almacenados deben existir en la base de datos.
