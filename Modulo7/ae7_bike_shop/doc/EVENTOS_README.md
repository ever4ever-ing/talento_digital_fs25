# 📅 Sistema de Eventos y Salidas en Grupo - BikeShop

## 🎯 Descripción

Sistema completo para gestionar eventos y salidas en bicicleta con inscripciones, cupos limitados y control de disponibilidad.

---

## ✨ Funcionalidades Principales

### Para Usuarios
- ✅ Ver lista de eventos disponibles
- ✅ Filtrar por tipo y dificultad
- ✅ Ver detalles completos del evento
- ✅ Inscribirse a eventos
- ✅ Gestionar inscripciones propias
- ✅ Cancelar inscripciones
- ✅ Ver historial de eventos

### Para Administradores
- ✅ Crear y editar eventos
- ✅ Gestionar cupos
- ✅ Ver todas las inscripciones
- ✅ Confirmar/cancelar inscripciones
- ✅ Acciones masivas

---

## 📊 Modelos

### Evento
```python
class Evento(models.Model):
    # Información básica
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_evento = models.CharField(max_length=20, choices=TIPO_EVENTO_CHOICES)
    dificultad = models.CharField(max_length=15, choices=DIFICULTAD_CHOICES)
    
    # Detalles
    destino = models.CharField(max_length=200)
    punto_encuentro = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()
    duracion_horas = models.DecimalField(max_digits=4, decimal_places=1)
    distancia_km = models.DecimalField(max_digits=5, decimal_places=1)
    
    # Cupos
    cupo_maximo = models.PositiveIntegerField(default=20)
    cupo_disponible = models.PositiveIntegerField(default=20)
    
    # Costo
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Inclusiones
    incluye_guia = models.BooleanField(default=True)
    incluye_seguro = models.BooleanField(default=True)
    incluye_hidratacion = models.BooleanField(default=True)
    incluye_snacks = models.BooleanField(default=False)
```

**Tipos de Eventos:**
- 🏞️ Salida a Parque
- 🌋 Salida a Volcán
- 🌊 Ruta Costera
- ⛰️ Mountain Bike
- 🏙️ Tour Urbano

**Niveles de Dificultad:**
- 🟢 Fácil
- 🟡 Intermedio
- 🟠 Difícil
- 🔴 Experto

### Inscripción
```python
class Inscripcion(models.Model):
    evento = models.ForeignKey(Evento)
    cliente = models.ForeignKey(Cliente)
    
    # Datos
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    num_personas = models.PositiveIntegerField(default=1)
    
    # Emergencia
    contacto_emergencia = models.CharField(max_length=100)
    telefono_emergencia = models.CharField(max_length=20)
    observaciones = models.TextField(blank=True)
    
    # Estado
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    pagado = models.BooleanField(default=False)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
```

**Estados de Inscripción:**
- ⏳ Pendiente
- ✅ Confirmada
- ❌ Cancelada
- 🎉 Completada

---

## 🎨 Templates

### 1. Lista de Eventos (`lista_eventos.html`)
**URL:** `/eventos/`

**Características:**
- Grid de cards responsive
- Filtros por tipo y dificultad
- Badges de cupos disponibles con colores:
  - 🟢 Verde: +10 cupos
  - 🟡 Amarillo: 4-10 cupos
  - 🔴 Rojo: 1-3 cupos (¡Últimos!)
  - ⚫ Gris: Sin cupos
- Precio destacado
- Hover effects

### 2. Detalle de Evento (`detalle_evento.html`)
**URL:** `/eventos/<id>/`

**Características:**
- Hero image o gradient
- Información completa del recorrido
- Lista de inclusiones
- Sidebar con:
  - Precio
  - Cupos disponibles
  - Barra de ocupación
  - Botón de inscripción
  - Verificación de inscripción previa

### 3. Formulario de Inscripción (`inscribirse.html`)
**URL:** `/eventos/<id>/inscribirse/`

**Campos:**
- Número de personas
- Contacto de emergencia
- Teléfono de emergencia
- Observaciones (alergias, condiciones, etc.)

**Validaciones:**
- Cupos suficientes
- Usuario autenticado
- No inscrito previamente
- Evento activo y futuro

### 4. Mis Inscripciones (`mis_inscripciones.html`)
**URL:** `/mis-inscripciones/`

**Características:**
- Grid de inscripciones
- Badges de estado
- Información del evento
- Datos de emergencia
- Botón de cancelación (si aplica)

---

## 🔧 Vistas y Lógica

### `lista_eventos(request)`
```python
def lista_eventos(request):
    """
    Muestra eventos activos y futuros.
    Permite filtrar por tipo y dificultad.
    """
    eventos = Evento.objects.filter(
        activo=True,
        fecha_hora__gte=timezone.now()
    ).order_by('fecha_hora')
```

### `detalle_evento(request, evento_id)`
```python
def detalle_evento(request, evento_id):
    """
    Muestra detalles completos del evento.
    Verifica si el usuario ya está inscrito.
    """
    evento = get_object_or_404(Evento, id=evento_id)
    ya_inscrito = Inscripcion.objects.filter(
        evento=evento,
        cliente=cliente
    ).exclude(estado='cancelada').exists()
```

### `inscribirse_evento(request, evento_id)`
```python
@login_required
def inscribirse_evento(request, evento_id):
    """
    Procesa la inscripción al evento.
    Reduce cupos disponibles automáticamente.
    """
    # Validaciones:
    # - Evento disponible
    # - No inscrito previamente
    # - Cupos suficientes
    
    inscripcion = Inscripcion.objects.create(
        evento=evento,
        cliente=cliente,
        num_personas=num_personas,
        estado='confirmada',
        total_pagado=total
    )
```

### `cancelar_inscripcion(request, inscripcion_id)`
```python
@login_required
def cancelar_inscripcion(request, inscripcion_id):
    """
    Cancela inscripción y libera cupos.
    Solo permite cancelar eventos futuros.
    """
    if inscripcion.estado != 'cancelada':
        inscripcion.estado = 'cancelada'
        inscripcion.evento.cupo_disponible += inscripcion.num_personas
        inscripcion.evento.save()
```

---

## 🎯 Métodos del Modelo Evento

### `tiene_cupos_disponibles()`
Verifica si hay cupos disponibles.

### `evento_pasado()`
Verifica si el evento ya pasó.

### `puede_inscribirse()`
Verifica si es posible inscribirse:
- Evento activo
- Tiene cupos
- No ha pasado

### `porcentaje_ocupacion()`
Calcula el porcentaje de ocupación para la barra de progreso.

---

## 🔒 Validaciones

### Modelo Inscripción

```python
def clean(self):
    """Validaciones personalizadas"""
    if self.evento.cupo_disponible < self.num_personas:
        raise ValidationError('No hay suficientes cupos.')
    
    if self.evento.evento_pasado():
        raise ValidationError('No se puede inscribir a un evento que ya pasó.')
```

### Unique Together
```python
class Meta:
    unique_together = ['evento', 'cliente']
```
Un cliente solo puede inscribirse una vez por evento.

---

## 🎨 Estilos y UI

### Colores del Sistema
```css
/* Verde oscuro */
--color-dark: #00392d;

/* Azul petróleo */
--color-primary: #006e8c;

/* Naranja */
--color-accent: #eb7f25;

/* Amarillo dorado */
--color-warning: #ffcc52;
```

### Cards de Eventos
```css
.event-card {
    transition: transform 0.3s, box-shadow 0.3s;
}
.event-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}
```

### Badges de Cupos
```css
.cupos-alto { background-color: #28a745; }   /* Verde */
.cupos-medio { background-color: #ffc107; }  /* Amarillo */
.cupos-bajo { background-color: #dc3545; }   /* Rojo */
```

---

## 📱 Responsive Design

- **Desktop:** Grid de 3 columnas
- **Tablet:** Grid de 2 columnas
- **Mobile:** 1 columna, sidebar apilado

---

## 🔗 URLs

```python
urlpatterns = [
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/<int:evento_id>/inscribirse/', views.inscribirse_evento, name='inscribirse_evento'),
    path('mis-inscripciones/', views.mis_inscripciones, name='mis_inscripciones'),
    path('inscripcion/<int:inscripcion_id>/cancelar/', views.cancelar_inscripcion, name='cancelar_inscripcion'),
]
```

---

## 🎯 Integración con el Sistema

### Navbar
Se agregó botón "📅 Eventos" en el navbar.

### Menú de Usuario
Se agregó "Mis Eventos" para ver inscripciones.

### Base de Datos
Relación con `Cliente` del sistema existente.

---

## 🚀 Cómo Usar

### 1. Crear un Evento (Admin)
```
1. Ir a /admin/
2. App Eventos → Eventos → Agregar
3. Completar todos los campos
4. Marcar como activo
5. Guardar
```

### 2. Usuario se Inscribe
```
1. Ir a /eventos/
2. Seleccionar un evento
3. Click en "Ver Detalles"
4. Click en "Inscribirse Ahora"
5. Completar formulario
6. Confirmar inscripción
```

### 3. Ver Mis Inscripciones
```
1. Navbar → "Mis Eventos"
2. Ver lista de inscripciones
3. Cancelar si es necesario
```

---

## 📋 Ejemplo de Evento

```python
evento = Evento.objects.create(
    nombre="Ruta al Volcán Villarrica",
    descripcion="Aventura épica...",
    tipo_evento="volcan",
    dificultad="intermedio",
    destino="Volcán Villarrica",
    punto_encuentro="Plaza de Armas, Pucón",
    fecha_hora=datetime(2025, 12, 15, 8, 0),
    duracion_horas=6.5,
    distancia_km=45.0,
    cupo_maximo=15,
    cupo_disponible=15,
    precio=45000,
    incluye_guia=True,
    incluye_seguro=True,
    incluye_hidratacion=True,
    incluye_snacks=True,
    nivel_minimo="Experiencia mínima de 3 meses",
    activo=True
)
```

---

## ✅ Checklist de Implementación

- ✅ Modelos creados (Evento, Inscripción)
- ✅ Admin configurado con acciones
- ✅ Vistas implementadas
- ✅ Templates responsive
- ✅ URLs configuradas
- ✅ Integración con navbar
- ✅ Validaciones de cupos
- ✅ Gestión de inscripciones
- ✅ Cancelación con liberación de cupos
- ✅ Filtros por tipo y dificultad
- ✅ Sistema de estados

---

## 🔮 Mejoras Futuras (Opcional)

### 1. Galería de Fotos
Agregar galería de fotos de eventos pasados.

### 2. Comentarios Post-Evento
Permitir comentarios después del evento.

### 3. Certificados
Generar certificados de participación.

### 4. Recordatorios
Enviar emails recordatorios 24h antes.

### 5. Lista de Espera
Implementar lista de espera cuando se llena.

### 6. Pago Integrado
Integrar con Mercado Pago para pago directo.

### 7. Mapa Interactivo
Mostrar ruta en Google Maps.

### 8. Compartir en Redes
Botones para compartir eventos.

---

## 📚 Archivos Creados

```
✅ app_eventos/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    └── migrations/
        ├── __init__.py
        └── 0001_initial.py

✅ templates/eventos/
    ├── lista_eventos.html
    ├── detalle_evento.html
    ├── inscribirse.html
    └── mis_inscripciones.html

✅ Configuración:
    ├── settings.py (INSTALLED_APPS)
    ├── urls.py (include eventos)
    └── base.html (navbar actualizado)

✅ doc/
    └── EVENTOS_README.md
```

---

**🎉 Sistema de Eventos implementado exitosamente!**

*Ahora los clientes pueden inscribirse a salidas en grupo, explorar nuevos lugares y compartir la pasión por el ciclismo.*
