class Animal:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.velocidad = 0
    def hacer_truco(self):
        print(f"{self.nombre} realiza un truco")
    def desplazarse(self, velocidad):
        self.velocidad = velocidad
        print(f"Animal desplazandose a {self.velocidad} Km/h") 
class Perro(Animal):
    def __init__(self, nombre, edad, color, raza, tamaño,vacunas,pedigree):
        super().__init__(nombre,edad,color)
        self.raza = raza
        self.tamaño = tamaño
        self.vacunas = vacunas
        self.pedigree = pedigree
    
    def buscar_pelota(self):
        velocidad = 30 #km/h
        super().desplazarse(velocidad)
        print(f'{self.nombre} encontró la pelota')
        
    def hacer_truco(self):
        self.buscar_pelota()
        
class Gato(Animal):
    def __init__(self, nombre, edad, color, tipo_pelaje):
        # Llama al constructor de la clase base Animal
        super().__init__(nombre, edad, color)
        self.tipo_pelaje = tipo_pelaje

    def rascar_sofa(self):
        print(f'{self.nombre} está rascando el sofá de su casa')

    def hacer_truco(self):
        print(f"{self.nombre} te ignora un momento")
        print(f"{self.nombre} se estira, se lame, rompe una taza")
        #print(f"{self.nombre} realiza un truco")
        super().hacer_truco()

gato1 = Gato("Michi", 3, "Gris", "Corto")
gato1.hacer_truco()
gato1.rascar_sofa()
print(isinstance(gato1, Animal))
print(isinstance(gato1, Gato))


perro1 = Perro("Firulais", 5, "Marrón", "Labrador", "Grande", True, True)
perro1.hacer_truco()
perro1.buscar_pelota()
