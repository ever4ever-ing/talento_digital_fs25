# 🚀 Quick Start - App Usuarios

## Instalación Rápida

### 1. Configurar Settings
```python
# project_eventos/settings.py
INSTALLED_APPS = [
    # ...
    'app_usuarios',  # Agregar
]

LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/usuarios/login/'
```

### 2. Configurar URLs
```python
# project_eventos/urls.py
urlpatterns = [
    path('usuarios/', include('app_usuarios.urls')),
    # ...
]
```

### 3. Ejecutar
```bash
python manage.py migrate
python manage.py runserver
```

---

## 📍 URLs Disponibles

| URL | Descripción | Vista |
|-----|-------------|-------|
| `/usuarios/registro/` | Registro de nuevos usuarios | `RegistroView` |
| `/usuarios/login/` | Inicio de sesión | `LoginView` |
| `/usuarios/logout/` | Cerrar sesión | `LogoutView` |
| `/usuarios/perfil/` | Ver/editar perfil | `PerfilView` |
| `/usuarios/info/` | Estadísticas del usuario | `InfoUsuarioView` |

---

## 🎯 Funcionalidades

### ✅ Registro
- Formulario completo con validación
- Email único
- Username único
- Auto-login después del registro
- Validación de contraseña fuerte

### ✅ Login
- Soporte para `?next=` parameter
- Mensaje de bienvenida
- Checkbox "Recordarme"

### ✅ Perfil
- Edición de datos personales
- Email, nombre, apellido
- Username NO editable
- Validación de email único

### ✅ Info Usuario
- Estadísticas de eventos
- Eventos creados
- Eventos participando
- Acciones rápidas

---

## 🔒 Seguridad

- ✅ CSRF Protection en todos los formularios
- ✅ LoginRequiredMixin en vistas protegidas
- ✅ Validación de email único
- ✅ Validación de contraseña (Django validators)
- ✅ Username no editable

---

## 📝 Uso en Código

### Requerir autenticación en una vista
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MiVista(LoginRequiredMixin, TemplateView):
    template_name = 'mi_template.html'
```

### Acceder al usuario en template
```django
{% if user.is_authenticated %}
    <p>Hola, {{ user.username }}</p>
    <p>Email: {{ user.email }}</p>
    <p>Nombre completo: {{ user.get_full_name }}</p>
{% endif %}
```

### Crear enlaces en templates
```django
<a href="{% url 'registro' %}">Registrarse</a>
<a href="{% url 'login' %}">Login</a>
<a href="{% url 'perfil' %}">Mi Perfil</a>
<a href="{% url 'info_usuario' %}">Mis Estadísticas</a>
<a href="{% url 'logout' %}">Cerrar Sesión</a>
```

---

## 🧪 Testing Rápido

```bash
# Crear usuario de prueba
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('test', 'test@example.com', 'testpass123')
>>> exit()

# Probar login
python manage.py runserver
# Visitar: http://localhost:8000/usuarios/login/
# User: test, Pass: testpass123
```

---

## 🎨 Personalización

### Cambiar estilos del formulario
Editar `app_usuarios/forms.py`:
```python
widget=forms.EmailInput(attrs={
    'class': 'form-control tu-clase-custom',
    'placeholder': 'Tu placeholder'
})
```

### Cambiar template
Crear tu propio template en:
```
app_usuarios/templates/usuarios/registro.html
```

### Agregar campos al registro
Editar `RegistroForm` en `forms.py`:
```python
telefono = forms.CharField(
    max_length=15,
    required=False,
    widget=forms.TextInput(attrs={'class': 'form-control'})
)
```

---

## 🐛 Troubleshooting

### No aparece la página de registro
✅ Verificar que `app_usuarios` está en `INSTALLED_APPS`  
✅ Verificar que las URLs están incluidas en `urls.py`

### Formulario sin estilos
✅ Verificar que `base.html` carga Bootstrap  
✅ Verificar widgets en `forms.py`

### Usuario no redirige después del login
✅ Configurar `LOGIN_REDIRECT_URL` en `settings.py`

---

## 📚 Documentación Completa

Para más detalles, ver: [`DOCUMENTACION_USUARIOS.md`](./DOCUMENTACION_USUARIOS.md)

---

## 🎓 Estructura de Archivos

```
app_usuarios/
├── forms.py              # RegistroForm, PerfilForm
├── views.py              # Vistas CBV
├── urls.py               # Rutas
└── templates/usuarios/   # Templates HTML
    ├── registro.html
    ├── login.html
    ├── perfil.html
    └── info_usuario.html
```

---

## ✅ Checklist de Integración

- [ ] App agregada a `INSTALLED_APPS`
- [ ] URLs incluidas en `project_eventos/urls.py`
- [ ] `LOGIN_URL` configurado
- [ ] `LOGIN_REDIRECT_URL` configurado
- [ ] Bootstrap cargado en `base.html`
- [ ] Migraciones aplicadas
- [ ] Servidor ejecutándose
- [ ] Probado registro exitoso
- [ ] Probado login exitoso
- [ ] Probado edición de perfil

---

**¡Listo para usar! 🎉**
