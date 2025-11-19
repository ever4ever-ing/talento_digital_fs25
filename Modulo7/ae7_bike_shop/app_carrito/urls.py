from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito_detalle, name='carrito_detalle'),
    path('carrito/agregar/<int:bicicleta_id>/', views.carrito_agregar, name='carrito_agregar'),
    path('carrito/eliminar/<int:bicicleta_id>/', views.carrito_eliminar, name='carrito_eliminar'),
    path('carrito/checkout/', views.iniciar_checkout, name='iniciar_checkout'),
    path('checkout/mercadopago/', views.checkout_mercadopago, name='checkout_mercadopago'),
    path('pago/exitoso/', views.pago_exitoso, name='pago_exitoso'),
    path('mis-ordenes/', views.mis_ordenes, name='mis_ordenes'),
]
