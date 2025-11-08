# Sistema de Control de Acceso y Permisos - Eventos Django

## 📋 Implementación Completa

### ✅ Componentes Implementados

#### 1. **Vista de Acceso Denegado (`403.html`)**
- Página personalizada y amigable para errores de permisos
- Diseño atractivo con Bootstrap
- Iconos y mensajes claros
- Botones de navegación hacia páginas permitidas
- Información sobre posibles razones del error

#### 2. **Mixin Personalizado de Permisos**
```python
PermissionDeniedMixin
```
- Maneja automáticamente errores de permisos
- Muestra mensajes personalizados al usuario
- Redirige a la página de acceso denegado
- Redirige al login si el usuario no está autenticado

#### 3. **Middleware de Permisos**
```python
PermissionDeniedMiddleware
```
- Captura excepciones de `PermissionDenied` a nivel de aplicación
- Redirige automáticamente a la página de acceso denegado
- Muestra mensajes de error apropiados

#### 4. **Vistas Protegidas Mejoradas**

**EditarEvento:**
- ✅ Verifica que el usuario sea el autor del evento
- ✅ Verifica permisos de edición (`app_eventos.change_evento`)
- ✅ Mensaje personalizado: "No tienes permiso para editar este evento. Solo el autor puede editarlo."
- ✅ Lanza `PermissionDenied` si intenta editar evento de otro usuario

**EliminarEvento:**
- ✅ Verifica que el usuario sea el autor del evento
- ✅ Verifica permisos de eliminación (`app_eventos.delete_evento`)
- ✅ Mensaje personalizado: "No tienes permiso para eliminar este evento. Solo el autor puede eliminarlo."
- ✅ Lanza `PermissionDenied` si intenta eliminar evento de otro usuario

**CrearEvento:**
- ✅ Solo usuarios autenticados pueden crear eventos
- ✅ Asigna automáticamente el autor al usuario actual
- ✅ Mensaje informativo si no está autenticado

#### 5. **Configuración del Proyecto**

**settings.py:**
- Middleware personalizado agregado
- Mapeo de mensajes a clases de Bootstrap
- Configuración de login/logout

**urls.py (principal):**
- Handler 403 personalizado configurado
- Ruta de acceso denegado agregada

### 🔒 Flujo de Control de Permisos

```
Usuario intenta acceder a recurso protegido
         ↓
¿Está autenticado?
         ↓ NO → Redirigir a /login/ con mensaje
         ↓ SÍ
¿Tiene los permisos necesarios?
         ↓ NO → PermissionDenied → Middleware → /acceso-denegado/ con mensaje
         ↓ SÍ
¿Es el autor del evento? (para editar/eliminar)
         ↓ NO → PermissionDenied → Middleware → /acceso-denegado/ con mensaje
         ↓ SÍ
✅ ACCESO CONCEDIDO
```

### 🧪 Casos de Prueba

#### Caso 1: Usuario no autenticado intenta crear evento
```
Resultado esperado:
- Redirige a /login/
- Mensaje: "⚠️ Debes iniciar sesión para crear eventos."
```

#### Caso 2: Usuario sin permisos intenta editar evento
```
Resultado esperado:
- Redirige a /acceso-denegado/
- Mensaje: "🚫 No tienes permiso para editar este evento. Solo el autor puede editarlo."
```

#### Caso 3: Usuario A intenta editar evento de Usuario B
```
Resultado esperado:
- Redirige a /acceso-denegado/
- Mensaje: "🚫 No puedes editar un evento que no te pertenece."
```

#### Caso 4: Usuario A intenta eliminar evento de Usuario B
```
Resultado esperado:
- Redirige a /acceso-denegado/
- Mensaje: "🚫 No puedes eliminar un evento que no te pertenece."
```

### 📝 Permisos de Django Utilizados

- `app_eventos.change_evento` - Para editar eventos
- `app_eventos.delete_evento` - Para eliminar eventos
- `app_eventos.add_evento` - Para crear eventos (implícito con LoginRequiredMixin)

### 🎨 Mensajes de Usuario

Todos los mensajes utilizan iconos emoji para mejor UX:
- ✓ - Éxito
- ⚠️ - Advertencia
- 🚫 - Error de permisos
- 📅 - Eventos
- 🔐 - Autenticación

### 🛠️ Configuración de Permisos por Usuario

Para otorgar permisos a un usuario:

```python
# En el admin de Django o en shell
from django.contrib.auth.models import User, Permission

user = User.objects.get(username='nombre_usuario')

# Dar permiso de editar eventos
permission = Permission.objects.get(codename='change_evento')
user.user_permissions.add(permission)

# Dar permiso de eliminar eventos
permission = Permission.objects.get(codename='delete_evento')
user.user_permissions.add(permission)

# O dar todos los permisos de eventos
from django.contrib.contenttypes.models import ContentType
from app_eventos.models import Evento

content_type = ContentType.objects.get_for_model(Evento)
permissions = Permission.objects.filter(content_type=content_type)
user.user_permissions.add(*permissions)
```

### 🚀 URLs Disponibles

- `/` - Lista de todos los eventos (público)
- `/mis_eventos/` - Eventos del usuario (requiere login)
- `/crear_evento/` - Crear nuevo evento (requiere login)
- `/editar_evento/<id>/` - Editar evento (requiere ser autor + permiso)
- `/eliminar_evento/<id>/` - Eliminar evento (requiere ser autor + permiso)
- `/acceso-denegado/` - Página de acceso denegado
- `/login/` - Iniciar sesión
- `/logout/` - Cerrar sesión

### 💡 Mejores Prácticas Implementadas

1. ✅ Uso de mixins de Django (LoginRequiredMixin, PermissionRequiredMixin)
2. ✅ Mixin personalizado para manejo consistente de errores
3. ✅ Middleware para captura global de excepciones de permisos
4. ✅ Mensajes de usuario claros y descriptivos
5. ✅ Verificación de autoría en get_object()
6. ✅ Página de error 403 personalizada y amigable
7. ✅ Separación de responsabilidades (vistas, middleware, templates)
8. ✅ Uso de raise_exception=False para redirigir en lugar de mostrar error
9. ✅ Configuración centralizada de handlers de error
10. ✅ Documentación clara del flujo de permisos

### 🎯 Seguridad Implementada

- ✅ Solo el autor puede editar sus propios eventos
- ✅ Solo el autor puede eliminar sus propios eventos
- ✅ Verificación de permisos a nivel de modelo
- ✅ Verificación de permisos a nivel de vista
- ✅ Protección CSRF en formularios
- ✅ Mensajes de error que no revelan información sensible
- ✅ Redirecciones seguras después de login

---

## 📚 Documentación Adicional

Para más información sobre el sistema de permisos de Django:
- https://docs.djangoproject.com/en/stable/topics/auth/default/
- https://docs.djangoproject.com/en/stable/topics/auth/customizing/

## 🎓 Autor
Sistema implementado siguiendo las mejores prácticas de Django para control de acceso y permisos.
