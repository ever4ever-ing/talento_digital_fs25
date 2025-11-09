---
marp: true
theme: gaia
paginate: true
---

# 🧩 Mixins en Django
## Reutilización y Modularidad

Añadiendo superpoderes a tus vistas

---

## 🤔 ¿Qué es un Mixin?

Un **mixin** es una clase que agrega funcionalidades específicas a otras clases mediante **herencia múltiple**.

### En Django:
- 🔧 Añaden comportamientos reutilizables a las vistas
- 🎯 Enfoque modular y limpio
- ⚡ Evitan duplicación de código

---

## 🏗️ Concepto de Herencia Múltiple

```python
class MiVista(Mixin1, Mixin2, BaseView):
    pass
```

### Orden de herencia (MRO):
1. **Mixins primero** (de izquierda a derecha)
2. **Clase base al final**

### Ejemplo:
```python
class EventCreateView(LoginRequiredMixin, 
                      PermissionRequiredMixin, 
                      generic.CreateView):
```

---

## 🔒 LoginRequiredMixin

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
```

### ¿Qué hace?
- ✅ Restringe acceso a usuarios autenticados
- ❌ Usuario no autenticado → Redirige a login
- 🔗 Usa `LOGIN_URL` de settings

---

## 🛡️ PermissionRequiredMixin

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class EventCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      generic.CreateView):
    permission_required = 'events.add_event'
```

### ¿Qué hace?
- ✅ Exige permisos específicos
- ❌ Sin permiso → Error 403 o redirección
- 🎯 Control granular de acceso

---

## 📋 Mixins en Este Proyecto

| Vista | Mixins Usados |
|-------|---------------|
| **EventListView** | `LoginRequiredMixin` |
| **EventCreateView** | `LoginRequiredMixin` + `PermissionRequiredMixin` |
| **EventUpdateView** | `LoginRequiredMixin` + `PermissionRequiredMixin` |
| **EventDeleteView** | `LoginRequiredMixin` + `PermissionRequiredMixin` |

---

## 🎯 Ejemplo Completo

```python
class EventCreateView(LoginRequiredMixin, 
                      PermissionRequiredMixin, 
                      generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/form.html'
    permission_required = 'events.add_event'
    success_url = reverse_lazy('events:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
```

---

## 🔐 Flujo de Seguridad

```
Usuario solicita crear evento
         ↓
¿Autenticado? (LoginRequiredMixin)
    NO → Redirige a /login/
    SÍ ↓
¿Tiene permiso 'add_event'? (PermissionRequiredMixin)
    NO → Error 403 / Redirección
    SÍ ↓
✅ Permite crear evento
```

---

## ✨ Ventajas de Usar Mixins

### 🔄 **Reutilización**
No repites código de autenticación/permisos

### 🧹 **Código Limpio**
Lógica separada y organizada

### 📚 **Legibilidad**
Intención clara al leer la clase

### 🎯 **Modularidad**
Combina mixins según necesites

---

## 🆚 Alternativa: Decoradores

### Antes (con decoradores):
```python
@login_required
@permission_required('events.add_event')
def create_event(request):
    # lógica de la vista...
```

### Ahora (con mixins):
```python
class EventCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      generic.CreateView):
    permission_required = 'events.add_event'
```

---

## 🧰 Otros Mixins Útiles de Django

| Mixin | Propósito |
|-------|-----------|
| `UserPassesTestMixin` | Test personalizado |
| `AccessMixin` | Base para control de acceso |
| `LoginRequiredMixin` | Requiere autenticación |
| `PermissionRequiredMixin` | Requiere permisos |

---

## 💡 Buenas Prácticas

### ✅ DO (Hacer):
- Usar mixins para lógica transversal
- Colocar mixins antes de la clase base
- Combinar múltiples mixins cuando sea necesario

### ❌ DON'T (No hacer):
- Crear mixins con estado complejo
- Abusar de la herencia múltiple
- Mezclar lógica de negocio en mixins

---

## 🔧 Crear Tu Propio Mixin

```python
class OwnerRequiredMixin:
    """Solo el owner puede editar"""
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            return redirect('access_denied')
        return super().dispatch(request, *args, **kwargs)

class EventUpdateView(LoginRequiredMixin,
                      OwnerRequiredMixin,
                      generic.UpdateView):
    model = Event
```

---

## 📊 Comparación de Enfoques

| Aspecto | Sin Mixins | Con Mixins |
|---------|------------|------------|
| **Código** | Duplicado | Reutilizable |
| **Mantenimiento** | Difícil | Fácil |
| **Legibilidad** | Media | Alta |
| **Testing** | Complejo | Modular |
| **Escalabilidad** | Baja | Alta |

---

## 🎓 Conclusión

Los mixins son una **herramienta poderosa** en Django:

1. 🔄 **Reutilización** de comportamientos
2. 🧹 **Código limpio** y modular
3. 🔒 **Seguridad** simplificada
4. 📈 **Escalabilidad** mejorada
5. ✨ **Mantenibilidad** aumentada

### Resultado:
Aplicaciones más robustas, seguras y fáciles de mantener

---

## 🚀 Próximos Pasos

- Explorar otros mixins de Django
- Crear mixins personalizados
- Combinar mixins para casos complejos
- Revisar documentación oficial de Django

**¡Domina los mixins y lleva tu código al siguiente nivel!** 🎉