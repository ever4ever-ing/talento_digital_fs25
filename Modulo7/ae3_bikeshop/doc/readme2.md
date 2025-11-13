# Documentación: Creación de la App Clientes

## Fecha: 29 de octubre de 2025

---

## Resumen
Se creó una nueva aplicación Django llamada `clientes` con modelos para gestionar clientes y sus perfiles, implementando una relación OneToOne entre ambos.

---

## Pasos Realizados

### 1. Creación de la Aplicación
Se ejecutó el comando de Django para crear la nueva app:

```bash
python manage.py startapp clientes
```

Este comando generó la estructura básica de la aplicación con los siguientes archivos:
- `__init__.py`
- `admin.py`
- `apps.py`
- `models.py`
- `tests.py`
- `views.py`
- `migrations/`

---

### 2. Definición de Modelos

Se editó el archivo `clientes/models.py` para incluir dos modelos:

#### Modelo Cliente
```python
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
```

**Campos:**
- `nombre`: Campo de texto con máximo 100 caracteres
- `email`: Campo de email con restricción de unicidad
- `created_at`: Fecha/hora de creación (se establece automáticamente)

#### Modelo PerfilCliente
```python
class PerfilCliente(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"
```

**Campos:**
- `cliente`: Relación OneToOne con el modelo Cliente
  - `on_delete=models.CASCADE`: Si se elimina el cliente, se elimina el perfil
  - `related_name='perfil'`: Permite acceder al perfil desde el cliente como `cliente.perfil`
- `direccion`: Campo de texto opcional (máximo 200 caracteres)
- `telefono`: Campo de texto opcional (máximo 20 caracteres)
- `fecha_nacimiento`: Campo de fecha opcional

**Nota:** Los campos opcionales tienen `blank=True` y `null=True`, lo que permite que sean vacíos en formularios y en la base de datos.

---

### 3. Registro en Settings

Se agregó la aplicación `clientes` a la lista `INSTALLED_APPS` en `bikeshop/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bicicletas',
    'clientes',  # ← Nueva app agregada
]
```

Este paso es **crucial** para que Django reconozca la aplicación y sus modelos.

---

### 4. Creación de Migraciones

Se generaron las migraciones para crear las tablas en la base de datos:

```bash
python manage.py makemigrations clientes
```

**Resultado:**
```
Migrations for 'clientes':
  clientes\migrations\0001_initial.py
    + Create model Cliente
    + Create model PerfilCliente
```

Este comando creó el archivo `clientes/migrations/0001_initial.py` que contiene las instrucciones SQL necesarias para crear las tablas.

---

### 5. Aplicación de Migraciones

Se aplicaron las migraciones a la base de datos MySQL:

```bash
python manage.py migrate
```

**Resultado:**
```
Operations to perform:
  Apply all migrations: admin, auth, bicicletas, clientes, contenttypes, sessions
Running migrations:
  Applying clientes.0001_initial... OK
```

Este comando creó las siguientes tablas en la base de datos:
- `clientes_cliente`
- `clientes_perfilcliente`

---

## Estructura de la Base de Datos

### Tabla: clientes_cliente
| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | BigInt | PRIMARY KEY, AUTO_INCREMENT |
| nombre | VARCHAR(100) | NOT NULL |
| email | VARCHAR(254) | UNIQUE, NOT NULL |
| created_at | DATETIME | NOT NULL |

### Tabla: clientes_perfilcliente
| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | BigInt | PRIMARY KEY, AUTO_INCREMENT |
| cliente_id | BigInt | UNIQUE, FOREIGN KEY → clientes_cliente(id), ON DELETE CASCADE |
| direccion | VARCHAR(200) | NULL |
| telefono | VARCHAR(20) | NULL |
| fecha_nacimiento | DATE | NULL |

---

## Relación OneToOne

La relación **OneToOne** entre `Cliente` y `PerfilCliente` significa que:
- Cada cliente puede tener **exactamente un** perfil
- Cada perfil pertenece a **exactamente un** cliente
- Se puede acceder al perfil desde el cliente: `cliente.perfil`
- Se puede acceder al cliente desde el perfil: `perfil.cliente`

### Ejemplo de uso:
```python
# Crear un cliente
cliente = Cliente.objects.create(
    nombre="Juan Pérez",
    email="juan@example.com"
)

# Crear su perfil
perfil = PerfilCliente.objects.create(
    cliente=cliente,
    direccion="Calle Principal 123",
    telefono="+56912345678",
    fecha_nacimiento="1990-05-15"
)

# Acceder al perfil desde el cliente
print(cliente.perfil.direccion)  # "Calle Principal 123"

# Acceder al cliente desde el perfil
print(perfil.cliente.nombre)  # "Juan Pérez"
```

---

## Próximos Pasos Sugeridos

1. **Registrar los modelos en el Admin**:
   ```python
   # clientes/admin.py
   from django.contrib import admin
   from .models import Cliente, PerfilCliente
   
   admin.site.register(Cliente)
   admin.site.register(PerfilCliente)
   ```

2. **Crear vistas y templates** para listar, crear y editar clientes

3. **Configurar URLs** en `clientes/urls.py`

4. **Agregar validaciones personalizadas** si es necesario

5. **Crear formularios** para facilitar la entrada de datos

---

## Comandos Útiles

```bash
# Ver el SQL de las migraciones sin aplicarlas
python manage.py sqlmigrate clientes 0001

# Crear un superusuario para acceder al admin
python manage.py createsuperuser

# Iniciar el servidor de desarrollo
python manage.py runserver

# Abrir la consola interactiva de Django
python manage.py shell
```

---

## Notas Técnicas

- **Base de datos**: MySQL (configurada en `settings.py`)
- **Django version**: 5.2.7
- **Python version**: 3.12
- **Comportamiento CASCADE**: Si se elimina un cliente, automáticamente se elimina su perfil asociado
- **Email único**: No se pueden crear dos clientes con el mismo email

---

## Archivos Modificados/Creados

1. ✅ `clientes/` - Nueva carpeta de aplicación
2. ✅ `clientes/models.py` - Modelos Cliente y PerfilCliente
3. ✅ `clientes/migrations/0001_initial.py` - Migración inicial
4. ✅ `bikeshop/settings.py` - Agregada 'clientes' a INSTALLED_APPS
5. ✅ Base de datos MySQL - Creadas tablas correspondientes

---

## Verificación

Para verificar que todo está funcionando correctamente:

```bash
# 1. Verificar que las migraciones están aplicadas
python manage.py showmigrations clientes

# 2. Verificar en la consola de Django
python manage.py shell
>>> from clientes.models import Cliente, PerfilCliente
>>> Cliente.objects.count()  # Debería retornar 0
>>> PerfilCliente.objects.count()  # Debería retornar 0
```

---

*Documentación generada automáticamente - 29 de octubre de 2025*
