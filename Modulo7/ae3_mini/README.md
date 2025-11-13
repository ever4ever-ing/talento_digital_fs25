# Proyecto Django "Academico"

Este proyecto implementa una aplicación minimalista para gestión académica usando Django y MySQL.

## Requisitos previos
- Python 3.x
- MySQL instalado y corriendo
- Usuario MySQL: `root`, contraseña: `password`

## Pasos para la creación

1. **Crear entorno virtual e instalar Django**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install django mysqlclient Pillow
   ```

2. **Crear el proyecto y la app**
   ```powershell
   django-admin startproject mini_proyecto .
   python manage.py startapp academico
   ```

3. **Configurar la base de datos MySQL**
   Edita `mini_proyecto/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'academico_db',
           'USER': 'root',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. **Crear la base de datos en MySQL**
   ```powershell
   mysql -u root -ppassword -e "CREATE DATABASE academico_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
   ```

5. **Agregar la app a `INSTALLED_APPS` en `settings.py`**
   ```python
   INSTALLED_APPS = [
       ...
       'academico',
   ]
   ```

6. **Definir los modelos en `academico/models.py`**
   - Profesor, Curso, Estudiante, Perfil, Inscripcion (ver código fuente)

7. **Crear y aplicar migraciones**
   ```powershell
   python manage.py makemigrations academico
   python manage.py migrate
   ```

8. **Crear superusuario para el admin**
   ```powershell
   python manage.py createsuperuser
   ```

9. **Registrar los modelos en `academico/admin.py`**
   - Permite gestión desde el panel de administración

10. **Crear formularios en `academico/forms.py`**
    - Para cada modelo

11. **Crear vistas en `academico/views.py`**
    - Vistas de registro y listado para cada modelo
    - Menú principal con navegación

12. **Configurar URLs**
    - En `academico/urls.py` y agregar en `mini_proyecto/urls.py`:
      ```python
      path('academico/', include('academico.urls')),
      ```

13. **Crear plantillas HTML en `academico/templates/academico/`**
    - Formularios y listas para cada modelo
    - Menú principal


14. **Configurar archivos media para imágenes de perfil**
      - En `settings.py` agrega:
         ```python
         MEDIA_URL = '/media/'
         MEDIA_ROOT = BASE_DIR / 'media'
         ```
      - En `mini_proyecto/urls.py` agrega:
         ```python
         from django.conf import settings
         from django.conf.urls.static import static
         ...
         if settings.DEBUG:
               urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
         ```
      - Las imágenes de perfil se guardan en la carpeta `media/perfiles/`.
      - Ejemplo de ruta de imagen: `perfiles/adventure-2548133_1280.jpg`

15. **Ejecutar el servidor**
      ```powershell
      python manage.py runserver
      ```

## Navegación
- Menú principal: `/academico/`
- Panel de administración: `/admin/`

## Notas

- El archivo `db.sqlite3` puede eliminarse, ya que la base de datos usada es MySQL.
- Todos los modelos y relaciones están implementados según los requisitos del enunciado.
- Las imágenes de perfil se muestran en círculo de 50x50 px en la lista de perfiles.

---
Desarrollado con ❤️ usando Django y MySQL.
