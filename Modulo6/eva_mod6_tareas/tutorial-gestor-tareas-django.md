# Tutorial: Gestor de Tareas con Django

## Introducción

Este tutorial te guiará paso a paso para crear un gestor de tareas completo usando Django. El proyecto incluye autenticación de usuarios, gestión de tareas en memoria y una interfaz responsiva con Bootstrap.

---

## Parte 1: Configuración Inicial

### 1.1 Crear el Proyecto Django

1. **Activar el entorno virtual** (si no está activado):
   ```bash
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

2. **Instalar Django** (si no está instalado):
   ```bash
   pip install django
   ```

3. **Crear el proyecto Django**:
   ```bash
   django-admin startproject gestor_tareas
   cd gestor_tareas
   ```

### 1.2 Crear la Aplicación de Tareas

1. **Crear la aplicación `tareas`**:
   ```bash
   python manage.py startapp tareas
   ```

### 1.3 Configurar el Proyecto

1. **Editar `settings.py`** para registrar la aplicación:
   ```python
   # gestor_tareas/settings.py
   
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'tareas',  # Agregar esta línea
   ]
   ```

2. **Configurar idioma y zona horaria** (opcional):
   ```python
   # gestor_tareas/settings.py
   
   LANGUAGE_CODE = 'es-es'
   TIME_ZONE = 'America/Santiago'  # Ajustar según tu ubicación
   ```

### 1.4 Configuración de URLs

1. **Crear `urls.py` en la aplicación tareas**:
   ```python
   # tareas/urls.py
   
   from django.urls import path
   from . import views
   
   app_name = 'tareas'
   
   urlpatterns = [
       path('', views.lista_tareas, name='lista_tareas'),
       path('detalle/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
       path('agregar/', views.agregar_tarea, name='agregar_tarea'),
       path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
   ]
   ```

2. **Configurar URLs principales**:
   ```python
   # gestor_tareas/urls.py
   
   from django.contrib import admin
   from django.urls import path, include
   from django.shortcuts import redirect
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('tareas/', include('tareas.urls')),
       path('accounts/', include('django.contrib.auth.urls')),
       path('', lambda request: redirect('tareas:lista_tareas')),
   ]
   ```

---

## Parte 2: Vistas y Plantillas

### 2.1 Crear el Formulario para Tareas

1. **Crear `forms.py` en la aplicación tareas**:
   ```python
   # tareas/forms.py
   
   from django import forms
   
   class TareaForm(forms.Form):
       titulo = forms.CharField(
           max_length=200,
           widget=forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Título de la tarea'
           })
       )
       descripcion = forms.CharField(
           widget=forms.Textarea(attrs={
               'class': 'form-control',
               'rows': 4,
               'placeholder': 'Descripción de la tarea'
           }),
           required=False
       )
   ```

### 2.2 Crear las Vistas

1. **Editar `views.py`**:
   ```python
   # tareas/views.py
   
   from django.shortcuts import render, redirect
   from django.contrib.auth.decorators import login_required
   from django.http import Http404
   from django.contrib import messages
   from .forms import TareaForm
   
   # Almacenamiento en memoria - Diccionario por usuario
   tareas_por_usuario = {}
   contador_id = 0
   
   def obtener_tareas_usuario(user_id):
       """Obtiene las tareas del usuario o crea una lista vacía si no existe"""
       if user_id not in tareas_por_usuario:
           tareas_por_usuario[user_id] = []
       return tareas_por_usuario[user_id]
   
   @login_required
   def lista_tareas(request):
       """Vista para mostrar todas las tareas del usuario autenticado"""
       tareas = obtener_tareas_usuario(request.user.id)
       return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})
   
   @login_required
   def detalle_tarea(request, tarea_id):
       """Vista para mostrar los detalles de una tarea específica"""
       tareas = obtener_tareas_usuario(request.user.id)
       
       # Buscar la tarea por ID
       tarea = None
       for t in tareas:
           if t['id'] == tarea_id:
               tarea = t
               break
       
       if not tarea:
           raise Http404("La tarea no existe")
       
       return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})
   
   @login_required
   def agregar_tarea(request):
       """Vista para agregar una nueva tarea"""
       if request.method == 'POST':
           form = TareaForm(request.POST)
           if form.is_valid():
               global contador_id
               contador_id += 1
               
               nueva_tarea = {
                   'id': contador_id,
                   'titulo': form.cleaned_data['titulo'],
                   'descripcion': form.cleaned_data['descripcion'],
                   'usuario_id': request.user.id
               }
               
               tareas = obtener_tareas_usuario(request.user.id)
               tareas.append(nueva_tarea)
               
               messages.success(request, 'Tarea agregada exitosamente.')
               return redirect('tareas:lista_tareas')
       else:
           form = TareaForm()
       
       return render(request, 'tareas/agregar_tarea.html', {'form': form})
   
   @login_required
   def eliminar_tarea(request, tarea_id):
       """Vista para eliminar una tarea existente"""
       tareas = obtener_tareas_usuario(request.user.id)
       
       # Buscar y eliminar la tarea
       tarea_eliminada = False
       for i, tarea in enumerate(tareas):
           if tarea['id'] == tarea_id:
               del tareas[i]
               tarea_eliminada = True
               break
       
       if tarea_eliminada:
           messages.success(request, 'Tarea eliminada exitosamente.')
       else:
           messages.error(request, 'No se pudo eliminar la tarea.')
       
       return redirect('tareas:lista_tareas')
   ```

### 2.3 Crear las Plantillas

1. **Crear la estructura de directorios**:
   ```
   tareas/
   ├── templates/
   │   ├── tareas/
   │   │   ├── base.html
   │   │   ├── lista_tareas.html
   │   │   ├── detalle_tarea.html
   │   │   └── agregar_tarea.html
   │   └── registration/
   │       ├── login.html
   │       ├── register.html
   │       └── logged_out.html
   ```

2. **Crear plantilla base**:
   ```html
   <!-- tareas/templates/tareas/base.html -->
   
   <!DOCTYPE html>
   <html lang="es">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>{% block title %}Gestor de Tareas{% endblock %}</title>
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
   </head>
   <body>
       <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
           <div class="container">
               <a class="navbar-brand" href="{% url 'tareas:lista_tareas' %}">Gestor de Tareas</a>
               
               <div class="navbar-nav ms-auto">
                   {% if user.is_authenticated %}
                       <span class="navbar-text me-3">Hola, {{ user.username }}!</span>
                       <a class="nav-link" href="{% url 'admin:logout' %}">Cerrar Sesión</a>
                   {% else %}
                       <a class="nav-link" href="{% url 'admin:login' %}">Iniciar Sesión</a>
                   {% endif %}
               </div>
           </div>
       </nav>
   
       <div class="container mt-4">
           <!-- Mensajes de éxito/error -->
           {% if messages %}
               {% for message in messages %}
                   <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                       {{ message }}
                       <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                   </div>
               {% endfor %}
           {% endif %}
   
           {% block content %}
           {% endblock %}
       </div>
   
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
   </body>
   </html>
   ```

3. **Crear plantilla de lista de tareas**:
   ```html
   <!-- tareas/templates/tareas/lista_tareas.html -->
   
   {% extends 'tareas/base.html' %}
   
   {% block title %}Mis Tareas - Gestor de Tareas{% endblock %}
   
   {% block content %}
   <div class="d-flex justify-content-between align-items-center mb-4">
       <h1>Mis Tareas</h1>
       <a href="{% url 'tareas:agregar_tarea' %}" class="btn btn-primary">
           <i class="bi bi-plus-circle"></i> Nueva Tarea
       </a>
   </div>
   
   {% if tareas %}
       <div class="row">
           {% for tarea in tareas %}
               <div class="col-md-6 col-lg-4 mb-3">
                   <div class="card">
                       <div class="card-body">
                           <h5 class="card-title">{{ tarea.titulo }}</h5>
                           <p class="card-text">
                               {% if tarea.descripcion %}
                                   {{ tarea.descripcion|truncatewords:10 }}
                               {% else %}
                                   <em>Sin descripción</em>
                               {% endif %}
                           </p>
                           <div class="d-flex gap-2">
                               <a href="{% url 'tareas:detalle_tarea' tarea.id %}" class="btn btn-outline-primary btn-sm">
                                   Ver Detalle
                               </a>
                               <a href="{% url 'tareas:eliminar_tarea' tarea.id %}" 
                                  class="btn btn-outline-danger btn-sm"
                                  onclick="return confirm('¿Estás seguro de que quieres eliminar esta tarea?')">
                                   Eliminar
                               </a>
                           </div>
                       </div>
                   </div>
               </div>
           {% endfor %}
       </div>
   {% else %}
       <div class="text-center mt-5">
           <div class="alert alert-info">
               <h4>No tienes tareas aún</h4>
               <p>¡Agrega tu primera tarea para comenzar!</p>
               <a href="{% url 'tareas:agregar_tarea' %}" class="btn btn-primary">Agregar Tarea</a>
           </div>
       </div>
   {% endif %}
   {% endblock %}
   ```

4. **Crear plantilla de detalle de tarea**:
   ```html
   <!-- tareas/templates/tareas/detalle_tarea.html -->
   
   {% extends 'tareas/base.html' %}
   
   {% block title %}{{ tarea.titulo }} - Gestor de Tareas{% endblock %}
   
   {% block content %}
   <div class="row">
       <div class="col-md-8">
           <div class="card">
               <div class="card-header">
                   <h2>{{ tarea.titulo }}</h2>
               </div>
               <div class="card-body">
                   <h5>Descripción:</h5>
                   {% if tarea.descripcion %}
                       <p class="card-text">{{ tarea.descripcion|linebreaks }}</p>
                   {% else %}
                       <p class="text-muted"><em>Sin descripción</em></p>
                   {% endif %}
               </div>
               <div class="card-footer">
                   <div class="d-flex gap-2">
                       <a href="{% url 'tareas:lista_tareas' %}" class="btn btn-secondary">
                           Volver a la Lista
                       </a>
                       <a href="{% url 'tareas:eliminar_tarea' tarea.id %}" 
                          class="btn btn-danger"
                          onclick="return confirm('¿Estás seguro de que quieres eliminar esta tarea?')">
                           Eliminar Tarea
                       </a>
                   </div>
               </div>
           </div>
       </div>
   </div>
   {% endblock %}
   ```

5. **Crear plantilla para agregar tarea**:
   ```html
   <!-- tareas/templates/tareas/agregar_tarea.html -->
   
   {% extends 'tareas/base.html' %}
   
   {% block title %}Agregar Tarea - Gestor de Tareas{% endblock %}
   
   {% block content %}
   <div class="row justify-content-center">
       <div class="col-md-6">
           <div class="card">
               <div class="card-header">
                   <h2>Agregar Nueva Tarea</h2>
               </div>
               <div class="card-body">
                   <form method="post">
                       {% csrf_token %}
                       <div class="mb-3">
                           <label for="{{ form.titulo.id_for_label }}" class="form-label">Título:</label>
                           {{ form.titulo }}
                           {% if form.titulo.errors %}
                               <div class="text-danger">
                                   {% for error in form.titulo.errors %}
                                       <small>{{ error }}</small>
                                   {% endfor %}
                               </div>
                           {% endif %}
                       </div>
                       
                       <div class="mb-3">
                           <label for="{{ form.descripcion.id_for_label }}" class="form-label">Descripción:</label>
                           {{ form.descripcion }}
                           {% if form.descripcion.errors %}
                               <div class="text-danger">
                                   {% for error in form.descripcion.errors %}
                                       <small>{{ error }}</small>
                                   {% endfor %}
                               </div>
                           {% endif %}
                       </div>
                       
                       <div class="d-flex gap-2">
                           <button type="submit" class="btn btn-primary">Agregar Tarea</button>
                           <a href="{% url 'tareas:lista_tareas' %}" class="btn btn-secondary">Cancelar</a>
                       </div>
                   </form>
               </div>
           </div>
       </div>
   </div>
   {% endblock %}
   ```

---

## Parte 3: Autenticación y Seguridad

### 3.1 Configurar Autenticación

1. **Crear vista de registro personalizada**:
   ```python
   # tareas/views.py (agregar al archivo existente)
   
   from django.contrib.auth import login
   from django.contrib.auth.forms import UserCreationForm
   
   def registro(request):
       """Vista para registrar nuevos usuarios"""
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               user = form.save()
               login(request, user)
               messages.success(request, '¡Cuenta creada exitosamente!')
               return redirect('tareas:lista_tareas')
       else:
           form = UserCreationForm()
       
       return render(request, 'registration/register.html', {'form': form})
   ```

2. **Actualizar URLs para incluir registro**:
   ```python
   # tareas/urls.py (actualizar)
   
   from django.urls import path
   from . import views
   
   app_name = 'tareas'
   
   urlpatterns = [
       path('', views.lista_tareas, name='lista_tareas'),
       path('detalle/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
       path('agregar/', views.agregar_tarea, name='agregar_tarea'),
       path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
       path('registro/', views.registro, name='registro'),
   ]
   ```

### 3.2 Crear Plantillas de Autenticación

1. **Plantilla de login**:
   ```html
   <!-- tareas/templates/registration/login.html -->
   
   {% extends 'tareas/base.html' %}
   
   {% block title %}Iniciar Sesión - Gestor de Tareas{% endblock %}
   
   {% block content %}
   <div class="row justify-content-center">
       <div class="col-md-6">
           <div class="card">
               <div class="card-header">
                   <h2>Iniciar Sesión</h2>
               </div>
               <div class="card-body">
                   <form method="post">
                       {% csrf_token %}
                       <div class="mb-3">
                           <label for="id_username" class="form-label">Usuario:</label>
                           <input type="text" name="username" class="form-control" required id="id_username">
                       </div>
                       
                       <div class="mb-3">
                           <label for="id_password" class="form-label">Contraseña:</label>
                           <input type="password" name="password" class="form-control" required id="id_password">
                       </div>
                       
                       <div class="d-grid">
                           <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
                       </div>
                       
                       {% if form.errors %}
                           <div class="alert alert-danger mt-3">
                               {{ form.errors }}
                           </div>
                       {% endif %}
                   </form>
                   
                   <div class="text-center mt-3">
                       <p>¿No tienes cuenta? <a href="{% url 'tareas:registro' %}">Regístrate aquí</a></p>
                   </div>
               </div>
           </div>
       </div>
   </div>
   {% endblock %}
   ```

2. **Plantilla de registro**:
   ```html
   <!-- tareas/templates/registration/register.html -->
   
   {% extends 'tareas/base.html' %}
   
   {% block title %}Registro - Gestor de Tareas{% endblock %}
   
   {% block content %}
   <div class="row justify-content-center">
       <div class="col-md-6">
           <div class="card">
               <div class="card-header">
                   <h2>Crear Cuenta</h2>
               </div>
               <div class="card-body">
                   <form method="post">
                       {% csrf_token %}
                       {{ form.as_p }}
                       
                       <div class="d-grid">
                           <button type="submit" class="btn btn-primary">Registrarse</button>
                       </div>
                   </form>
                   
                   <div class="text-center mt-3">
                       <p>¿Ya tienes cuenta? <a href="{% url 'admin:login' %}">Inicia sesión aquí</a></p>
                   </div>
               </div>
           </div>
       </div>
   </div>
   {% endblock %}
   ```

3. **Plantilla de logout**:
   ```html
   <!-- tareas/templates/registration/logged_out.html -->
   
   {% extends 'tareas/base.html' %}
   
   {% block title %}Sesión Cerrada - Gestor de Tareas{% endblock %}
   
   {% block content %}
   <div class="row justify-content-center">
       <div class="col-md-6">
           <div class="card">
               <div class="card-body text-center">
                   <h2>Sesión Cerrada</h2>
                   <p>Has cerrado sesión exitosamente.</p>
                   <a href="{% url 'admin:login' %}" class="btn btn-primary">Iniciar Sesión Nuevamente</a>
               </div>
           </div>
       </div>
   </div>
   {% endblock %}
   ```

### 3.3 Configurar Redirects de Login

1. **Actualizar `settings.py`**:
   ```python
   # gestor_tareas/settings.py (agregar al final)
   
   # URLs de redirección para autenticación
   LOGIN_URL = '/accounts/login/'
   LOGIN_REDIRECT_URL = '/tareas/'
   LOGOUT_REDIRECT_URL = '/accounts/login/'
   ```

---

## Parte 4: Ejecutar el Proyecto

### 4.1 Migraciones y Servidor

1. **Ejecutar migraciones**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Crear superusuario** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

3. **Ejecutar servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

4. **Acceder a la aplicación**:
   - Abrir navegador en: `http://127.0.0.1:8000/`
   - Panel de administración: `http://127.0.0.1:8000/admin/`

### 4.2 Funcionalidades Implementadas

✅ **Gestión de Tareas**:
- Crear nuevas tareas
- Ver lista de tareas
- Ver detalles de tarea individual
- Eliminar tareas

✅ **Autenticación**:
- Registro de usuarios
- Inicio de sesión
- Cierre de sesión
- Protección de vistas con `@login_required`

✅ **Seguridad**:
- Cada usuario solo ve sus propias tareas
- Protección CSRF en formularios
- Aislamiento de datos por usuario

✅ **Interfaz**:
- Diseño responsivo con Bootstrap 5
- Mensajes de éxito/error
- Navegación intuitiva

---

## Conclusión

Has creado exitosamente un gestor de tareas completo con Django que incluye:

1. **Configuración del proyecto** con aplicación personalizada
2. **Vistas funcionales** para CRUD de tareas
3. **Plantillas responsive** con Bootstrap
4. **Sistema de autenticación** completo
5. **Seguridad** a nivel de usuario

Este proyecto sirve como base sólida para expandir funcionalidades como edición de tareas, categorías, fechas de vencimiento, y más.

### Próximos Pasos Sugeridos

- Agregar funcionalidad de editar tareas
- Implementar categorías o etiquetas
- Añadir fechas de vencimiento
- Migrar a base de datos en lugar de memoria
- Añadir paginación para listas largas
- Implementar búsqueda y filtros