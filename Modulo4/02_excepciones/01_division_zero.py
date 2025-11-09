try:
    divisor = int(input("Ingresa un número divisor: "))
    x = 10 / divisor
    print(f"Resultado de la división: {x}")
except ZeroDivisionError:
    print("No puedes dividir por cero")
