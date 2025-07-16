def imprimir_numeros_0_n(n=100):
    print(f"1. Números del 0 al {n}:")
    for i in range(n+1):
        print(i)

def imprimir_multiplos_2(n=500):
    print(f"2. Múltiplos de 2 entre 2 y {n}:")
    for i in range(2, n+1, 2):
        print(i)

def vanilla_ice(j=1,n=100):
    print("3. Contando Vanilla Ice:")
    for i in range(j, n+1):
        if i % 10 == 0:
            print("baby")
        elif i % 5 == 0:
            print("ice ice")
        else:
            print(i)

def suma_pares_500k(n=50):
    suma_pares = 0
    for i in range(0, n+1, 2):
        suma_pares += i
    print(f"La suma total usando bucle es: {suma_pares}")
    return suma_pares

def cuenta_regresiva_3(n=30):
    for i in range(n, 0, -3):
        print(i)

def contador_dinamico(inicial=1, final=100, multiplo=1):
    numInicial = inicial
    numFinal = final
    for i in range(numInicial, numFinal+1):
        if i % multiplo == 0:
            print(i)


imprimir_numeros_0_n(10)
imprimir_multiplos_2(25)
vanilla_ice(30)
suma_pares_500k()
cuenta_regresiva_3()
contador_dinamico()
