---
marp: true
theme: default
paginate: true
header: 'AE5: Uso de Mixins en Django'
footer: 'BOTIC-SOFOF-24-28-13-0077 | Talento Digital'
---

# Uso de Mixins en Django

**Material Lectivo | Aula**

---

## Objetivos de Aprendizaje

Al finalizar esta lección, seremos capaces de:

1. ✅ Comprender qué es un mixin y su propósito en Python y Django
2. ✅ Conocer por qué y cuándo usar mixins en las vistas
3. ✅ Aplicar los mixins `LoginRequiredMixin` y `PermissionRequiredMixin`
4. ✅ Centralizar la lógica de autenticación y permisos usando mixins

---

## ¿Qué es un Mixin?

- Un **mixin** es una clase en Python que proporciona funcionalidades adicionales a otras clases
- **No forma parte** de una jerarquía de herencia completa
- La idea es **reutilizar código** sin obligar a todas las clases a heredar de una clase base común
- En Django, se usan principalmente en **vistas** para agregar comportamientos

---

## Ejemplo Simple de Mixin

```python
class SaludoMixin:
    def saludo(self):
        return "¡Hola desde el Mixin!"
        
class MiVista(SaludoMixin):
    def mostrar_saludo(self):
        return self.saludo()

vista = MiVista()
print(vista.mostrar_saludo())  # ¡Hola desde el Mixin!
```

**Conclusión:** Los mixins permiten agregar funcionalidades de forma **modular y reutilizable**.

---

## ¿Para qué sirven los Mixins en Django?

✅ **Evitan repetir código** en varias vistas
✅ Permiten **centralizar lógica común** (autenticación, permisos)
✅ Son ideales para mantener código **limpio, modular y mantenible**

### Ejemplos frecuentes:

- `LoginRequiredMixin`: vista accesible solo para usuarios autenticados
- `PermissionRequiredMixin`: vista accesible solo con permisos específicos

---

## ¿Cuándo usar Mixins?

| Mixin | Cuándo usarlo |
|-------|---------------|
| **LoginRequiredMixin** | Vista privada (solo usuarios autenticados) |
| **PermissionRequiredMixin** | Control fino sobre acceso según permisos específicos |

**Por qué usarlo:**
- Facilita la gestión de **seguridad y acceso**
- Mantiene la lógica de control separada de la lógica principal

---

## Diferencia: Clase vs Mixin

| Característica | Clase normal | Mixin |
|----------------|--------------|-------|
| **Propósito** | Representar un objeto completo | Añadir funcionalidades modulares |
| **Independencia** | Funciona por sí misma | Necesita combinarse con otra clase |
| **Herencia** | Puede ser independiente | Se combina mediante herencia múltiple |
| **Reutilización** | Comportamiento completo | Comportamiento específico reutilizable |
| **Ejemplo Django** | TemplateView, ListView | LoginRequiredMixin, PermissionRequiredMixin |

---

## LoginRequiredMixin

**¿Qué hace?**
- Garantiza que el usuario debe estar **autenticado** para acceder
- Si no está autenticado, **redirige automáticamente** al login
- Útil para: perfiles, paneles de usuario, contenido restringido

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class VistaPrivada(LoginRequiredMixin, TemplateView):
    template_name = 'privada.html'
```

---

## LoginRequiredMixin - Explicación

```python
class VistaPrivada(LoginRequiredMixin, TemplateView):
    template_name = 'privada.html'
```

**¿Cómo funciona?**

1. `LoginRequiredMixin` se coloca **antes** de la clase principal
2. Python evalúa la herencia de **izquierda a derecha**
3. Django verifica si `request.user` está autenticado
4. Si no, redirige a `LOGIN_URL` definido en `settings.py`

---

## PermissionRequiredMixin

**¿Qué hace?**
- Asegura que el usuario tenga un **permiso específico**
- Útil para **roles y permisos avanzados**
- Ejemplo: "solo administradores pueden editar"

```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView

class VistaConPermiso(PermissionRequiredMixin, TemplateView):
    template_name = 'con_permiso.html'
    permission_required = 'blog.change_post'
```

---

## PermissionRequiredMixin - Explicación

```python
class VistaConPermiso(PermissionRequiredMixin, TemplateView):
    permission_required = 'blog.change_post'
```

**¿Cómo funciona?**

1. `permission_required` define el permiso necesario (`app.codename`)
2. Si el usuario **no tiene el permiso**, devuelve error **403**
3. Se puede combinar con `LoginRequiredMixin` para exigir autenticación primero

---

## Ejemplo Práctico: Mini Blog

Vamos a crear tres vistas:

1. 📖 **Vista pública**: lista todos los posts
2. 🔒 **Vista privada**: muestra posts del usuario autenticado
3. 🔑 **Vista con permiso**: permite editar solo con permiso

---

## Modelo Post

```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
```

---

## Vistas con Mixins

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, TemplateView
from .models import Post

# Vista pública
class ListaPosts(ListView):
    model = Post
    template_name = 'lista_posts.html'
```

---

## Vista Privada (Usuarios Autenticados)

```python
# Vista privada (solo usuarios autenticados)
class MisPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'mis_posts.html'
    
    def get_queryset(self):
        # Solo muestra posts del usuario logueado
        return Post.objects.filter(autor=self.request.user)
```

---

## Vista con Permiso

```python
# Vista con permiso (editar posts)
class EditarPost(PermissionRequiredMixin, TemplateView):
    template_name = 'editar_post.html'
    permission_required = 'blog.change_post'
```

---

## Configuración de URLs

```python
from django.urls import path
from .views import ListaPosts, MisPosts, EditarPost

urlpatterns = [
    path('', ListaPosts.as_view(), name='lista_posts'),
    path('mis-posts/', MisPosts.as_view(), name='mis_posts'),
    path('editar/', EditarPost.as_view(), name='editar_post'),
]
```

---

## Explicación del Ejemplo

1. **ListaPosts**: 
   - Accesible para todos
   - No requiere autenticación

2. **MisPosts**: 
   - Requiere `LoginRequiredMixin`
   - Solo muestra posts del usuario logueado

3. **EditarPost**: 
   - Requiere permiso `blog.change_post`
   - Control fino de acceso

---

## Otros Casos de Uso de Mixins

1. 🔍 **Filtrado de datos**: mostrar solo objetos con ciertos criterios
2. 💬 **Mensajes automáticos**: agregar mensajes de éxito/error
3. 📝 **Registro de acciones**: auditar creación/edición/eliminación
4. 🔀 **Redirecciones automáticas**: según condiciones del usuario
5. 📊 **Datos al contexto**: variables comunes sin repetir código
6. 📄 **Paginación/ordenamiento**: funcionalidades en listas
7. 🔐 **Control avanzado**: acceso según criterios adicionales

---

## Vistas: Funciones vs Clases

### Vistas Basadas en Funciones (FBV)

```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def perfil_usuario(request):
    return render(request, 'perfil.html')
```

- Funciones que reciben `request` y devuelven respuesta
- Para vistas **simples**
- Control de acceso mediante **decoradores**

---

## Vistas Basadas en Clases (CBV)

```python
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class MisPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'mis_posts.html'

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)
```

- Heredan de vistas genéricas de Django
- Reutilizan lógica mediante **herencia y mixins**
- Para vistas **complejas o repetitivas**

---

## Comparación FBV vs CBV

| Característica | FBV | CBV |
|----------------|-----|-----|
| **Complejidad** | Simple | Media a alta |
| **Reutilización** | Baja | Alta (mixins, herencia) |
| **Operaciones CRUD** | Manual | Vistas genéricas |
| **Control de acceso** | Decoradores | Mixins |
| **Curva de aprendizaje** | Baja | Media |

---

## ¿Cuándo usar cada una?

### FBV (Funciones)
- Vistas simples
- Prototipos rápidos
- Páginas estáticas

### CBV (Clases)
- Vistas complejas
- Operaciones CRUD
- Permisos específicos
- Código que se repite mucho

---

## Buenas Prácticas

1. ✅ **Centraliza** autenticación y permisos usando mixins
2. ✅ **Define bien los permisos** en tu app
3. ✅ **Aplica mixins consistentemente** en todas las vistas que lo requieran
4. ✅ **Combina mixins** cuando necesites autenticación + permisos
5. ✅ Evita **lógica repetida** en cada vista

---

## Resumen

- Los **mixins** son clases que añaden funcionalidades modulares
- **LoginRequiredMixin**: protege vistas privadas
- **PermissionRequiredMixin**: control fino de permisos
- Permiten **código limpio, reutilizable y mantenible**
- Ideales para **CBV** en Django
- Centralizan la lógica de **seguridad y acceso**

---

## ¡Gracias!

**Preguntas**

---
