# Creando primer proyecto django
1. **Crear entorno virtual (venv)**  
    ```bash
    python -m venv .venv
    ```

2. **Activar entorno virtual (PowerShell)**  
    ```bash
    .\.venv\Scripts\Activate
    ```

3. **Instalar Django**  
    ```bash
    pip install django
    ```

4. **Crear proyecto llamado `mi_proyecto`**  
    ```bash
    django-admin startproject mi_proyecto .
    ```

5. **Crear app llamada `web` dentro del proyecto**  
    ```bash
    python manage.py startapp web
    ```

6. **Configurar `mi_proyecto/settings.py` para templates**

     - Asegúrate de que `INSTALLED_APPS` incluya tu app (`web`):

        ```python
        INSTALLED_APPS = [
             # otras apps de Django...
             'web',
        ]
        ```

     - Configura los templates (por defecto):

        ```python
        TEMPLATES = [
             {
                  'BACKEND': 'django.template.backends.django.DjangoTemplates',
                  'DIRS': [],
                  'APP_DIRS': True,
                  'OPTIONS': {
                        # opciones adicionales...
                  },
             },
        ]
        ```

     - Si quieres usar una carpeta global de templates, modifica `'DIRS'`:

        ```python
        'DIRS': [BASE_DIR / 'templates'],
        ```

     > **Nota:** Con `APP_DIRS: True`, Django buscará templates dentro de cada app, por ejemplo: `web/templates/web/inicio.html`.

7. **Crear vista en `web/views.py`**  
    ```python
    from django.shortcuts import render

    def inicio(request):
         contexto = {'mensaje': '¡Hola desde Django!'}
         return render(request, 'web/inicio.html', contexto)
    ```

8. **Configurar URLs en `mi_proyecto/urls.py`**  
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('web.urls')),  # enruta la raíz a la app 'web'
    ]
    ```

9. **Crear Archivo mi_aplicacion/urls.py**
``` 
from django.urls import path
from . import views

app_name = 'mi_aplicacion'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
```
10. **Crear migraciones y ejecutar servidor**

     - Migraciones iniciales:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

     - Ejecutar servidor:
        ```bash
        python manage.py runserver
        ```



# Admin 
python manage.py createsuperuser
