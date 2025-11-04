# Pasos realizados — Login / Logout (concesionaria)

Este documento describe, paso a paso, los cambios aplicados al proyecto para implementar el flujo de login y logout, proteger vistas y cómo probarlo localmente.

## Archivos modificados/creados

- `mi_concesionaria/settings.py`
  - Añadidos:
    - `LOGIN_URL = '/login/'`
    - `LOGIN_REDIRECT_URL = '/autos/'`
    - `LOGOUT_REDIRECT_URL = '/login/'`
  - Propósito: Indicar a los decoradores y utilidades de autenticación dónde redirigir usuarios no autenticados y tras login/logout.

- `mi_concesionaria/urls.py`
  - Añadidas rutas de proyecto:
    - `path('login/', autos_views.login_view, name='login')`
    - `path('logout/', autos_views.logout_view, name='logout')`
    - `path('autos/', include('app_autos.urls'))`
  - Propósito: Exponer `login/` y `logout/` a nivel de proyecto y colocar la app bajo `/autos/`.

- `app_autos/views.py` (modificado)
  - Importaciones nuevas:
    - `authenticate`, `login`, `logout`
    - `login_required`, `permission_required`
  - Nuevas/actualizadas vistas:
    - `login_view(request)` — procesa POST de username/password, autentica y usa `login()`.
    - `logout_view(request)` — decorada con `@login_required`, llama `logout()` y redirige a `login`.
    - `lista_automoviles(request)` — ahora decorada con `@login_required`.
    - `crear_automovil(request)` — ahora decorada con `@login_required` y `@permission_required('app_autos.add_automovil', raise_exception=True)`.

- `app_autos/templates/login.html` (nuevo)
  - Plantilla mínima con formulario POST para `username` y `password` y manejo simple de `error`.

- `docs/login_logout_steps.md` (nuevo)
  - Este documento (el que estás leyendo) con el paso a paso.

## Detalle de cambios realizados (paso a paso)

1. Añadí las redirecciones en `mi_concesionaria/settings.py`.
   - Motivo: Los decoradores `@login_required` redirigen a `LOGIN_URL` cuando el usuario no está autenticado; `LOGIN_REDIRECT_URL` controla la redirección tras un login exitoso; `LOGOUT_REDIRECT_URL` controla la redirección tras cerrar sesión.

2. Añadí rutas en `mi_concesionaria/urls.py`.
   - Importé `app_autos.views` como `autos_views`.
   - Declaré `login/` y `logout/` a nivel de proyecto para evitar depender de rutas relativas dentro de la app.
   - Incluí la app bajo `autos/` para que el listado y creación queden en `/autos/` y `/autos/crear/`.

3. Implementé `login_view` en `app_autos/views.py`.
   - Lógica básica:
     - Si `request.method == 'POST'`, extraer `username` y `password` del `POST`.
     - Llamar `authenticate(request, username, password)`.
     - Si el usuario existe y está activo, llamar `login(request, user)` y redirigir a `lista_automoviles`.
     - Si las credenciales son inválidas, volver a mostrar `login.html` con `error`.
     - Si `GET`, mostrar `login.html` vacío.

4. Implementé `logout_view` en `app_autos/views.py`.
   - Decorada con `@login_required`.
   - Llama `logout(request)` y redirige a la ruta con nombre `login`.

5. Protegí `lista_automoviles` y `crear_automovil`.
   - `lista_automoviles` ahora requiere autenticación (`@login_required`).
   - `crear_automovil` requiere autenticación y permiso `app_autos.add_automovil`. Si el usuario no tiene permiso, se lanza un 403 (`raise_exception=True`).

6. Creé `login.html` con un formulario mínimo.

## Cómo probar localmente

1. Crear superusuario (si no existe):

```powershell
python manage.py createsuperuser
```

2. Levantar servidor de desarrollo:

```powershell
python manage.py runserver
```

3. Abrir en el navegador:

- Página de login: http://127.0.0.1:8000/login/
- Tras login exitoso debes ser redirigido a: http://127.0.0.1:8000/autos/
- Página para crear autos: http://127.0.0.1:8000/autos/crear/

4. Asignar permisos:

- Ir a http://127.0.0.1:8000/admin/ con el superusuario.
- Abrir un usuario y en la sección "User permissions" asignar "Can add automovil" (o el permiso correspondiente al modelo de la app).

O usar el shell para asignar permisos:

```powershell
python manage.py shell
```

```python
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from app_autos.models import Automovil

user = User.objects.get(username='juan')
content_type = ContentType.objects.get_for_model(Automovil)
perm = Permission.objects.get(codename='add_automovil', content_type=content_type)
user.user_permissions.add(perm)
```
