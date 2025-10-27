# Proyecto Django - Recetas Deliciosas 🍳

## Descripción
Aplicación web minimalista creada con Django y Bootstrap que permite gestionar y visualizar recetas de cocina. Incluye un sistema completo con navbar, jumbotron, footer, vistas dinámicas y formulario de contacto.

## Características Principales

✅ **Navbar responsivo** con navegación a todas las secciones
✅ **Jumbotron** en la página de inicio
✅ **Footer** con información del sitio
✅ **Páginas dinámicas** para recetas individuales
✅ **Sistema de templates** con herencia
✅ **Formulario de contacto** con validación
✅ **Manejo de errores 404** personalizado
✅ **Diseño responsivo** para móviles y escritorio
✅ **Soporte para imágenes** de recetas
✅ **Estilos CSS personalizados** minimalistas

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación y Configuración

### 1. Instalar Django y Pillow

```bash
pip install django pillow
```

**Nota:** Pillow es necesario para manejar el campo `ImageField` del modelo Receta.

### 2. Realizar las Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Crear un Superusuario

Para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu usuario administrador.

### 4. Ejecutar el Servidor

```bash
python manage.py runserver
```

El sitio estará disponible en: `http://127.0.0.1:8000/`

## Uso del Proyecto

### Acceder al Panel de Administración

1. Ve a: `http://127.0.0.1:8000/admin/`
2. Inicia sesión con tu superusuario
3. Agrega recetas desde el panel

### Agregar Recetas

Desde el panel de administración:
- Click en "Recetas" → "Agregar Receta"
- Completa los campos:
  - **Nombre**: Título de la receta
  - **Ingredientes**: Lista de ingredientes (usa saltos de línea)
  - **Instrucciones**: Pasos de preparación (usa saltos de línea)
  - **Imagen**: Sube una imagen (opcional)

### Navegación del Sitio

- **Inicio** (`/`): Muestra el jumbotron y las últimas 6 recetas
- **Recetas** (`/recetas/`): Lista completa de todas las recetas
- **Detalle de Receta** (`/recetas/<id>/`): Ver detalles completos de una receta
- **Contacto** (`/contacto/`): Formulario para enviar mensajes

## Estructura del Proyecto

```
ae3_grupal/
│
├── recetas_project/          # Configuración principal del proyecto
│   ├── settings.py          # Configuración (apps, BD, archivos estáticos)
│   ├── urls.py              # URLs principales
│   └── wsgi.py
│
├── recetas/                  # Aplicación de recetas
│   ├── models.py            # Modelo Receta
│   ├── views.py             # Vistas (inicio, lista, detalle, contacto)
│   ├── urls.py              # URLs de la app
│   ├── forms.py             # Formulario de contacto
│   └── admin.py             # Configuración del admin
│
├── templates/                # Templates HTML
│   ├── base.html            # Template base (navbar + footer)
│   ├── inicio.html          # Página de inicio con jumbotron
│   ├── lista_recetas.html   # Lista de todas las recetas
│   ├── detalle_receta.html  # Detalle de una receta
│   ├── contacto.html        # Formulario de contacto
│   ├── confirmacion_contacto.html  # Confirmación de mensaje
│   └── 404.html             # Página de error personalizada
│
├── static/                   # Archivos estáticos
│   └── css/
│       └── styles.css       # Estilos CSS personalizados
│
├── media/                    # Archivos subidos (imágenes)
│   └── recetas/             # Imágenes de recetas
│
├── manage.py                 # Comando de gestión de Django
└── db.sqlite3               # Base de datos SQLite
```

## Funcionalidades Implementadas

### 1. Modelo de Datos
- Modelo `Receta` con campos: nombre, ingredientes, instrucciones, imagen
- Ordenamiento por fecha de creación (más recientes primero)
- Método para obtener descripción corta

### 2. Vistas
- **inicio**: Muestra jumbotron y últimas 6 recetas
- **lista_recetas**: Lista completa con iteradores
- **detalle_receta**: Detalles individuales con manejo de errores
- **contacto**: Formulario con validación
- **confirmacion_contacto**: Página de confirmación
- **handler404**: Página de error personalizada

### 3. Templates
- Herencia de templates desde `base.html`
- Uso de template tags ({% url %}, {% static %}, {% if %}, {% for %})
- Bootstrap 5 integrado
- Diseño responsivo

### 4. Formularios
- Formulario de contacto con validación
- Mensajes de error personalizados
- Redirección tras envío exitoso

### 5. Archivos Estáticos
- CSS personalizado minimalista
- Integración con Bootstrap
- Soporte para imágenes de recetas

### 6. Manejo de Errores
- Página 404 personalizada
- Validación de formularios
- Manejo de recetas inexistentes

## URLs Dinámicas

El proyecto utiliza etiquetas URL para enlaces dinámicos:

```django
{% url 'recetas:inicio' %}
{% url 'recetas:lista_recetas' %}
{% url 'recetas:detalle_receta' receta.pk %}
{% url 'recetas:contacto' %}
```

## Personalización

### Modificar Colores
Edita el archivo `static/css/styles.css` en las variables CSS:

```css
:root {
    --primary-color: #0d6efd;
    --dark-color: #212529;
    --light-bg: #f8f9fa;
}
```

### Cambiar Número de Recetas en Inicio
En `recetas/views.py`, modifica la vista `inicio`:

```python
recetas = Receta.objects.all()[:6]  # Cambia el 6 por el número deseado
```

## Tecnologías Utilizadas

- **Backend**: Django 5.2.7
- **Frontend**: Bootstrap 5.3.0
- **Base de Datos**: SQLite
- **Manejo de Imágenes**: Pillow
- **Lenguaje**: Python 3.x

## Características de Diseño

- 🎨 Diseño minimalista y limpio
- 📱 Totalmente responsivo
- ⚡ Animaciones suaves
- 🎯 Navegación intuitiva
- ♿ Accesible y amigable

## Próximas Mejoras (Opcionales)

- [ ] Sistema de búsqueda de recetas
- [ ] Filtros por categorías
- [ ] Sistema de valoraciones
- [ ] Comentarios en recetas
- [ ] Compartir en redes sociales
- [ ] API REST
- [ ] Autenticación de usuarios

## Solución de Problemas

### Error: No module named 'PIL'
**Solución**: Instala Pillow
```bash
pip install pillow
```

### Las imágenes no se muestran
**Solución**: Verifica que `DEBUG = True` en `settings.py` y que las URLs de media estén configuradas.

### Error 404 en archivos estáticos
**Solución**: Ejecuta:
```bash
python manage.py collectstatic
```

## Autor

Proyecto creado como actividad grupal - Módulo 6

## Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

¡Disfruta cocinando con Recetas Deliciosas! 👨‍🍳👩‍🍳
