Proyecto minimal de Events (Django)

Pasos mínimos:

1. Crear y activar un virtualenv e instalar Django

   python -m venv .venv; .\.venv\Scripts\Activate; python -m pip install --upgrade pip; pip install django

2. Ejecutar migraciones:

   python manage.py makemigrations
   python manage.py migrate

3. Crear superusuario si desea acceder al admin:

   python manage.py createsuperuser

4. Inicializar roles/grupos:

   python manage.py initroles

5. Ejecutar servidor de desarrollo:

   python manage.py runserver

Rutas útiles:

- /login/ - login
- /logout/ - logout
- /events/ - lista de eventos
