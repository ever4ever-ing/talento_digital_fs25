---
marp: true
theme: gaia
paginate: true
---

# 🎉 Sistema de Gestión de Eventos
## Aplicación Django

Control completo de eventos con autenticación y permisos

---

## 📋 Índice

1. 🎯 **Descripción General**
2. 🏗️ **Arquitectura del Proyecto**
3. 🔐 **Sistema de Seguridad**
4. 💾 **Modelos de Datos**
5. 🎭 **Vistas y Funcionalidades**
6. 🚀 **Instalación y Uso**
7. 📊 **Casos de Uso**

---

## 🎯 Descripción General

### ¿Qué es?
Sistema web para **crear, editar, eliminar y listar eventos** con control de acceso basado en roles y permisos.

### Características principales:
- ✅ Autenticación de usuarios
- ✅ Sistema de permisos granular
- ✅ Eventos públicos y privados
- ✅ Interfaz intuitiva con mensajes

---

## 🏗️ Arquitectura del Proyecto

```
ae5_eventos_mixin/
├── config/          # Configuración Django
│   ├── settings.py  # Settings
│   └── urls.py      # URLs principales
├── events/          # App principal
│   ├── models.py    # Modelo Event
│   ├── views.py     # Vistas CBV/FBV
│   ├── forms.py     # Formularios
│   └── urls.py      # URLs de eventos
└── templates/       # Templates HTML
```

---

## 🔐 Sistema de Seguridad

### Capas de Protección:

| Capa | Implementación |
|------|----------------|
| **1. Autenticación** | `LoginRequiredMixin` |
| **2. Permisos** | `PermissionRequiredMixin` |
| **3. Ownership** | Filtrado por propietario |
| **4. Mensajes** | Feedback claro al usuario |

---

## 🔑 Roles y Permisos

#### Roles Disponibles:

**👔 Organizador**
- ✅ Crear eventos
- ✅ Editar eventos
- ✅ Eliminar eventos
- ✅ Ver todos sus eventos
---

## 🔑 Roles y Permisos
**👥 Asistente**
- ✅ Ver eventos públicos
- ✅ Ver sus propios eventos
- ❌ No puede crear/editar/eliminar

---

## 💾 Modelo de Datos: Event

```python
class Event(models.Model):
    title = CharField(max_length=200)
    description = TextField(blank=True)
    date = DateTimeField()
    is_private = BooleanField(default=False)
    owner = ForeignKey(User, on_delete=CASCADE)
```

### Permisos del Modelo:
- `events.add_event` - Crear eventos
- `events.change_event` - Editar eventos
- `events.delete_event` - Eliminar eventos
- `events.view_event` - Ver eventos

---

## 🎭 Vistas Principales

### CRUD Completo:

| Vista | URL | Requiere Login | Requiere Permiso |
|-------|-----|----------------|------------------|
| Lista | `/events/` | ✅ | ❌ |
| Crear | `/events/create/` | ✅ | `add_event` |
| Editar | `/events/<id>/edit/` | ✅ | `change_event` |
| Eliminar | `/events/<id>/delete/` | ✅ | `delete_event` |

---

## 🔍 EventListView

```python
class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'events/list.html'
    
    def get_queryset(self):
        qs = Event.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(
                Q(is_private=False) | 
                Q(owner=self.request.user)
            )
        return qs
```

### Lógica de Filtrado:
- **Staff**: Ve todos los eventos
- **Usuarios**: Solo públicos o propios

---

## ➕ EventCreateView

```python
class EventCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      generic.CreateView):
    permission_required = 'events.add_event'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Evento creado.')
        return super().form_valid(form)
```
---

## ➕ EventCreateView
### Características:
- Asigna automáticamente el `owner`
- Valida permisos antes de crear
- Mensaje de confirmación

---

## ✏️ EventUpdateView & 🗑️ EventDeleteView

### EventUpdateView:
- Permite editar eventos existentes
- Requiere permiso `change_event`
- Redirección si no tiene permiso

### EventDeleteView:
- Confirmación antes de eliminar
- Requiere permiso `delete_event`
- Mensaje de error si no autorizado

---

## 🔐 Sistema de Autenticación

### CustomLoginView:
```python
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_invalid(self, form):
        messages.error(self.request, 
                      'Usuario o contraseña inválidos.')
        return super().form_invalid(form)
```
---
### Seguridad:
- ✅ Mensaje genérico (no revela usuarios)
- ✅ Previene enumeración
- ✅ Redirección post-login

---

## 🚀 Instalación

### 1. Crear entorno virtual:
```bash
python -m venv .venv
.\.venv\Scripts\Activate
pip install --upgrade pip
pip install django
```

### 2. Ejecutar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 Configuración Inicial

### 3. Crear superusuario:
```bash
python manage.py createsuperuser
```

### 4. Inicializar roles:
```bash
python manage.py initroles
```

### 5. Ejecutar servidor:
```bash
python manage.py runserver
```

---

## 🌐 Rutas Disponibles

| Ruta | Descripción | Acceso |
|------|-------------|--------|
| `/login/` | Página de login | Público |
| `/logout/` | Cerrar sesión | Autenticado |
| `/events/` | Lista de eventos | Autenticado |
| `/events/create/` | Crear evento | Organizador |
| `/events/<id>/edit/` | Editar evento | Organizador |
| `/events/<id>/delete/` | Eliminar evento | Organizador |
| `/admin/` | Panel admin | Superusuario |

---

## 📊 Casos de Uso: Organizador

### Flujo típico:

1. **Login** → Inicia sesión con credenciales
2. **Ver eventos** → Lista todos sus eventos
3. **Crear evento** → Nuevo evento (público/privado)
4. **Editar evento** → Modifica detalles
5. **Eliminar evento** → Elimina con confirmación
6. **Logout** → Cierra sesión

---

## 📊 Casos de Uso: Asistente

### Flujo típico:

1. **Login** → Inicia sesión
2. **Ver eventos públicos** → Lista de eventos disponibles
3. **Ver sus eventos** → Eventos donde es owner
4. **Intentar crear** → ❌ Acceso denegado
5. **Logout** → Cierra sesión

---

## 🧩 Uso de Mixins

### Ventajas en este proyecto:

```python
class EventCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      generic.CreateView):
```

- 🔄 **Reutilización**: No repites código
- 🧹 **Limpieza**: Lógica separada
- 🎯 **Claridad**: Intención explícita
- 🔒 **Seguridad**: Capas de protección

---

## 💬 Sistema de Mensajes

### Tipos implementados:

```python
# Éxito
messages.success(request, 'Evento creado.')

# Error
messages.error(request, 'No tienes permiso.')

# Información
messages.info(request, 'Has cerrado sesión.')
```

### Feedback en tiempo real al usuario

---

## 🛠️ Comandos Personalizados

### `initroles`
```bash
python manage.py initroles
```
Crea grupos: Organizador y Asistente con permisos

### `show_permissions`
```bash
python manage.py show_permissions
```
Muestra todos los permisos de la app events

---

## 📁 Estructura de Templates

```
templates/
├── base.html              # Template base
├── login.html             # Página de login
├── access_denied.html     # Error de acceso
└── events/
    ├── list.html          # Lista de eventos
    ├── form.html          # Crear/editar
    ├── confirm_delete.html # Confirmación
    └── 404.html           # Página no encontrada
```

---

## ⚙️ Configuración de Settings

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/events/'
LOGOUT_REDIRECT_URL = '/login/'

# Seguridad (desarrollo)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
# En producción: True + HTTPS
```

---

## 🎯 Mejores Prácticas Implementadas

✅ **Class-Based Views (CBV)** - Reutilización
✅ **Mixins** - Modularidad
✅ **Mensajes** - UX mejorada
✅ **Permisos granulares** - Seguridad
✅ **Filtrado inteligente** - Privacy
✅ **Comandos custom** - Automatización
✅ **Templates base** - DRY
✅ **Logging** - Debugging

---

## 📈 Flujo de Seguridad Completo

```
Usuario accede a /events/create/
         ↓
¿Autenticado? (LoginRequiredMixin)
    NO → /login/
    SÍ ↓
¿Tiene permiso 'add_event'? (PermissionRequiredMixin)
    NO → Access Denied
    SÍ ↓
¿Formulario válido?
    NO → Muestra errores
    SÍ ↓
✅ Crea evento + Asigna owner + Mensaje éxito
```

---

## 🔍 Características de Privacidad

### Eventos Privados:
- Solo visibles para el owner
- Staff puede verlos todos
- Filtrado automático en la lista

### Eventos Públicos:
- Visibles para todos los usuarios autenticados
- Pueden ser editados solo por owner con permisos
- Aparecen en la lista general

---

## 🎓 Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.x | Lenguaje base |
| **Django** | Latest | Framework web |
| **SQLite** | 3.x | Base de datos |
| **HTML/CSS** | 5/3 | Frontend |
| **Bootstrap** | (opcional) | Estilos |

---

## 🚀 Próximas Mejoras

### Posibles extensiones:

- 📅 Calendario de eventos
- 🔔 Notificaciones
- 🏷️ Categorías/Tags
- 🔍 Búsqueda avanzada
- 📊 Estadísticas
- 📱 API REST
- 🌍 Internacionalización
- 📧 Invitaciones por email

---

## 📚 Recursos de Aprendizaje

### Documentación:
- [Django Docs](https://docs.djangoproject.com/)
- [Django Auth Mixins](https://docs.djangoproject.com/en/stable/topics/auth/default/)
- [Class-Based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)

### En este proyecto:
- `models.md` - Explicación del modelo
- `views.md` - Detalles de las vistas
- `mixin.md` - Uso de mixins

---

## ✨ Conclusión

Este proyecto demuestra:

1. 🏗️ **Arquitectura sólida** con Django
2. 🔐 **Seguridad robusta** multinivel
3. 🎯 **Buenas prácticas** implementadas
4. 📈 **Escalabilidad** para crecer
5. 🧩 **Código modular** y mantenible

### Resultado:
Una aplicación profesional, segura y lista para producción

---

## 🙏 ¡Gracias!

### ¿Preguntas?

**Contacto:**
- 📧 Email: [tu_email]
- 🌐 GitHub: [tu_github]
- 💼 LinkedIn: [tu_linkedin]

**¡Feliz codificación!** 🎉👨‍💻👩‍💻
