# Solución: Consultas y operaciones avanzadas con Django ORM y SQL

---

## 1. Modelo Producto

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)  # Índice en nombre
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField()
```

---

## 2. Recuperando todos los registros

```python
productos = Producto.objects.all()
```

---

## 3. Aplicando Filtros

```python
# Productos con precio mayor a 50
productos_precio_mayor_50 = Producto.objects.filter(precio__gt=50)

# Productos cuyo nombre empieza con "A"
productos_nombre_a = Producto.objects.filter(nombre__startswith="A")

# Productos disponibles
productos_disponibles = Producto.objects.filter(disponible=True)
```

---

## 4. Ejecutando Queries SQL con raw()

```python
productos_menor_100 = Producto.objects.raw('SELECT * FROM app_producto WHERE precio < 100')
```

---

## 5. Mapeando campos con raw()

```python
# Si los campos coinciden con el modelo, el mapeo es automático
productos = Producto.objects.raw('SELECT id, nombre, precio, disponible FROM app_producto WHERE disponible=1')
```

---

## 6. Índices en Django

**¿Qué son?**  
Los índices en bases de datos permiten búsquedas más rápidas en columnas específicas.  
**En Django:**  
Se pueden crear con `db_index=True` en el campo del modelo.

**Impacto:**  
Las búsquedas por nombre serán más rápidas, especialmente con grandes volúmenes de datos.

---

## 7. Exclusión de campos del modelo

```python
# Excluir el campo 'disponible'
productos = Producto.objects.values('id', 'nombre', 'precio')
```

**Explicación:**  
Django solo recupera los campos especificados, omitiendo los demás. Esto reduce el tamaño de los datos transferidos y puede mejorar el rendimiento.

---

## 8. Añadiendo anotaciones en consultas

```python
from django.db.models import F, ExpressionWrapper, DecimalField

productos = Producto.objects.annotate(
    precio_con_impuesto=ExpressionWrapper(F('precio') * 1.16, output_field=DecimalField(max_digits=6, decimal_places=2))
)
for p in productos:
    print(p.nombre, p.precio_con_impuesto)
```

---

## 9. raw() con parámetros

```python
precio_limite = 80
productos = Producto.objects.raw('SELECT * FROM app_producto WHERE precio < %s', [precio_limite])
```

**Diferencia y beneficios:**  
Usar parámetros evita inyección SQL y permite consultas dinámicas y seguras.

---

## 10. SQL personalizado con connection.cursor()

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("UPDATE app_producto SET disponible=0 WHERE precio > 100")
```

**¿Cuándo usarlo?**  
Cuando necesitas operaciones complejas, masivas o no soportadas por el ORM.

---

## 11. Conexiones y cursores

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT nombre, precio FROM app_producto")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```

**Ventajas:**  
- Más control y flexibilidad.
- Permite ejecutar SQL nativo.

**Desventajas:**  
- Menos seguro y más propenso a errores.
- No aprovecha las ventajas del ORM (validaciones, mapeo automático, etc).

---

## 12. Procedimientos almacenados

**¿Qué son?**  
Funciones SQL almacenadas en la base de datos para lógica compleja o reutilizable.

**Uso en Django:**

```python
with connection.cursor() as cursor:
    cursor.callproc('nombre_del_procedimiento', [param1, param2])
    results = cursor.fetchall()
```

---

**Fin de la solución.**