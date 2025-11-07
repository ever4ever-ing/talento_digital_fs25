---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# Sistema de Mensajes en Django
## Django Messages Framework

Implementación de notificaciones y alertas en aplicaciones web

---

## ¿Qué son los mensajes en Django?

- **Framework integrado** para mostrar notificaciones temporales
- Almacena mensajes en la sesión del usuario
- Se muestran una sola vez (one-time notifications)
- Perfecto para feedback después de acciones del usuario

---

## Tipos de Mensajes

Django proporciona 5 niveles de mensajes:

| Nivel | Uso | Color Bootstrap |
|-------|-----|-----------------|
| `DEBUG` | Información de desarrollo | Secondary (gris) |
| `INFO` | Información general | Info (azul) |
| `SUCCESS` | Operación exitosa | Success (verde) |
| `WARNING` | Advertencia | Warning (amarillo) |
| `ERROR` | Error | Danger (rojo) |

---

## Configuración en settings.py

```python
from django.contrib.messages import constants as messages_constants

MESSAGE_TAGS = {
    messages_constants.DEBUG: 'secondary',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
    messages_constants.ERROR: 'danger',
}
```

**Propósito**: Mapear los tags de Django a clases CSS de Bootstrap

---

## Importar el módulo messages

En tus vistas, importa el módulo:

```python
from django.contrib import messages
```

Este módulo proporciona funciones para agregar mensajes:
- `messages.debug()`
- `messages.info()`
- `messages.success()`
- `messages.warning()`
- `messages.error()`

---

## Uso en Vistas - Ejemplo 1: Login

```python
class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'✓ ¡Bienvenido, {user.username}!')
            return redirect('lista_eventos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
```

---

## Uso en Vistas - Ejemplo 2: Logout

```python
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, '✓ Has cerrado sesión exitosamente.')
        return redirect('lista_eventos')
```

**Simple y directo**: Solo necesitas una línea para agregar el mensaje

---

## Uso con Mixins - LoginRequiredMixin

```python
class MisEventos(LoginRequiredMixin, ListView):
    model = Evento
    login_url = '/login/'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(
                request, 
                '⚠️ Debes iniciar sesión para ver tus eventos.'
            )
        return super().dispatch(request, *args, **kwargs)
```

**Método `dispatch`**: Se ejecuta antes de procesar la petición

---

## Mostrar Mensajes en Templates

En `base.html`, agrega este código:

```html
{% if messages %}
    <div class="messages-container">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }} 
                        alert-dismissible fade show" 
                 role="alert">
                {{ message }}
                <button type="button" class="btn-close" 
                        data-bs-dismiss="alert" 
                        aria-label="Close"></button>
            </div>
        {% endfor %}
    </div>
{% endif %}
```

---

## Anatomía del Template de Mensajes

```html
<div class="alert alert-{{ message.tags }}">
```
- `message.tags`: Contiene el tipo de mensaje (success, warning, etc.)
- Se concatena con `alert-` para crear clases Bootstrap

```html
<button type="button" class="btn-close" 
        data-bs-dismiss="alert"></button>
```
- Botón de Bootstrap para cerrar el mensaje
- Funciona automáticamente con JavaScript de Bootstrap

---

## Ventajas del Sistema de Mensajes

✅ **Fácil de usar**: Una línea de código
✅ **Automático**: Se muestran una vez y desaparecen
✅ **Integrado**: Funciona con la sesión de Django
✅ **Flexible**: Personalizable con CSS
✅ **Accesible**: Soporte para lectores de pantalla
✅ **Responsive**: Compatible con Bootstrap

---

## Flujo de Trabajo Completo

1. **Usuario intenta acceder** a página protegida sin login
2. **LoginRequiredMixin** detecta que no está autenticado
3. **dispatch()** agrega mensaje de advertencia
4. **Usuario es redirigido** a la página de login
5. **Mensaje se muestra** en el template
6. **Usuario inicia sesión**
7. **Nuevo mensaje** de bienvenida se muestra
8. **Usuario es redirigido** a la página original

---

## Mejores Prácticas

📌 **Usa emojis** para hacer mensajes más visuales
📌 **Sé específico** en los mensajes
📌 **Usa el nivel correcto** (success, warning, error)
📌 **Coloca mensajes en base.html** para que se muestren en toda la app
📌 **Usa `alert-dismissible`** para permitir cerrar mensajes
📌 **Combina con Bootstrap** para mejor apariencia

---

## Ejemplo de Mensajes con Emojis

```python
# Éxito
messages.success(request, '✓ ¡Operación completada!')

# Advertencia
messages.warning(request, '⚠️ Acción requiere confirmación')

# Error
messages.error(request, '❌ No se pudo completar la operación')

# Información
messages.info(request, 'ℹ️ Nuevo evento disponible')
```

---

## Casos de Uso Comunes

- ✅ Confirmación de acciones (guardar, eliminar, actualizar)
- ⚠️ Validaciones de permisos
- 🔐 Notificaciones de autenticación
- 📧 Confirmación de envío de emails
- 💾 Estados de operaciones CRUD
- 🔄 Feedback de procesos asíncronos

---

## Mensajes Persistentes (Opcional)

Si necesitas mensajes que persistan por múltiples requests:

```python
from django.contrib.messages import constants

messages.add_message(
    request,
    constants.WARNING,
    'Mensaje persistente',
    extra_tags='persist'
)
```

**Nota**: Requiere configuración adicional en settings

---

## Personalización Avanzada

Puedes agregar tags extras para estilos personalizados:

```python
messages.success(
    request, 
    'Evento creado', 
    extra_tags='evento-creado'
)
```

En el template:
```html
<div class="alert alert-{{ message.tags }} {{ message.extra_tags }}">
```

Resultado: `<div class="alert alert-success evento-creado">`

---

## Debug de Mensajes

Para verificar si los mensajes están funcionando:

```python
from django.contrib.messages import get_messages

# En una vista
storage = get_messages(request)
for message in storage:
    print(f"Nivel: {message.level}, Mensaje: {message}")
```

---

## Integración con AJAX

Para aplicaciones SPA, puedes devolver mensajes como JSON:

```python
from django.contrib.messages import get_messages

def mi_vista_ajax(request):
    # ... tu lógica ...
    messages.success(request, 'Operación exitosa')
    
    msgs = [
        {"level": m.level, "message": str(m)} 
        for m in get_messages(request)
    ]
    return JsonResponse({"messages": msgs})
```

---

## Resumen

✨ **Django Messages Framework** es una herramienta poderosa
🎯 **Fácil de implementar** en cualquier proyecto
🎨 **Compatible con Bootstrap** y otros frameworks CSS
🔧 **Flexible y extensible** para casos avanzados
👍 **Mejora la UX** con feedback inmediato

---

## Código Completo del Ejemplo

**views.py**
```python
from django.contrib import messages

class MisEventos(LoginRequiredMixin, ListView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '⚠️ Debes iniciar sesión')
        return super().dispatch(request, *args, **kwargs)
```

**base.html**
```html
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
    {% endfor %}
{% endif %}
```

---

## Recursos Adicionales

📚 **Documentación oficial**: 
https://docs.djangoproject.com/en/stable/ref/contrib/messages/

📚 **Bootstrap Alerts**: 
https://getbootstrap.com/docs/5.3/components/alerts/

💻 **Código del proyecto**: 
Disponible en el repositorio del curso

---

# ¡Gracias!

## Preguntas

¿Dudas sobre el Sistema de Mensajes en Django?

---