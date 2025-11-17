---
marp: true
theme: default
paginate: true
header: 'Gestión de Productos con Django'
footer: 'Talento Digital FS25 - Módulo 6'
---

# Aplicación de Gestión de Productos con Django

Una aplicación web completa para gestionar catálogos de productos

**Características:**
- ✅ Listar productos existentes
- ✅ Registrar nuevos productos
- ✅ Interfaz web intuitiva

---

## Configuración del Entorno de Desarrollo

### Windows (PowerShell)

```powershell
# Instalar virtualenv
pip install virtualenv

# Crear entorno virtual
virtualenv venv

# Activar el entorno virtual
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalación de Dependencias

```bash
# Instalar Django
pip install django

# Instalar widget tweaks para mejorar formularios
pip install django-widget-tweaks
```

---

## Creación del Proyecto

```bash
# Crear el proyecto Django
django-admin startproject mi_tienda .

# Crear la aplicación de productos
python manage.py startapp productos
```

---

## Registrar la Aplicación

En `mi_tienda/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos',  # ← Nuestra nueva aplicación
]
```

---

## Modelo de Datos: Producto

En `productos/models.py`:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=0)
    disponible = models.BooleanField(default=True)
    

    def __str__(self):
        return self.nombre
```

---

## Migraciones de Base de Datos

```bash
# Crear migraciones basadas en los modelos
python manage.py makemigrations

# Aplicar las migraciones a la base de datos
python manage.py migrate
```

**¿Qué hacen las migraciones?**
- Detectan cambios en los modelos
- Crean las tablas en la base de datos
- Mantienen sincronizada la estructura de datos

---

## Formularios: ProductoForm

En `productos/forms.py`:

```python
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']
```

**ModelForm** crea automáticamente un formulario basado en el modelo.

---

## Vistas: Lista de Productos

En `productos/views.py`:

```python
from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    """Vista para mostrar todos los productos."""
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'productos/lista_productos.html', 
                  {'productos': productos})
```

---

## Vistas: Registrar Producto

```python
from django.shortcuts import render, redirect
from .forms import ProductoForm

def registrar_producto(request):
    """Vista para registrar un nuevo producto."""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:lista_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'productos/registrar_producto.html', 
                  {'form': form})
```

---

## Estructura de Plantillas

```
productos/
└── templates/
    └── productos/
        ├── lista_productos.html
        └── registrar_producto.html
```

**Buena práctica:** Crear subdirectorio con el nombre de la app dentro de templates para evitar conflictos.

---

## Plantilla: Lista de Productos

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Productos</title>
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
```

---

## Plantilla: Lista de Productos (cont.)

```html
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
    <a href="{% url 'productos:registrar_producto' %}">
        Registrar Nuevo Producto
    </a>
</body>
</html>
```

---

## Plantilla: Registrar Producto

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registrar Producto</title>
</head>
<body>
    <h1>Registrar Nuevo Producto</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar Producto</button>
    </form>
    <a href="{% url 'productos:lista_productos' %}">Volver a la lista</a>
</body>
</html>
```

---

## Configuración de URLs del Proyecto

En `mi_tienda/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]
```

---

## Configuración de URLs de la Aplicación

En `productos/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'productos'  # ← Espacio de nombres

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('registrar/', views.registrar_producto, 
         name='registrar_producto'),
]
```

---

## Espacios de Nombres en URLs

**¿Por qué usar `app_name`?**

Evita conflictos cuando múltiples apps tienen URLs con el mismo nombre.

**Uso correcto:**
```python
# En vistas
return redirect('productos:lista_productos')

# En plantillas
{% url 'productos:registrar_producto' %}
```

---

## Problema Común: URLs sin Espacio de Nombres

❌ **Incorrecto:**
```python
return redirect('lista_productos')
```

✅ **Correcto:**
```python
return redirect('productos:lista_productos')
```

**Síntoma:** Error `NoReverseMatch` al intentar renderizar URLs.

---

## Ejecución del Servidor

```bash
# Iniciar el servidor de desarrollo
python manage.py runserver
```

**Acceder a la aplicación:**
- 🏠 Lista de productos: `http://127.0.0.1:8000/productos/`
- ➕ Registrar producto: `http://127.0.0.1:8000/productos/registrar/`

---

## Flujo de Trabajo Completo

1. **Usuario accede** → URL `/productos/`
2. **Django busca** → En `urls.py` la ruta correspondiente
3. **Ejecuta vista** → `lista_productos(request)`
4. **Vista consulta** → Base de datos con `Producto.objects.all()`
5. **Renderiza** → Plantilla con contexto
6. **Responde** → HTML al navegador

---

## Arquitectura MTV de Django

**Model-Template-View**

- **Model** (Modelo): Define estructura de datos
- **Template** (Plantilla): Define presentación HTML
- **View** (Vista): Lógica de negocio y controlador

Similar a MVC pero con diferencias en la nomenclatura.

---

## Próximos Pasos: Funcionalidades

1. **Autenticación de Usuarios**
   - Registro y login
   - Protección de vistas con permisos

2. **CRUD Completo**
   - Editar productos existentes
   - Eliminar productos
   - Búsqueda y filtrado

---

## Próximos Pasos: Mejoras

3. **Diseño Mejorado**
   - Integrar Bootstrap o Tailwind CSS
   - Diseño responsivo
   - Mejores formularios con widgets

4. **Funcionalidades Avanzadas**
   - Carrito de compras
   - Imágenes de productos
   - Categorías y etiquetas

---

## Conceptos Clave de Django

- **ORM**: Object-Relational Mapping
- **Migraciones**: Control de versiones de BD
- **CSRF Token**: Protección contra ataques
- **Template Tags**: Lógica en plantillas (`{% %}`, `{{ }}`)
- **URL Routing**: Sistema de rutas flexible

---

## Buenas Prácticas

✅ **Siempre usar espacios de nombres en URLs**
✅ **Validar formularios con `is_valid()`**
✅ **Usar `{% csrf_token %}` en formularios POST**
✅ **Ordenar queries con `.order_by()`**
✅ **Usar `blank=True` y `null=True` apropiadamente**
✅ **Crear migraciones después de cambios en modelos**

---

## Recursos Adicionales

- 📚 Documentación oficial: [docs.djangoproject.com](https://docs.djangoproject.com)
- 🎓 Django Tutorial: [djangoproject.com/start](https://www.djangoproject.com/start/)
- 💬 Comunidad: Django Forum, Stack Overflow
- 📦 Paquetes: [djangopackages.org](https://djangopackages.org)

---

## ¡Gracias!

### Preguntas y Respuestas

**Proyecto completo disponible en:**
`ae6_productos`

**Contacto y más información:**
Talento Digital FS25 - Módulo 6
