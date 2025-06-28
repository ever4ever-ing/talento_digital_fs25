"""
Ejercicio: Calculadora de Ganancias Netas de una Frutería
Objetivo: Escribir un script en Python para calcular la ganancia neta de una frutería, considerando ingresos y costos.

Instrucciones:

1. Define las variables para los precios, costos y cantidades vendidas:
    - Precios de Venta: Manzanas: $950/kg, Naranjas: $1300/kg.
    - Costos de Compra: Manzanas: $600/kg, Naranjas: $850/kg.
    - Cantidades Vendidas: Manzanas: 10 kg, Naranjas: 15 kg.
    - Costos Fijos del día: $5000.

2. Calcula los ingresos totales por la venta de ambas frutas.
3. Calcula los costos totales (costo de la fruta + costos fijos).
4. Calcula la ganancia neta (ingresos - costos).
5. Muestra un resumen detallado en la consola.
"""
#Definir variables
#Realizar cálculos
# 1. Calcular Ingresos Totales
# 2. Calcular Costos Totales
# 3. Calcular Ganancia Neta
# 4. Mostrar Resultado

#venta
precio_manzanas = 950
precio_naranjas = 1300
#costos
costo_manzanas = 600
costo_naranjas = 850
#cantidades vendidas
kilos_manzanas = 10
kilos_naranjas = 15
costos_fijos = 5000

#Calcular los ingresos totales
ingresos_manzanas = precio_manzanas * kilos_manzanas
ingresos_naranjas = precio_naranjas * kilos_naranjas
ingresos_totales = ingresos_manzanas + ingresos_naranjas

#costos totales
costos_totales_manzanas = costo_manzanas * kilos_manzanas
costos_totales_naranjas = costo_naranjas * kilos_naranjas
costos_totales = costos_totales_manzanas + costos_totales_naranjas + costos_fijos

ganancia_neta = ingresos_totales - costos_totales

print(f"El ingreso de manzanas es: ${ingresos_manzanas}")
print(f"El ingreso de naranjas es: ${ingresos_naranjas}")
print(f"El ingreso total es: ${ingresos_totales}")
print(f"El costo total es: ${costos_totales}")
print(f"La ganancia neta es: ${ganancia_neta}")