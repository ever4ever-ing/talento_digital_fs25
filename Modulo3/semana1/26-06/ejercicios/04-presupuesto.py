"""
Ejercicio: Calculadora de Autonomía de Viaje
Objetivo: Crear un script que calcule cuántos kilómetros puede recorrer un auto con un presupuesto determinado para bencina.

Instrucciones:

Define las siguientes variables con los datos proporcionados:

Rendimiento del auto: 12.5 kilómetros por litro.
Precio de la bencina: $1200 por litro.
Presupuesto disponible: $15000.
Realiza los cálculos necesarios:

Calcula cuántos litros de bencina se pueden comprar con el presupuesto.
Calcula la distancia total que se puede recorrer con esos litros.
Muestra el resultado en la consola con el siguiente formato: Con $presupuesto puedes recorrer km_recorridos km!
"""
#Datos del vehiculo
autonomia = 12.5  # Consumo del auto (km/L)
precio_combustible = 1200  # Precio por litro (CLP)
# Presupuesto disponible (int o float)
presupuesto = 15000
cant_litros = presupuesto / precio_combustible
distancia_presupuesto = autonomia * cant_litros #(L * km/L)
print(f"La cantidad de litros comprados es {cant_litros} L")
print(f"La distancia que lograre recorrer es {distancia_presupuesto} Km")
