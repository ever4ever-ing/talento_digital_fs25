# 🚀 GUÍA RÁPIDA DE USO

## Paso 1: Configuración Inicial

### Opción A: Instalación rápida
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Opción B: Instalación manual
```bash
pip install django pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Paso 2: Poblar Base de Datos (Opcional)

Para agregar recetas de ejemplo:
```bash
python manage.py shell < poblar_db.py
```

## Paso 3: Iniciar Servidor

```bash
python manage.py runserver
```

## 🌐 URLs Disponibles

- **Página Principal**: http://127.0.0.1:8000/
- **Lista de Recetas**: http://127.0.0.1:8000/recetas/
- **Contacto**: http://127.0.0.1:8000/contacto/
- **Admin**: http://127.0.0.1:8000/admin/

## 📝 Cómo Agregar Recetas

1. Accede al admin: http://127.0.0.1:8000/admin/
2. Inicia sesión con tu superusuario
3. Click en "Recetas"
4. Click en "Agregar Receta"
5. Completa los campos:
   - **Nombre**: Título de la receta
   - **Ingredientes**: Lista (usa Enter para separar líneas)
   - **Instrucciones**: Pasos numerados
   - **Imagen**: Sube una foto (opcional)
6. Click en "Guardar"

## ✨ Funcionalidades

✅ **Navbar**: Navegación entre Inicio, Recetas y Contacto
✅ **Jumbotron**: Destacado en página de inicio
✅ **Cards**: Visualización atractiva de recetas
✅ **Páginas Dinámicas**: URLs con parámetros
✅ **Formulario de Contacto**: Con validación
✅ **Error 404**: Página personalizada
✅ **Responsive**: Funciona en móviles y escritorio

## 🎨 Personalización

### Cambiar colores
Edita `static/css/styles.css`:
```css
:root {
    --primary-color: #tu-color;
}
```

### Modificar número de recetas en inicio
Edita `recetas/views.py`, función `inicio`:
```python
recetas = Receta.objects.all()[:6]  # Cambia el número
```

## 🔧 Comandos Útiles

```bash
# Ver todas las recetas en la base de datos
python manage.py shell
>>> from recetas.models import Receta
>>> Receta.objects.all()

# Crear nueva migración
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario adicional
python manage.py createsuperuser

# Recopilar archivos estáticos
python manage.py collectstatic
```

## 📁 Estructura Importante

```
ae3_grupal/
├── templates/          # Todos los HTML
├── static/css/         # Estilos personalizados
├── media/recetas/      # Imágenes subidas
├── recetas/            # App principal
└── recetas_project/    # Configuración
```

## 🐛 Solución de Problemas

### Error: No module named 'PIL'
```bash
pip install pillow
```

### Las imágenes no se muestran
Verifica que DEBUG = True en settings.py

### Error en migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### Puerto ocupado
```bash
python manage.py runserver 8001
```

## 📸 Agregar Imágenes a Recetas

1. Desde el admin, edita una receta
2. Click en "Elegir archivo" en el campo Imagen
3. Selecciona una imagen de tu computador
4. Guarda la receta
5. La imagen se guardará en `media/recetas/`

## 🔐 Seguridad

**IMPORTANTE**: En producción:
- Cambia SECRET_KEY en settings.py
- Establece DEBUG = False
- Configura ALLOWED_HOSTS
- Usa una base de datos robusta (PostgreSQL, MySQL)

## 📚 Recursos

- Django Docs: https://docs.djangoproject.com/
- Bootstrap: https://getbootstrap.com/
- Pillow: https://pillow.readthedocs.io/

---

¡Feliz cocina! 👨‍🍳
