"""
Script de ejemplo para crear órdenes de compra en BikeShop
Ejecutar con: python manage.py shell < ejemplo_ordenes.py
O copiar y pegar en: python manage.py shell
"""

from clientes.models import Cliente, PerfilCliente
from bicicletas.models import Bicicleta
from ordenes.models import Orden, DetalleOrden

print("\n=== EJEMPLO DE CREACIÓN DE ÓRDENES - BikeShop ===\n")

# 1. CREAR CLIENTE
print("Creando cliente...")
c = Cliente.objects.create(
    nombre="Laura Gómez",
    email="laura.gomez@example.com"
)
print(f"Cliente creado: {c}")

# Crear perfil del cliente (opcional)
perfil = PerfilCliente.objects.create(
    cliente=c,
    direccion="Av. Providencia 1234, Santiago",
    telefono="+56912345678",
    fecha_nacimiento="1990-05-15"
)
print(f"Perfil creado: {perfil}\n")

# 2. CREAR BICICLETAS
print("Creando bicicletas...")
b1 = Bicicleta.objects.create(
    marca="Trek",
    modelo="Marlin 7",
    tipo="MTB",
    precio=850000,
    anio=2024,
    disponible=True
)
print(f"Bicicleta 1: {b1} - ${b1.precio_formateado()}")

b2 = Bicicleta.objects.create(
    marca="Giant",
    modelo="TCR Advanced",
    tipo="Ruta",
    precio=1200000,
    anio=2024,
    disponible=True
)
print(f"Bicicleta 2: {b2} - ${b2.precio_formateado()}")

b3 = Bicicleta.objects.create(
    marca="Specialized",
    modelo="Stumpjumper",
    tipo="Enduro",
    precio=2500000,
    anio=2024,
    disponible=True
)
print(f"Bicicleta 3: {b3} - ${b3.precio_formateado()}\n")

# 3. CREAR ORDEN
print("Creando orden...")
o = Orden.objects.create(
    cliente=c,
    total=0,
    estado='pendiente'
)
print(f"Orden creada: {o}\n")

# 4. AGREGAR DETALLES A LA ORDEN
print("Agregando productos a la orden...")
d1 = DetalleOrden.objects.create(
    orden=o,
    bicicleta=b1,
    cantidad=2,
    precio_unitario=b1.precio
)
print(f"Detalle 1: {d1} - Subtotal: ${d1.subtotal():,.0f}".replace(",", "."))

d2 = DetalleOrden.objects.create(
    orden=o,
    bicicleta=b2,
    cantidad=1,
    precio_unitario=b2.precio
)
print(f"Detalle 2: {d2} - Subtotal: ${d2.subtotal():,.0f}".replace(",", "."))

d3 = DetalleOrden.objects.create(
    orden=o,
    bicicleta=b3,
    cantidad=1,
    precio_unitario=b3.precio
)
print(f"Detalle 3: {d3} - Subtotal: ${d3.subtotal():,.0f}".replace(",", ".\n"))


# 6. CONSULTAS - Acceder a las relaciones
print("\n=== CONSULTAS Y RELACIONES ===\n")

print("Bicicletas en la orden:")
for bici in o.bicicletas.all():
    print(f"  - {bici}")

print("\nDetalles de la orden:")
for detalle in o.detalles.all():
    print(f"  - {detalle} - ${detalle.subtotal():,.0f}".replace(",", "."))

print(f"\nÓrdenes que incluyen '{b1}':")
for orden in b1.ordenes.all():
    print(f"  - {orden} - Total: ${orden.total:,.0f}".replace(",", "."))

print(f"\nÓrdenes del cliente '{c.nombre}':")
for orden in c.ordenes.all():
    print(f"  - {orden} - Total: ${orden.total:,.0f} - Estado: {orden.estado}".replace(",", "."))

# 7. CREAR UNA SEGUNDA ORDEN
print("\n=== CREANDO SEGUNDA ORDEN ===\n")

c2 = Cliente.objects.create(
    nombre="Pedro Martínez",
    email="pedro.martinez@example.com"
)
print(f"Cliente creado: {c2}")

o2 = Orden.objects.create(cliente=c2, estado='pendiente')
print(f"Orden creada: {o2}")

DetalleOrden.objects.create(
    orden=o2,
    bicicleta=b2,
    cantidad=1,
    precio_unitario=b2.precio
)

o2.calcular_total()
print(f"Total: ${o2.total:,.0f}".replace(",", "."))

# 8. RESUMEN FINAL
print("\n=== RESUMEN FINAL ===\n")
print(f"Total de clientes: {Cliente.objects.count()}")
print(f"Total de bicicletas: {Bicicleta.objects.count()}")
print(f"Total de órdenes: {Orden.objects.count()}")
print(f"Total de detalles: {DetalleOrden.objects.count()}")

print("\nÓrdenes creadas:")
for orden in Orden.objects.all():
    print(f"  - {orden}")
    print(f"    Cliente: {orden.cliente.nombre}")
    print(f"    Total: ${orden.total:,.0f}".replace(",", "."))
    print(f"    Estado: {orden.estado}")
    print(f"    Productos: {orden.bicicletas.count()}")

# 9. OPERACIONES ADICIONALES
print("\n=== OPERACIONES ADICIONALES ===\n")

print("Cambiando estado de la primera orden a 'pagada'...")
o.estado = 'pagada'
o.save()
print(f"Estado actualizado: {o.estado}")

print("\nÓrdenes pendientes:")
ordenes_pendientes = Orden.objects.filter(estado='pendiente')
print(f"Total: {ordenes_pendientes.count()}")
for orden in ordenes_pendientes:
    print(f"  - {orden}")

print("\nÓrdenes pagadas:")
ordenes_pagadas = Orden.objects.filter(estado='pagada')
print(f"Total: {ordenes_pagadas.count()}")
for orden in ordenes_pagadas:
    print(f"  - {orden} - ${orden.total:,.0f}".replace(",", "."))

ventas_totales = sum(o.total for o in Orden.objects.filter(estado='pagada'))
print(f"\nVentas totales (órdenes pagadas): ${ventas_totales:,.0f}".replace(",", "."))

print("\nBicicleta más vendida:")
from django.db.models import Sum
ventas_por_bici = DetalleOrden.objects.values(
    'bicicleta__marca',
    'bicicleta__modelo'
).annotate(
    total_vendido=Sum('cantidad')
).order_by('-total_vendido')

if ventas_por_bici:
    top = ventas_por_bici[0]
    print(f"  {top['bicicleta__marca']} {top['bicicleta__modelo']} - {top['total_vendido']} unidades")

print("\n=== EJEMPLO COMPLETADO ===\n")

