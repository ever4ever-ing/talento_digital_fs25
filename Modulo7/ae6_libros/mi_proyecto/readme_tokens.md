# Seguridad CSRF y Enrutamiento con Parámetros en Django

## 1. Manejo de tokens de seguridad CSRF en Django

Django incluye protección contra ataques CSRF (Cross-Site Request Forgery) de forma predeterminada.  
Cuando creas un formulario que envía datos mediante POST, debes incluir el token CSRF para que Django acepte la petición.

**Ejemplo en un template:**

```html
<form method="post">
    {% csrf_token %}
    <!-- Campos del formulario -->
    <button type="submit">Enviar</button>
</form>
```

- `{% csrf_token %}` inserta un token oculto en el formulario.
- Django verifica este token en cada petición POST para asegurar que proviene de tu sitio.

---

## 2. Proceso de enrutamiento y paso de parámetros en URLs de Django

### a) Definición de rutas en `urls.py`

Puedes definir rutas que acepten parámetros usando la sintaxis `<tipo:parametro>`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('detalle/<int:id>/', views.detalle_libro, name='detalle_libro'),
]
```

- `<int:id>` indica que la URL espera un parámetro entero llamado `id`.

### b) Recepción de parámetros en la vista

La función de vista recibe el parámetro como argumento:

```python
def detalle_libro(request, id):
    # Lógica para obtener el libro con ese id
    ...
```

### c) Generación de URLs dinámicas en los templates

Para crear enlaces que incluyan parámetros, usa el tag `url`:

```html
<a href="{% url 'detalle_libro' libro.id %}">Ver detalle</a>
```

- Esto generará una URL como `/detalle/5/` si `libro.id` es 5.

---

**Resumen:**  
- Usa `{% csrf_token %}` en formularios para protección CSRF.
- Define rutas con parámetros en `urls.py` usando `<tipo:parametro>`.
- Recibe los parámetros en la función de vista.
- Genera enlaces dinámicos en los templates con