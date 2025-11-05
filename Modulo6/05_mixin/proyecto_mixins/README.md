# 🎯 Blog con Mixins - Proyecto Django Educativo

Proyecto demostrativo del uso de **Mixins** en Django, específicamente `LoginRequiredMixin` y `PermissionRequiredMixin`.

## 📚 Descripción

Este proyecto implementa un sistema de blog simple que demuestra:

- ✅ **Vistas públicas** sin restricciones
- 🔒 **Vistas privadas** con `LoginRequiredMixin`
- 🔑 **Vistas con permisos** usando `PermissionRequiredMixin`
- ⚡ **Vistas combinadas** con múltiples mixins
- ✨ **Mixins personalizados** creados desde cero

## 🎓 Objetivos de Aprendizaje

1. Comprender qué es un mixin y su propósito
2. Aplicar `LoginRequiredMixin` para proteger vistas privadas
3. Usar `PermissionRequiredMixin` para control de acceso basado en permisos
4. Combinar múltiples mixins en una vista
5. Crear mixins personalizados

## 🏗️ Estructura del Proyecto

```
proyecto_mixins/
├── blog_project/           # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py        # Configuración principal
│   ├── urls.py            # URLs del proyecto
│   ├── wsgi.py
│   └── asgi.py
├── blog/                   # Aplicación blog
│   ├── __init__.py
│   ├── models.py          # Modelo Post
│   ├── views.py           # Vistas con mixins
│   ├── urls.py            # URLs de la app
│   ├── admin.py           # Configuración admin
│   ├── apps.py
│   └── tests.py           # Tests unitarios
├── templates/              # Templates HTML
│   ├── base.html          # Template base
│   └── blog/              # Templates de blog
│       ├── lista_posts.html
│       ├── mis_posts.html
│       ├── editar_post.html
│       ├── editar_mis_posts.html
│       ├── detalle_post.html
│       └── vista_mixin_personalizado.html
├── manage.py              # Comando principal de Django
└── README.md              # Este archivo
```

## 🚀 Instalación y Configuración

### 1. Crear entorno virtual (recomendado)

```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Si hay error de permisos en PowerShell:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Instalar Django

```powershell
pip install django
```

### 3. Aplicar migraciones

```powershell
cd proyecto_mixins
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario

```powershell
python manage.py createsuperuser
```

Sigue las instrucciones e ingresa:
- Nombre de usuario
- Email (opcional)
- Contraseña

### 5. Cargar datos de prueba (opcional)

```powershell
python manage.py shell
```

Luego en el shell de Django:

```python
from django.contrib.auth.models import User
from blog.models import Post

# Obtener el superusuario creado
user = User.objects.first()

# Crear posts de prueba
Post.objects.create(
    titulo="Introducción a Django",
    contenido="Django es un framework web de alto nivel escrito en Python...",
    autor=user
)

Post.objects.create(
    titulo="¿Qué son los Mixins?",
    contenido="Los mixins son clases que proporcionan funcionalidades adicionales...",
    autor=user
)

Post.objects.create(
    titulo="LoginRequiredMixin en acción",
    contenido="Este mixin protege vistas para que solo usuarios autenticados puedan acceder...",
    autor=user
)

print(f"✅ {Post.objects.count()} posts creados exitosamente")
exit()
```

### 6. Iniciar el servidor

```powershell
python manage.py runserver
```

Abre tu navegador en: `http://127.0.0.1:8000`

## 🎯 Vistas Implementadas

### 1. 📖 Vista Pública - Lista de Posts
- **URL:** `/`
- **Vista:** `ListaPosts`
- **Acceso:** Público (sin restricciones)
- **Descripción:** Muestra todos los posts del blog

### 2. 🔒 Vista Privada - Mis Posts
- **URL:** `/mis-posts/`
- **Vista:** `MisPosts`
- **Mixin:** `LoginRequiredMixin`
- **Acceso:** Solo usuarios autenticados
- **Descripción:** Muestra solo los posts del usuario logueado

### 3. 🔑 Vista con Permiso - Editar Posts
- **URL:** `/editar/`
- **Vista:** `EditarPost`
- **Mixin:** `PermissionRequiredMixin`
- **Permiso requerido:** `blog.change_post`
- **Acceso:** Solo usuarios con permiso
- **Descripción:** Permite editar posts si tienes el permiso

### 4. ⚡ Vista Combinada - Editar Mis Posts
- **URL:** `/editar-mis-posts/`
- **Vista:** `EditarMisPropioPosts`
- **Mixins:** `LoginRequiredMixin` + `PermissionRequiredMixin`
- **Permiso requerido:** `blog.can_edit_all_posts`
- **Acceso:** Autenticación + Permiso personalizado
- **Descripción:** Demuestra el uso combinado de múltiples mixins

### 5. ✨ Vista con Mixin Personalizado
- **URL:** `/mixin-personalizado/`
- **Vista:** `VistaConMixinPersonalizado`
- **Mixin:** `MensajeMixin` (personalizado)
- **Acceso:** Público
- **Descripción:** Muestra cómo crear y usar mixins propios

## 🔐 Gestión de Permisos

### Otorgar permisos a un usuario:

1. Ir al panel de administración: `http://127.0.0.1:8000/admin/`
2. Iniciar sesión con el superusuario
3. Ir a **Usuarios** → Seleccionar un usuario
4. En la sección **Permisos de usuario**:
   - Buscar "blog | post | Can change post"
   - Agregarlo a "Permisos elegidos"
   - Guardar

### Crear usuarios adicionales para pruebas:

```powershell
python manage.py shell
```

```python
from django.contrib.auth.models import User

# Usuario con todos los permisos
admin_user = User.objects.create_user('editor', 'editor@blog.com', 'pass123')
admin_user.is_staff = True
admin_user.save()

# Usuario normal sin permisos especiales
normal_user = User.objects.create_user('lector', 'lector@blog.com', 'pass123')
normal_user.save()

print("✅ Usuarios creados: editor (con permisos) y lector (sin permisos)")
exit()
```

## 🧪 Ejecutar Tests

```powershell
python manage.py test blog
```

## 📊 Casos de Prueba

### Probar LoginRequiredMixin:

1. **Sin autenticación:**
   - Ir a `/mis-posts/`
   - Debe redirigir al login

2. **Con autenticación:**
   - Iniciar sesión en `/admin/login/`
   - Ir a `/mis-posts/`
   - Debe mostrar tus posts

### Probar PermissionRequiredMixin:

1. **Usuario sin permiso:**
   - Iniciar sesión con un usuario sin permisos
   - Ir a `/editar/`
   - Debe mostrar error 403 Forbidden

2. **Usuario con permiso:**
   - Iniciar sesión con usuario que tenga `blog.change_post`
   - Ir a `/editar/`
   - Debe mostrar la vista de edición

### Probar mixins combinados:

1. Ir a `/editar-mis-posts/`
2. Requiere estar autenticado Y tener el permiso `blog.can_edit_all_posts`

## 💡 Conceptos Clave

### ¿Qué es un Mixin?

Un **mixin** es una clase que proporciona funcionalidades adicionales a otras clases sin formar parte de una jerarquía de herencia completa. Permite reutilizar código de forma modular.

### LoginRequiredMixin

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MiVista(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login/'
    template_name = 'mi_template.html'
```

- Verifica que `request.user.is_authenticated` sea True
- Si no, redirige a `login_url`
- Útil para contenido privado

### PermissionRequiredMixin

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class MiVista(PermissionRequiredMixin, TemplateView):
    permission_required = 'app.codename'
    raise_exception = True
```

- Verifica que el usuario tenga el permiso específico
- Si no, devuelve 403 o redirige
- Útil para control de acceso basado en roles

### Orden de Mixins

⚠️ **Importante:** El orden importa

```python
# ✅ CORRECTO
class MiVista(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    pass

# ❌ INCORRECTO (puede no funcionar como esperas)
class MiVista(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    pass
```

Python evalúa la herencia de **izquierda a derecha**.

## 🎨 Características del Proyecto

- ✅ Interfaz moderna y responsive
- ✅ Código comentado y documentado
- ✅ Ejemplos prácticos de cada tipo de mixin
- ✅ Tests unitarios incluidos
- ✅ Panel de administración configurado
- ✅ Mensajes informativos en cada vista
- ✅ Explicaciones pedagógicas en templates

## 📖 Recursos Adicionales

- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Django Auth Mixins](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.mixins.LoginRequiredMixin)
- [Class-based Views](https://docs.djangoproject.com/en/4.2/topics/class-based-views/)
- [Permisos en Django](https://docs.djangoproject.com/en/4.2/topics/auth/default/#permissions-and-authorization)

## 🤝 Contribuir

Este es un proyecto educativo. Siéntete libre de:
- Agregar más ejemplos de mixins
- Mejorar la documentación
- Crear nuevos casos de uso
- Reportar issues

## 📝 Licencia

Proyecto educativo para Talento Digital - BOTIC-SOFOF-24-28-13-0077

## ✨ Autor

Proyecto creado con fines educativos para demostrar el uso de Mixins en Django.

---

**¡Feliz aprendizaje! 🚀**
