# Creando primer proyecto django
1. **Crear entorno virtual (venv)**  
    ```bash
    virtualenv venv
    ```

2. **Activar entorno virtual (PowerShell)**  
    ```bash
    .\.venv\Scripts\Activate
    ```

3. **Instalar Django**  
    ```bash
    pip install django
    ```

4. **Crear proyecto llamado `mi_concesionaria`**  
    ```bash
    django-admin startproject mi_concesionaria .
    ```

5. **Crear app llamada `app_autos` dentro del proyecto**  
    ```bash
    python manage.py startapp app_autos
    ```

6. **Configurar `mi_concesionaria/settings.py` para templates**

     - Asegúrate de que `INSTALLED_APPS` incluya tu app (`app_autos`):

        ```python
        INSTALLED_APPS = [
             # otras apps de Django...
             'app_autos',
        ]
        ```

     > **Nota:** Con `APP_DIRS: True`, Django buscará templates dentro de cada app, por ejemplo: `app_autos/templates/app_autos/inicio.html`.

7. **Crear vista en `app_autos/views.py`**  
    ```python
    from django.shortcuts import render

    def inicio(request):
         contexto = {'mensaje': '¡Hola desde Django!'}
         return render(request, 'app_autos/inicio.html', contexto)
    ```

8. **Configurar URLs en `mi_concesionaria/urls.py`**  
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('app_autos.urls')),  # enruta la raíz a la app 'app_autos'
    ]
    ```

9. **Crear Archivo app_autos/urls.py**
``` 
from django.urls import path
from . import views

app_name = 'app_autos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
```

10. **Crear models.py**

    ```
    class Automovil(models.Model):
        marca = models.CharField(max_length=50)
        modelo = models.CharField(max_length=50)
        anio = models.IntegerField()
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        disponible = models.BooleanField(default=True)
    ```
11. **Crear migraciones y ejecutar servidor**

     - Migraciones iniciales:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

     - Ejecutar servidor:
        ```bash
        python manage.py runserver
        ```
12. **Admin** 
    python manage.py createsuperuser

13. **Formulario**
```from django import forms
from .models import Automovil

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'anio', 'precio', 'disponible']```