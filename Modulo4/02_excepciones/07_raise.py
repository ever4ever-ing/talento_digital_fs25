def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
if __name__ == "__main__":
    try:
        resultado = dividir(10, 0)
        print("El resultado es:", resultado)
    except ZeroDivisionError as e:
        print("Excepción capturada")
        print(e)
        
        
