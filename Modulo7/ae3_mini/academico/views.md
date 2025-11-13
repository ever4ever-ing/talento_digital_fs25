# Documentación de Vistas Basadas en Clases (CBV) en Django

Este proyecto utiliza Vistas Basadas en Clases (Class-Based Views, CBV) para la gestión de los modelos académicos. Las CBV permiten una estructura más limpia, reutilizable y fácil de mantener que las vistas basadas en funciones.

## ¿Qué son las CBV?
Las CBV son clases que heredan de clases genéricas de Django y encapsulan la lógica de las vistas. Django provee muchas CBV listas para usar, como `ListView`, `CreateView`, `UpdateView`, `DeleteView`, entre otras.

## Ventajas de las CBV
- Reutilización de código.
- Separación clara de responsabilidades.
- Personalización sencilla mediante herencia y métodos.
- Menos código repetitivo.

## Vistas implementadas en este proyecto

### 1. Menú principal
```python
class MenuAcademicoView(TemplateView):
    template_name = 'academico/menu.html'
```
- Muestra el menú principal de navegación de la app.
- Hereda de `TemplateView`, que sirve para renderizar una plantilla estática.

### 2. Listado de registros
Para cada modelo existe una vista de listado:
```python
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'academico/profesor_list.html'
    context_object_name = 'profesores'
```
- Hereda de `ListView`.
- Muestra todos los registros del modelo indicado.
- El atributo `context_object_name` define el nombre de la variable en la plantilla.

Se repite la estructura para:
- `CursoListView`
- `EstudianteListView`
- `PerfilListView`
- `InscripcionListView`

### 3. Registro de nuevos datos
Para cada modelo existe una vista de creación:
```python
class ProfesorCreateView(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'academico/profesor_form.html'
    success_url = reverse_lazy('profesor_create')
```
- Hereda de `CreateView`.
- Usa un formulario personalizado (`form_class`).
- Redirige a la misma vista tras guardar (`success_url`).

Se repite la estructura para:
- `CursoCreateView`
- `EstudianteCreateView`
- `PerfilCreateView`
- `InscripcionCreateView`

## Personalización de CBV
Las CBV pueden personalizarse sobrescribiendo métodos como:
- `get_queryset()`: para filtrar los datos listados.
- `form_valid()`: para lógica extra al guardar formularios.
- `get_context_data()`: para agregar datos extra al contexto de la plantilla.

## Ejemplo de URL
Las vistas se conectan a URLs en `academico/urls.py`:
```python
path('profesor/lista/', ProfesorListView.as_view(), name='profesor_list')
path('profesor/crear/', ProfesorCreateView.as_view(), name='profesor_create')
```

## Plantillas
Cada vista usa una plantilla HTML específica, ubicada en `academico/templates/academico/`.

## Referencias
- [Documentación oficial Django CBV](https://docs.djangoproject.com/en/5.2/topics/class-based-views/)
- [ListView](https://docs.djangoproject.com/en/5.2/ref/class-based-views/generic-display/#listview)
- [CreateView](https://docs.djangoproject.com/en/5.2/ref/class-based-views/generic-editing/#createview)
- [TemplateView](https://docs.djangoproject.com/en/5.2/ref/class-based-views/base/#templateview)

---
Las CBV facilitan la creación y mantenimiento de aplicaciones Django robustas y escalables.
