---
marp: true
theme: gaia
paginate: true
---

# 🎭 Views.py
## El Corazón de la Aplicación

Lógica de presentación y control de eventos en Django

---

## 🎯 ¿Qué es `views.py`?

Es el **corazón de la lógica de presentación** de la aplicación de eventos.

### Responsabilidades:
- ✅ Gestionar la interacción usuarios ↔ datos
- ✅ Controlar el acceso y permisos
- ✅ Proporcionar una excelente UX

---

## 📦 Componentes Principales

### 1. **Importaciones**
```python
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
```

### 2. **Vistas Basadas en Clases** (CBV)
### 3. **Vistas Basadas en Funciones** (FBV)
### 4. **Vista Personalizada de Login**

---

## 📋 Vista: `EventListView`

```python
class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'events/list.html'
```

### Funcionalidad:
- 👁️ Muestra la lista de eventos
- 🔒 Solo usuarios autenticados
- 📊 Los asistentes solo ven eventos públicos o propios
- ⚙️ Filtrado con `Q` objects

---

## ➕ Vista: `EventCreateView`

```python
class EventCreateView(LoginRequiredMixin, 
                      PermissionRequiredMixin,
                      generic.CreateView):
    permission_required = 'events.add_event'
```

### Características:
- ✍️ Crear nuevos eventos
- 🔐 Requiere autenticación + permiso
- 👤 Asigna el usuario como `owner`
- ✅ Mensaje de éxito al crear

---

## ✏️ Vista: `EventUpdateView`

```python
class EventUpdateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      generic.UpdateView):
    permission_required = 'events.change_event'
```

### Características:
- 📝 Editar eventos existentes
- 🔐 Control de permisos
- ❌ Mensaje de error si no tiene permiso
- ↩️ Redirección a la lista

---

## 🗑️ Vista: `EventDeleteView`

```python
class EventDeleteView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      generic.DeleteView):
    permission_required = 'events.delete_event'
```

### Características:
- 🗑️ Eliminar eventos
- ⚠️ Confirmación antes de eliminar
- 🔐 Validación de permisos
- 💬 Mensajes informativos

---

## 🚫 Vista: `access_denied`

```python
def access_denied(request):
    messages.error(request, 'Acceso denegado...')
    return render(request, 'access_denied.html')
```

### Propósito:
- Página de error personalizada
- Mensaje claro al usuario
- Mejor experiencia que error 403

---

## 🚪 Vista: `logout_view`

```python
@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect(settings.LOGOUT_REDIRECT_URL)
```

### Seguridad:
- 🔒 Solo acepta método POST
- 📤 Cierra sesión del usuario
- 💬 Mensaje informativo
- ↩️ Redirección al login

---

## 🔑 Vista: `CustomLoginView`

```python
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_invalid(self, form):
        messages.error(self.request, 
                      'Usuario o contraseña inválidos.')
        return super().form_invalid(form)
```

### Seguridad mejorada:
- 🛡️ Mensaje genérico (no revela detalles)
- 🚫 Previene enumeración de usuarios
- 🎨 Template personalizado

---

## 🔐 Gestión de Permisos

### Mixins Utilizados:

| Mixin | Propósito |
|-------|-----------|
| `LoginRequiredMixin` | Requiere autenticación |
| `PermissionRequiredMixin` | Requiere permiso específico |

### Flujo de Seguridad:
1. ¿Usuario autenticado? ❌ → Login
2. ¿Tiene permiso? ❌ → Access Denied
3. ✅ → Acceso permitido

---

## 💬 Sistema de Mensajes

```python
messages.success(request, 'Evento creado.')
messages.error(request, 'No tienes permiso.')
messages.info(request, 'Has cerrado sesión.')
```

### Tipos de mensajes:
- ✅ **success**: Operación exitosa
- ❌ **error**: Error o denegación
- ℹ️ **info**: Información general

---

## 🎯 Patrón de Filtrado

```python
def get_queryset(self):
    qs = Event.objects.all()
    if not self.request.user.is_staff:
        qs = qs.filter(
            Q(is_private=False) | 
            Q(owner=self.request.user)
        )
    return qs
```

### Lógica:
- **Staff**: Ve todos los eventos
- **Usuarios**: Solo públicos o propios

---

## 🏆 Buenas Prácticas Implementadas

✅ **DRY**: Reutilización con mixins
✅ **Seguridad**: Múltiples capas de protección
✅ **UX**: Mensajes claros y redirecciones
✅ **Separación**: Lógica separada por vista
✅ **Logging**: Sistema de logs configurado
✅ **CBV**: Vistas genéricas de Django

---

## 📊 Resumen de Vistas

| Vista | Tipo | Permisos | Acción |
|-------|------|----------|--------|
| EventListView | CBV | Login | Ver lista |
| EventCreateView | CBV | Login + add | Crear |
| EventUpdateView | CBV | Login + change | Editar |
| EventDeleteView | CBV | Login + delete | Eliminar |
| CustomLoginView | CBV | Público | Login |
| logout_view | FBV | POST | Logout |

---

## 🎓 Conclusión

`views.py` es un **ejemplo de excelencia** en Django:

1. 🔒 **Seguridad robusta** con múltiples capas
2. 🎨 **Código limpio** y mantenible
3. 👥 **UX optimizada** con mensajes claros
4. ⚡ **Eficiente** usando vistas genéricas
5. 📝 **Bien documentado** y organizado

### Resultado:
Una aplicación segura, escalable y amigable con el usuario

---

## 🚀 Próximos Pasos

- Explorar `forms.py` para validaciones
- Revisar `urls.py` para enrutamiento
- Analizar templates para el frontend
- Estudiar `tests.py` para casos de prueba

**¡Gracias por tu atención!** 🎉