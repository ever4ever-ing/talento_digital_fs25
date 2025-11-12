# Conexión de Django con MySQL en Windows

Esta guía te ayudará a conectar un proyecto Django con una base de datos MySQL en Windows.
Resultado esperado: ejecucion sin errores y acceso al panel de administración de Django.

## Requisitos previos
- Python instalado
- MySQL instalado y en funcionamiento
- pip actualizado
- entorno virtual (opcional pero recomendado)
- Django instalado (`pip install django`)

---

## 1. Instalar el paquete mysqlclient

Abre PowerShell y ejecuta:

```powershell
pip install mysqlclient
```

> Si tienes problemas en Windows, busca una versión precompilada de `mysqlclient` o instala los compiladores de C necesarios. Alternativamente, puedes usar Anaconda.

---

## 2. Crear un proyecto Django (si no tienes uno)

```powershell
django-admin startproject mi_proyecto
cd mi_proyecto
```

---

## 3. Crear una aplicación Django 

```powershell
python manage.py startapp mi_aplicacion
```

---

```
# Crear las migraciones iniciales
python manage.py makemigrations

# Ejecutar las migraciones para crear las tablas
python manage.py migrate

# Opcional: crear un superusuario
python manage.py createsuperuser

```


## 4. Crear la base de datos en MySQL

Accede a MySQL y ejecuta:

```sql
CREATE DATABASE mi_base_de_datos CHARACTER SET UTF8MB4;
```

---

## 5. Configurar la conexión en `settings.py`

Edita la sección `DATABASES` en el archivo `settings.py` de tu proyecto:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mi_base_de_datos',
        'USER': 'mi_usuario',
        'PASSWORD': 'mi_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 6. Verificar la configuración

Asegúrate de que MySQL esté corriendo. Luego ejecuta:

```powershell
python manage.py runserver
```

Si todo está bien, verás el mensaje de que el servidor de desarrollo está corriendo.

---

## 7. Crear y aplicar migraciones

Crea las migraciones:

```powershell
python manage.py makemigrations
```

Aplica las migraciones:

```powershell
python manage.py migrate
```

---

## 8. Crear un superusuario

```powershell
python manage.py createsuperuser
```

Sigue las instrucciones para crear el usuario administrador.

---

## 9. Acceder al panel de administración

Inicia el servidor si no está corriendo:

```powershell
python manage.py runserver
```

Abre tu navegador y ve a:

http://127.0.0.1:8000/admin

Inicia sesión con el superusuario creado y verifica que puedes ver y administrar las tablas.

---

## Notas adicionales
- Si tienes errores de conexión, revisa usuario, contraseña, nombre de la base de datos y que el servicio MySQL esté activo.
- Puedes usar herramientas como MySQL Workbench para gestionar la base de datos visualmente.

---

¡Listo! Ahora tu proyecto Django está conectado a MySQL.
