def calcular_ganancia(precio_actual, cantidad_acciones, precio_futuro):
    inversion_total = precio_actual * cantidad_acciones
    valor_futuro = precio_futuro * cantidad_acciones
    ganancia = valor_futuro - inversion_total
    return ganancia
# Datos de entrada
precio_actual = float(input("Ingrese el precio actual de la acción en pesos chilenos: "))
cantidad_acciones = int(input("Ingrese la cantidad de acciones que planea comprar: "))
precio_futuro = float(input("Ingrese su estimación del precio futuro de la acción en pesos chilenos: "))

# Calcular la ganancia potencial
ganancia_potencial = calcular_ganancia(precio_actual, cantidad_acciones, precio_futuro)

print("La ganancia potencial al comprar {} acciones sería de {} pesos chilenos.".format(cantidad_acciones, ganancia_potencial))