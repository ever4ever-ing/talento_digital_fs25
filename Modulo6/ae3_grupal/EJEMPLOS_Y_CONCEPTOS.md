# 📖 EJEMPLOS DE USO Y CONCEPTOS EXPLICADOS

## 1. HERENCIA DE TEMPLATES 📋

### ¿Qué es?
La herencia permite crear un template "padre" con la estructura común (navbar, footer) 
y templates "hijos" que solo definen su contenido específico.

### Ejemplo en el proyecto:

**base.html (Template padre)**
```django
<!DOCTYPE html>
<html>
<head>...</head>
<body>
    <nav>...</nav>
    {% block content %}{% endblock %}
    <footer>...</footer>
</body>
</html>
```

**inicio.html (Template hijo)**
```django
{% extends 'base.html' %}
{% block content %}
    <h1>Mi contenido específico</h1>
{% endblock %}
```


## 2. ITERADORES (FOR LOOPS) 🔁

### ¿Para qué sirve?
Permite recorrer listas de objetos y mostrarlos dinámicamente.

### Ejemplo en lista_recetas.html:
```django
{% for receta in recetas %}
    <div class="card">
        <h5>{{ receta.nombre }}</h5>
        <p>{{ receta.get_descripcion_corta }}</p>
    </div>
{% endfor %}
```

### Si no hay datos:
```django
{% if recetas %}
    {% for receta in recetas %}
        ...
    {% endfor %}
{% else %}
    <p>No hay recetas disponibles</p>
{% endif %}
```


## 3. CONDICIONALES (IF/ELSE) ❓

### ¿Para qué sirve?
Permite mostrar contenido diferente según condiciones.

### Ejemplo en detalle_receta.html:
```django
{% if receta.imagen %}
    <img src="{{ receta.imagen.url }}" alt="{{ receta.nombre }}">
{% else %}
    <div class="placeholder-image">🍽️</div>
{% endif %}
```

### Otro ejemplo - Link activo en navbar:
```django
<a class="nav-link {% if request.resolver_match.url_name == 'inicio' %}active{% endif %}" 
   href="{% url 'recetas:inicio' %}">
    Inicio
</a>
```


## 4. URLS DINÁMICAS 🔗

### ¿Por qué usar {% url %}?
En lugar de URLs hardcodeadas, usa nombres de URL para mantener flexibilidad.

### ❌ MAL (URL hardcodeada):
```html
<a href="/recetas/1/">Ver receta</a>
```

### ✅ BIEN (URL dinámica):
```django
<a href="{% url 'recetas:detalle_receta' receta.pk %}">Ver receta</a>
```

### Ventajas:
- Si cambias la URL en urls.py, los links se actualizan automáticamente
- Más mantenible
- Previene errores


## 5. VISTAS Y CONTEXTO 👁️

### ¿Cómo funcionan?
Las vistas obtienen datos del modelo y los pasan al template.

### Ejemplo - views.py:
```python
def inicio(request):
    recetas = Receta.objects.all()[:6]  # Obtiene datos del modelo
    context = {
        'recetas': recetas  # Pasa datos al template
    }
    return render(request, 'inicio.html', context)
```

### Uso en template:
```django
{% for receta in recetas %}
    {{ receta.nombre }}
{% endfor %}
```


## 6. FORMULARIOS 📝

### ¿Cómo funciona el formulario de contacto?

### forms.py:
```python
class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
```

### views.py:
```python
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar formulario
            return redirect('recetas:confirmacion_contacto')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
```

### template:
```django
<form method="post">
    {% csrf_token %}
    {{ form.nombre }}
    {{ form.email }}
    {{ form.mensaje }}
    <button type="submit">Enviar</button>
</form>
```


## 7. MODELO DE DATOS 💾

### ¿Qué es un modelo?
Define la estructura de la base de datos.

### models.py:
```python
class Receta(models.Model):
    nombre = models.CharField(max_length=200)        # Texto corto
    ingredientes = models.TextField()                # Texto largo
    instrucciones = models.TextField()               # Texto largo
    imagen = models.ImageField(upload_to='recetas/') # Imagen
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Fecha automática
```

### Tipos de campos más comunes:
- `CharField`: Texto corto (max_length requerido)
- `TextField`: Texto largo
- `IntegerField`: Números enteros
- `ImageField`: Imágenes (requiere Pillow)
- `DateTimeField`: Fecha y hora


## 8. ARCHIVOS ESTÁTICOS 🎨

### ¿Cómo cargar archivos estáticos?

### En template:
```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

### Estructura:
```
static/
├── css/
│   └── styles.css
├── js/
│   └── script.js
└── images/
    └── logo.png
```


## 9. ARCHIVOS MEDIA (Imágenes subidas) 📸

### Diferencia: Static vs Media
- **Static**: Archivos del desarrollador (CSS, JS, imágenes del diseño)
- **Media**: Archivos subidos por usuarios (fotos de recetas)

### Configuración en settings.py:
```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Uso en template:
```django
{% if receta.imagen %}
    <img src="{{ receta.imagen.url }}" alt="{{ receta.nombre }}">
{% endif %}
```


## 10. REDIRECCIONES 🔀

### ¿Cuándo usar redirect()?
Después de procesar un formulario o acción exitosa.

### Ejemplo:
```python
from django.shortcuts import redirect

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar datos
            return redirect('recetas:confirmacion_contacto')  # Redirigir
```


## 11. MENSAJES FLASH 💬

### ¿Qué son?
Mensajes temporales que se muestran una vez.

### En vista:
```python
from django.contrib import messages

messages.success(request, 'Tu mensaje ha sido enviado.')
messages.warning(request, 'Por favor completa todos los campos.')
messages.error(request, 'Ocurrió un error.')
```

### En template:
```django
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
```


## 12. MANEJO DE ERRORES 404 ⚠️

### ¿Cómo funciona?

### views.py:
```python
from django.shortcuts import get_object_or_404

def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    # Si no existe, muestra 404 automáticamente
```

### urls.py (proyecto principal):
```python
handler404 = 'recetas.views.handler404'
```

### views.py (handler personalizado):
```python
def handler404(request, exception):
    return render(request, '404.html', status=404)
```


## 13. PANEL DE ADMINISTRACIÓN 👨‍💼

### ¿Cómo configurarlo?

### admin.py:
```python
from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')  # Columnas a mostrar
    search_fields = ('nombre', 'ingredientes')   # Campos buscables
    list_filter = ('fecha_creacion',)            # Filtros laterales
```

### Acceso:
1. Crear superusuario: `python manage.py createsuperuser`
2. Acceder: http://127.0.0.1:8000/admin/


## 14. MIGRACIONES 🔄

### ¿Qué son?
Sistema de control de versiones para la base de datos.

### Flujo:
1. **Crear modelo** en models.py
2. **Crear migración**: `python manage.py makemigrations`
3. **Aplicar migración**: `python manage.py migrate`

### Comandos útiles:
```bash
python manage.py showmigrations        # Ver migraciones
python manage.py sqlmigrate recetas 0001  # Ver SQL de una migración
```


## 15. CONSULTAS A LA BASE DE DATOS (ORM) 🔍

### Operaciones comunes:

```python
# Obtener todas las recetas
Receta.objects.all()

# Filtrar
Receta.objects.filter(nombre__contains='Pizza')

# Obtener una
Receta.objects.get(pk=1)

# Crear nueva
Receta.objects.create(nombre='Nueva Receta', ...)

# Contar
Receta.objects.count()

# Ordenar
Receta.objects.order_by('-fecha_creacion')

# Limitar resultados
Receta.objects.all()[:5]
```


## 16. RESPONSIVE DESIGN 📱

### Bootstrap Grid System:

```html
<div class="container">
    <div class="row">
        <div class="col-md-6 col-lg-4">
            <!-- En móvil: 100% ancho -->
            <!-- En tablet: 50% ancho -->
            <!-- En desktop: 33% ancho -->
        </div>
    </div>
</div>
```

### Breakpoints:
- `col-`: Móvil (<576px)
- `col-sm-`: Pequeño (≥576px)
- `col-md-`: Mediano (≥768px)
- `col-lg-`: Grande (≥992px)
- `col-xl-`: Extra grande (≥1200px)


## 17. CSRF PROTECTION 🔒

### ¿Qué es?
Protección contra ataques Cross-Site Request Forgery.

### SIEMPRE incluir en formularios POST:
```django
<form method="post">
    {% csrf_token %}
    ...
</form>
```

### Sin esto, Django rechazará el formulario por seguridad.


## 18. MÉTODO GET VS POST 📬

### GET:
- Obtener datos
- Parámetros en URL
- No modifica datos
- Ejemplo: Buscar, filtrar

### POST:
- Enviar datos
- Parámetros en cuerpo
- Modifica datos
- Ejemplo: Formularios, crear, actualizar

### En Django:
```python
if request.method == 'POST':
    # Procesar formulario
else:
    # Mostrar formulario vacío
```


## 19. CONTEXT PROCESSORS 🔄

### ¿Qué son?
Variables disponibles en TODOS los templates.

### En settings.py:
```python
TEMPLATES = [{
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',  # Acceso a request
            'django.contrib.messages.context_processors.messages',  # Mensajes
        ],
    },
}]
```


## 20. DEBUG MODE ⚙️

### En desarrollo:
```python
DEBUG = True  # Muestra errores detallados
```

### En producción:
```python
DEBUG = False  # Oculta errores por seguridad
ALLOWED_HOSTS = ['tu-dominio.com']
```

---

## 🎓 EJERCICIOS PROPUESTOS

1. **Agregar campo "tiempo de preparación"** al modelo Receta
2. **Crear filtro por categorías** (Postres, Platos Principales, etc.)
3. **Agregar sistema de valoraciones** (1-5 estrellas)
4. **Implementar búsqueda** de recetas por nombre
5. **Agregar paginación** (10 recetas por página)
6. **Crear vista de "Recetas Populares"**
7. **Agregar campo de autor** a las recetas
8. **Implementar newsletter** con email

---

💡 **TIP**: Experimenta con el código. ¡La mejor forma de aprender es haciendo!

🚀 **¡Feliz aprendizaje con Django!**
