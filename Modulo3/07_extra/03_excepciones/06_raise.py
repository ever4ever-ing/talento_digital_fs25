def dividir_numeros(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error capturado en la función")
        raise  # Re-lanza la excepción 

try:
    resultado = dividir_numeros(10, 0)
except ZeroDivisionError:
    print("Error capturado en el nivel superior")# Manejo de la excepción en el nivel superior

"""
¿Por qué usar raise?
Logging/Registro: La función puede registrar el error pero no manejarlo completamente
Responsabilidad: Permite que quien llama la función decida qué hacer con el error
"""