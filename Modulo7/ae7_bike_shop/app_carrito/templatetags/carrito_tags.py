from django import template
from app_carrito.carrito import Carrito

register = template.Library()


@register.simple_tag
def cantidad_total_carrito(request):
    """
    Template tag para mostrar la cantidad total de items en el carrito.
    Uso: {% cantidad_total_carrito request %}
    """
    carrito = Carrito(request)
    return len(carrito)


@register.simple_tag
def total_carrito(request):
    """
    Template tag para mostrar el total del carrito.
    Uso: {% total_carrito request %}
    """
    carrito = Carrito(request)
    return carrito.obtener_precio_total()
