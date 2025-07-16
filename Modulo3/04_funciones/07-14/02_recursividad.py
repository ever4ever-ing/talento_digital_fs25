def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        print(f"{n}")
        return n * factorial(n-1)
    
print(factorial(4))

def factorial_iterativo(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

print(factorial_iterativo(4))