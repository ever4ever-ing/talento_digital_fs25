# 🏗️ Arquitectura del Sistema de Usuarios

## Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────────┐
│                        NAVEGADOR DEL USUARIO                     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │ HTTP Request
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DJANGO URL ROUTER                          │
│                   project_eventos/urls.py                        │
├─────────────────────────────────────────────────────────────────┤
│  /usuarios/ ──────────► app_usuarios.urls                       │
│  /          ──────────► app_eventos.urls                        │
│  /admin/    ──────────► Django Admin                            │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      APP_USUARIOS URLs                           │
│                     app_usuarios/urls.py                         │
├─────────────────────────────────────────────────────────────────┤
│  registro/     ──► RegistroView                                 │
│  login/        ──► LoginView                                    │
│  logout/       ──► LogoutView                                   │
│  perfil/       ──► PerfilView                                   │
│  info/         ──► InfoUsuarioView                              │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                           VIEWS                                  │
│                     app_usuarios/views.py                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  RegistroView (CreateView)                                      │
│  ├─ form_class: RegistroForm                                    │
│  ├─ form_valid(): auto-login                                    │
│  └─ dispatch(): check if authenticated                          │
│                                                                  │
│  LoginView (DjangoLoginView)                                    │
│  ├─ get_success_url(): handle 'next'                            │
│  └─ form_valid(): welcome message                               │
│                                                                  │
│  LogoutView (LoginRequiredMixin + TemplateView)                 │
│  └─ get(): logout + redirect                                    │
│                                                                  │
│  PerfilView (LoginRequiredMixin + UpdateView)                   │
│  ├─ form_class: PerfilForm                                      │
│  ├─ get_object(): return request.user                           │
│  └─ form_valid(): success message                               │
│                                                                  │
│  InfoUsuarioView (LoginRequiredMixin + TemplateView)            │
│  └─ get_context_data(): add user stats                          │
│                                                                  │
└───────────────────┬───────────────────┬─────────────────────────┘
                    │                   │
                    ▼                   ▼
        ┌───────────────────┐   ┌──────────────────┐
        │      FORMS        │   │    TEMPLATES     │
        │  forms.py         │   │  templates/      │
        ├───────────────────┤   ├──────────────────┤
        │                   │   │                  │
        │  RegistroForm     │   │  registro.html   │
        │  - clean_email()  │   │  login.html      │
        │  - clean_username │   │  perfil.html     │
        │                   │   │  info_usuario.   │
        │  PerfilForm       │   │      html        │
        │  - clean_email()  │   │                  │
        │  - __init__()     │   │  base.html       │
        │                   │   │  (extends)       │
        └────────┬──────────┘   └──────────────────┘
                 │
                 ▼
        ┌────────────────────┐
        │       MODEL        │
        │   django.contrib   │
        │    .auth.models    │
        ├────────────────────┤
        │                    │
        │  User              │
        │  ├─ username       │
        │  ├─ email          │
        │  ├─ first_name     │
        │  ├─ last_name      │
        │  ├─ password       │
        │  ├─ is_active      │
        │  ├─ is_staff       │
        │  ├─ date_joined    │
        │  └─ last_login     │
        │                    │
        └──────────┬─────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │      DATABASE        │
        │     (SQLite/PG)      │
        ├──────────────────────┤
        │  auth_user           │
        │  app_eventos_evento  │
        │  ...                 │
        └──────────────────────┘
```

---

## Flujo de Datos: Registro de Usuario

```
USUARIO
  │
  │ 1. Visita /usuarios/registro/
  ▼
DJANGO URL ROUTER
  │
  │ 2. Match URL pattern
  ▼
RegistroView.dispatch()
  │
  │ 3. Check if authenticated
  ▼
RegistroView.get()
  │
  │ 4. Instancia RegistroForm
  │ 5. Renderiza registro.html
  ▼
NAVEGADOR
  │
  │ 6. Usuario llena formulario
  │ 7. Submit (POST)
  ▼
RegistroView.post()
  │
  │ 8. Valida formulario
  ▼
RegistroForm.clean_email()
RegistroForm.clean_username()
  │
  │ 9. Si válido ──► form_valid()
  │ 10. Si inválido ─► form_invalid()
  ▼
RegistroView.form_valid()
  │
  │ 11. form.save() → Crea User
  │ 12. login(request, user)
  │ 13. messages.success()
  ▼
DATABASE
  │
  │ 14. INSERT INTO auth_user
  ▼
REDIRECT
  │
  │ 15. Redirige a lista_eventos
  ▼
NAVEGADOR
  │
  └─► Usuario autenticado y en home
```

---

## Flujo de Datos: Login

```
USUARIO
  │
  │ 1. Visita /usuarios/login/
  ▼
LoginView.get()
  │
  │ 2. Renderiza login.html
  ▼
NAVEGADOR
  │
  │ 3. Ingresa credenciales
  │ 4. Submit (POST)
  ▼
LoginView.post()
  │
  │ 5. AuthenticationForm valida
  ▼
Django Authentication Backend
  │
  │ 6. Verifica password_hash
  ▼
DATABASE
  │
  │ 7. SELECT * FROM auth_user WHERE username=?
  ▼
LoginView.form_valid()
  │
  │ 8. django.contrib.auth.login()
  │ 9. Crea sesión
  │ 10. messages.success()
  ▼
SESSION STORE
  │
  │ 11. Guarda session_key
  ▼
REDIRECT
  │
  │ 12. Redirige a 'next' o home
  ▼
NAVEGADOR
  │
  └─► Usuario autenticado
```

---

## Flujo de Datos: Editar Perfil

```
USUARIO AUTENTICADO
  │
  │ 1. Visita /usuarios/perfil/
  ▼
LoginRequiredMixin
  │
  │ 2. Check if authenticated
  │ 3. Si no ──► Redirect LOGIN_URL
  ▼
PerfilView.get()
  │
  │ 4. get_object() → request.user
  │ 5. Instancia PerfilForm con user
  ▼
PerfilForm.__init__()
  │
  │ 6. Deshabilita campo username
  │ 7. Pre-popula campos
  ▼
NAVEGADOR
  │
  │ 8. Muestra perfil.html
  │ 9. Usuario edita datos
  │ 10. Submit (POST)
  ▼
PerfilView.post()
  │
  │ 11. Valida formulario
  ▼
PerfilForm.clean_email()
  │
  │ 12. Verifica email único
  │     (excluyendo usuario actual)
  ▼
DATABASE
  │
  │ 13. SELECT COUNT(*) FROM auth_user
  │     WHERE email=? AND id!=?
  ▼
PerfilView.form_valid()
  │
  │ 14. form.save() → UPDATE user
  │ 15. messages.success()
  ▼
DATABASE
  │
  │ 16. UPDATE auth_user SET ...
  ▼
REDIRECT
  │
  │ 17. Redirige a /usuarios/perfil/
  ▼
NAVEGADOR
  │
  └─► Perfil actualizado
```

---

## Integración con app_eventos

```
┌─────────────────────────────────────────────────────────┐
│                    APP_EVENTOS                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Modelo: Evento                                         │
│  ├─ autor (ForeignKey → User) ◄──────┐                │
│  └─ participantes (ManyToMany → User)│                 │
│                                        │                │
│  Views:                                │                │
│  ├─ CrearEvento                        │                │
│  │  └─ LoginRequiredMixin ────────────┼────┐          │
│  ├─ EditarEvento                       │    │          │
│  │  └─ AutorRequeridoMixin ───────────┼────┤          │
│  └─ UnirseEventoView                   │    │          │
│     └─ LoginRequiredMixin ─────────────┼────┤          │
│                                        │    │          │
└────────────────────────────────────────┼────┼──────────┘
                                         │    │
                                         │    │
┌────────────────────────────────────────┼────┼──────────┐
│                 APP_USUARIOS            │    │          │
├─────────────────────────────────────────┼────┼──────────┤
│                                         │    │          │
│  User Model (Django)                    │    │          │
│  ├─ username                            │    │          │
│  ├─ email                               │    │          │
│  └─ ...                                 │    │          │
│                                         │    │          │
│  RegistroView ─────────────────────────►│    │          │
│  LoginView ────────────────────────────►│    │          │
│  PerfilView ◄──────────────────────────────►│          │
│  InfoUsuarioView                             │          │
│  └─ Muestra eventos del usuario ◄────────────┘          │
│                                                          │
└──────────────────────────────────────────────────────────┘

RELACIONES:
1. User ──(1:N)──► Evento (como autor)
2. User ──(N:M)──► Evento (como participante)
3. LoginRequiredMixin requiere User autenticado
4. InfoUsuarioView lee eventos relacionados al User
```

---

## Capas de Seguridad

```
┌──────────────────────────────────────────────────────┐
│                   CAPA 1: URLs                       │
│  - LoginRequiredMixin                                │
│  - redirect_authenticated_user                       │
└─────────────────┬────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────┐
│                  CAPA 2: VIEWS                       │
│  - dispatch() checks                                 │
│  - get_object() validation                           │
│  - UserPassesTestMixin                               │
└─────────────────┬────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────┐
│                  CAPA 3: FORMS                       │
│  - clean_email() validation                          │
│  - clean_username() validation                       │
│  - Django password validators                        │
│  - CSRF token validation                             │
└─────────────────┬────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────┐
│                  CAPA 4: MODEL                       │
│  - unique=True constraints                           │
│  - max_length limits                                 │
│  - required fields                                   │
└─────────────────┬────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────┐
│                CAPA 5: DATABASE                      │
│  - UNIQUE constraints                                │
│  - NOT NULL constraints                              │
│  - Foreign Key integrity                             │
└──────────────────────────────────────────────────────┘
```

---

## Stack Tecnológico

```
┌─────────────────────────────────────┐
│          FRONTEND                   │
├─────────────────────────────────────┤
│  - HTML5                            │
│  - Bootstrap 5.3.0                  │
│  - Bootstrap Icons 1.11.1           │
│  - JavaScript (Bootstrap bundle)    │
└─────────────────────────────────────┘
              ▲
              │
              ▼
┌─────────────────────────────────────┐
│          BACKEND                    │
├─────────────────────────────────────┤
│  - Django 5.2.8                     │
│  - Python 3.x                       │
│  - Django Templates                 │
│  - Class-Based Views                │
│  - Django Forms                     │
│  - Django Auth System               │
└─────────────────────────────────────┘
              ▲
              │
              ▼
┌─────────────────────────────────────┐
│         DATABASE                    │
├─────────────────────────────────────┤
│  - SQLite3 (dev)                    │
│  - PostgreSQL (prod)                │
└─────────────────────────────────────┘
```

---

## Ciclo de Vida de una Request

```
1. Browser
    │
    │ GET /usuarios/perfil/
    ▼
2. Web Server (Django runserver)
    │
    │ WSGI
    ▼
3. Middleware Stack
    │
    ├─► SecurityMiddleware
    ├─► SessionMiddleware
    ├─► AuthenticationMiddleware ◄─ Adjunta user a request
    ├─► MessageMiddleware
    └─► CsrfViewMiddleware
    │
    ▼
4. URL Router
    │
    │ Match pattern
    ▼
5. View (PerfilView)
    │
    ├─► LoginRequiredMixin.dispatch()
    │   └─► Check: request.user.is_authenticated
    │
    ├─► get_object()
    │   └─► Return: request.user
    │
    ├─► get_context_data()
    │   └─► Add: form, user data
    │
    └─► TemplateResponse
    │
    ▼
6. Template Engine
    │
    ├─► Load: perfil.html
    ├─► Extends: base.html
    ├─► Context: {user, form, messages}
    └─► Render HTML
    │
    ▼
7. HTTP Response
    │
    │ 200 OK + HTML
    ▼
8. Browser
    │
    └─► Display Page
```

---

## Patrones de Diseño Utilizados

### 1. MTV (Model-Template-View)
```
Model ──────► Django User Model
Template ───► HTML con Django Template Language
View ───────► Class-Based Views
```

### 2. Mixins
```
LoginRequiredMixin ──► Requiere autenticación
UserPassesTestMixin ──► Valida permisos custom
```

### 3. Form Validation
```
clean_<field>() ──► Validación por campo
clean() ─────────► Validación multi-campo
```

### 4. Template Inheritance
```
base.html
  ├─► registro.html
  ├─► login.html
  ├─► perfil.html
  └─► info_usuario.html
```

---

## Resumen de Componentes

| Componente | Archivos | Responsabilidad |
|-----------|----------|----------------|
| **URLs** | `urls.py` | Enrutamiento |
| **Vistas** | `views.py` | Lógica de negocio |
| **Formularios** | `forms.py` | Validación |
| **Templates** | `templates/` | Presentación |
| **Modelo** | Django User | Datos |
| **Configuración** | `settings.py` | Ajustes globales |

---

**Fecha:** Noviembre 2025  
**Versión:** 1.0.0
