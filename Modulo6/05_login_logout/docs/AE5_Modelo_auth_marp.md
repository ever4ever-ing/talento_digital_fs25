---
marp: true
theme: default
paginate: true
class: lead
---

# Modelo Auth de Django

_Autenticación y autorización aplicada al proyecto Concesionaria_

---

## Objetivos de la lección

- Entender el modelo Auth de Django y sus componentes.
- Crear y administrar usuarios y superusuarios.
- Proteger vistas con `@login_required` y gestionar permisos.
- Aplicar autenticación al proyecto Concesionaria (protección de creación de autos).

---

## ¿Qué es el modelo Auth de Django?

- Sistema integrado en `django.contrib.auth`.
- Maneja usuarios, contraseñas, permisos y grupos.
- Proporciona funciones y utilidades listas para usar: `User`, `authenticate`, `login`, `logout`, `Permission`, `Group`.

---

## Componentes principales

- User: modelo con `username`, `email`, `password`, etc.
- Permissions: acciones específicas (`add`, `change`, `delete`, `view`).
- Groups: conjuntos de permisos reutilizables.
- Authentication: funciones para verificar credenciales.

---

## Seguridad que aporta Django

- CSRF: tokens en formularios para evitar forjado de peticiones.
- XSS: plantillas escapadas por defecto.
- SQL Injection: uso del ORM para consultas parametrizadas.
- Password hashing: Django nunca guarda contraseñas en texto plano.

---

## Password hashers (ejemplo)

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
```

---

## Crear usuarios (ejemplos)

```python
from django.contrib.auth.models import User

# Usuario normal
user = User.objects.create_user('cliente1', password='contrasena123')

# Superusuario
superuser = User.objects.create_superuser('admin', password='admin123')
```

- También puedes usar `python manage.py createsuperuser` (interactivo).

---

## Autenticación en vistas (ejemplo)

```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'autos/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'autos/login.html')
```

---

## Cierre de sesión (logout)

```python
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')
```

---

## Protegiendo vistas con decoradores

```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def lista_autos(request):
    ...

@login_required
@permission_required('app_autos.add_automovil', raise_exception=True)
def crear_auto(request):
    ...
```

- `@login_required` redirige al `LOGIN_URL` si el usuario no está autenticado.
- `@permission_required(..., raise_exception=True)` devuelve 403 si no hay permiso.

---

## Migraciones relacionadas con Auth

- Django crea las tablas de `auth` por defecto.
- Comandos útiles:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py migrate auth
```

---

## Aplicación práctica: Concesionaria — pasos

1. Crear usuario de prueba o superuser.
2. Añadir en `settings.py`:

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/autos/'
LOGOUT_REDIRECT_URL = '/login/'
```

3. Implementar `login_view`, `logout_view` y proteger vistas (`lista`, `crear`).
4. Crear plantillas: `login.html`, `crear_auto.html`, `lista.html`.

---

## URLs recomendadas (ejemplo)

```python
# proyecto urls.py
path('login/', autos_views.login_view, name='login')
path('logout/', autos_views.logout_view, name='logout')
path('autos/', include('app_autos.urls'))

# app_autos/urls.py
path('', views.lista_autos, name='lista_autos')
path('crear/', views.crear_auto, name='crear_auto')
```

---

## Plantilla mínima `login.html`

```html
<!DOCTYPE html>
<html lang="es">
<body>
  <form method="post">
    {% csrf_token %}
    <input name="username" required>
    <input name="password" type="password" required>
    <button type="submit">Entrar</button>
  </form>
</body>
</html>
```

---

## Probar el flujo (resumen rápido)

1. `python manage.py migrate`
2. `python manage.py createsuperuser`
3. `python manage.py runserver`
4. Abrir: `/login/` → `/autos/` → `/autos/crear/`

---

## Asignar permisos (admin o shell)

```python
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from app_autos.models import Automovil

user = User.objects.get(username='juan')
ct = ContentType.objects.get_for_model(Automovil)
perm = Permission.objects.get(codename='add_automovil', content_type=ct)
user.user_permissions.add(perm)
```

---

## Recomendaciones finales

- Usa `django.contrib.messages` para feedback de login/logout.
- Considera una plantilla base para nav/links (login/logout).
- Para producción revisa la configuración de seguridad y HTTPS.

---

## Fin

Archivo: `docs/AE5_Modelo_auth_marp.md` — listo para abrir con Marp o exportar a PDF/HTML.
