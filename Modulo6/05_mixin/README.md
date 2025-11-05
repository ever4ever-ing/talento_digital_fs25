# 🎯 AE5: Uso de Mixins en Django

## 📚 Material Educativo Completo

Este repositorio contiene material educativo completo sobre el uso de **Mixins en Django**, incluyendo presentación Marp y proyecto Django funcional.

---

## 🚀 INICIO RÁPIDO

### 1️⃣ Ver la Presentación
Abre `presentacion_mixins.md` con la extensión Marp en VS Code

### 2️⃣ Ejecutar el Proyecto Django
```powershell
cd proyecto_mixins
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3️⃣ Abrir en el navegador
http://127.0.0.1:8000

📖 **Guía completa:** [INDICE.md](INDICE.md)

---

## 📁 Estructura del Repositorio

```
05_mixin/
├── 📊 presentacion_mixins.md          ← Presentación Marp (slides)
├── 📚 INDICE.md                        ← EMPIEZA AQUÍ (guía navegación)
├── 📋 RESUMEN_PROYECTO.md              ← Visión general
├── 🌳 ESTRUCTURA_PROYECTO.md           ← Árbol de archivos
├── 🔄 FLUJO_VISTAS.md                  ← Diagramas de flujo
│
└── 📁 proyecto_mixins/                 ← Proyecto Django completo
    ├── 📘 README.md                    ← Documentación completa
    ├── ⚡ INICIO_RAPIDO.md             ← Quick start (5 min)
    ├── 🛠️ COMANDOS_UTILES.md           ← Cheat sheet
    │
    ├── 📁 blog_project/                ← Configuración
    ├── 📁 blog/                        ← Aplicación blog
    │   ├── models.py                   ← Modelo Post
    │   ├── views.py                    ← 6 vistas con mixins
    │   ├── urls.py                     ← Rutas
    │   └── admin.py                    ← Panel admin
    │
    └── 📁 templates/                   ← Templates HTML
        ├── base.html
        └── blog/*.html
```

---

## 🎯 Contenido

### 📊 Presentación (Marp)
- **Archivo:** `presentacion_mixins.md`
- **Slides:** 25+ diapositivas profesionales
- **Contenido:**
  - ¿Qué son los mixins?
  - LoginRequiredMixin
  - PermissionRequiredMixin
  - Ejemplos prácticos
  - FBV vs CBV
  - Buenas prácticas

### 💻 Proyecto Django
- **Carpeta:** `proyecto_mixins/`
- **Framework:** Django 4.2+
- **Vistas:** 6 diferentes con mixins
- **Templates:** 7 HTML profesionales
- **Documentación:** Completa en español

---

## 🎓 Objetivos de Aprendizaje

✅ Comprender qué es un mixin  
✅ Aplicar LoginRequiredMixin  
✅ Usar PermissionRequiredMixin  
✅ Combinar múltiples mixins  
✅ Crear mixins personalizados  
✅ Comparar FBV vs CBV  
✅ Implementar buenas prácticas  

---

## 🎯 Vistas Implementadas

| Vista | URL | Mixin | Acceso |
|-------|-----|-------|--------|
| ListaPosts | `/` | Ninguno | 🟢 Público |
| MisPosts | `/mis-posts/` | LoginRequiredMixin | 🟡 Login |
| EditarPost | `/editar/` | PermissionRequiredMixin | 🔴 Permiso |
| EditarMisPropioPosts | `/editar-mis-posts/` | Ambos | 🔴 Login + Permiso |
| DetallePost | `/post/<id>/` | Ninguno | 🟢 Público |
| MixinPersonalizado | `/mixin-personalizado/` | Custom | 🟢 Público |

---

## 📖 Guías Disponibles

| Archivo | Propósito | Tiempo |
|---------|-----------|--------|
| **[INDICE.md](INDICE.md)** | 🗺️ Guía de navegación completa | 5 min |
| **[presentacion_mixins.md](presentacion_mixins.md)** | 📊 Slides educativas | 30 min |
| **[RESUMEN_PROYECTO.md](RESUMEN_PROYECTO.md)** | 📋 Visión general | 10 min |
| **[ESTRUCTURA_PROYECTO.md](ESTRUCTURA_PROYECTO.md)** | 🌳 Árbol de archivos | 5 min |
| **[FLUJO_VISTAS.md](FLUJO_VISTAS.md)** | 🔄 Diagramas de flujo | 10 min |
| **[proyecto_mixins/README.md](proyecto_mixins/README.md)** | 📘 Documentación completa | 40 min |
| **[proyecto_mixins/INICIO_RAPIDO.md](proyecto_mixins/INICIO_RAPIDO.md)** | ⚡ Quick start | 5 min |
| **[proyecto_mixins/COMANDOS_UTILES.md](proyecto_mixins/COMANDOS_UTILES.md)** | 🛠️ Cheat sheet | Referencia |

---

## 🚦 Rutas de Aprendizaje

### 🟢 Principiante
1. Leer `presentacion_mixins.md`
2. Seguir `proyecto_mixins/INICIO_RAPIDO.md`
3. Explorar URLs en navegador
4. Leer `proyecto_mixins/README.md`

### 🟡 Intermedio
1. Revisar `RESUMEN_PROYECTO.md`
2. Instalar proyecto
3. Analizar código en `views.py`
4. Revisar `FLUJO_VISTAS.md`

### 🔴 Avanzado
1. Escanear `ESTRUCTURA_PROYECTO.md`
2. Estudiar implementación completa
3. Crear propios mixins
4. Extender funcionalidad

---

## 💡 Características Destacadas

### Proyecto Django:
- ✅ 6 vistas con diferentes mixins
- ✅ Interfaz moderna y responsive
- ✅ Código comentado en español
- ✅ Tests unitarios incluidos
- ✅ Panel admin configurado
- ✅ Script de datos de prueba
- ✅ Permisos personalizados

### Documentación:
- ✅ Presentación Marp profesional
- ✅ 7 guías en markdown
- ✅ Diagramas de flujo
- ✅ Ejemplos prácticos
- ✅ Cheat sheet de comandos
- ✅ Solución de problemas

---

## 🛠️ Tecnologías

- **Backend:** Django 4.2+
- **Base de Datos:** SQLite3
- **Frontend:** HTML5 + CSS3
- **Templates:** Django Template Language
- **Presentación:** Marp
- **Documentación:** Markdown

---

## 👥 Usuarios de Prueba

Una vez instalado el proyecto:

| Usuario | Password | Permisos |
|---------|----------|----------|
| admin | admin123 | Superusuario |
| editor | editor123 | Puede editar posts |
| lector | lector123 | Sin permisos especiales |

---

## 🔗 Enlaces Rápidos

### Proyecto en ejecución:
- 🏠 http://127.0.0.1:8000/ - Inicio
- 🔒 http://127.0.0.1:8000/mis-posts/ - Mis Posts
- 🔑 http://127.0.0.1:8000/editar/ - Editar
- ⚙️ http://127.0.0.1:8000/admin/ - Admin

---

## 📦 Instalación

### Requisitos:
- Python 3.8+
- pip

### Pasos:
```powershell
# Clonar o descargar el repositorio
cd proyecto_mixins

# Instalar Django
pip install django

# Configurar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos de prueba (opcional)
python manage.py shell < setup_data.py

# Iniciar servidor
python manage.py runserver
```

**Guía detallada:** `proyecto_mixins/INICIO_RAPIDO.md`

---

## 📚 Recursos Adicionales

- [Documentación Django](https://docs.djangoproject.com/)
- [Django Auth Mixins](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.mixins.LoginRequiredMixin)
- [Class-based Views](https://docs.djangoproject.com/en/4.2/topics/class-based-views/)
- [Marp](https://marp.app/)

---

## 🆘 Ayuda

### ¿Por dónde empezar?
→ Lee el **[INDICE.md](INDICE.md)** completo

### ¿Problemas de instalación?
→ Ver `proyecto_mixins/COMANDOS_UTILES.md` > Solución de Problemas

### ¿No entiendes un concepto?
→ Revisar `presentacion_mixins.md` o `proyecto_mixins/README.md`

---

## 📊 Estadísticas

- **Archivos creados:** 30+
- **Líneas de código:** ~2,500+
- **Vistas:** 6 diferentes
- **Templates:** 7 HTML
- **Documentación:** 8 archivos markdown
- **Mixins demostrados:** 3 oficiales + 1 personalizado

---

## ✨ Lo que Aprenderás

1. ✅ Fundamentos de mixins en Python
2. ✅ LoginRequiredMixin para autenticación
3. ✅ PermissionRequiredMixin para permisos
4. ✅ Combinar múltiples mixins
5. ✅ Crear mixins personalizados
6. ✅ Diferencias entre FBV y CBV
7. ✅ Gestión de permisos en Django
8. ✅ Buenas prácticas de desarrollo

---

## 🎯 Casos de Uso Prácticos

- 📱 Dashboard de usuario
- 🔐 Sistemas con roles
- 📝 Blogs privados
- 🏢 Aplicaciones empresariales
- 👥 Gestión de equipos
- 📊 Reportes con acceso controlado

---

## 🎉 Proyecto Completo

Este material está **100% completo y funcional**, listo para usar como:
- 📚 Material de estudio
- 🎓 Referencia de código
- 🧪 Playground para experimentar
- 🏗️ Base para proyectos propios

---

## 📬 Información del Curso

**Programa:** Talento Digital  
**Código:** BOTIC-SOFOF-24-28-13-0077  
**Actividad:** AE5 - Uso de Mixins  
**Objetivo:** Comprender y aplicar mixins en Django  

---

## 🌟 Siguiente Paso

### 👉 Lee el **[INDICE.md](INDICE.md)** para comenzar tu aprendizaje

---

**💡 Consejo:** Este proyecto está diseñado para ser explorado paso a paso. No te apresures, toma tu tiempo para entender cada concepto.

**🎉 ¡Disfruta aprendiendo sobre Mixins en Django!**
