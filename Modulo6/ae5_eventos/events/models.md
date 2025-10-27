# Explicación detallada de `models.py`

El archivo `models.py` define la estructura de los datos principales de la aplicación de eventos utilizando el sistema de modelos de Django. Aquí se describe cómo se almacena y gestiona la información de los eventos.

## Modelo principal: `Event`

La clase `Event` representa un evento en la base de datos. Hereda de `models.Model`, lo que le permite interactuar con el ORM de Django.

### Campos del modelo
- **title**: `CharField` de hasta 200 caracteres. Es el nombre del evento.
- **description**: `TextField` opcional para una descripción más extensa del evento.
- **date**: `DateTimeField` que almacena la fecha y hora del evento.
- **is_private**: `BooleanField` que indica si el evento es privado (solo visible para el propietario y administradores).
- **owner**: `ForeignKey` que enlaza el evento con el usuario que lo creó. Si el usuario se elimina, también se eliminan sus eventos. El parámetro `related_name='events'` permite acceder a los eventos de un usuario mediante `user.events`.

### Metadatos y permisos
La clase interna `Meta` define permisos personalizados:
- **can_manage_event**: Permite crear y gestionar eventos. Este permiso puede ser asignado a roles específicos para controlar el acceso a funcionalidades avanzadas.

### Métodos del modelo
- **__str__**: Devuelve el título del evento, facilitando su identificación en el panel de administración y otros lugares donde se represente como texto.
- **get_absolute_url**: Retorna la URL a la que se debe redirigir tras crear o editar un evento, normalmente la lista de eventos. Utiliza el sistema de rutas de Django para mayor flexibilidad.

## Relación con usuarios
El modelo utiliza `get_user_model()` para obtener el modelo de usuario activo, permitiendo compatibilidad con sistemas personalizados de autenticación.

## Conclusión
El archivo `models.py` es fundamental para definir cómo se almacenan y gestionan los eventos en la aplicación. Permite estructurar los datos, establecer relaciones con los usuarios y controlar el acceso mediante permisos, facilitando una gestión robusta y segura de la información.