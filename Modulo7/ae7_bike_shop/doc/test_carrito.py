# Script de ejemplo para probar el carrito programáticamente

from app_bicicletas.models import Bicicleta
from app_carrito.carrito import Carrito
from django.contrib.sessions.backends.db import SessionStore

# Crear una sesión de prueba
session = SessionStore()

# Crear un objeto request simulado
class FakeRequest:
    def __init__(self, session):
        self.session = session

request = FakeRequest(session)

# Crear instancia del carrito
carrito = Carrito(request)

# Obtener algunas bicicletas
bicicletas = Bicicleta.objects.all()[:3]

print("=== Agregando bicicletas al carrito ===")
for bici in bicicletas:
    carrito.agregar(bici, cantidad=1)
    print(f"✓ Agregada: {bici.marca} {bici.modelo} - ${bici.precio}")

print(f"\n=== Estado del carrito ===")
print(f"Total de items: {len(carrito)}")
print(f"Precio total: ${carrito.obtener_precio_total()}")

print(f"\n=== Contenido detallado ===")
for item in carrito:
    print(f"- {item['bicicleta'].marca} {item['bicicleta'].modelo}")
    print(f"  Cantidad: {item['cantidad']}")
    print(f"  Precio unitario: ${item['precio']}")
    print(f"  Total: ${item['total_precio']}")
    print()

# Actualizar cantidad
if bicicletas:
    print("=== Actualizando cantidad ===")
    carrito.agregar(bicicletas[0], cantidad=3, actualizar_cantidad=True)
    print(f"Cantidad actualizada para {bicicletas[0].marca} {bicicletas[0].modelo}")
    print(f"Nuevo total: ${carrito.obtener_precio_total()}")

# Eliminar un producto
if len(bicicletas) > 1:
    print(f"\n=== Eliminando producto ===")
    carrito.eliminar(bicicletas[1])
    print(f"Eliminado: {bicicletas[1].marca} {bicicletas[1].modelo}")
    print(f"Items restantes: {len(carrito)}")

print("\n✅ Script completado!")
