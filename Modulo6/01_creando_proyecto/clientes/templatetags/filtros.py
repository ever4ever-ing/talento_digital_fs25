from django import template

register = template.Library()

@register.filter
def formato_precio(valor):
    """Devuelve el precio con formato de moneda."""
    return f"${valor:,.0f}"