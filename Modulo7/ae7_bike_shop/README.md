# Proyecto Django - BikeShop 🚴

Proyecto básico de Django para gestionar un catálogo de bicicletas.

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- MySQL Server instalado y en ejecución
- Cliente MySQL (MySQL Workbench o línea de comandos)

## Pasos para crear el proyecto desde cero

### 1. **Crear un entorno virtual**
```powershell
virtualenv venv
o
python -m venv venv
```

### 2. **Activar el entorno virtual**
```powershell
.\venv\Scripts\Activate
```

### 3. **Instalar Django y mysqlclient**
```powershell
pip install django mysqlclient
```

### 4. **Crear la base de datos en MySQL**
Conectarse a MySQL y ejecutar:
```sql
CREATE DATABASE bikeshop;
```

### 5. **Crear el proyecto Django**
```powershell
django-admin startproject bikeshop .
```

### 6. **Crear la aplicación**
```powershell
python manage.py startapp bicicletas
```

### 7. **Configurar la conexión a MySQL en settings.py**
Editar `bikeshop/settings.py` y reemplazar la configuración de `DATABASES`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bikeshop',
        'USER': 'root',          # Tu usuario de MySQL
        'PASSWORD': 'tu_password',  # Tu contraseña de MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 8. **Registrar la aplicación en settings.py**
Agregar la app en `INSTALLED_APPS` en `bikeshop/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bicicletas',  # <- Agregar esta línea
]
```

### 9. **Crear el modelo en models.py**
Editar `bicicletas/models.py`:
```python
from django.db import models

class Bicicleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)  # mtb, ruta, enduro, trail, bmx
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"
```

### 10. **Registrar el modelo en el admin**
Editar `bicicletas/admin.py`:
```python
from django.contrib import admin
from .models import Bicicleta

@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'tipo', 'precio', 'disponible', 'anio']
    list_filter = ['tipo', 'disponible']
    search_fields = ['marca', 'modelo']
```

### 11. **Crear las migraciones**
```powershell
python manage.py makemigrations
```

### 12. **Aplicar las migraciones**
```powershell
python manage.py migrate
```

### 13. **Crear la vista para listar bicicletas**
Editar `bicicletas/views.py`:
```python
from django.shortcuts import render
from .models import Bicicleta

def lista_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'bicicletas/lista_bicicletas.html', {'bicicletas': bicicletas})
```

### 14. **Crear la estructura de templates**
Crear el directorio `bicicletas/templates/bicicletas/` y dentro crear el archivo `lista_bicicletas.html`:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BikeShop - Catálogo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 20px;
            background: #f5f5f5;
        }
    </style>
</head>
<body>
    <h1>BikeShop - Catálogo de Bicicletas</h1>
    
    {% if bicicletas %}
        <table>
            <thead>
                <tr>
                    <th>Marca</th>
                    <th>Modelo</th>
                    <th>Tipo</th>
                    <th>Año</th>
                    <th>Precio</th>
                    <th>Disponibilidad</th>
                </tr>
            </thead>
            <tbody>
                {% for bici in bicicletas %}
                <tr>
                    <td>{{ bici.marca }}</td>
                    <td>{{ bici.modelo }}</td>
                    <td>{{ bici.tipo }}</td>
                    <td>{{ bici.anio }}</td>
                    <td>${{ bici.precio }}</td>
                    <td>
                        {% if bici.disponible %}
                            <span class="disponible">Disponible</span>
                        {% else %}
                            <span class="no-disponible">No disponible</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <div class="no-bikes">
            <p>No hay bicicletas en el catálogo.</p>
        </div>
    {% endif %}
    
    <div class="admin-link">
        <a href="/admin/">Ir al Panel de Administración</a>
    </div>
</body>
</html>
```

### 15. **Configurar las URLs de la aplicación**
Crear el archivo `bicicletas/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bicicletas, name='lista_bicicletas'),
]
```

### 16. **Configurar las URLs principales**
Editar `bikeshop/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bicicletas.urls')),
]
```

### 17. **Crear un superusuario**
```powershell
python manage.py createsuperuser
```
Sigue las instrucciones en pantalla para crear tu usuario administrador.

### 18. **Ejecutar el servidor**
```powershell
python manage.py runserver
```

### 19. **Acceder al proyecto**
- **Catálogo de Bicicletas**: http://127.0.0.1:8000/
- **Panel Admin**: http://127.0.0.1:8000/admin/

## Estructura del proyecto

```
bikeshop/
├── venv/                    # Entorno virtual
├── bikeshop/                # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py         # Configuración principal
│   ├── urls.py             # URLs principales
│   ├── asgi.py
│   └── wsgi.py
├── bicicletas/             # Aplicación de bicicletas
│   ├── migrations/         # Migraciones de la BD
│   ├── templates/          # Plantillas HTML
│   │   └── bicicletas/
│   │       └── lista_bicicletas.html
│   ├── __init__.py
│   ├── admin.py           # Configuración del admin
│   ├── apps.py
│   ├── models.py          # Modelos de datos
│   ├── tests.py
│   ├── urls.py            # URLs de la app
│   └── views.py           # Vistas
└── manage.py              # Script de gestión
```

## Configuración de MySQL

La base de datos utilizada es **MySQL**. Asegúrate de:

1. Tener MySQL Server instalado y en ejecución
2. Crear la base de datos `bikeshop`:
   ```sql
   CREATE DATABASE bikeshop;
   ```
3. Configurar las credenciales en `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'bikeshop',
           'USER': 'root',
           'PASSWORD': 'tu_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

## Modelo de datos: Bicicleta

El modelo `Bicicleta` contiene los siguientes campos:

- **marca**: Marca de la bicicleta (máx. 50 caracteres)
- **modelo**: Modelo de la bicicleta (máx. 50 caracteres)
- **tipo**: Tipo de bicicleta (mtb, ruta, enduro, trail, bmx) (máx. 20 caracteres)
- **precio**: Precio con 2 decimales
- **disponible**: Indica si está disponible para venta (por defecto: True)
- **anio**: Año de fabricación

## Vistas y Templates

### Vista de Lista de Bicicletas

La vista `lista_bicicletas` en `bicicletas/views.py` muestra todas las bicicletas del catálogo:

- **URL**: http://127.0.0.1:8000/
- **Template**: `bicicletas/templates/bicicletas/lista_bicicletas.html`
- **Características**:
  - Diseño minimalista con tabla
  - Estilos limpios y simples
  - Información clara y organizada
  - Indicadores de disponibilidad
  - Enlace directo al panel de administración

## Uso del panel de administración

1. Accede a http://127.0.0.1:8000/admin/
2. Ingresa con las credenciales del superusuario
3. Administra las bicicletas: agregar, editar, eliminar
4. Usa los filtros por tipo y disponibilidad
5. Busca bicicletas por marca o modelo
6. Las bicicletas agregadas aparecerán automáticamente en el catálogo principal

## Comandos útiles

```powershell
# Activar entorno virtual
.\venv\Scripts\Activate

# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Iniciar servidor de desarrollo
python manage.py runserver

# Crear superusuario adicional
python manage.py createsuperuser

# Acceder al shell de Django
python manage.py shell
```

## Notas adicionales

- Este proyecto utiliza **MySQL** como base de datos
- El servidor de desarrollo se ejecuta en http://127.0.0.1:8000/
- No olvides activar el entorno virtual antes de trabajar en el proyecto
- Asegúrate de que MySQL Server esté en ejecución antes de ejecutar migraciones
- Si tienes problemas con `mysqlclient`, en Windows puedes intentar: `pip install mysqlclient` o usar `pymysql` como alternativa

## Autor

Talento Digital - Módulo 7

## Licencia

Este proyecto es con fines educativos.
