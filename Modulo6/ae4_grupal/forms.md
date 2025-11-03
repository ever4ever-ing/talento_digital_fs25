# 📚 Guía  -  Esta guía explica cómo funciona el código de manera simple.

## 📁 Estructura del Proyecto

```
events/
├── models.py          # Define las tablas de la base de datos
├── forms.py           # Define los formularios web
├── views.py           # Contiene la lógica de cada página
├── urls.py            # Define las rutas/URLs
└── templates/         # Contiene las páginas HTML
```

---

## 🗄️ 1. Models.py - Base de Datos

Define dos tablas:

### **Event (Evento)**
- `name` = Nombre del evento
- `date` = Fecha del evento
- `location` = Ubicación (opcional)

### **Participant (Participante)**
- `event` = A qué evento pertenece (ForeignKey)
- `name` = Nombre del participante
- `email` = Correo electrónico

**Relación:** Un evento puede tener muchos participantes.

---

## 📝 2. Forms.py - Formularios

### **EventForm**
Formulario para crear un evento con 3 campos:
- Nombre
- Fecha (tipo date para calendario)
- Ubicación

### **ParticipantForm**
Formulario para agregar participantes con 2 campos:
- Nombre
- Email

---

## 🎯 3. Views.py - Lógica del Sistema

### **register_event(request)**
Página principal para registrar eventos.

**¿Cómo funciona?**

1. **Crear el formset:**
   - `modelformset_factory` crea múltiples formularios de participantes
   - `extra=3` muestra 3 formularios vacíos

2. **Si el usuario envía el formulario (POST):**
   - Valida el formulario del evento
   - Valida los formularios de participantes
   - Guarda el evento en la base de datos
   - Guarda cada participante y lo asocia al evento
   - Muestra página de éxito

3. **Si el usuario solo está viendo la página (GET):**
   - Muestra formularios vacíos

### **event_list(request)**
Lista todos los eventos de la base de datos.

### **event_detail(request, pk)**
Muestra el detalle de un evento específico.
- `pk` = primary key (ID del evento)
- `get_object_or_404` busca el evento o muestra error 404

---

## 🌐 4. Templates - Páginas HTML

### **register.html**
Formulario con dos secciones:
1. **Datos del Evento:** Nombre, fecha, ubicación
2. **Participantes:** Lista de participantes (3 formularios)

**Elementos importantes:**
- `{% csrf_token %}` = Seguridad de Django (obligatorio)
- `{{ event_form.name }}` = Campo del formulario
- `{% for form in formset %}` = Repite para cada formulario de participante
- `{{ forloop.counter }}` = Número actual del ciclo (1, 2, 3...)

### **list.html**
Muestra lista de eventos con:
- Nombre
- Fecha
- Cantidad de participantes

### **detail.html**
Muestra información completa de un evento:
- Datos del evento
- Lista de todos los participantes

### **success.html**
Página de confirmación después de registrar un evento.

---

## 🔄 Flujo Completo

```
1. Usuario visita /register/
   ↓
2. Django llama a register_event(request)
   ↓
3. Se renderizan los formularios vacíos
   ↓
4. Usuario completa y envía formulario
   ↓
5. Django valida los datos
   ↓
6. Se guarda evento en base de datos
   ↓
7. Se guardan participantes asociados al evento
   ↓
8. Se muestra página de éxito
```

---

## 🛠️ Comandos Útiles

### Iniciar el servidor
```powershell
python manage.py runserver
```

### Crear migraciones (después de cambiar models.py)
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Crear superusuario
```powershell
python manage.py createsuperuser
```

### Acceder al panel de administración
http://127.0.0.1:8000/admin/

---

## 📖 Conceptos Clave de Django

### **Model (Modelo)**
Define la estructura de la base de datos.

### **Form (Formulario)**
Define campos de entrada para el usuario.

### **View (Vista)**
Contiene la lógica: qué hacer cuando el usuario visita una URL.

### **Template (Plantilla)**
Define cómo se ve la página (HTML).

### **URL**
Conecta una dirección web con una vista.

### **Request (Solicitud)**
Información que llega del navegador del usuario.
- `GET` = Solo ver la página
- `POST` = Enviar datos (formulario)

### **QuerySet**
Resultado de una consulta a la base de datos.
- `Event.objects.all()` = Todos los eventos
- `Event.objects.filter(name='Fiesta')` = Eventos filtrados
- `get_object_or_404(Event, pk=1)` = Un evento específico

---

## 💡 Tips para Principiantes

1. **Siempre usa `{% csrf_token %}`** en formularios POST
2. **Lee los errores:** Django da mensajes muy descriptivos
3. **Usa `print()` o `{{ variable }}`** para ver qué contiene una variable
4. **Revisa el admin:** Es la forma más fácil de ver tus datos
5. **Las migraciones son importantes:** Córrelas después de cambiar models.py

---

## 🐛 Debugging (Encontrar Errores)

### Ver qué contiene una variable en el template:
```html
<p>Debug: {{ variable }}</p>
```

### Ver qué contiene una variable en la vista:
```python
print(f"Debug: {variable}")
```

### Ver todos los métodos POST:
```python
print(request.POST)
```

---
