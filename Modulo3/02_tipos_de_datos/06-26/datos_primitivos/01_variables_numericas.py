import math

# Ejemplo 1: Calcular el area de un triangulo
base = 6.9
altura = 8.2

area= (base * altura) / 2
area= round(area)
print(area)


# Ejemplo 2: Encontrar la hipotenusa de un triángulo rectángulo
"""
Problema: Un árbitro corre 30 metros hacia el norte y 40 metros hacia el este. ¿Cuál es la distancia directa desde el punto donde comenzo?
"""
distancia_norte= 30 
distancia_este= 40

#(norte^2+este ^2)^1/2
distancia_directa= math.hypot(distancia_norte, distancia_este)

print("La distancia recorrida por el arbitro es: ", distancia_directa, "m")


# Situación: Calcular cuántos taxis necesitas para un grupo.

personas = 10
capacidad_taxi = 4

operacion= personas / capacidad_taxi
print("Sin redondear:", operacion)
taxis_necesarios = math.ceil(personas / capacidad_taxi)
print("Necesitas", taxis_necesarios, " taxis.")

# Situación: Dividir porciones de pizza entre personas.

porciones = 24
personas = 7

sin_redon=porciones / personas
print(f"Cada uno recibe {sin_redon} trozos.")
porciones_por_persona = math.floor(porciones / personas)
print(f"Cada uno recibe {porciones_por_persona} trozos.")



""" 
Un archivo de 500 MB se descarga a 6.3 MB/s. 
¿Cuánto MB has descargado en 60s?
"""

velocidad = 6.3  # MB/s
tiempo = 60  # segundos
mb_descargados = math.floor(velocidad * tiempo)

print(f" Descargaste {mb_descargados} MB en {tiempo} segundos ( {velocidad*tiempo}).")



# Tiempo estimado de entrega (3 días y 4.8 horas)

tiempo_real = 3.2 #dias

entrega_round = round(tiempo_real)  # 3 días

#Cuanto le digo al cliente?
entrega_ceil = math.ceil(tiempo_real)  # 4 días
print(f"Estimado cliente: Su entrega llegará en {entrega_ceil} dias")

