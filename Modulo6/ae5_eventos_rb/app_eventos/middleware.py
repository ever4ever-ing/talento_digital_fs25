from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied


class PermissionDeniedMiddleware:
    """
    Middleware para manejar excepciones de permisos denegados
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """
        Captura las excepciones de PermissionDenied y redirige a la página de acceso denegado
        """
        if isinstance(exception, PermissionDenied):
            messages.error(request, '🚫 No tienes permisos suficientes para realizar esta acción.')
            return redirect('acceso_denegado')
        
        return None
