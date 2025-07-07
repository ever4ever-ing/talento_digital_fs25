"""
Tuplas (tuple)
Inmutables: No se pueden modificar después de su creación.
Ordenadas: Mantienen el orden de inserción.
Sintaxis: Se definen con paréntesis () o sin ellos (separando elementos por comas).
Usos: Ideales para datos constantes (ej. coordenadas, fechas).
"""
dato1=(1, "hola", 3.14)
dato2= 1, 2, 3
print(type(dato2))
dato3=(42)
print(type(dato3))
dato4=(42,)
print(type(dato4))
dato5=42,
print(type(dato5))
dato6=42,9
print(type(dato6))
print(len(dato6))

print("-"*60)
print("Transformar a tupla")
lista = [1, 2, 3, 4]
tupla_desde_lista = tuple(lista)
print(type(tupla_desde_lista))
nueva_lista=list(tupla_desde_lista)
print(type(nueva_lista))
print("-"*60)
print("Slicing")
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Primeros 3 [0:3]: {numeros[0:3]}")
print(f"Últimos 3 [-3:]: {numeros[-3:]}")
print(f"Reversa [::-1]: {numeros[::-1]}")

print("-"*60)

matriz = ((1, 2, 3), (4, 5, 6), [7, 8, 9])
print(f"Primera fila [0]: {matriz[0]}")
print(f"Segunda fila [1]: {matriz[1]}")
print(f"Tercera fila [2]: {matriz[2].append(10)}")
print(f"Tercera fila [2]: {matriz[2]}") 
print(matriz) 


print("-"*60)
print("Elementos repetidos")
numeros_repetidos = (1, 2, 3, 2, 4, 2, 5)
conteo_2 = numeros_repetidos.count(2)
print(f"El número 2 aparece {conteo_2} veces")


print("-"*60)
print("Desempaquetar tupla")
punto=(10, 15, 30)
x, y, z = punto
print(f"Coordenadas: x= {x}, y= {y} , z= {z}")

#La variable con * siempre se convierte en una lista (aunque la original sea tupla)
#Es muy útil para funciones que reciben argumentos variables
numeros = (1, 2, 3, 4, 5)
primero, *resto = numeros
print(f"Primero: {primero}")# 1
print(f"Resto: {resto}")# [2, 3, 4, 5]

a, b, *medio, z = numeros
print(f"a: {a}")
print(f"b: {b}")
print(f"medio: {medio}")
print(f"z: {z}")

# Intercambio de variables (muy pythónico)
a = "gato"
b = "perro"
print(f"Antes: a={a}, b={b}")
a, b = (b, a)  # Intercambio usando tuplas
print(f"Después: a={a}, b={b}")

#Forma tradicional
a = 10
b = 20
temp = a
a = b
b = temp

# Método aritmético (solo para números)
a = 10
b = 20
a = a + b  # a = 30
b = a - b  # b = 10
a = a - b  # a = 20

# Método XOR (solo para enteros)
a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b

print("-"*60)
print("Casos practicos")

# Ejemplo 1: Coordenadas geográficas
#Diccionarios

ciudades = {
    "Madrid": (40.4168, -3.7038),
    "Barcelona": (41.3851, 2.1734),
    "Valencia": (39.4699, -0.3763)
}

# Ejemplo 2: Configuración de colores RGB
colores = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "blanco": (255, 255, 255),
    "negro": (0, 0, 0)
}