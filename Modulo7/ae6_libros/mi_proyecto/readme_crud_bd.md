# Explicación: Registro CRUD en la Base de Datos con Django

## ¿A qué base de datos se conecta el proyecto?

La configuración de la base de datos se encuentra en el archivo `settings.py` del proyecto. En este caso, el proyecto está conectado a una base de datos MySQL con los siguientes parámetros:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mi_base_de_datos',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Esto significa que los datos se almacenan en la base de datos llamada **mi_base_de_datos** en tu servidor local de MySQL.

---

## ¿Cómo se generan los registros de libros en la base de datos?

### 1. Definición del Modelo

El modelo `Libro` define la estructura de la tabla en la base de datos:

```python
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
```

Cuando ejecutas las migraciones, Django crea automáticamente una tabla llamada `gestion_libros_libro` en la base de datos.

---

### 2. Creación de registros (INSERT)

Cuando un usuario llena el formulario para crear un libro y lo envía, Django ejecuta internamente una consulta SQL similar a:

```sql
INSERT INTO gestion_libros_libro (titulo, autor, fecha_publicacion, numero_paginas)
VALUES ('El Quijote', 'Miguel de Cervantes', '1605-01-16', 863);
```

Esto se realiza mediante el método `form.save()` en la vista `crear_libro`.

---

### 3. Lectura de registros (SELECT)

Para mostrar la lista de libros, Django ejecuta una consulta como:

```sql
SELECT * FROM gestion_libros_libro;
```

Esto se hace en la vista `lista_libros` usando `Libro.objects.all()`.

---

### 4. Actualización de registros (UPDATE)

Cuando editas un libro, Django ejecuta una consulta similar a:

```sql
UPDATE gestion_libros_libro
SET titulo='Nuevo Título', autor='Nuevo Autor'
WHERE id=1;
```

Esto ocurre cuando usas `form.save()` en la vista `actualizar_libro` con una instancia existente.

---

### 5. Eliminación de registros (DELETE)

Cuando eliminas un libro, Django ejecuta:

```sql
DELETE FROM gestion_libros_libro WHERE id=1;
```

Esto se realiza en la vista `eliminar_libro` con `libro.delete()`.

---

---

## ORM de Django: Métodos y Funciones para CRUD

### ¿Qué es el ORM de Django?

El **ORM (Object-Relational Mapping)** de Django es una herramienta que permite interactuar con la base de datos usando código Python en lugar de escribir consultas SQL directamente. El ORM traduce automáticamente las operaciones de Python a consultas SQL.

---

## Métodos CRUD del ORM de Django

### 1. CREATE (Crear registros)

#### Método 1: Crear y guardar instancia
```python
# Crear una nueva instancia del modelo
libro = Libro(
    titulo='Cien años de soledad',
    autor='Gabriel García Márquez',
    fecha_publicacion='1967-06-05',
    numero_paginas=471
)
# Guardar en la base de datos
libro.save()
```

#### Método 2: Usar create()
```python
# Crear y guardar en una sola operación
libro = Libro.objects.create(
    titulo='Don Quijote de la Mancha',
    autor='Miguel de Cervantes',
    fecha_publicacion='1605-01-16',
    numero_paginas=863
)
```

#### Método 3: Usar get_or_create()
```python
# Crear solo si no existe
libro, created = Libro.objects.get_or_create(
    titulo='1984',
    defaults={
        'autor': 'George Orwell',
        'fecha_publicacion': '1949-06-08',
        'numero_paginas': 328
    }
)
```

#### Método 4: Creación en lote (bulk_create)
```python
# Crear múltiples registros de una vez
libros = [
    Libro(titulo='Libro 1', autor='Autor 1', fecha_publicacion='2023-01-01', numero_paginas=200),
    Libro(titulo='Libro 2', autor='Autor 2', fecha_publicacion='2023-02-01', numero_paginas=300),
]
Libro.objects.bulk_create(libros)
```

---

### 2. READ (Leer/Consultar registros)

#### Obtener todos los registros
```python
# Obtener todos los libros
todos_los_libros = Libro.objects.all()

# Obtener solo ciertos campos
libros_titulos = Libro.objects.values('titulo', 'autor')

# Obtener valores como tuplas
libros_tuplas = Libro.objects.values_list('titulo', 'autor')
```

#### Filtrar registros
```python
# Filtrar por campo específico
libros_cervantes = Libro.objects.filter(autor='Miguel de Cervantes')

# Filtrar con múltiples condiciones
libros_largos = Libro.objects.filter(numero_paginas__gt=500, fecha_publicacion__year__lt=2000)

# Excluir registros
libros_no_cervantes = Libro.objects.exclude(autor='Miguel de Cervantes')
```

#### Obtener un solo registro
```python
# Obtener por ID (lanza excepción si no existe)
libro = Libro.objects.get(id=1)

# Obtener el primero que coincida
primer_libro = Libro.objects.filter(autor='Gabriel García Márquez').first()

# Obtener el último
ultimo_libro = Libro.objects.last()

# Obtener o devolver None si no existe
libro = Libro.objects.filter(titulo='Inexistente').first()
```

#### Búsquedas avanzadas
```python
# Búsqueda que contenga texto
libros = Libro.objects.filter(titulo__icontains='quijote')

# Búsqueda que empiece con
libros = Libro.objects.filter(titulo__istartswith='el')

# Búsqueda por fecha
from datetime import date
libros = Libro.objects.filter(fecha_publicacion__gte=date(2000, 1, 1))

# Búsqueda en lista de valores
libros = Libro.objects.filter(autor__in=['García Márquez', 'Cervantes'])
```

#### Ordenamiento
```python
# Ordenar ascendente
libros_ordenados = Libro.objects.order_by('titulo')

# Ordenar descendente
libros_desc = Libro.objects.order_by('-fecha_publicacion')

# Ordenamiento múltiple
libros = Libro.objects.order_by('autor', '-numero_paginas')
```

#### Paginación y limitación
```python
# Obtener los primeros 5 libros
primeros_5 = Libro.objects.all()[:5]

# Obtener del 10 al 20
libros_10_20 = Libro.objects.all()[10:20]

# Contar registros
cantidad = Libro.objects.count()
```

---

### 3. UPDATE (Actualizar registros)

#### Método 1: Actualizar instancia específica
```python
# Obtener el libro a actualizar
libro = Libro.objects.get(id=1)
# Modificar campos
libro.titulo = 'Nuevo Título'
libro.numero_paginas = 500
# Guardar cambios
libro.save()
```

#### Método 2: Actualizar usando update()
```python
# Actualizar múltiples registros que cumplan condición
Libro.objects.filter(autor='Miguel de Cervantes').update(numero_paginas=900)

# Actualizar un solo registro
Libro.objects.filter(id=1).update(titulo='Título Actualizado')
```

#### Método 3: Actualizar o crear (update_or_create)
```python
# Actualizar si existe, crear si no existe
libro, created = Libro.objects.update_or_create(
    titulo='1984',
    defaults={
        'autor': 'George Orwell Actualizado',
        'numero_paginas': 350
    }
)
```

#### Método 4: Actualización en lote (bulk_update)
```python
# Actualizar múltiples objetos de una vez
libros = Libro.objects.filter(autor='García Márquez')
for libro in libros:
    libro.numero_paginas += 10

Libro.objects.bulk_update(libros, ['numero_paginas'])
```

---

### 4. DELETE (Eliminar registros)

#### Eliminar instancia específica
```python
# Obtener y eliminar
libro = Libro.objects.get(id=1)
libro.delete()
```

#### Eliminar múltiples registros
```python
# Eliminar todos los libros de un autor
Libro.objects.filter(autor='Autor a eliminar').delete()

# Eliminar todos los registros (¡CUIDADO!)
Libro.objects.all().delete()
```

#### Eliminar con condiciones
```python
# Eliminar libros con menos de 100 páginas
Libro.objects.filter(numero_paginas__lt=100).delete()

# Eliminar libros anteriores a cierta fecha
from datetime import date
Libro.objects.filter(fecha_publicacion__lt=date(1900, 1, 1)).delete()
```

---

## Métodos Auxiliares del ORM

### Agregaciones
```python
from django.db.models import Count, Sum, Avg, Max, Min

# Contar libros por autor
stats = Libro.objects.values('autor').annotate(total_libros=Count('id'))

# Promedio de páginas
promedio_paginas = Libro.objects.aggregate(Avg('numero_paginas'))

# Libro con más páginas
max_paginas = Libro.objects.aggregate(Max('numero_paginas'))
```

### Verificar existencia
```python
# Verificar si existe
existe = Libro.objects.filter(titulo='El Quijote').exists()

# Obtener o crear con verificación
if not Libro.objects.filter(titulo='Nuevo Libro').exists():
    Libro.objects.create(titulo='Nuevo Libro', autor='Autor', ...)
```

### Consultas relacionadas (si hay ForeignKey)
```python
# Si tienes un modelo Autor relacionado
libros_con_autor = Libro.objects.select_related('autor')

# Para relaciones Many-to-Many
libros_con_categorias = Libro.objects.prefetch_related('categorias')
```

---

## Transacciones y Operaciones Atómicas

```python
from django.db import transaction

# Operación atómica
@transaction.atomic
def crear_libros_atomico():
    Libro.objects.create(titulo='Libro 1', ...)
    Libro.objects.create(titulo='Libro 2', ...)
    # Si algo falla, se revierte todo

# Usando context manager
with transaction.atomic():
    libro1 = Libro.objects.create(titulo='Libro 1', ...)
    libro2 = Libro.objects.create(titulo='Libro 2', ...)
```

---

## Mejores Prácticas del ORM

1. **Usa select_related() y prefetch_related()** para optimizar consultas con relaciones
2. **Evita consultas N+1** usando las técnicas anteriores
3. **Usa bulk_create() y bulk_update()** para operaciones masivas
4. **Usa exists()** en lugar de len() o count() para verificar existencia
5. **Aprovecha las transacciones** para operaciones críticas
6. **Usa values() y values_list()** cuando solo necesites ciertos campos

---

## Resumen

- **Django ORM** traduce las acciones del usuario en operaciones SQL sobre la base de datos configurada.
- Los registros de libros se almacenan, consultan, actualizan y eliminan en la tabla `gestion_libros_libro` de la base de datos MySQL definida en `settings.py`.
- El **ORM** proporciona métodos Python intuitivos para todas las operaciones CRUD sin necesidad de escribir SQL.
- **Manager objects** (como `Libro.objects`) es el punto de entrada para todas las consultas a la base de datos.
- Todo el proceso es transparente para el usuario final, quien interactúa solo con formularios y vistas web.

---