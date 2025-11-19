from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from decimal import Decimal
import uuid
from app_bicicletas.models import Bicicleta
from app_ordenes.models import Orden, DetalleOrden
from app_clientes.models import Cliente
from .carrito import Carrito
from .forms import CarritoAgregarBicicletaForm


@require_POST
def carrito_agregar(request, bicicleta_id):
    """
    Agregar una bicicleta al carrito.
    """
    carrito = Carrito(request)
    bicicleta = get_object_or_404(Bicicleta, id=bicicleta_id)
    form = CarritoAgregarBicicletaForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        carrito.agregar(
            bicicleta=bicicleta,
            cantidad=cd['cantidad'],
            actualizar_cantidad=cd['actualizar']
        )
        messages.success(request, f'🛒 {bicicleta.marca} {bicicleta.modelo} agregado al carrito')
    
    return redirect('carrito_detalle')


@require_POST
def carrito_eliminar(request, bicicleta_id):
    """
    Eliminar una bicicleta del carrito.
    """
    carrito = Carrito(request)
    bicicleta = get_object_or_404(Bicicleta, id=bicicleta_id)
    carrito.eliminar(bicicleta)
    messages.info(request, f'🗑️ {bicicleta.marca} {bicicleta.modelo} eliminado del carrito')
    
    return redirect('carrito_detalle')


def carrito_detalle(request):
    """
    Mostrar el detalle del carrito.
    """
    carrito = Carrito(request)
    
    # Crear formularios para cada item del carrito
    for item in carrito:
        item['actualizar_cantidad_form'] = CarritoAgregarBicicletaForm(
            initial={
                'cantidad': item['cantidad'],
                'actualizar': True
            }
        )
    
    context = {
        'carrito': carrito
    }
    return render(request, 'carrito/carrito_detalle.html', context)


@login_required
def iniciar_checkout(request):
    """
    Iniciar el proceso de checkout con Mercado Pago.
    Redirige a la página de pago.
    """
    carrito = Carrito(request)
    
    if len(carrito) == 0:
        messages.warning(request, '⚠️ Tu carrito está vacío')
        return redirect('carrito_detalle')
    
    # Verificar si el usuario tiene un cliente asociado
    try:
        cliente = Cliente.objects.get(email=request.user.email)
    except Cliente.DoesNotExist:
        # Crear un cliente automáticamente si no existe
        cliente = Cliente.objects.create(
            nombre=request.user.get_full_name() or request.user.username,
            email=request.user.email
        )
        messages.info(request, '✅ Perfil de cliente creado automáticamente')
    
    return redirect('checkout_mercadopago')


@login_required
def checkout_mercadopago(request):
    """
    Página de checkout con simulación de Mercado Pago.
    """
    carrito = Carrito(request)
    
    if len(carrito) == 0:
        messages.warning(request, '⚠️ Tu carrito está vacío')
        return redirect('carrito_detalle')
    
    if request.method == 'POST':
        return procesar_pago_mercadopago(request)
    
    # Calcular totales para cuotas
    total = carrito.obtener_precio_total()
    total_3_cuotas = round(total / 3, 2)
    total_6_cuotas = round(total / 6, 2)
    total_12_cuotas = round(total / 12, 2)
    
    context = {
        'carrito': carrito,
        'total': total,
        'total_3_cuotas': total_3_cuotas,
        'total_6_cuotas': total_6_cuotas,
        'total_12_cuotas': total_12_cuotas,
    }
    return render(request, 'carrito/checkout_mercadopago.html', context)


@login_required
def procesar_pago_mercadopago(request):
    """
    Procesar el pago simulado de Mercado Pago.
    Crea la orden y simula el procesamiento del pago.
    """
    carrito = Carrito(request)
    
    if len(carrito) == 0:
        messages.warning(request, '⚠️ Tu carrito está vacío')
        return redirect('carrito_detalle')
    
    # Obtener datos del formulario
    payment_method = request.POST.get('payment_method')
    
    # Verificar cliente
    try:
        cliente = Cliente.objects.get(email=request.user.email)
    except Cliente.DoesNotExist:
        cliente = Cliente.objects.create(
            nombre=request.user.get_full_name() or request.user.username,
            email=request.user.email
        )
    
    # Crear la orden
    orden = Orden.objects.create(
        cliente=cliente,
        estado='pagado'  # Simulación: estado pagado directamente
    )
    
    # Crear los detalles de la orden
    for item in carrito:
        DetalleOrden.objects.create(
            orden=orden,
            bicicleta=item['bicicleta'],
            precio_unitario=item['precio'],
            cantidad=item['cantidad']
        )
    
    # Calcular el total de la orden
    orden.calcular_total()
    
    # Preparar información del pago para mostrar
    payment_info = {
        'method': payment_method,
        'transaction_id': f'MP-{uuid.uuid4().hex[:12].upper()}',
        'timestamp': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    
    # Información específica según método de pago
    if payment_method in ['credit_card', 'debit_card']:
        payment_info['method_display'] = 'Tarjeta de Crédito' if payment_method == 'credit_card' else 'Tarjeta de Débito'
        payment_info['card_number'] = request.POST.get('card_number', '')[-4:]  # Últimos 4 dígitos
        
        if payment_method == 'credit_card':
            installments = int(request.POST.get('installments', 1))
            payment_info['installments'] = installments
            if installments > 1:
                payment_info['installment_amount'] = float(round(orden.total / installments, 2))
    
    elif payment_method == 'bank_transfer':
        payment_info['method_display'] = 'Transferencia Bancaria (PSE)'
        payment_info['bank'] = request.POST.get('bank', '').title()
    
    elif payment_method == 'cash':
        payment_info['method_display'] = 'Pago en Efectivo'
        payment_info['payment_code'] = f'CASH-{uuid.uuid4().hex[:10].upper()}'
    
    # Guardar info de pago en sesión
    request.session['last_payment_info'] = payment_info
    request.session['last_order_id'] = orden.id
    
    # Limpiar el carrito
    carrito.limpiar()
    
    messages.success(
        request,
        f'✅ ¡Pago procesado exitosamente! Orden #{orden.id} creada'
    )
    
    return redirect('pago_exitoso')


@login_required
def pago_exitoso(request):
    """
    Página de confirmación de pago exitoso.
    """
    # Recuperar información de la sesión
    order_id = request.session.get('last_order_id')
    payment_info = request.session.get('last_payment_info', {})
    
    if not order_id:
        messages.warning(request, '⚠️ No se encontró información de la orden')
        return redirect('carrito_detalle')
    
    orden = get_object_or_404(Orden, id=order_id, cliente__email=request.user.email)
    
    context = {
        'orden': orden,
        'payment_info': payment_info,
    }
    
    # Limpiar la sesión
    if 'last_payment_info' in request.session:
        del request.session['last_payment_info']
    if 'last_order_id' in request.session:
        del request.session['last_order_id']
    
    return render(request, 'carrito/pago_exitoso.html', context)


@login_required
def mis_ordenes(request):
    """
    Mostrar las órdenes del usuario actual.
    """
    try:
        cliente = Cliente.objects.get(email=request.user.email)
        ordenes = Orden.objects.filter(cliente=cliente).prefetch_related('detalles__bicicleta').order_by('-fecha')
    except Cliente.DoesNotExist:
        ordenes = []
        messages.info(request, 'ℹ️ Aún no tienes órdenes')
    
    context = {
        'ordenes': ordenes
    }
    return render(request, 'carrito/mis_ordenes.html', context)
