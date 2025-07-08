num = 0
while num < 4:
    print("bucle while :", num)
    num += 1

print("-"*10)
i = 0
while i < 4:
    print("bucle while :", i)
    i += 1 #incremento
else:
    print("Acabamos de salir del bucle")

#IMPORTANTE:
contador = 0
while contador < 5:
    print("Iteración:", contador)
    contador += 1  # Asegurar que la condición cambiará

#CICLOS INFINITOS
print("-"*10)
print("Este es un while infinito:")
print("Ejecutando programa:")
while True:
    entrada = input("Escribe un numero: ('x' para terminar:) ")
    if entrada.lower() == "x":
        break