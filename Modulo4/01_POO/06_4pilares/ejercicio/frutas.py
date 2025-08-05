"""
Herencia: 
Permite que una clase (hija) herede atributos y métodos de otra clase (padre), facilitando la reutilización de código.
Polimorfismo:
Permite que objetos de diferentes clases respondan de manera diferente al mismo mensaje (método).

"""
#Clase base

class Chile:
    def __init__(self, productos):
        self.productos = productos

class Flora(Chile):
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre


class Fruta(Flora):
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def describir(self):
        return f"Una {self.nombre} de color {self.color}"
    
    def sabor(self):
        return "Tiene un sabor genérico"
    
#Clase heredada de la clase base    
class Citricos(Fruta):
    def __init__(self, nombre, acidez):
        self.nombre = nombre
        self.acidez = acidez

    def sacar_jugo(self):
        print( f"{self.nombre} está transformado en jugo")

class Naranja(Citricos, Fruta):
    def __init__(self, nombre, color, dulzor, origen):
        super().__init__(nombre, color)
        self.dulzor = dulzor
        self.origen = origen
    
    def sabor(self):
        return "Tiene sabor citrico "

class toronja (Citricos, Fruta):
    def __init__(self, nombre, acidez, ph):
        super().__init__(nombre, acidez)
        self.acidez = acidez
        self.ph = ph

class Mandarina(Citricos, Fruta):
    def __init__(self, nombre, acidez):
        self.nombre = nombre
        self.acidez = acidez

    def pelar(self):
        return f"Sacándole cáscaara a {self.nombre}"

class Papaya(Fruta):
    def __init__(self, nombre, color, dulzor):
        self.nombre = nombre
        self.color = color
        self.dulzor = dulzor


pomelo = Citricos("pomelo", "mucha") 
print(pomelo.sacar_jugo())


mi_naranja =Naranja("naranja","naranja xd",True,"Chile")
print(mi_naranja.sabor())