---
marp: true
theme: default
paginate: true
class: lead
---

# Login & Logout — Concesionaria

_Aplicación de autenticación y protección de vistas en Django_

---

## Objetivos

- Implementar login y logout funcionales.
- Proteger vistas con `@login_required` y `@permission_required`.
- Configurar redirecciones en `settings.py`.
- Probar el flujo completo (login → lista → crear → logout).

---

## Archivos modificados / creados

- `mi_concesionaria/settings.py` — añadidos `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`.
- `mi_concesionaria/urls.py` — rutas `login/`, `logout/`, `autos/`.
- `app_autos/views.py` — `login_view`, `logout_view`, protecciones con decoradores.
- `app_autos/templates/login.html` — plantilla mínima de login.
- `docs/login_logout_steps.md` — documentación paso a paso.

---

## settings.py 

```python
# Redirects for authentication views (login/logout)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/autos/'
LOGOUT_REDIRECT_URL = '/login/'
```

---

## urls.py 

```python
from app_autos import views as autos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', autos_views.login_view, name='login'),
    path('logout/', autos_views.logout_view, name='logout'),
    path('autos/', include('app_autos.urls')),
]
```

---

## views.py — login_view / logout_view (snippet)

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_automoviles')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
```

---

## Protecciones en vistas (snippet)

```python
@login_required
def lista_automoviles(request):
    autos = Automovil.objects.all()
    return render(request, 'lista.html', {'autos': autos})

@login_required
@permission_required('app_autos.add_automovil', raise_exception=True)
def crear_automovil(request):
    ...
```

---

## Plantilla de login (login.html)

```html
<form method="post">
  {% csrf_token %}
  <input name="username" required>
  <input name="password" type="password" required>
  <button type="submit">Entrar</button>
</form>
```

---

## Flujo de prueba (rápido)

1. Migraciones (si corresponde):

```powershell
python manage.py migrate
```

2. Crear superusuario:

```powershell
python manage.py createsuperuser
```

3. Levantar servidor:

```powershell
python manage.py runserver
```

4. Probar en navegador:
- http://127.0.0.1:8000/login/
- Tras login → http://127.0.0.1:8000/autos/
- Crear auto → http://127.0.0.1:8000/autos/crear/

---

## Asignar permisos (admin o shell)

- Desde Admin: Usuarios → seleccionar → User permissions → marcar "Can add automovil"

- Desde shell:

```powershell
python manage.py shell
```
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

## Notas y recomendaciones

- `LOGIN_URL` determina a dónde se envía un usuario no autenticado.
- `LOGIN_REDIRECT_URL` controla la página tras login.
- `@permission_required(..., raise_exception=True)` retorna 403 si el usuario no tiene permiso; considera usar redirecciones amigables según UX.

---

## Fin

