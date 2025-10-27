# Paso a paso para definir permisos en Django

## 1. Verifica el modelo y permisos automáticos

En `models.py`, asegúrate de que el modelo `Automovil` esté definido (ej. `class Automovil(models.Model): ...`).

Django crea permisos automáticamente: `add_automovil`, `change_automovil`, `delete_automovil`, `view_automovil`.

*Si necesitas permisos personalizados, agrégalos en el modelo con `Meta.permissions = [('custom_perm', 'Descripción')]`.*
## 2. Crea grupos de usuarios

En el admin de Django (`http://localhost:8000/admin/`), ve a "Grupos" y crea dos grupos:

- **Vendedores:** Asigna el permiso `ventas | automóvil | Can add automóvil` (esto es `add_automovil`).
- **Clientes:** No asignes permisos relacionados con agregar automóviles (pueden tener otros, como `view_automovil` si necesitan ver).

## 3. Asigna usuarios a grupos

Edita usuarios en el admin y agrégalos a los grupos correspondientes (Vendedores o Clientes).

## 4. Protege la vista (opcional, pero recomendado)

En `views.py`, agrega el decorador `@permission_required('ventas.add_automovil', raise_exception=True)` a la vista de creación para lanzar un error 403 si no tiene permiso.

## 5. Prueba los permisos

- Inicia el servidor: `python manage.py runserver`.
- Inicia sesión con un usuario vendedor: Debería ver el formulario.
- Inicia sesión con un cliente: Debería ver el mensaje de "No tienes permisos".
- Verifica en el admin que los permisos estén asignados correctamente.