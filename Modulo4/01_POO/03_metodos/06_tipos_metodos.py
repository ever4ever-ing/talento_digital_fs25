class Mascota:
    especies_permitidas = ["perro", "gato", "ave", "pez", "roedor","reptil", "anfibio"]
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def describir(self):
        return f"{self.nombre} es un {self.especie} de {self.edad} años"
    @classmethod
    def crear_perro(cls, nombre, edad):
        return cls(nombre, "perro", edad)
    @classmethod
    def crear_gato(cls, nombre, edad):
        return cls(nombre, "gato", edad)
    @staticmethod
    def es_especie_valida(especie):
        return especie.lower() in Mascota.especies_permitidas
    @staticmethod
    def edad_humana(especie, edad_mascota):
        if especie == "perro":
            if edad_mascota ==  1:
                return 15
            elif edad_mascota==2:
                return 24
            elif edad_mascota > 2:
                return 24 + (edad_mascota - 2) * 5
            
        elif especie == "gato":
            return edad_mascota * 5
        else:
            return edad_mascota * 3
        
"""
Primer año: 15 años humanos (aproximadamente) 
Segundo año: 9 años humanos adicionales (totalizando 24 años humanos) 
A partir del tercer año: Cada año canino equivale a 4-5 años humanos, dependiendo de la raza y tamaño.
"""

mi_perro = Mascota.crear_perro("Rex", 3)
mi_gato = Mascota.crear_gato("Misi", 2)

print(mi_perro.describir())  # Rex es un perro de 3 años
print(mi_gato.describir())   # Misi es un gato de 2 años

# Uso de métodos estáticos
print(Mascota.es_especie_valida("pez"))     # True
print(Mascota.es_especie_valida("reptil"))  # True
print(Mascota.es_especie_valida("Marsupial"))

print(f"Edad humana de Rex: {Mascota.edad_humana('perro', 3)}")  # 21
print(f"Edad humana de Misi: {Mascota.edad_humana('gato', 2)}")   # 10

# También podemos usar los métodos estáticos desde instancias
print(mi_perro.es_especie_valida("ave"))  # True
print(mi_gato.edad_humana("gato", 5))     # 25