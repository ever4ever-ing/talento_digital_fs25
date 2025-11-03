Minimal Django app para registrar eventos con múltiples participantes.

## 🚀 Inicio Rápido

Pasos para ejecutar (Windows PowerShell):

1. Crear y activar entorno virtual:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instalar dependencias:
   ```powershell
   pip install -r requirements.txt
   ```

3. Aplicar migraciones y ejecutar servidor:
   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```

4. Abrir en el navegador:
   ```
   http://127.0.0.1:8000/
   ```

## 👤 Panel de Administración (Opcional)

Para acceder al admin de Django:

1. Crear superusuario:
   ```powershell
   python manage.py createsuperuser
   ```

2. Ingresar nombre de usuario, email (opcional) y contraseña

3. Acceder al admin en:
   ```
   http://127.0.0.1:8000/admin/
   ```
