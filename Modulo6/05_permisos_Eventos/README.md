## Plataforma de Gestión de Eventos en Django

Esta es una plataforma web desarrollada en Django que permite a los usuarios registrarse y gestionar eventos como conferencias, conciertos y seminarios. Algunos eventos pueden ser privados y solo accesibles por usuarios específicos.

### Características

- **Registro de usuarios**: Los usuarios pueden crear cuentas y autenticarse.
- **Gestión de eventos**: Crear, listar y ver detalles de eventos.
- **Eventos privados**: Los eventos pueden ser marcados como privados y restringidos a usuarios específicos.
- **Permisos**: Control de acceso basado en permisos para eventos privados.

### Requisitos

- Python 3.8 o superior
- Django 5.2
- Un navegador web

### Instalación

1. Clona o descarga el proyecto.

2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```

3. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En Linux/Mac: `source venv/bin/activate`

4. Instala las dependencias:
   ```
   pip install django
   ```

5. Navega al directorio del proyecto (donde está manage.py).

6. Ejecuta las migraciones:
   ```
   python manage.py migrate
   ```

7. Crea un superusuario (opcional, para acceder al admin):
   ```
   python manage.py createsuperuser
   ```

### Uso

1. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

2. Abre tu navegador y ve a `http://127.0.0.1:8000/`

3. Regístrate como nuevo usuario o inicia sesión si ya tienes cuenta.

4. Crea eventos desde la interfaz.

5. Los eventos privados solo serán visibles para los usuarios permitidos.

### Estructura del Proyecto

- `eventos/`: Contiene la configuración principal del proyecto Django.
  - `settings.py`: Configuración del proyecto (apps, base de datos, etc.).
  - `urls.py`: URLs principales del proyecto.
- `events/`: Aplicación principal que gestiona los eventos.
  - `models.py`: Define los modelos de la base de datos (ej. `Event`).
  - `views.py`: Lógica de las vistas que manejan las peticiones.
  - `urls.py`: URLs específicas de la aplicación `events`.
  - `forms.py`: Formularios de Django (ej. `EventForm`).
  - `templates/events/`: Plantillas HTML específicas de la app.
- `templates/`: Contiene las plantillas HTML globales.
  - `base.html`: Plantilla base que se hereda en las demás.
  - `registration/`: Plantillas para login y registro.
- `manage.py`: Utilidad de línea de comandos para interactuar con el proyecto.
- `db.sqlite3`: Base de datos SQLite utilizada en desarrollo.

## Modelos

#### Event
- `title`: Título del evento
- `description`: Descripción del evento
- `date`: Fecha y hora del evento
- `is_private`: Booleano para indicar si es privado
- `allowed_users`: Usuarios permitidos para eventos privados
- `creator`: Usuario que creó el evento

### Vistas

- `event_list`: Lista de eventos accesibles al usuario
- `event_detail`: Detalles de un evento específico
- `event_create`: Formulario para crear nuevos eventos
- `register`: Registro de nuevos usuarios

### Roles y Permisos

La aplicación implementa un sistema de roles para gestionar el acceso de los usuarios:

- **Administradores**: Tienen control total sobre todos los eventos.
  - **Permisos**: `add_event`, `change_event`, `delete_event`.
  - **Acceso**: Pueden crear, editar y eliminar cualquier evento.

- **Organizadores de eventos**: Pueden gestionar los eventos que crean.
  - **Permisos**: `add_event`, `change_event`.
  - **Acceso**: Pueden crear y editar sus propios eventos, pero no eliminarlos.

- **Asistentes**: Solo pueden ver los eventos a los que tienen acceso.
  - **Permisos**: Ninguno por defecto.
  - **Acceso**: Pueden ver eventos públicos y privados a los que han sido invitados.

#### Implementación

- **Grupos de Django**: Los roles se implementan usando el sistema de `Group` de Django.
- **Permisos por defecto**: Se utilizan los permisos `add`, `change`, y `delete` que Django crea automáticamente para cada modelo.
- **Lógica de negocio**: Las vistas y plantillas verifican los permisos del usuario (`user.has_perm()`) antes de permitir acciones.

## Autenticación y Permisos

### Sistema de Login/Logout

La aplicación utiliza el sistema de autenticación integrado de Django:

- **URLs de autenticación**: `/accounts/login/`, `/accounts/logout/`
- **Redirección**: Después del login/logout, los usuarios son redirigidos a la página principal
- **Registro**: Los nuevos usuarios pueden registrarse en `/register/`

### Control de Acceso

- Todas las vistas principales requieren autenticación (`@login_required`)
- Los eventos privados solo son visibles para:
  - El creador del evento
  - Usuarios explícitamente permitidos
- La navegación se adapta dinámicamente según el estado de autenticación

### Flujo de Autenticación

1. **Registro**: Usuario crea cuenta → Redirigido al login
2. **Login**: Credenciales válidas → Acceso a eventos
3. **Logout**: Cierre de sesión → Página principal
4. **Acceso restringido**: Eventos privados verifican permisos por usuario

## Permisos

Los eventos privados solo son accesibles por:
- El creador del evento
- Usuarios explícitamente permitidos en `allowed_users`

