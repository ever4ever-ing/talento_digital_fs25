try:
    # Bloque de código que puede causar una excepción
    divisor = int(input("Ingresa un número divisor: "))
    x = 10 / divisor
    print(f"Resultado de la división: {x}")
except ZeroDivisionError:
    # Bloque de código que se ejecuta si ocurre la excepción
    print("No puedes dividir por cero")

# while True:
#     divisor = int(input("Ingresa un número divisor: "))
#     x = 10 / divisor
#     print(f"Resultado de la división: {x}")
