# PASO A PASO PARA CREAR UN CRUD EN DJANGO (`gestion_libros`)

## 1. Crear la aplicación
```bash
python manage.py startapp gestion_libros
```

## 2. Definir el modelo Libro en `gestion_libros/models.py`
```python
from django.db import models
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
    def __str__(self):
        return self.titulo
```

## 3. Registrar el modelo en el admin (`gestion_libros/admin.py`)
```python
from .models import Libro
admin.site.register(Libro)
```

## 4. Crear el formulario en `gestion_libros/forms.py`
```python
from django import forms
from .models import Libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'numero_paginas']
```

## 5. Crear las vistas CRUD en `gestion_libros/views.py`
- crear_libro
- lista_libros
- actualizar_libro
- eliminar_libro

## 6. Crear el archivo `gestion_libros/urls.py` y definir las rutas
```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('actualizar/<int:pk>/', views.actualizar_libro, name='actualizar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
```

## 7. Agregar `'gestion_libros'` a `INSTALLED_APPS` en `settings.py`

## 8. Incluir las URLs de la app en `mi_proyecto/urls.py`
```python
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_libros/', include('gestion_libros.urls')),
]
```

## 9. Crear los templates HTML en `gestion_libros/templates/gestion_libros/`
- crear_libro.html
- lista_libros.html
- actualizar_libro.html

Ejemplo básico de cada template:

**lista_libros.html**
```html
<h1>Lista de Libros</h1>
<a href="{% url 'crear_libro' %}">Agregar libro</a>
<ul>
    {% for libro in libros %}
        <li>
            {{ libro.titulo }} - {{ libro.autor }} ({{ libro.fecha_publicacion }})
            <a href="{% url 'actualizar_libro' libro.pk %}">Editar</a>
            <a href="{% url 'eliminar_libro' libro.pk %}">Eliminar</a>
        </li>
    {% empty %}
        <li>No hay libros registrados.</li>
    {% endfor %}
</ul>
```

**crear_libro.html**
```html
<h1>Crear Libro</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
</form>
<a href="{% url 'lista_libros' %}">Volver a la lista</a>
```

**actualizar_libro.html**
```html
<h1>Actualizar Libro</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Actualizar</button>
</form>
<a href="{% url 'lista_libros' %}">Volver a la lista</a>
```

## 10. Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

## 11. Ejecutar el proyecto

1. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
3. Abre tu navegador en: [http://localhost:8000/gestion_libros/](http://localhost:8000/gestion_libros/)

¡Listo! Ya puedes usar el CRUD de libros en tu proyecto Django.
