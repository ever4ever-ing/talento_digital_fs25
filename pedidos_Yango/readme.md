# Aplicación de Pedidos Yango

Esta es una aplicación web desarrollada con Django para gestionar pedidos de productos. Incluye autenticación de usuarios, gestión de productos y pedidos.

## Requisitos

- Python 3.12 o superior
- MySQL Server
- Pip (gestor de paquetes de Python)

## Instalación

### 1. Instalar Python y Django

Asegúrate de tener Python instalado. Verifica con:

```bash
python --version
```

Instala Django y el conector de MySQL:

```bash
pip install django mysqlclient
```

### 2. Crear el proyecto Django

```bash
django-admin startproject pedidos_yango .
```

### 3. Configurar la base de datos MySQL

Crea una base de datos en MySQL:

```sql
CREATE DATABASE pedidos_yango_db;
```

Edita `pedidos_yango/settings.py` para configurar la conexión:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pedidos_yango_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Crear la aplicación

```bash
python manage.py startapp pedidos
```

Agrega 'pedidos' a INSTALLED_APPS en settings.py.

### 5. Definir modelos

En `pedidos/models.py`, define los modelos Producto, Pedido y PedidoProducto.

### 6. Crear migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear vistas y URLs

Define vistas en `pedidos/views.py` y URLs en `pedidos/urls.py`.

Incluye las URLs en `pedidos_yango/urls.py`.

### 8. Configurar plantillas

Crea directorio `templates/pedidos/` y agrega plantillas HTML.

Actualiza TEMPLATES en settings.py.

### 9. Autenticación

Usa Django auth. Agrega vistas para registro y login.

Incluye `django.contrib.auth.urls` en URLs.

### 10. Ejecutar el servidor

```bash
python manage.py runserver
```

## Uso

- **Página principal**: `http://127.0.0.1:8000/` - Muestra botones para acceder a registro, direcciones, pedidos y productos. Incluye login/logout automático.
- Regístrate en /register/ (redirige a home después).
- Inicia sesión en /accounts/login/ (redirige a home).
- Gestiona direcciones en /direcciones/ (solo las tuyas).
- Gestiona pedidos en /pedidos/ (solo los tuyos).
- Gestiona productos en /productos/ (listar, crear, editar, eliminar).
- Admin en /admin/ para gestión avanzada.

## Funcionalidades

- **Productos**: CRUD completo (Crear, Leer, Actualizar, Eliminar).
- **Direcciones**: CRUD para direcciones de entrega (asociadas a usuarios/clientes).
- **Pedidos**: Crear pedidos seleccionando productos y cantidades, listar pedidos del usuario, ver detalles, eliminar (restaura stock). Incluye selección de dirección de entrega.
- **Autenticación**: Registro, login, logout (los usuarios registrados son los clientes).
- **Admin**: Interfaz administrativa para gestionar todo.

## Próximos pasos

- Mejorar la interfaz de usuario con CSS/Bootstrap
- Agregar validaciones adicionales
- Implementar pagos o integración con APIs
- Desplegar en un servidor de producción