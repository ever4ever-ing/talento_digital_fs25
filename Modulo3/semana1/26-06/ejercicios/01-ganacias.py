"""
Ejercicio 1: Calculadora de Ganancias de una Frutería
Objetivo: Escribir un script en Python para calcular la ganancia total de la venta de manzanas y naranjas en un día.

Instrucciones:

Define las variables para los precios y las cantidades vendidas según los siguientes datos:

Precio por kilo de manzanas: $950
Precio por kilo de naranjas: $1300
Kilos de manzanas vendidos: 10
Kilos de naranjas vendidos: 15

Calcula la ganancia obtenida por cada tipo de fruta.

Suma las ganancias para obtener el total del día.

Muestra el resultado en la consola utilizando un f-string. El mensaje debe tener el siguiente formato, mostrando el total:  Ganaste $monto_total hoy!
"""
#Definir variables
precio_manzanas = 950
precio_naranjas = 1300
kilos_manzanas = 10
kilos_naranjas = 15
#Realizar cálculo
ganancia_manzanas = precio_manzanas * kilos_manzanas
ganancia_naranjas = precio_naranjas * kilos_naranjas
ganancia_total = ganancia_manzanas + ganancia_naranjas
print(f"La ganancia del día es: {ganancia_total}")
