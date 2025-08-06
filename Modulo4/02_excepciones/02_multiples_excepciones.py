while True:
    try:
        x = int(input("Ingresa un número: "))
        
        lista = [1, 2, 3]
        x = lista[x]  #  Esto puede causar IndexError si x está fuera del rango de la lista
        y = 10 / x
        print(f"Resultado de la división: {y}")
    except ValueError:
        print("ValueError: Debes ingresar un número válido.")
    except ZeroDivisionError:
        print("ZeroDivision: No puedes dividir por cero.")
    except Exception as e:
        # Captura cualquier otra excepción no prevista
        print(f"Exception: Ha ocurrido un error inesperado: {e}")
    except IndexError:
        print("IndexError: El índice está fuera del rango de la lista.")