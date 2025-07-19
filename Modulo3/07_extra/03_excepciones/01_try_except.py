while True:
    try:
        numero = float(input("Ingresa un número: "))
        resultado = 10 / numero
        print(f"10 dividido por {numero} es: {resultado}")
    except ValueError:
        print("Error: No ingresaste un número válido")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")