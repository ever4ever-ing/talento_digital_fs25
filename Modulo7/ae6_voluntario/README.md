# Sistema de Gestión de Voluntarios 🤝

Sistema Django minimalista para gestionar voluntarios que participan en eventos comunitarios de una ONG.

## 📋 Características

- ✅ Registro y gestión de voluntarios
- ✅ Creación y administración de eventos
- ✅ Asignación de voluntarios a eventos
- ✅ Panel de administración Django
- ✅ Interfaz web moderna y responsive
- ✅ Operaciones CRUD completas

## 🛠️ Tecnologías

- Python 3.x
- Django 4.x
- **MySQL** (base de datos)
- HTML/CSS

## 📁 Estructura del Proyecto

```
ae7_voluntario/
│
├── config/                 # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py        # Configuración principal
│   ├── urls.py            # URLs principales
│   ├── wsgi.py
│   └── asgi.py
│
├── voluntarios/           # Aplicación principal
│   ├── __init__.py
│   ├── admin.py           # Configuración del admin
│   ├── apps.py
│   ├── models.py          # Modelos Voluntario y Evento
│   ├── views.py           # Vistas
│   └── urls.py            # URLs de la app
│
├── templates/             # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── voluntarios/
│   │   ├── lista.html
│   │   ├── detalle.html
│   │   ├── crear.html
│   │   ├── editar.html
│   │   └── eliminar.html
│   └── eventos/
│       ├── lista.html
│       ├── detalle.html
│       ├── crear.html
│       ├── editar.html
│       ├── eliminar.html
│       └── asignar_voluntarios.html
│
├── manage.py
└── requirements.txt
```

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.x instalado
- MySQL Server instalado y corriendo
- Visual Studio C++ Build Tools (para Windows)

### 1. Instalar MySQL

Descarga e instala MySQL desde: https://dev.mysql.com/downloads/installer/

### 2. Crear la base de datos

```sql
mysql -u root -p
CREATE DATABASE voluntarios_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 3. Instalar dependencias

```powershell
pip install django
pip install mysqlclient
```

**Nota**: Si tienes problemas con mysqlclient en Windows, usa PyMySQL:
```powershell
pip install pymysql
```

Y agrega al inicio de `config/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### 4. Configurar credenciales

Edita `config/settings.py` y ajusta las credenciales de MySQL (líneas 62-69):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'voluntarios_db',
        'USER': 'root',  # Tu usuario
        'PASSWORD': 'tu_password',  # Tu contraseña
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Crear las migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario

```powershell
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```powershell
python manage.py runserver
```

### 8. Acceder a la aplicación

- **Aplicación web**: http://127.0.0.1:8000/
- **Panel de administración**: http://127.0.0.1:8000/admin/

---

## 🔧 Script de Instalación Automática

Para facilitar la instalación, puedes usar el script automatizado:

```powershell
.\setup.ps1
```

Este script:
- ✅ Verifica Python y MySQL
- ✅ Instala dependencias
- ✅ Crea y aplica migraciones
- ✅ Te guía en la creación del superusuario

---

## 📖 Documentación Adicional

Para instrucciones detalladas sobre MySQL, consulta: **[MYSQL_SETUP.md](MYSQL_SETUP.md)**

## 📊 Modelos

### Voluntario

- `nombre`: Nombre completo del voluntario
- `email`: Correo electrónico único
- `telefono`: Número de teléfono (opcional)
- `fecha_registro`: Fecha y hora de registro (automático)

### Evento

- `titulo`: Título del evento
- `descripcion`: Descripción detallada
- `fecha`: Fecha del evento
- `voluntarios`: Relación ManyToMany con voluntarios

## 🔧 Funcionalidades

### Voluntarios

- ✅ Listar todos los voluntarios
- ✅ Ver detalle de un voluntario
- ✅ Crear nuevo voluntario
- ✅ Editar voluntario existente
- ✅ Eliminar voluntario
- ✅ Ver eventos asignados a un voluntario

### Eventos

- ✅ Listar todos los eventos
- ✅ Ver detalle de un evento
- ✅ Crear nuevo evento
- ✅ Editar evento existente
- ✅ Eliminar evento
- ✅ Asignar/desasignar voluntarios a eventos
- ✅ Ver lista de voluntarios asignados

### Dashboard

- 📊 Estadísticas generales
- 👥 Voluntarios recientes
- 📅 Próximos eventos

## 🎨 Interfaz

La aplicación cuenta con una interfaz moderna que incluye:

- Diseño responsive
- Navegación intuitiva
- Mensajes de confirmación
- Alertas de advertencia
- Formularios validados
- Tablas organizadas

## 🔐 Panel de Administración

El panel de administración de Django incluye:

- Gestión completa de voluntarios
- Gestión completa de eventos
- Filtros por fecha
- Búsqueda por nombre, email, título
- Asignación de voluntarios mediante interfaz horizontal

## 📝 Notas de Desarrollo

Este es un proyecto **minimalista** que:

- No usa formularios de Django (forms.py) - todo manual con HTML
- No usa class-based views - solo function-based views
- No usa librerías CSS externas - CSS inline en base.html
- Usa **MySQL** como base de datos (migrado desde SQLite)
- Es perfecto para aprendizaje y proyectos pequeños

## 🔍 Comandos Útiles de MySQL

```sql
-- Ver las tablas
SHOW TABLES;

-- Ver voluntarios
SELECT * FROM voluntarios_voluntario;

-- Ver eventos
SELECT * FROM voluntarios_evento;

-- Contar voluntarios
SELECT COUNT(*) FROM voluntarios_voluntario;
```

## 👨‍💻 Autor

Desarrollado para el curso Talento Digital 2025 - Módulo 7

## 📄 Licencia

Proyecto educativo - Uso libre para aprendizaje
