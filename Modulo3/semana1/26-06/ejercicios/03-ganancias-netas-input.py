"""
Mismo ejercicio anterior pero ingresando datos por teclado
"""
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

precio_manzanas = int(input("Ingrese precio actual de venta de manzanas:"))
precio_naranjas = int(input("Ingrese precio actual de venta de naranjas:"))
kilos_manzanas = int(input("Ingrese cuantos kilos vendió de manzanas:"))
kilos_naranjas = int(input("Ingrese cuantos kilos vendió de naranjas:"))

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