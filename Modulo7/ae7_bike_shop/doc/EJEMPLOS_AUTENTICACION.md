# 📖 Ejemplos de Uso - Autenticación y Permisos

## 1. Registro de Nuevo Usuario

**Ruta:** `GET/POST /auth/registro/`

```bash
# Acceder a la página de registro
GET http://localhost:8000/auth/registro/

# Enviar formulario (POST)
POST http://localhost:8000/auth/registro/
Body:
{
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "password1": "MiPassword123!",
    "password2": "MiPassword123!"
}

# Respuesta: Redirige a /auth/login/
```

---

## 2. Inicio de Sesión

**Ruta:** `GET/POST /auth/login/`

```bash
# Acceder a la página de login
GET http://localhost:8000/auth/login/

# Enviar credenciales (POST)
POST http://localhost:8000/auth/login/
Body:
{
    "username": "juan@example.com",
    "password": "MiPassword123!"
}

# Respuesta: Crea sesión y redirige a /
```

---

## 3. Cerrar Sesión

**Ruta:** `GET /auth/logout/`

```bash
GET http://localhost:8000/auth/logout/

# Respuesta: Destruye sesión y redirige a /
```

---

## 4. Ver/Editar Perfil

**Ruta:** `GET/POST /auth/perfil/`

```bash
# Ver perfil (requiere autenticación)
GET http://localhost:8000/auth/perfil/

# Editar perfil (POST)
POST http://localhost:8000/auth/perfil/
Body:
{
    "direccion": "Calle Principal 123",
    "telefono": "+34 612345678",
    "fecha_nacimiento": "1990-05-15"
}

# Respuesta: Actualiza y redirige a /auth/perfil/
```

---

## 5. Listar Bicicletas (Pública)

**Ruta:** `GET /`

```bash
# Acceso público (sin autenticación)
GET http://localhost:8000/

# Respuesta: Lista todas las bicicletas
# - Clientes: Solo ven el catálogo
# - Personal: Ven catálogo + botones de editar/eliminar
```

---

## 6. Crear Bicicleta (Protegida - Solo Personal)

**Ruta:** `GET/POST /crear/`

```bash
# Acceso solo para usuarios autenticados del grupo "Personal"
POST http://localhost:8000/crear/
Headers:
    Cookie: sessionid=...

Body (form-data):
    marca=Trek
    modelo=FX 3
    tipo=Urbana
    anio=2024
    precio=599.99
    disponible=true
    imagen=<archivo>

# Respuestas:
# - Sin autenticación: Redirige a /auth/login/
# - Grupo Cliente: 403 Forbidden
# - Grupo Personal: Crea bicicleta y redirige a /
```

---

## 7. Editar Bicicleta (Protegida - Solo Personal)

**Ruta:** `GET/POST /actualizar/<id>/`

```bash
# Acceso solo para usuarios autenticados del grupo "Personal"
POST http://localhost:8000/actualizar/1/
Headers:
    Cookie: sessionid=...

Body (form-data):
    marca=Trek
    modelo=FX 3
    tipo=Urbana
    anio=2024
    precio=699.99
    disponible=true

# Respuestas:
# - Sin autenticación: Redirige a /auth/login/
# - Grupo Cliente: 403 Forbidden
# - Grupo Personal: Actualiza y redirige a /
```

---

## 8. Eliminar Bicicleta (Protegida - Solo Personal)

**Ruta:** `GET /eliminar/<id>/`

```bash
# Acceso solo para usuarios autenticados del grupo "Personal"
GET http://localhost:8000/eliminar/1/
Headers:
    Cookie: sessionid=...

# Respuestas:
# - Sin autenticación: Redirige a /auth/login/
# - Grupo Cliente: 403 Forbidden
# - Grupo Personal: Elimina y redirige a /
```

---

## Ejemplos de Código Python

### Verificar si un usuario está autenticado

```python
from django.shortcuts import render, redirect

def mi_vista(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'template.html', {
        'usuario': request.user
    })
```

### Verificar si un usuario pertenece a un grupo

```python
def verificar_grupo(request):
    if request.user.groups.filter(name='Personal').exists():
        print("Es personal")
    elif request.user.groups.filter(name='Cliente').exists():
        print("Es cliente")
```

### Verificar permisos específicos

```python
def crear_bicicleta_view(request):
    if not request.user.has_perm('app_bicicletas.add_bicicleta'):
        raise PermissionDenied("No tienes permiso para crear bicicletas")
    
    # Código para crear bicicleta
```

### Obtener datos del usuario en template

```django
{% if user.is_authenticated %}
    <p>Bienvenido, {{ user.first_name }}</p>
    <p>Email: {{ user.email }}</p>
    
    {% if user.groups.all %}
        <p>Grupos: 
            {% for group in user.groups.all %}
                {{ group.name }}
            {% endfor %}
        </p>
    {% endif %}
    
    <a href="{% url 'logout' %}">Cerrar sesión</a>
{% else %}
    <p>Debes <a href="{% url 'login' %}">iniciar sesión</a></p>
{% endif %}
```

### Crear un usuario programáticamente

```python
from django.contrib.auth.models import User, Group

# Crear usuario
user = User.objects.create_user(
    username='usuario@example.com',
    email='usuario@example.com',
    password='MiPassword123!',
    first_name='Juan'
)

# Asignar a grupo
personal_group = Group.objects.get(name='Personal')
user.groups.add(personal_group)

# Asignar permiso específico
from django.contrib.auth.models import Permission
perm = Permission.objects.get(codename='add_bicicleta')
user.user_permissions.add(perm)
```

### Cambiar contraseña programáticamente

```python
from django.contrib.auth.models import User

user = User.objects.get(username='usuario@example.com')
user.set_password('NuevaPassword123!')
user.save()
```

---

## Flujo Completo de Un Nuevo Usuario

1. **Usuario accede a la app**
   ```
   GET http://localhost:8000/
   → Ve catálogo (sin autenticación)
   ```

2. **Se registra**
   ```
   POST /auth/registro/
   → Se crea User + Cliente + PerfilCliente
   → Se asigna al grupo "Cliente"
   ```

3. **Inicia sesión**
   ```
   POST /auth/login/
   → Django crea sesión
   ```

4. **Intenta crear bicicleta**
   ```
   GET /crear/
   → 403 Forbidden (solo Personal puede)
   ```

5. **Edita su perfil**
   ```
   POST /auth/perfil/
   → Actualiza datos personales
   ```

6. **Cierra sesión**
   ```
   GET /auth/logout/
   → Sesión destruida
   ```

---

## Curls de Prueba

```bash
# Registro
curl -X POST http://localhost:8000/auth/registro/ \
  -F "nombre=Test User" \
  -F "email=test@example.com" \
  -F "password1=TestPass123!" \
  -F "password2=TestPass123!"

# Login
curl -X POST http://localhost:8000/auth/login/ \
  -d "username=test@example.com&password=TestPass123!" \
  -c cookies.txt

# Ver catálogo con sesión
curl -b cookies.txt http://localhost:8000/

# Intentar crear (sin permisos)
curl -b cookies.txt http://localhost:8000/crear/
# Respuesta: 403 Forbidden

# Logout
curl -b cookies.txt http://localhost:8000/auth/logout/
```

---

## Códigos de Estado HTTP

| Código | Significado | Ejemplo |
|--------|------------|---------|
| 200 | OK | Página cargada correctamente |
| 302 | Redirect | Redirige a otra página |
| 403 | Forbidden | Usuario sin permisos |
| 404 | Not Found | Página no existe |
| 500 | Server Error | Error interno del servidor |

---

## Variables de Contexto Disponibles

En los templates tienes acceso a:

```django
{{ user.is_authenticated }}      → True/False
{{ user.username }}               → juan@example.com
{{ user.email }}                  → juan@example.com
{{ user.first_name }}             → Juan
{{ user.groups.all }}             → [Cliente, Personal]
{{ user.has_perm('...') }}        → True/False
{{ user.is_staff }}               → True/False
{{ user.is_superuser }}           → True/False
```

---

**Última actualización:** 19 de noviembre de 2025
