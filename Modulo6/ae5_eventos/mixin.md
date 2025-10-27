# Uso de Mixins en Django

Un **mixin** es una clase que agrega funcionalidades específicas a otras clases mediante herencia múltiple. En Django, los mixins se usan comúnmente para añadir comportamientos reutilizables a las vistas.

## Ejemplo en este proyecto
En el archivo `views.py` se emplean los siguientes mixins:

- **LoginRequiredMixin**: Restringe el acceso a la vista solo a usuarios autenticados. Si el usuario no ha iniciado sesión, se le redirige a la página de login.
- **PermissionRequiredMixin**: Exige que el usuario tenga permisos específicos para acceder a la vista. Por ejemplo, para crear, editar o eliminar eventos, el usuario debe tener los permisos correspondientes.

### Ventajas de usar mixins
- Permiten reutilizar código y comportamientos en varias vistas.
- Facilitan la gestión de autenticación y permisos sin duplicar lógica.
- Mejoran la organización y legibilidad del código.

### Ejemplo de uso
```python
class EventCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    # ...
    permission_required = 'events.add_event'
```
En este ejemplo, la vista solo permite crear eventos a usuarios autenticados y con el permiso `add_event`.

## Conclusión
Los mixins son una herramienta poderosa para agregar funcionalidades reutilizables y mantener el código limpio y modular en aplicaciones Django.