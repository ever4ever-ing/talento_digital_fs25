# 🔐 Sistema de Autenticación, Grupos y Permisos

## Descripción General

Se ha implementado un sistema completo de autenticación, gestión de usuarios, grupos y permisos en la aplicación Bike Shop. Este sistema controla:

- **Registro/Login**: Creación de nuevas cuentas de usuario
- **Sesiones seguras**: Gestión automática de sesiones
- **Contraseñas**: Hash seguro y validación
- **Grupos**: Cliente y Personal
- **Permisos**: Control granular de acciones

---

## 🎯 Casos de Uso

### 1. **Cliente** (Grupo por defecto)
- ✅ Ver catálogo de bicicletas
- ❌ NO puede crear, editar o eliminar bicicletas
- ✅ Puede editar su perfil

### 2. **Personal** (Grupo para empleados)
- ✅ Ver catálogo de bicicletas
- ✅ **Crear** nuevas bicicletas
- ✅ **Editar** bicicletas existentes
- ✅ **Eliminar** bicicletas
- ✅ Editar su perfil

---

## 📋 Configuración Inicial

### Paso 1: Crear los Grupos y Permisos

```bash
python manage.py shell
```

Dentro del shell:

```python
exec(open('setup_groups_permissions.py').read())
```

**Resultado esperado:**
```
✓ Grupos creados exitosamente:
  - Cliente (permisos: ver)
  - Personal (permisos: crear, editar, eliminar, ver)
```

### Paso 2: Crear un Usuario de Prueba (Personal)

```bash
python manage.py createsuperuser
# O usa el admin para crear usuarios regulares
```

Para agregar un usuario al grupo Personal:

```python
from django.contrib.auth.models import User, Group

user = User.objects.get(username='tu_usuario')
personal_group = Group.objects.get(name='Personal')
user.groups.add(personal_group)
```

---

## 🔗 URLs Disponibles

| Ruta | Descripción | Autenticación Requerida |
|------|-------------|----------------------|
| `/auth/registro/` | Página de registro | No |
| `/auth/login/` | Página de inicio de sesión | No |
| `/auth/logout/` | Cerrar sesión | Sí |
| `/auth/perfil/` | Ver/Editar perfil | Sí |
| `/` | Listar bicicletas | No |
| `/crear/` | Crear bicicleta | Sí + Grupo Personal |
| `/actualizar/<id>/` | Editar bicicleta | Sí + Grupo Personal |
| `/eliminar/<id>/` | Eliminar bicicleta | Sí + Grupo Personal |

---

## 🛡️ Decoradores Utilizados

### `@login_required(login_url='login')`
Requiere que el usuario esté autenticado. Si no lo está, lo redirige al login.

```python
@login_required(login_url='login')
def mi_vista(request):
    return render(request, 'template.html')
```

### `@user_passes_test(es_personal)`
Verifica si el usuario pertenece a un grupo específico.

```python
def es_personal(user):
    return user.groups.filter(name='Personal').exists()

@login_required
@user_passes_test(es_personal)
def crear_bicicleta(request):
    # Solo los del grupo Personal pueden acceder
    pass
```

### `@permission_required('app_bicicletas.add_bicicleta')`
Verifica si el usuario tiene un permiso específico.

```python
@permission_required('app_bicicletas.add_bicicleta', raise_exception=True)
def crear_bicicleta(request):
    pass
```

---

## 👤 Estructura del Usuario

### User (Django)
- `username`: Identificador único (se usa el email)
- `email`: Correo del usuario
- `password`: Contraseña (hasheada)
- `first_name`: Nombre completo
- `groups`: Grupos a los que pertenece
- `user_permissions`: Permisos específicos

### Cliente (Modelo Personalizado)
- `nombre`: Nombre del cliente
- `email`: Email único

### PerfilCliente (Modelo Personalizado)
- `cliente`: Referencia al cliente
- `direccion`: Dirección (opcional)
- `telefono`: Teléfono (opcional)
- `fecha_nacimiento`: Fecha de nacimiento (opcional)

---

## 📝 Flujo de Registro

1. Usuario accede a `/auth/registro/`
2. Completa el formulario (nombre, email, contraseña)
3. Django valida:
   - Email único
   - Contraseña segura
   - Confirmación de contraseña
4. Se crea el User (username = email)
5. Se crea el Cliente
6. Se crea el PerfilCliente
7. Se asigna al grupo **Cliente**
8. Usuario es redirigido al login

---

## 🔒 Flujo de Login

1. Usuario accede a `/auth/login/`
2. Ingresa email y contraseña
3. Django autentica las credenciales
4. Se crea la sesión
5. Usuario es redirigido al catálogo

---

## 🚪 Cerrar Sesión

```
GET /auth/logout/
→ Destruye la sesión
→ Redirige a la lista de bicicletas
```

---

## 🔑 Gestión de Permisos

### En el Admin de Django

1. Ir a: `http://localhost:8000/admin/`
2. Seleccionar **Grupos**
3. Editar "Cliente" o "Personal"
4. Asignar/remover permisos

### Permisos Disponibles para Bicicleta

- `add_bicicleta`: Crear bicicletas
- `change_bicicleta`: Editar bicicletas
- `delete_bicicleta`: Eliminar bicicletas
- `view_bicicleta`: Ver bicicletas

---

## 🧪 Pruebas Recomendadas

### 1. Registrar un Cliente Normal
```
→ Va a /auth/registro/
→ Rellena formulario
→ Se asigna al grupo "Cliente"
→ Puede ver catálogo pero NO editar
```

### 2. Crear un Usuario Personal
```
→ En admin, crear usuario
→ Asignarlo al grupo "Personal"
→ Puede crear, editar y eliminar bicicletas
```

### 3. Protección de Vistas
```
→ Usuario no autenticado intenta acceder a /crear/
→ Es redirigido a /auth/login/
→ Usuario autenticado (Cliente) intenta acceder a /crear/
→ Recibe acceso denegado (Unauthorized)
```

### 4. Cambio de Contraseña
```
→ Usuario puede cambiar contraseña desde /auth/perfil/
→ Django valida la nueva contraseña automáticamente
```

---

## 📚 Archivos Modificados

- ✅ `app_clientes/forms.py` - Formularios de registro, login y perfil
- ✅ `app_clientes/views.py` - Vistas de autenticación
- ✅ `app_clientes/urls.py` - URLs de autenticación
- ✅ `app_bicicletas/views.py` - Vistas protegidas
- ✅ `bikeshop/urls.py` - URLs del proyecto
- ✅ `app_clientes/templates/auth/` - Templates de autenticación
- ✅ `app_bicicletas/templates/lista_bicicletas.html` - Interfaz actualizada
- ✅ `setup_groups_permissions.py` - Script de inicialización

---

## ⚠️ Consideraciones de Seguridad

1. **Contraseñas**: Django usa PBKDF2 por defecto
2. **CSRF**: Protección CSRF habilitada ({% csrf_token %} en formularios)
3. **Sesiones**: Sesiones almacenadas en la base de datos
4. **Hash**: Las contraseñas nunca se almacenan en texto plano
5. **Decoradores**: Uso de decoradores para proteger vistas

---

## 🔧 Personalización Futura

### Agregar Nuevos Permisos
```python
class Meta:
    permissions = [
        ("can_export_data", "Can export data"),
        ("can_view_reports", "Can view reports"),
    ]
```

### Permisos Personalizados en Vistas
```python
def vista_personalizada(request):
    if not request.user.has_perm('app_bicicletas.can_export_data'):
        raise PermissionDenied
    # ... código ...
```

### Grupos Adicionales
```python
admin_group = Group.objects.create(name='Administrador')
admin_group.permissions.add(...)
```

---

## 🎓 Recursos de Aprendizaje

- [Django Authentication System](https://docs.djangoproject.com/en/5.2/topics/auth/)
- [Django Groups and Permissions](https://docs.djangoproject.com/en/5.2/topics/auth/default/#groups)
- [Django Password Validation](https://docs.djangoproject.com/en/5.2/topics/auth/passwords/)

---

**Implementado:** 19 de noviembre de 2025
