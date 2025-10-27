# Explicación de `models.py`

El archivo `models.py` define el modelo principal de la aplicación: el evento (`Event`). Este modelo representa la estructura de los datos que se almacenan en la base de datos y cómo se relacionan con los usuarios.

## Modelo `Event`

- **title**: Nombre del evento. Es un campo de texto corto (máx. 200 caracteres).
- **description**: Descripción opcional del evento. Permite texto libre.
- **date**: Fecha y hora en que se realizará el evento.
- **is_private**: Indica si el evento es privado (solo el propietario y administradores pueden verlo).
- **owner**: Usuario que creó el evento. Si el usuario se elimina, también se eliminan sus eventos. El atributo `related_name='events'` permite acceder a todos los eventos de un usuario con `user.events`.

## Permisos personalizados
En la clase interna `Meta`, se define el permiso `can_manage_event`, que permite crear y gestionar eventos. Este permiso puede ser asignado a roles específicos para controlar el acceso a ciertas funcionalidades.

## Métodos
- **__str__**: Devuelve el título del evento, útil para mostrarlo en el panel de administración y en listados.
- **get_absolute_url**: Retorna la URL de la lista de eventos, utilizada para redirigir tras crear o editar un evento.

## Relación con usuarios
El modelo utiliza `get_user_model()` para obtener el modelo de usuario configurado en el proyecto, permitiendo flexibilidad si se usa un modelo de usuario personalizado.

## Resumen
Este archivo es esencial para definir cómo se almacenan y gestionan los eventos en la aplicación, estableciendo relaciones, permisos y comportamientos clave para el funcionamiento del sistema.