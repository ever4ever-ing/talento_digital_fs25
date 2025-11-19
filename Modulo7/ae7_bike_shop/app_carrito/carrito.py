"""
Clase Carrito: Maneja el carrito de compras usando sesiones de Django.

El carrito se guarda en request.session['carrito'] como un diccionario:
{
    'bicicleta_id': {
        'cantidad': int,
        'precio': str (Decimal se serializa como string)
    }
}
"""
from decimal import Decimal
from django.conf import settings
from app_bicicletas.models import Bicicleta


class Carrito:
    """
    Clase para manejar el carrito de compras usando sesiones.
    """
    
    def __init__(self, request):
        """
        Inicializar el carrito.
        """
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        
        if not carrito:
            # Guardar un carrito vacío en la sesión
            carrito = self.session[settings.CART_SESSION_ID] = {}
        
        self.carrito = carrito
    
    def agregar(self, bicicleta, cantidad=1, actualizar_cantidad=False):
        """
        Agregar una bicicleta al carrito o actualizar su cantidad.
        
        Args:
            bicicleta: Instancia del modelo Bicicleta
            cantidad: Cantidad a agregar
            actualizar_cantidad: Si True, reemplaza la cantidad; si False, la incrementa
        """
        bicicleta_id = str(bicicleta.id)
        
        if bicicleta_id not in self.carrito:
            self.carrito[bicicleta_id] = {
                'cantidad': 0,
                'precio': str(bicicleta.precio)
            }
        
        if actualizar_cantidad:
            self.carrito[bicicleta_id]['cantidad'] = cantidad
        else:
            self.carrito[bicicleta_id]['cantidad'] += cantidad
        
        self.guardar()
    
    def guardar(self):
        """
        Marcar la sesión como modificada para asegurar que se guarde.
        """
        self.session.modified = True
    
    def eliminar(self, bicicleta):
        """
        Eliminar una bicicleta del carrito.
        """
        bicicleta_id = str(bicicleta.id)
        
        if bicicleta_id in self.carrito:
            del self.carrito[bicicleta_id]
            self.guardar()
    
    def __iter__(self):
        """
        Iterar sobre los items del carrito y obtener las bicicletas desde la BD.
        """
        bicicletas_ids = self.carrito.keys()
        # Obtener las bicicletas y agregarlas al carrito
        bicicletas = Bicicleta.objects.filter(id__in=bicicletas_ids)
        
        carrito = self.carrito.copy()
        
        for bicicleta in bicicletas:
            carrito[str(bicicleta.id)]['bicicleta'] = bicicleta
        
        for item in carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item
    
    def __len__(self):
        """
        Contar todos los items en el carrito.
        """
        return sum(item['cantidad'] for item in self.carrito.values())
    
    def obtener_precio_total(self):
        """
        Calcular el precio total de todos los items en el carrito.
        """
        return sum(
            Decimal(item['precio']) * item['cantidad']
            for item in self.carrito.values()
        )
    
    def limpiar(self):
        """
        Limpiar el carrito de la sesión.
        """
        del self.session[settings.CART_SESSION_ID]
        self.guardar()
