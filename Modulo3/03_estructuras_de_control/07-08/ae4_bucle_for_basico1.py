"""Básico: imprime todos los números enteros del 0 al 100."""

print("1. Números del 0 al 100:")
for i in range(101):
    print(i)

"""Múltiplos de 2: imprime todos los números múltiplos de 2 entre 2 y 500"""
print("2. Múltiplos de 2 entre 2 y 500:")
for i in range(2, 501, 2):
    print(i)

"""
Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
Wow.
"""
print("3. Contando Vanilla Ice:")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
"""
Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
"""
suma_pares = 0
for i in range(0, 500001, 2):
    suma_pares += i
print(f"La suma total usando bucle es: {suma_pares}")


"""
Regrésame al 3: imprime los números positivos comenzando desde 2025, en cuenta regresiva de 3 en 3.
"""
for i in range(2025, 0, -3):
    print(i)

"""
Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas)."""


numInicial = int(input("dame el numero inicial: "))
numFinal = int(input("dame el numero final: "))
multiplo =  int(input("dame el multiplo: "))
for i in range(numInicial,numFinal+1):
    if i % multiplo == 0:
        print(i)