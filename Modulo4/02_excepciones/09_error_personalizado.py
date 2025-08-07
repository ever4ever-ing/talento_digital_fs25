class ChocolateNoPermitidoError(Exception):
       def __init__(self, mensaje="¡El chocolate es tóxico para los perros! No se permite."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def alimentar(self, comida):
        if comida.lower() == "chocolate" and self.especie.lower() == "perro" or self.especie.lower() == "gato":
            raise ChocolateNoPermitidoError() # Lanzar el error personalizado
        else:
            print(f"{self.nombre} ha sido alimentado con {comida}.")
# --- Uso ---
try:
    mi_perro = Mascota("Rex", "perro")
    mi_perro.alimentar("pollo")  # Esto funciona
    mi_perro.alimentar("chocolate")  # Esto lanza el error personalizado
except ChocolateNoPermitidoError as e:
    print(f"Error: {e}")