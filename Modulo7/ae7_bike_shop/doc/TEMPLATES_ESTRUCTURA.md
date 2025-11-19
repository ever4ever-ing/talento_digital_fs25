# 📁 Estructura de Templates Centralizada - BikeShop

## 🎯 Nueva Organización

Los templates ahora están centralizados en la carpeta `templates/` en la raíz del proyecto, organizados por app en subcarpetas.

## 📂 Estructura Actual

```
bikeshop/
├── templates/
│   ├── base/
│   │   └── base.html                 # Template base compartido
│   ├── bicicletas/
│   │   ├── lista_bicicletas.html     # Catálogo de bicicletas
│   │   └── crear_bicicleta.html      # Crear/editar bicicleta
│   ├── clientes/
│   │   ├── login.html                # Inicio de sesión
│   │   ├── registro.html             # Registro de usuarios
│   │   └── perfil.html               # Perfil de usuario
│   ├── carrito/
│   │   ├── carrito_detalle.html      # Detalle del carrito
│   │   └── mis_ordenes.html          # Lista de órdenes
│   └── resenas/
│       ├── detalle_bicicleta.html    # Detalle + reseñas
│       ├── crear_resena.html         # Crear reseña
│       ├── editar_resena.html        # Editar reseña
│       └── mis_resenas.html          # Mis reseñas
```

---

## ⚙️ Configuración

### settings.py
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ Templates centralizados
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## 🎨 Template Base (base.html)

El template base incluye:

- ✅ Fuente Google Fonts (Sora)
- ✅ Bootstrap 5.3.2
- ✅ Paleta de colores personalizada
- ✅ Navbar con carrito y autenticación
- ✅ Sistema de mensajes
- ✅ Bloques extendibles

### Uso:
```django
{% extends 'base/base.html' %}

{% block title %}Mi Página - BikeShop{% endblock %}

{% block extra_css %}
    <style>
        /* Estilos adicionales */
    </style>
{% endblock %}

{% block content %}
    <!-- Contenido de la página -->
{% endblock %}

{% block extra_js %}
    <script>
        // JavaScript adicional
    </script>
{% endblock %}
```

---

## 📝 Rutas de Templates en Vistas

### app_bicicletas/views.py
```python
# Antes
return render(request, 'lista_bicicletas.html', context)

# Ahora
return render(request, 'bicicletas/lista_bicicletas.html', context)
```

### app_clientes/views.py
```python
# Antes
return render(request, 'auth/login.html', context)

# Ahora
return render(request, 'clientes/login.html', context)
```

### app_carrito/views.py
```python
# Antes
return render(request, 'carrito_detalle.html', context)

# Ahora
return render(request, 'carrito/carrito_detalle.html', context)
```

### app_resenas/views.py
```python
# Antes
return render(request, 'detalle_bicicleta.html', context)

# Ahora
return render(request, 'resenas/detalle_bicicleta.html', context)
```

---

## ✅ Ventajas de la Nueva Estructura

### 1. **Organización Clara**
- Cada app tiene su propia carpeta
- Fácil localizar templates
- Estructura escalable

### 2. **Evita Conflictos**
- No hay riesgo de nombres duplicados
- Namespacing automático
- Mejor mantenibilidad

### 3. **Template Base Compartido**
- Estilos consistentes
- Navbar unificada
- Un solo lugar para cambios globales

### 4. **Separación de Responsabilidades**
- Templates de apps independientes
- Base global para elementos comunes
- Fácil de modificar por secciones

### 5. **Mejor para Equipos**
- Desarrolladores pueden trabajar en apps diferentes
- Menos conflictos en git
- Estructura profesional

---

## 🔄 Migración Realizada

### Cambios en el Código:

✅ **settings.py**: Agregado `BASE_DIR / 'templates'` a `DIRS`

✅ **app_bicicletas/views.py**: 
- `'lista_bicicletas.html'` → `'bicicletas/lista_bicicletas.html'`
- `'crear_bicicleta.html'` → `'bicicletas/crear_bicicleta.html'`

✅ **app_clientes/views.py**:
- `'auth/login.html'` → `'clientes/login.html'`
- `'auth/registro.html'` → `'clientes/registro.html'`
- `'auth/perfil.html'` → `'clientes/perfil.html'`

✅ **app_carrito/views.py**:
- `'carrito_detalle.html'` → `'carrito/carrito_detalle.html'`
- `'mis_ordenes.html'` → `'carrito/mis_ordenes.html'`

✅ **app_resenas/views.py**:
- `'detalle_bicicleta.html'` → `'resenas/detalle_bicicleta.html'`
- `'crear_resena.html'` → `'resenas/crear_resena.html'`
- `'editar_resena.html'` → `'resenas/editar_resena.html'`
- `'mis_resenas.html'` → `'resenas/mis_resenas.html'`

---

## 🎨 Paleta de Colores en base.html

```css
/* Verde oscuro */
--color-dark: #00392d;

/* Azul petróleo */
--color-primary: #006e8c;

/* Naranja */
--color-accent: #eb7f25;

/* Amarillo dorado */
--color-warning: #ffcc52;

/* Amarillo claro */
--color-light: #ffff8f;
```

---

## 📋 Checklist de Verificación

Para verificar que todo funciona:

```bash
# 1. Iniciar el servidor
python manage.py runserver

# 2. Probar todas las URLs:
- http://localhost:8000/                  # Lista de bicicletas ✓
- http://localhost:8000/auth/login/       # Login ✓
- http://localhost:8000/auth/registro/    # Registro ✓
- http://localhost:8000/auth/perfil/      # Perfil ✓
- http://localhost:8000/carrito/          # Carrito ✓
- http://localhost:8000/mis-ordenes/      # Órdenes ✓
- http://localhost:8000/bicicleta/<id>/   # Detalle + Reseñas ✓
```

---

## 🔮 Futuras Mejoras (Opcional)

### 1. Componentes Reutilizables
```
templates/
├── components/
│   ├── navbar.html
│   ├── footer.html
│   ├── card_bicicleta.html
│   └── star_rating.html
```

### 2. Layouts Alternativos
```
templates/
├── base/
│   ├── base.html           # Layout principal
│   ├── base_simple.html    # Sin navbar (login/registro)
│   └── base_admin.html     # Layout para admin
```

### 3. Archivos Estáticos Centralizados
```
static/
├── css/
│   ├── base.css
│   └── colors.css
├── js/
│   └── main.js
└── img/
    └── logos/
```

---

## 📚 Recursos

- [Django Templates Documentation](https://docs.djangoproject.com/en/5.2/topics/templates/)
- [Template Inheritance](https://docs.djangoproject.com/en/5.2/ref/templates/language/#template-inheritance)
- [Template Loading](https://docs.djangoproject.com/en/5.2/ref/templates/api/#django.template.loaders.filesystem.Loader)

---

**¡Estructura de templates reorganizada exitosamente! 📁✨**
