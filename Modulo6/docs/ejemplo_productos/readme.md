# Aplicación de Gestión de Productos con Django

Este proyecto es una aplicación web desarrollada con Django que permite gestionar un catálogo de productos. Incluye funcionalidades para listar productos existentes y registrar nuevos productos.

## Configuración del Entorno de Desarrollo

### 1. Crear y Activar el Entorno Virtual

En Windows:
```powershell
# Instalar virtualenv si no lo tienes
pip install virtualenv

# Crear entorno virtual
virtualenv venv

# Activar el entorno virtual
venv\Scripts\activate
```

En macOS/Linux:
```bash
# Instalar virtualenv si no lo tienes
pip install virtualenv

# Crear entorno virtual
virtualenv venv

# Activar el entorno virtual
source venv/bin/activate
```

### 2. Instalar Django
```bash
pip install django
```

### 3. Crear el Proyecto Django
```bash
django-admin startproject mi_tienda .
```

### 4. Crear la Aplicación de Productos
```bash
python manage.py startapp productos
```

### 5. Registrar la Aplicación en el Proyecto

En `mi_tienda/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos'  # Nuestra nueva aplicación
]
```


## Modelos de Datos

### 1. Definir el Modelo de Producto

En `productos/models.py`:
```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # blank=True permite que el campo esté vacío en formularios
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se añade la fecha automáticamente al crear

    def __str__(self):
        return self.nombre
```

### 2. Crear y Aplicar las Migraciones

```bash
# Crear migraciones basadas en los cambios en los modelos
python manage.py makemigrations

# Aplicar las migraciones a la base de datos
python manage.py migrate
```

## Formularios

### Crear Formulario para el Modelo Producto

En `productos/forms.py`:
```python
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Incluimos los campos que queremos que aparezcan en el formulario
        fields = ['nombre', 'descripcion', 'precio']
        # También podríamos personalizar los widgets, etiquetas, etc.
        # widgets = {
        #    'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        # }
```


## Vistas

### Crear las Vistas para Gestionar los Productos

En `productos/views.py`:
```python
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    """
    Vista para mostrar la lista de todos los productos.
    """
    productos = Producto.objects.all().order_by('-fecha_creacion')  # Los más nuevos primero
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def registrar_producto(request):
    """
    Vista para registrar un nuevo producto usando un formulario.
    """
    if request.method == 'POST':
        # Si el formulario ha sido enviado (es una petición POST)
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            # NOTA: Esto se corregirá más adelante para usar el espacio de nombres
            return redirect('productos:lista_productos')  # Redirige a la lista de productos
    else:
        # Si es la primera vez que se carga la página (petición GET)
        form = ProductoForm()

    # Renderiza la plantilla con el formulario
    return render(request, 'productos/registrar_producto.html', {'form': form})
```

## Plantillas HTML

### Estructura de Directorios para las Plantillas

```
productos/
└── templates/
    └── productos/
        ├── lista_productos.html
        └── registrar_producto.html
```

### 1. Plantilla para Listar Productos

En `productos/templates/productos/lista_productos.html`:
```html
<!-- productos/templates/productos/lista_productos.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Productos</title>
    <style>
        body { font-family: sans-serif; margin: 2em; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        a { display: inline-block; margin-top: 1em; padding: 8px 12px; background-color: #007bff; color: white; text-decoration: none; border-radius: 4px;}
    </style>
</head>
<body>
    <h1>Lista de Productos</h1>
    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Precio</th>
            </tr>
        </thead>
        <tbody>
            {% for producto in productos %}
            <tr>
                <td>{{ producto.nombre }}</td>
                <td>{{ producto.descripcion }}</td>
                <td>${{ producto.precio }}</td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="3">No hay productos registrados.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="{% url 'productos:registrar_producto' %}">Registrar Nuevo Producto</a>
</body>
</html>
```

### 2. Plantilla para Registrar Productos

En `productos/templates/productos/registrar_producto.html`:
```html
<!-- productos/templates/productos/registrar_producto.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registrar Producto</title>
    <style>
        body { font-family: sans-serif; margin: 2em; }
        form { display: flex; flex-direction: column; max-width: 400px; }
        form p { display: flex; flex-direction: column; }
        a { margin-top: 1em; }
    </style>
</head>
<body>
    <h1>Registrar Nuevo Producto</h1>
    <form method="post">
        {% csrf_token %}  <!-- Token de seguridad de Django, ¡muy importante! -->
        {{ form.as_p }}   <!-- Esto renderizará los campos del formulario como párrafos -->
        <button type="submit">Guardar Producto</button>
    </form>
    <a href="{% url 'productos:lista_productos' %}">Volver a la lista</a>
</body>
</html>
```

## Configuración de URLs

### 1. Configurar las URLs del Proyecto

En `mi_tienda/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),  # Incluye las URLs de la aplicación productos
]
```

### 2. Configurar las URLs de la Aplicación

En `productos/urls.py`:
```python
from django.urls import path
from . import views

# Define el espacio de nombres para evitar colisiones con otras aplicaciones
app_name = 'productos'

urlpatterns = [
    # Define aquí las rutas de la aplicación productos
    path('', views.lista_productos, name='lista_productos'),  # Ruta para listar productos
    path('registrar/', views.registrar_producto, name='registrar_producto'),  # Ruta para registrar productos
]
```

## Solución de Problemas Comunes

### Problema de URLs con Espacios de Nombres

Cuando se utiliza un espacio de nombres (`app_name = 'productos'`) en el archivo de URLs, es necesario referenciar las URLs usando el formato `'nombre_espacio:nombre_url'`.

#### 1. Corregir las Referencias en las Vistas

En `productos/views.py`:
```python
# Cambiar:
return redirect('lista_productos')  

# Por:
return redirect('productos:lista_productos')  # Incluir el espacio de nombres
```

#### 2. Corregir las Referencias en las Plantillas

En `productos/templates/productos/lista_productos.html`:
```html
<!-- Cambiar: -->
<a href="{% url 'registrar_producto' %}">Registrar Nuevo Producto</a>

<!-- Por: -->
<a href="{% url 'productos:registrar_producto' %}">Registrar Nuevo Producto</a>
```

En `productos/templates/productos/registrar_producto.html`:
```html
<!-- Cambiar: -->
<a href="{% url 'lista_productos' %}">Volver a la lista</a>

<!-- Por: -->
<a href="{% url 'productos:lista_productos' %}">Volver a la lista</a>
```

## Ejecución y Pruebas

### Iniciar el Servidor de Desarrollo
```bash
python manage.py runserver
```

### Acceder a la Aplicación
- Lista de productos: http://127.0.0.1:8000/productos/
- Registrar nuevo producto: http://127.0.0.1:8000/productos/registrar/

## Próximos Pasos

1. **Implementar la Autenticación de Usuarios**
   - Agregar registro y login de usuarios
   - Proteger las vistas con permisos

2. **Mejorar el Diseño de la Interfaz**
   - Integrar un framework CSS como Bootstrap
   - Crear un diseño responsivo

3. **Expandir las Funcionalidades**
   - Agregar opción de editar y eliminar productos
   - Implementar un carrito de compras
   - Añadir imágenes a los productos
