# Ejemplos avanzados de consultas y filtros en Django ORM
## Introducción sobre el modelo Producto

A partir del siguiente modelo:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField(default=True)
```

## Recuperar todos los registros de Producto
```python
from productos.models import Producto
productos = Producto.objects.all()
print(productos)
```

## 1. Productos con precio mayor a 50
```python
productos_precio_mayor_50 = Producto.objects.filter(precio__gt=50)
for producto in productos_precio_mayor_50:
    print(producto.nombre, producto.precio)
```

## 2. Productos cuyo nombre empieza con "A"
```python
productos_nombre_a = Producto.objects.filter(nombre__startswith="A")
for producto in productos_nombre_a:
    print(producto.nombre)
```

## 3. Productos disponibles (requiere campo disponible en el modelo)
```python
productos_disponibles = Producto.objects.filter(disponible=True)
for producto in productos_disponibles:
    print(producto.nombre, producto.disponible)
```

## 4. Consulta SQL con raw() para productos con precio menor a 100
```python
productos_menor_100 = Producto.objects.raw('SELECT * FROM productos_producto WHERE precio < 100')
for producto in productos_menor_100:
    print(producto.nombre, producto.precio)
```

## 5. Consulta SQL con parámetros en raw()
```python
precio_limite = 100
productos_param = Producto.objects.raw('SELECT * FROM productos_producto WHERE precio < %s', [precio_limite])
for producto in productos_param:
    print(producto.nombre, producto.precio)
```

## 6. Consulta SQL personalizada y mapeo al modelo
```python
productos_custom = Producto.objects.raw('SELECT * FROM productos_producto WHERE categoria = %s', ['General'])
for producto in productos_custom:
    print(producto.nombre, producto.categoria)
```

## 7. Crear índice en el campo nombre (en el modelo)
```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    # ...otros campos...
```

## 8. Excluir campo disponible usando values()
```python
productos_sin_disponible = Producto.objects.values('id', 'nombre', 'descripcion', 'precio', 'categoria', 'fecha_creacion')
```

## 9. Anotación de campo adicional precio_con_impuesto (16%)
```python
from django.db.models import F, ExpressionWrapper, DecimalField
productos_con_impuesto = Producto.objects.annotate(
    precio_con_impuesto=ExpressionWrapper(F('precio') * 1.16, output_field=DecimalField())
)
for producto in productos_con_impuesto:
    print(producto.nombre, producto.precio_con_impuesto)
```

## 10. Ejecutar SQL personalizado directamente (UPDATE)
```python
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("UPDATE productos_producto SET precio = precio * 1.10 WHERE precio < %s", [100])
```

## 11. Conexión manual y recuperación de datos
```python
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT nombre, precio FROM productos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```

## Cómo crear un procedimiento almacenado en SQLite
En SQLite, puedes crear un procedimiento almacenado usando una función definida por el usuario o, en bases como MySQL o PostgreSQL, con la instrucción `CREATE PROCEDURE`. Ejemplo en MySQL:

```sql
DELIMITER //
CREATE PROCEDURE productos_baratos(IN precio_max DECIMAL(5,0))
BEGIN
    SELECT * FROM productos_producto WHERE precio < precio_max;
END //
DELIMITER ;
```

En SQLite, deberás simularlo con una consulta parametrizada, ya que no soporta procedimientos almacenados nativos.

## 12. Invocación a procedimiento almacenado (ejemplo)
```python
from django.db import connection
with connection.cursor() as cursor:
    cursor.callproc('nombre_del_procedimiento', [param1, param2])
    results = cursor.fetchall()
    for result in results:
        print(result)
```

---
**Notas:**
- Para el filtro de productos disponibles, agrega `disponible = models.BooleanField(default=True)` al modelo.
- Para crear el índice, agrega `db_index=True` en el campo nombre del modelo.
- Los procedimientos almacenados deben existir en la base de datos.
