class Mascota:
    def __init__(self, nombre, especie, edad):
        self._nombre = nombre  # Usamos _ para indicar que es "protegido"
        self._especie = especie
        self._edad = edad
    
    # Getter para nombre
    @property
    def nombre(self):
        print("Obteniendo nombre...")
        return self._nombre
    
    # Setter para nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        print(f"Cambiando nombre de {self._nombre} a {nuevo_nombre}...")
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena no vacía")
    
    # Getter para especie
    @property
    def especie(self):
        return self._especie
    
    # Setter para especie
    @especie.setter
    def especie(self, nueva_especie):
        especies_validas = ["perro", "gato", "ave", "pez", "roedor"]
        if nueva_especie.lower() in especies_validas:
            self._especie = nueva_especie.lower()
        else:
            print(f"Error: Especie no válida. Las opciones son: {', '.join(especies_validas)}")
    
    # Getter para edad
    @property
    def edad(self):
        return self._edad
    
    # Setter para edad
    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("Error: La edad debe ser un número entero positivo")
    
    def __str__(self):
        return f"{self.nombre} es un {self.especie} de {self.edad} años"


# Crear una instancia de Mascota
mi_mascota = Mascota("Firulais", "perro", 5)

# Usar los getters
print(mi_mascota.nombre)  # Output: Obteniendo nombre... \n Firulais
print(mi_mascota.especie) # Output: perro
print(mi_mascota.edad)    # Output: 5

# Usar los setters
mi_mascota.nombre = "Rex"      # Cambia el nombre
mi_mascota.nombre = ""         # Muestra error
mi_mascota.especie = "GATO"    # Cambia a minúsculas
mi_mascota.especie = "tigre"   # Muestra error
mi_mascota.edad = 6            # Cambia la edad
mi_mascota.edad = -1           # Muestra error

print(mi_mascota)  # Output: Rex es un gato de 6 años