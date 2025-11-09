---
marp: true
theme: gaia
paginate: true
---

# 📋 Models.py
## Explicación detallada

Estructura de datos para la aplicación de eventos en Django

---

## 🎯 Propósito

El archivo `models.py` define la estructura de los datos principales de la aplicación de eventos utilizando el **sistema de modelos de Django**.

### ¿Qué hace?
- Almacena información de eventos
- Gestiona relaciones con usuarios
- Define permisos personalizados

---

## 🏗️ Modelo Principal: `Event`

La clase `Event` representa un evento en la base de datos.

```python
class Event(models.Model):
    # Campos del modelo
    ...
```

**Hereda de**: `models.Model`
**Permite**: Interactuar con el ORM de Django

---

## 📊 Campos del Modelo

| Campo | Tipo | Descripción |
|-------|------|-------------|
| **title** | `CharField(200)` | Nombre del evento |
| **description** | `TextField` | Descripción extensa (opcional) |
| **date** | `DateTimeField` | Fecha y hora del evento |
| **is_private** | `BooleanField` | Evento privado o público |
| **owner** | `ForeignKey` | Usuario propietario |

---

## 🔗 Campo `owner` (Relación)

```python
owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='events'
)
```

### Características:
- Enlaza el evento con el usuario creador
- `on_delete=CASCADE`: Si se elimina el usuario, se eliminan sus eventos
- `related_name='events'`: Acceso mediante `user.events.all()`

---

## 🔐 Metadatos y Permisos

```python
class Meta:
    permissions = [
        ('can_manage_event', 'Puede gestionar eventos')
    ]
```

### Permiso personalizado:
- **can_manage_event**: Permite crear y gestionar eventos
- Asignable a roles específicos
- Control de acceso a funcionalidades avanzadas

---

## ⚙️ Métodos del Modelo

### `__str__(self)`
```python
def __str__(self):
    return self.title
```
- Representación textual del evento
- Facilita identificación en admin y vistas

### `get_absolute_url(self)`
```python
def get_absolute_url(self):
    return reverse('events:list')
```
- URL de redirección tras crear/editar
- Utiliza el sistema de rutas de Django

---

## 👥 Relación con Usuarios

### `get_user_model()`
```python
from django.contrib.auth import get_user_model
```

### Beneficios:
✅ Obtiene el modelo de usuario activo
✅ Compatibilidad con autenticación personalizada
✅ Flexibilidad para diferentes configuraciones

---

## 🎓 Conclusión

El archivo `models.py` es **fundamental** para:

1. ✅ Definir cómo se almacenan los eventos
2. ✅ Establecer relaciones con usuarios
3. ✅ Controlar acceso mediante permisos
4. ✅ Gestión robusta y segura de datos

### Resultado:
Una aplicación escalable y mantenible siguiendo las mejores prácticas de Django

---

## 🚀 Próximos Pasos

- Explorar `views.py` para ver cómo se usan estos modelos
- Revisar `forms.py` para formularios de eventos
- Analizar `admin.py` para gestión administrativa

**¡Gracias!** 🎉