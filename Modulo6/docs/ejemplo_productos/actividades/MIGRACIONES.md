# Migraciones en Django

## ¿Qué son las Migraciones?

Las migraciones en Django son archivos Python que contienen instrucciones para modificar la estructura de la base de datos. Son la forma que tiene Django de propagar los cambios que realizas en tus modelos (agregar un campo, eliminar un modelo, etc.) al esquema de tu base de datos.

## ¿Por qué son Importantes?

1. **Control de Versiones de la Base de Datos**: Las migraciones permiten versionar los cambios en la estructura de la base de datos junto con tu código.

2. **Colaboración en Equipo**: Todos los desarrolladores del equipo pueden aplicar los mismos cambios a sus bases de datos locales.

3. **Despliegue Consistente**: Garantizan que la base de datos en producción tenga la misma estructura que en desarrollo.

4. **Historial de Cambios**: Mantienen un registro de todos los cambios realizados en la base de datos a lo largo del tiempo.

## Tipos de Migraciones

### 1. Migración Inicial
La primera migración que se crea cuando defines un modelo por primera vez. Contiene las instrucciones para crear las tablas iniciales.

### 2. Migraciones de Esquema
Modifican la estructura de la base de datos:
- Agregar nuevos campos
- Eliminar campos existentes
- Cambiar tipos de datos
- Agregar o quitar índices
- Crear o eliminar tablas

### 3. Migraciones de Datos
Modifican los datos existentes en la base de datos:
- Migrar datos de un campo a otro
- Poblar nuevos campos con valores por defecto
- Limpiar datos inconsistentes

## Comandos Principales

### 1. Crear Migraciones
```bash
python manage.py makemigrations
```
**¿Qué hace?**
- Examina tus modelos actuales
- Los compara con el estado anterior
- Genera archivos de migración con los cambios necesarios

**Opciones útiles:**
```bash
# Crear migración para una aplicación específica
python manage.py makemigrations productos

# Crear migración vacía (para migraciones de datos personalizadas)
python manage.py makemigrations --empty productos

# Dar un nombre específico a la migración
python manage.py makemigrations --name agregar_campo_categoria productos
```

### 2. Aplicar Migraciones
```bash
python manage.py migrate
```
**¿Qué hace?**
- Ejecuta las migraciones pendientes
- Actualiza la estructura de la base de datos
- Registra qué migraciones se han aplicado

**Opciones útiles:**
```bash
# Migrar hasta una migración específica
python manage.py migrate productos 0001

# Migrar solo una aplicación específica
python manage.py migrate productos

# Mostrar qué migraciones se ejecutarían (sin aplicarlas)
python manage.py migrate --plan
```

### 3. Ver Estado de las Migraciones
```bash
python manage.py showmigrations
```
**Muestra:**
- Qué migraciones existen
- Cuáles se han aplicado (marcadas con [X])
- Cuáles están pendientes (marcadas con [ ])

### 4. Deshacer Migraciones
```bash
# Volver a una migración anterior
python manage.py migrate productos 0001

# Deshacer todas las migraciones de una aplicación
python manage.py migrate productos zero
```

## Estructura de un Archivo de Migración

### Ejemplo: 0001_initial.py
```python
from django.db import migrations, models

class Migration(migrations.Migration):
    # Indica si es la migración inicial
    initial = True

    # Lista de aplicaciones y migraciones de las que depende
    dependencies = [
    ]

    # Lista de operaciones a realizar
    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

### Componentes Principales:

1. **initial**: Indica si es la primera migración de la aplicación
2. **dependencies**: Lista de migraciones que deben ejecutarse antes
3. **operations**: Lista de operaciones a realizar en la base de datos

## Tipos de Operaciones Comunes

### 1. CreateModel
Crea una nueva tabla en la base de datos
```python
migrations.CreateModel(
    name='Producto',
    fields=[
        ('id', models.AutoField(primary_key=True)),
        ('nombre', models.CharField(max_length=100)),
    ],
)
```

### 2. DeleteModel
Elimina una tabla de la base de datos
```python
migrations.DeleteModel(
    name='Producto',
)
```

### 3. AddField
Agrega un campo a una tabla existente
```python
migrations.AddField(
    model_name='producto',
    name='categoria',
    field=models.CharField(max_length=50, default='General'),
)
```

### 4. RemoveField
Elimina un campo de una tabla
```python
migrations.RemoveField(
    model_name='producto',
    name='descripcion',
)
```

### 5. AlterField
Modifica un campo existente
```python
migrations.AlterField(
    model_name='producto',
    name='precio',
    field=models.DecimalField(decimal_places=3, max_digits=12),
)
```

### 6. RenameField
Renombra un campo
```python
migrations.RenameField(
    model_name='producto',
    old_name='descripcion',
    new_name='detalle',
)
```

## Migración de Datos Personalizada

### Ejemplo: Poblar datos iniciales
```python
from django.db import migrations

def crear_productos_iniciales(apps, schema_editor):
    Producto = apps.get_model('productos', 'Producto')
    Producto.objects.create(
        nombre='Producto de Ejemplo',
        precio=100.00,
        descripcion='Descripción del producto'
    )

def eliminar_productos_iniciales(apps, schema_editor):
    Producto = apps.get_model('productos', 'Producto')
    Producto.objects.filter(nombre='Producto de Ejemplo').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            crear_productos_iniciales,
            eliminar_productos_iniciales
        ),
    ]
```

## Buenas Prácticas

### 1. Hacer Migraciones Pequeñas y Frecuentes
- Es mejor hacer muchas migraciones pequeñas que pocas grandes
- Facilita la identificación de problemas
- Simplifica el proceso de reversión

### 2. Probar las Migraciones
```bash
# Aplicar migración en entorno de desarrollo
python manage.py migrate

# Probar reversión
python manage.py migrate productos 0001
python manage.py migrate productos 0002
```

### 3. Hacer Backup Antes de Migrar en Producción
```bash
# Ejemplo para PostgreSQL
pg_dump mi_base_datos > backup_antes_migracion.sql

# Ejemplo para MySQL
mysqldump mi_base_datos > backup_antes_migracion.sql
```

### 4. Verificar Migraciones Antes de Confirmar
```bash
# Ver qué se va a ejecutar
python manage.py migrate --plan

# Ver SQL que se ejecutará
python manage.py sqlmigrate productos 0002
```

### 5. Nunca Editar Migraciones Aplicadas
- Si una migración ya se aplicó en producción, no la edites
- Crea una nueva migración para hacer cambios adicionales

## Problemas Comunes y Soluciones

### 1. Conflictos de Migraciones
**Problema**: Dos desarrolladores crean migraciones con el mismo número
**Solución**: 
```bash
# Django puede resolver automáticamente
python manage.py makemigrations --merge
```

### 2. Migración Falsa (Fake)
**Problema**: Necesitas marcar una migración como aplicada sin ejecutarla
**Solución**:
```bash
python manage.py migrate --fake productos 0001
```

### 3. Resetear Migraciones
**Problema**: Las migraciones están muy enredadas
**Solución**:
```bash
# ¡CUIDADO! Esto borra todos los datos
python manage.py migrate productos zero
# Eliminar archivos de migración (excepto __init__.py)
# Crear nuevas migraciones
python manage.py makemigrations productos
python manage.py migrate
```

## Flujo de Trabajo Típico

### 1. Durante el Desarrollo
```bash
# 1. Modificar modelos en models.py
# 2. Crear migración
python manage.py makemigrations

# 3. Revisar la migración generada
cat productos/migrations/0002_add_categoria.py

# 4. Aplicar migración
python manage.py migrate

# 5. Probar la aplicación
python manage.py runserver
```

### 2. En Equipo
```bash
# 1. Obtener últimos cambios del repositorio
git pull origin main

# 2. Aplicar nuevas migraciones
python manage.py migrate

# 3. Continuar desarrollo...
```

### 3. En Producción
```bash
# 1. Hacer backup de la base de datos
# 2. Aplicar migraciones
python manage.py migrate

# 3. Verificar que todo funciona correctamente
# 4. Si hay problemas, restaurar backup y revertir código
```

## Comandos de Utilidad

### Ver SQL de una Migración
```bash
python manage.py sqlmigrate productos 0001
```

### Ver Migraciones sin Aplicar
```bash
python manage.py showmigrations --plan
```

### Simular Aplicación de Migraciones
```bash
python manage.py migrate --dry-run
```

### Obtener Información Detallada
```bash
python manage.py migrate --verbosity=2
```

## Conclusión

Las migraciones son una herramienta fundamental en Django que te permite:
- Mantener sincronizada la estructura de la base de datos con tu código
- Colaborar eficientemente en equipo
- Desplegar cambios de manera segura y consistente
- Mantener un historial completo de los cambios en la base de datos

Dominar las migraciones es esencial para cualquier desarrollador Django, ya que son una parte integral del ciclo de desarrollo y despliegue de aplicaciones.
