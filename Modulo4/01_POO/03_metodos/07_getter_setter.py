class Mascota:
    def __init__(self, nombre, especie, edad):
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            print("Error: Nombre no válido")
    def get_especie(self):
        return self._especie
    def set_especie(self, nueva_especie):
        especies_validas = ["perro", "gato", "ave", "pez", "roedor"]
        if nueva_especie.lower() in especies_validas:
            self._especie = nueva_especie.lower()
        else:
            print(f"Error: Especies válidas son {', '.join(especies_validas)}")
    
    # Getter simple para edad
    def get_edad(self):
        return self._edad
    
    # Setter simple para edad
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("Error: Edad debe ser entero positivo")

    def __str__(self):
        return f"{self.get_nombre()} es un {self.get_especie()} de {self.get_edad()} años"


# Uso de la versión simple
mi_mascota = Mascota("Firulais", "perro", 5)

# Accediendo con getters
print(mi_mascota.get_nombre())  # Output: Firulais

# Modificando con setters
mi_mascota.set_nombre("Rex")
mi_mascota.set_edad(6)
mi_mascota.set_especie("gato")

print(mi_mascota)  # Output: Rex es un gato de 6 años