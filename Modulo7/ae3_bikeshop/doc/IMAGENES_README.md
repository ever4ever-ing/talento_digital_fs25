# 📸 Guía de Uso: Imágenes en BikeShop

## ✅ Implementación Completada

Se ha configurado exitosamente el manejo de imágenes en la aplicación BikeShop con **almacenamiento local**.

---

## 🎯 ¿Qué se implementó?

### 1. **Pillow Instalado**
- Librería Python para procesamiento de imágenes
- Requerido por Django para manejar `ImageField`

### 2. **Configuración en Settings**
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
- `MEDIA_URL`: URL base para acceder a las imágenes (`/media/`)
- `MEDIA_ROOT`: Carpeta donde se guardan físicamente (`/media/`)

### 3. **Campo Imagen Agregado al Modelo**
```python
imagen = models.ImageField(upload_to='bicicletas/', blank=True, null=True)
```
- `upload_to='bicicletas/'`: Las imágenes se guardan en `media/bicicletas/`
- `blank=True, null=True`: El campo es opcional

### 4. **URLs Configuradas**
- Django sirve automáticamente los archivos media en desarrollo
- Solo funciona cuando `DEBUG=True`

### 5. **Template Actualizado**
- Diseño tipo "tarjetas" (grid) en lugar de tabla
- Muestra las imágenes si existen
- Muestra un ícono 🚲 si no hay imagen
- Diseño responsive y moderno

---

## 🚀 Cómo Usar

### Opción 1: Desde el Admin de Django (Recomendado)

1. **Iniciar el servidor**:
   ```bash
   python manage.py runserver
   ```

2. **Ir al admin**:
   ```
   http://localhost:8000/admin/
   ```

3. **Agregar/Editar una bicicleta**:
   - Click en "Bicicletas" → "Add Bicicleta" o editar una existente
   - Completar los campos (marca, modelo, tipo, etc.)
   - En el campo "Imagen", click en "Choose File"
   - Seleccionar una imagen de tu computadora
   - Click en "Save"

4. **Ver el catálogo**:
   ```
   http://localhost:8000/
   ```

### Opción 2: Programáticamente (Python Shell)

```bash
python manage.py shell
```

```python
from bicicletas.models import Bicicleta
from django.core.files import File

# Crear bicicleta con imagen
with open('ruta/a/tu/imagen.jpg', 'rb') as f:
    bici = Bicicleta.objects.create(
        marca="Trek",
        modelo="X-Caliber",
        tipo="MTB",
        precio=1500.00,
        anio=2024,
        imagen=File(f, name='trek.jpg')
    )
```

---

## 📁 Estructura de Archivos

```
ae3_bikeshop/
├── media/                          ← Carpeta creada automáticamente
│   └── bicicletas/                 ← Imágenes de bicicletas aquí
│       ├── imagen1.jpg
│       ├── imagen2.png
│       └── ...
├── bicicletas/
│   ├── models.py                   ← Modelo con ImageField
│   ├── admin.py                    ← Admin configurado
│   └── templates/
│       └── lista_bicicletas.html   ← Template actualizado
├── bikeshop/
│   ├── settings.py                 ← MEDIA_URL y MEDIA_ROOT
│   └── urls.py                     ← URLs para servir media
└── manage.py
```

---

## 🖼️ Formatos de Imagen Soportados

- **JPG/JPEG** ✅ (recomendado)
- **PNG** ✅ (recomendado)
- **GIF** ✅
- **WEBP** ✅
- **BMP** ✅

**Recomendación**: Usa JPG o PNG con tamaño menor a 2MB para mejor rendimiento.

---

## 💡 Características del Template

### Diseño en Tarjetas (Grid)
- Diseño responsive que se adapta al tamaño de pantalla
- Mínimo 300px por tarjeta
- Efecto hover al pasar el mouse

### Imagen o Placeholder
```django
{% if bici.imagen %}
    <img src="{{ bici.imagen.url }}" alt="...">
{% else %}
    <div class="no-image">🚲</div>
{% endif %}
```

### Información Mostrada
- ✅ Imagen de la bicicleta (o ícono si no tiene)
- ✅ Marca y modelo
- ✅ Tipo (badge colorido)
- ✅ Año de fabricación
- ✅ Precio destacado
- ✅ Estado de disponibilidad

---

## 🔧 Solución de Problemas

### Problema: "Las imágenes no se muestran"

**Solución 1**: Verificar que el servidor esté corriendo
```bash
python manage.py runserver
```

**Solución 2**: Verificar que la carpeta media existe
```bash
# Debería existir: ae3_bikeshop/media/bicicletas/
```

**Solución 3**: Verificar la configuración en settings.py
```python
DEBUG = True  # Debe estar en True para desarrollo
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**Solución 4**: Verificar las URLs
```python
# En bikeshop/urls.py debe estar:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Problema: "No puedo subir imágenes en el admin"

**Solución**: Verificar que Pillow está instalado
```bash
pip list | grep -i pillow
# O en Windows:
pip list | findstr /i pillow
```

Si no está:
```bash
pip install Pillow
```

### Problema: "Error 404 al acceder a /media/..."

**Solución**: Asegurarse de que `DEBUG=True` en settings.py

---

## 🌐 Para Producción (Futuro)

Cuando despliegues tu aplicación en producción, **NO** uses esta configuración. En producción debes:

### Opción 1: Almacenamiento en la Nube (Recomendado)
- **AWS S3**: Amazon Simple Storage Service
- **Azure Blob Storage**: Servicio de almacenamiento de Microsoft
- **Google Cloud Storage**: Almacenamiento de Google
- **Cloudinary**: Servicio especializado en imágenes

### Opción 2: Servidor de Archivos
- Usar un servidor web (Nginx, Apache) para servir archivos estáticos
- Separar los archivos media del servidor de aplicación

### Librería Recomendada
```bash
pip install django-storages boto3  # Para AWS S3
```

---

## 📊 Buenas Prácticas

### 1. Validación de Tamaño
Puedes agregar validación en el modelo:

```python
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_image_size(image):
    file_size = image.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f"El tamaño máximo es {limit_mb}MB")

class Bicicleta(models.Model):
    # ... otros campos ...
    imagen = models.ImageField(
        upload_to='bicicletas/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp']),
            validate_image_size
        ]
    )
```

### 2. Generar Thumbnails
Para mejor rendimiento, puedes generar miniaturas:

```bash
pip install django-imagekit
```

```python
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Bicicleta(models.Model):
    imagen = models.ImageField(upload_to='bicicletas/')
    imagen_thumbnail = ImageSpecField(
        source='imagen',
        processors=[ResizeToFill(300, 200)],
        format='JPEG',
        options={'quality': 85}
    )
```

### 3. Nombres de Archivo Únicos
Para evitar colisiones de nombres:

```python
import uuid
from django.utils.text import slugify

def upload_to_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{slugify(instance.marca)}-{slugify(instance.modelo)}-{uuid.uuid4().hex[:8]}.{ext}"
    return f'bicicletas/{filename}'

class Bicicleta(models.Model):
    imagen = models.ImageField(upload_to=upload_to_path, blank=True, null=True)
```

---

## 🎨 Personalización del Template

### Cambiar el Tamaño de las Tarjetas
En `lista_bicicletas.html`, línea 14:
```css
.bikes-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    /* Cambiar 300px por el ancho mínimo deseado */
}
```

### Cambiar la Altura de las Imágenes
Línea 30:
```css
.bike-image {
    height: 200px;  /* Cambiar este valor */
}
```

### Cambiar los Colores
```css
/* Color del precio */
.precio {
    color: #27ae60;  /* Verde */
}

/* Color del badge de tipo */
.tipo-badge {
    background: #3498db;  /* Azul */
}

/* Gradiente del placeholder sin imagen */
.no-image {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

---

## 📝 Notas Importantes

1. ✅ **Almacenamiento Local**: Las imágenes se guardan en tu computadora/servidor
2. ✅ **Solo Desarrollo**: Esta configuración es solo para desarrollo (DEBUG=True)
3. ✅ **Git**: Considera agregar `media/` al `.gitignore`
4. ✅ **Respaldo**: Haz backups de la carpeta `media/` regularmente
5. ✅ **Migración Aplicada**: La base de datos ya tiene el campo `imagen`

---

## 🔐 Seguridad

### Agregar al .gitignore
```gitignore
# Media files
media/

# Excepto la carpeta base
!media/.gitkeep
```

### Crear .gitkeep
```bash
mkdir -p media/bicicletas
touch media/bicicletas/.gitkeep
```

---

## ✨ Resultado Final

- ✅ Pillow instalado y configurado
- ✅ Campo `imagen` agregado al modelo Bicicleta
- ✅ Migraciones aplicadas
- ✅ URLs configuradas para servir archivos media
- ✅ Template actualizado con diseño moderno
- ✅ Admin configurado para subir imágenes
- ✅ Carpeta `media/bicicletas/` lista para recibir imágenes

**¡Listo para subir imágenes de bicicletas!** 🚴‍♂️📸

---

## 🆘 ¿Necesitas Ayuda?

1. Verifica que el servidor esté corriendo: `python manage.py runserver`
2. Verifica que Pillow esté instalado: `pip list`
3. Verifica la configuración en `settings.py`
4. Revisa la consola del servidor para errores
5. Usa las herramientas de desarrollador del navegador (F12)

---

*Documentación creada - 9 de noviembre de 2025*
