def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def mostrar_fibonacci(n):
    print(f"Fibonacci hasta {n}:")
    for i in range(n + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

n = int(input("Ingrese un número para calcular la serie de Fibonacci: "))
mostrar_fibonacci(n)