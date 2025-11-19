# 💳 Sistema de Pagos - Mercado Pago (Simulación)

## 🎯 Descripción

Sistema de checkout simulado integrado con Mercado Pago que permite procesar pagos de manera ficticia para el carrito de compras de BikeShop.

## ⚠️ Importante: Simulación

**Este es un sistema de SIMULACIÓN** con fines educativos. No procesa pagos reales ni se conecta a la API real de Mercado Pago.

---

## 🔄 Flujo de Checkout

```
Carrito de Compras
       ↓
[Ir a Pagar] (requiere login)
       ↓
Checkout Mercado Pago
       ↓
Seleccionar Método de Pago
       ↓
Completar Datos
       ↓
Procesar Pago (simulado)
       ↓
Crear Orden (estado: pagado)
       ↓
Página de Confirmación
```

---

## 💳 Métodos de Pago Disponibles

### 1. **Tarjeta de Crédito** 💳
- Hasta 12 cuotas sin interés
- Requiere datos de la tarjeta
- Cuotas disponibles: 1, 3, 6, 12

**Tarjeta de prueba:**
```
Número: 4507 9907 6623 8769
CVV: 123
Vencimiento: Cualquier fecha futura
Titular: Cualquier nombre
```

### 2. **Tarjeta de Débito** 💳
- Pago único (sin cuotas)
- Requiere datos de la tarjeta
- Débito directo a cuenta

### 3. **Transferencia Bancaria (PSE)** 🏦
- Selección de banco
- Simulación de redirección bancaria
- Confirmación inmediata

**Bancos disponibles:**
- Bancolombia
- Davivienda
- BBVA
- Banco de Bogotá
- Banco Popular

### 4. **Pago en Efectivo** 💵
- Código de pago generado
- Válido por 48 horas
- Puntos de pago: Baloto, Efecty, Su Red

---

## 🏗️ Estructura de Archivos

### Templates

```
templates/carrito/
├── carrito_detalle.html          # Carrito con botón "Ir a Pagar"
├── checkout_mercadopago.html     # Página de checkout
└── pago_exitoso.html             # Confirmación de pago
```

### Vistas

```python
# app_carrito/views.py

def iniciar_checkout(request):
    """Redirige al checkout (verifica carrito y usuario)"""

def checkout_mercadopago(request):
    """Muestra formulario de pago de Mercado Pago"""

def procesar_pago_mercadopago(request):
    """Procesa el pago y crea la orden"""

def pago_exitoso(request):
    """Muestra confirmación de pago exitoso"""
```

### URLs

```python
# app_carrito/urls.py

path('carrito/checkout/', views.iniciar_checkout, name='iniciar_checkout'),
path('checkout/mercadopago/', views.checkout_mercadopago, name='checkout_mercadopago'),
path('pago/exitoso/', views.pago_exitoso, name='pago_exitoso'),
```

---

## 🎨 Características del Checkout

### Interfaz de Usuario

✅ **Diseño Mercado Pago:**
- Colores oficiales: #009ee3 (azul MP)
- Logo y branding
- Diseño responsive

✅ **Selección Visual de Métodos:**
- Cards interactivas
- Iconos representativos
- Feedback visual al seleccionar

✅ **Validación en Tiempo Real:**
- Formateo automático de tarjeta
- Validación de campos requeridos
- Mensajes de error claros

✅ **Experiencia de Pago:**
- Loading spinner al procesar
- Animaciones de éxito
- Resumen de orden visible

### Funcionalidades

🔒 **Seguridad:**
- Solo usuarios autenticados
- Validación de carrito no vacío
- Tokens CSRF en formularios

💰 **Cálculo de Cuotas:**
- 1 cuota: Total completo
- 3 cuotas: Total / 3
- 6 cuotas: Total / 6
- 12 cuotas: Total / 12

📦 **Gestión de Orden:**
- Creación automática de orden
- Estado: "pagado" (simulación)
- Detalles con productos y cantidades
- Cálculo de total

🎫 **Identificadores Únicos:**
- Transaction ID: `MP-XXXXXXXXXXXX`
- Payment Code (efectivo): `CASH-XXXXXXXXXX`

---

## 📝 Datos que se Capturan

### Información General
```python
payment_info = {
    'method': 'credit_card',              # Método seleccionado
    'transaction_id': 'MP-A1B2C3D4E5F6',  # ID transacción
    'timestamp': timezone.now(),           # Fecha y hora
}
```

### Tarjeta de Crédito/Débito
```python
{
    'method_display': 'Tarjeta de Crédito',
    'card_number': '8769',                 # Últimos 4 dígitos
    'installments': 6,                     # Número de cuotas
    'installment_amount': 166.67,          # Monto por cuota
}
```

### Transferencia Bancaria
```python
{
    'method_display': 'Transferencia Bancaria (PSE)',
    'bank': 'Bancolombia',                 # Banco seleccionado
}
```

### Pago en Efectivo
```python
{
    'method_display': 'Pago en Efectivo',
    'payment_code': 'CASH-A1B2C3D4E5',    # Código de pago
}
```

---

## 🔄 Proceso de Pago Simulado

### 1. Usuario va al carrito
```
URL: /carrito/
Template: carrito_detalle.html
Botón: "💳 Ir a Pagar"
```

### 2. Inicio de Checkout
```python
@login_required
def iniciar_checkout(request):
    # Verificar carrito no vacío
    # Verificar/crear cliente
    # Redirigir a checkout
```

### 3. Formulario de Pago
```
URL: /checkout/mercadopago/
Template: checkout_mercadopago.html

- Seleccionar método de pago
- Completar datos
- Ver resumen de orden
```

### 4. Procesamiento
```python
def procesar_pago_mercadopago(request):
    # Validar datos
    # Crear orden (estado: pagado)
    # Crear detalles de orden
    # Generar info de pago
    # Guardar en sesión
    # Limpiar carrito
    # Redirigir a éxito
```

### 5. Confirmación
```
URL: /pago/exitoso/
Template: pago_exitoso.html

- Mostrar orden creada
- Mostrar detalles de pago
- Botones: Ver Órdenes / Seguir Comprando
```

---

## 🎯 Validaciones Implementadas

### Backend
```python
# Carrito no vacío
if len(carrito) == 0:
    messages.warning(request, '⚠️ Tu carrito está vacío')
    return redirect('carrito_detalle')

# Usuario autenticado
@login_required

# Cliente existe o se crea
try:
    cliente = Cliente.objects.get(user=request.user)
except Cliente.DoesNotExist:
    cliente = Cliente.objects.create(...)
```

### Frontend (JavaScript)
```javascript
// Validación de método de pago
if (!selectedMethod) {
    alert('Por favor selecciona un método de pago');
    return;
}

// Validación de datos de tarjeta
if (selectedMethod === 'credit_card' || selectedMethod === 'debit_card') {
    if (!cardNumber || !cardHolder || !cvv || !expMonth || !expYear) {
        alert('Por favor completa todos los datos de la tarjeta');
        return;
    }
}

// Validación de banco
if (selectedMethod === 'bank_transfer') {
    if (!bank) {
        alert('Por favor selecciona tu banco');
        return;
    }
}
```

---

## 📊 Estados de Orden

```python
# app_ordenes/models.py

ESTADOS_ORDEN = [
    ('pendiente', 'Pendiente'),
    ('pagado', 'Pagado'),          # ← Estado al simular pago
    ('enviado', 'Enviado'),
    ('entregado', 'Entregado'),
    ('cancelado', 'Cancelado'),
]
```

**Nota:** En esta simulación, las órdenes se crean directamente con estado `pagado`.

---

## 🎨 Colores y Estilos

### Mercado Pago
```css
/* Azul oficial Mercado Pago */
background: linear-gradient(135deg, #009ee3 0%, #00b0ed 100%);
color: white;
```

### BikeShop (integración)
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

---

## 🚀 Cómo Probar

### 1. Agregar productos al carrito
```
1. Ve a la lista de bicicletas
2. Agrega productos al carrito
3. Ve al carrito (icono 🛒)
```

### 2. Iniciar proceso de pago
```
1. Click en "💳 Ir a Pagar"
2. Si no estás logueado, te pedirá login
```

### 3. Completar checkout
```
1. Selecciona método de pago
2. Completa los datos requeridos
3. Click en "💳 Pagar $XXXX"
```

### 4. Ver confirmación
```
- Verás la página de éxito
- Orden creada con número único
- Info del pago
- Links a órdenes y catálogo
```

---

## 🔮 Mejoras Futuras (Opcional)

### Integración Real con Mercado Pago
```bash
pip install mercadopago
```

```python
import mercadopago

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")

preference_data = {
    "items": [
        {
            "title": bicicleta.marca,
            "quantity": cantidad,
            "unit_price": float(precio)
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
```

### Webhooks
```python
@csrf_exempt
def mercadopago_webhook(request):
    """Recibir notificaciones de Mercado Pago"""
    # Actualizar estado de orden según notificación
```

### Estados Intermedios
```python
ESTADOS_ORDEN = [
    ('pendiente', 'Pendiente'),
    ('procesando', 'Procesando Pago'),    # Nuevo
    ('pagado', 'Pagado'),
    ('fallido', 'Pago Fallido'),          # Nuevo
    # ...
]
```

### Email de Confirmación
```python
from django.core.mail import send_mail

send_mail(
    subject=f'Confirmación de Orden #{orden.id}',
    message=f'Tu pago ha sido procesado...',
    from_email='noreply@bikeshop.com',
    recipient_list=[user.email],
)
```

---

## ✅ Checklist de Funcionalidades

- ✅ Interfaz de checkout con diseño Mercado Pago
- ✅ 4 métodos de pago simulados
- ✅ Validación de formularios
- ✅ Cálculo de cuotas
- ✅ Creación de orden con estado "pagado"
- ✅ Generación de IDs únicos
- ✅ Página de confirmación con detalles
- ✅ Limpieza automática del carrito
- ✅ Integración con sistema de órdenes existente
- ✅ Responsive design
- ✅ Animaciones y feedback visual

---

## 📚 Archivos Involucrados

```
✅ templates/carrito/checkout_mercadopago.html    (Nuevo)
✅ templates/carrito/pago_exitoso.html            (Nuevo)
✅ templates/carrito/carrito_detalle.html         (Modificado)
✅ app_carrito/views.py                           (Modificado)
✅ app_carrito/urls.py                            (Modificado)
✅ doc/MERCADOPAGO_README.md                      (Nuevo)
```

---

**🎉 Sistema de Pagos Mercado Pago implementado exitosamente!**

*Nota: Recuerda que esta es una simulación educativa. Para producción, deberías integrar la API oficial de Mercado Pago.*
