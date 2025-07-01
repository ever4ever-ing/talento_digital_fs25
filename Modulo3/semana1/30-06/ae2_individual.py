# 1. Imprime "Hola, mundo"
print("Hola, mundo")
# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Valeria"
print("Hola,", nombre)  # con una coma
print("Hola, " + nombre)  # con un +
# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156
print("Hola", numero, "!")  # con una coma
# print("Hola " + numero + "!")  # Esto arrojaría un error
print("Hola " + str(numero) + "!")  # corregido con conversión
# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "completos"
comida2 = "empanadas"
print("¡Me encanta comer {} y {}!".format(comida1, comida2))  # con .format()
print(f"¡Me encanta comer {comida1} y {comida2}!")  # con una cadena f