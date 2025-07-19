class EdadInvalidaError(Exception):
    """Excepción personalizada para edad inválida"""
    def __init__(self, edad, mensaje="Edad no válida"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError(edad, "La edad no puede ser negativa")
    elif edad > 150:
        raise EdadInvalidaError(edad, "La edad no puede ser mayor a 150 años")
    else:
        print(f"Edad válida: {edad}")
    return True
while True:
    edad = int(input("Introduce tu edad: "))
    validar_edad(edad)