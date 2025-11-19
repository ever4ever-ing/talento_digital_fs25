# Ejemplos de Filtros en Django ORM

A continuación se muestran ejemplos prácticos de cómo usar filtros en consultas con Django ORM usando el modelo `Orden`.

## Importar el modelo
```python
from ordenes.models import Orden
```

## Filtrar órdenes pagadas
```python
ordenes_pagadas = Orden.objects.filter(estado='pagada')
for orden in ordenes_pagadas:
    print(orden.id, orden.cliente.nombre, orden.total)
```

## Tipos de filtros útiles

### 1. exact (Coincidencia exacta)
```python
ordenes = Orden.objects.filter(estado__exact='pendiente')
```

### 2. contains (Contiene una subcadena)
```python
ordenes = Orden.objects.filter(cliente__nombre__contains='Juan')
```

### 3. startswith / endswith (Empieza o termina con un valor)
```python
ordenes = Orden.objects.filter(cliente__nombre__startswith='A')
ordenes = Orden.objects.filter(cliente__nombre__endswith='z')
```

### 4. gte, lte (Mayor o igual / menor o igual)
```python
# Filtrar órdenes con total mayor o igual a 10000
ordenes = Orden.objects.filter(total__gte=10000)
# Filtrar órdenes con fecha menor o igual a hoy
from django.utils import timezone
ordenes = Orden.objects.filter(fecha__lte=timezone.now())
```

### 5. in (Filtrar por un conjunto de valores)
```python
ordenes = Orden.objects.filter(estado__in=['pagada', 'pendiente'])
```

---

Puedes combinar varios filtros para consultas más avanzadas:
```python
ordenes = Orden.objects.filter(estado='pagada', total__gte=5000)
```



## Ejemplos con el modelo Cliente

```python
from clientes.models import Cliente

# Coincidencia exacta
clientes_activos = Cliente.objects.filter(activo=True)

# Contiene subcadena
clientes_nombre = Cliente.objects.filter(nombre__contains='Juan')

# Empieza o termina con
clientes_apellido_a = Cliente.objects.filter(apellido__startswith='A')
clientes_apellido_z = Cliente.objects.filter(apellido__endswith='z')

# Mayor o igual / menor o igual (por ejemplo, edad)
clientes_mayores = Cliente.objects.filter(edad__gte=18)
clientes_menores = Cliente.objects.filter(edad__lte=65)

# Filtrar por conjunto de valores
clientes_ciudad = Cliente.objects.filter(ciudad__in=['Santiago', 'Valparaíso'])
```

Consulta la [documentación oficial de Django](https://docs.djangoproject.com/en/4.2/topics/db/queries/#retrieving-specific-objects-with-filters) para más detalles.
