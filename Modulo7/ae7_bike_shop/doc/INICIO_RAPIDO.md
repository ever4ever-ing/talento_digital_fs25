# 🚀 Guía Rápida de Inicio - Autenticación y Permisos

## ✅ Implementación Completada

Se ha implementado un **sistema completo de autenticación**, **gestión de usuarios**, **grupos** y **permisos** en la aplicación Bike Shop.

---

## 🎯 Funcionalidades Principales

### ✨ Login/Registro
- ✅ Registro de nuevos usuarios
- ✅ Login con email y contraseña
- ✅ Logout seguro
- ✅ Protección CSRF
- ✅ Hashing de contraseñas

### 👥 Grupos
- ✅ **Cliente**: Acceso de lectura (ver catálogo)
- ✅ **Personal**: Acceso completo (crear, editar, eliminar)

### 🔐 Permisos
- ✅ `add_bicicleta`: Crear bicicletas
- ✅ `change_bicicleta`: Editar bicicletas
- ✅ `delete_bicicleta`: Eliminar bicicletas
- ✅ `view_bicicleta`: Ver bicicletas

### 👤 Gestión de Perfil
- ✅ Ver datos personales
- ✅ Editar dirección, teléfono, fecha de nacimiento
- ✅ Historial de compras (preparado para futuro)

---

## 📋 Pasos para Configurar

### 1️⃣ Crear Grupos y Permisos

Ejecuta este comando una sola vez:

```bash
python manage.py shell
```

Dentro del shell, pega:

```python
exec(open('setup_groups_permissions.py').read())
```

**O simplemente ejecuta:**

```bash
python crear_grupos.py
```

---

### 2️⃣ Crear un Usuario de Prueba (Personal)

```bash
# En el shell de Django
python manage.py shell
```

```python
from django.contrib.auth.models import User, Group
from app_clientes.models import Cliente, PerfilCliente

# Crear usuario
user = User.objects.create_user(
    username='personal@bikeshop.com',
    email='personal@bikeshop.com',
    password='PersonalPass123!',
    first_name='Juan'
)

# Asignar grupo Personal
personal_group = Group.objects.get(name='Personal')
user.groups.add(personal_group)

# Crear cliente y perfil asociado
cliente, _ = Cliente.objects.get_or_create(
    email=user.email,
    defaults={'nombre': user.first_name}
)
PerfilCliente.objects.get_or_create(cliente=cliente)

print("✅ Usuario Personal creado:")
print(f"   Email: {user.email}")
print(f"   Contraseña: PersonalPass123!")
```

---

### 3️⃣ Crear un Usuario de Prueba (Cliente)

```python
# En el shell de Django

# Crear usuario
user = User.objects.create_user(
    username='cliente@example.com',
    email='cliente@example.com',
    password='ClientePass123!',
    first_name='María'
)

# Asignar grupo Cliente
cliente_group = Group.objects.get(name='Cliente')
user.groups.add(cliente_group)

# Crear cliente y perfil
cliente, _ = Cliente.objects.get_or_create(
    email=user.email,
    defaults={'nombre': user.first_name}
)
PerfilCliente.objects.get_or_create(cliente=cliente)

print("✅ Usuario Cliente creado:")
print(f"   Email: {user.email}")
print(f"   Contraseña: ClientePass123!")
```

---

## 🌐 URLs Disponibles

| URL | Descripción | Necesita Autenticación | Necesita Permiso |
|-----|-------------|------------------------|--------------------|
| `/` | Ver catálogo | No | No |
| `/auth/registro/` | Registrarse | No | No |
| `/auth/login/` | Iniciar sesión | No | No |
| `/auth/logout/` | Cerrar sesión | ✅ Sí | No |
| `/auth/perfil/` | Mi perfil | ✅ Sí | No |
| `/crear/` | Crear bicicleta | ✅ Sí | ✅ Personal |
| `/actualizar/<id>/` | Editar bicicleta | ✅ Sí | ✅ Personal |
| `/eliminar/<id>/` | Eliminar bicicleta | ✅ Sí | ✅ Personal |

---

## 🧪 Pruebas Recomendadas

### Test 1: Acceso como Cliente

```
1. Ir a http://localhost:8000/auth/registro/
2. Registrarse con: 
   - Nombre: Test Cliente
   - Email: cliente@test.com
   - Contraseña: TestPass123!
3. Iniciar sesión
4. Intentar ir a http://localhost:8000/crear/
   → Debería ver: "Acceso Denegado" o ser redirigido
```

### Test 2: Acceso como Personal

```
1. Ir a http://localhost:8000/auth/login/
2. Iniciar sesión con: 
   - Email: personal@bikeshop.com
   - Contraseña: PersonalPass123!
3. Ver que en el catálogo aparecen botones de Editar/Eliminar
4. Crear una nueva bicicleta desde http://localhost:8000/crear/
5. Editar y eliminar bicicletas
```

### Test 3: Protección de Sesión

```
1. Iniciar sesión como usuario
2. Abrir http://localhost:8000/auth/logout/
3. Intentar acceder a /crear/ (sin autenticar)
4. Debería ser redirigido a /auth/login/
```

---

## 📁 Archivos Creados/Modificados

### ✅ Archivos Nuevos

- `app_clientes/forms.py` - Formularios de autenticación
- `app_clientes/urls.py` - Rutas de autenticación
- `app_clientes/templates/auth/registro.html` - Template de registro
- `app_clientes/templates/auth/login.html` - Template de login
- `app_clientes/templates/auth/perfil.html` - Template de perfil
- `setup_groups_permissions.py` - Script de inicialización
- `crear_grupos.py` - Script alternativo de inicialización
- `doc/AUTENTICACION_README.md` - Documentación completa
- `doc/EJEMPLOS_AUTENTICACION.md` - Ejemplos de uso

### ✅ Archivos Modificados

- `app_clientes/views.py` - Vistas de autenticación
- `app_bicicletas/views.py` - Vistas protegidas
- `app_bicicletas/templates/lista_bicicletas.html` - Interfaz actualizada
- `app_bicicletas/templates/crear_bicicleta.html` - Template mejorado
- `bikeshop/urls.py` - URLs actualizadas

---

## 🔒 Características de Seguridad

✅ **Contraseñas Hasheadas**: Django usa PBKDF2 por defecto
✅ **Protección CSRF**: Token en todos los formularios
✅ **Validación de Contraseñas**: Mínimo 8 caracteres, no números solamente
✅ **Sesiones Seguras**: Almacenadas en base de datos
✅ **Decoradores**: Protección a nivel de vista
✅ **Permisos Granulares**: Control por grupo y permiso específico

---

## 🚀 Inicio Rápido

```bash
# 1. Asegúrate de estar en el directorio del proyecto
cd C:\Users\Ever\DOJO\talento_digital_fs25\Modulo7\ae7_bike_shop

# 2. Ejecutar migraciones (si no lo has hecho)
python manage.py migrate

# 3. Crear grupos y permisos
python manage.py shell
# Dentro del shell:
exec(open('setup_groups_permissions.py').read())
exit()

# 4. Iniciar servidor
python manage.py runserver

# 5. Acceder en el navegador
# http://localhost:8000/
```

---

## 📚 Documentación Completa

Para más detalles, revisa:

1. **`doc/AUTENTICACION_README.md`** - Documentación técnica completa
2. **`doc/EJEMPLOS_AUTENTICACION.md`** - Ejemplos prácticos y curls
3. **Panel Admin** - Gestionar usuarios, grupos y permisos en `/admin/`

---

## 🆘 Solución de Problemas

### ❌ "ModuleNotFoundError: No module named 'bicicletas'"
✅ **Solución**: Ya fue solucionado. El nombre debe ser `app_bicicletas`.

### ❌ "403 Forbidden" al intentar crear bicicleta
✅ **Solución**: Tu usuario no está en el grupo "Personal". Asígnalo en el admin o con:
```python
user.groups.add(Group.objects.get(name='Personal'))
```

### ❌ "No module named 'app_clientes'"
✅ **Solución**: Asegúrate de que `'app_clientes'` está en `INSTALLED_APPS` en `settings.py`.

### ❌ "Grupos no creados"
✅ **Solución**: Ejecuta:
```bash
python manage.py shell
exec(open('setup_groups_permissions.py').read())
```

---

## 📞 Próximos Pasos

1. ✅ Sistema de autenticación
2. ⏳ Sistema de órdenes con autenticación
3. ⏳ Notificaciones por email
4. ⏳ API REST con permisos
5. ⏳ Descargas de reportes

---

**Última actualización**: 19 de noviembre de 2025

