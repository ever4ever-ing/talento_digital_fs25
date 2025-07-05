# Datos de entrada
num_productos = int(input("Ingrese el número de productos comprados: "))
es_frecuente = input("¿El cliente es frecuente? (sí/no): ") == "sí"
monto_compra = float(input("Ingrese el monto total de la compra: "))
dia_promocion = input("¿Es día de promoción especial? (sí/no): ") == "sí"
# Inicializar descuento
descuento = 0

# Evaluar condiciones
if num_productos > 10:
    descuento += 10

if es_frecuente:
    descuento += 5

if monto_compra > 500:
    descuento += 7

if dia_promocion:
    descuento += 15

# Limitar el descuento máximo a 30%
if descuento > 30:
    descuento = 30

# Mostrar resultado
print(f"El descuento aplicado es del {descuento}%.")