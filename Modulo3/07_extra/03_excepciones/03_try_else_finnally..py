while True:
    try:
        print("-"*20)
        print("Intentando ejecutar código...")
        numero = int(input("Ingresa un número: "))
        # Código que puede fallar
        resultado = 10 / numero
        print(f"10 dividido por {numero} es: {resultado}")
    except Exception:
        # Captura cualquier excepción
        print("Error: Algo salió mal")
    else:
        # Se ejecuta si no hay excepciones
        print("Bloque else: Se ejecuta si NO hay excepciones")
    finally:
        # Se ejecuta siempre, haya o no excepciones
        print("Bloque finally: Siempre se ejecuta")
