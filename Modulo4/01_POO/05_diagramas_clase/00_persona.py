class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def presentarse(self):
        print(f"\n Hola!, ¿cómo estás? Me llamo {self.nombre} {self.apellido}")


class Lenguaje:
    def __init__(self, nombre, esTipado):
        self.nombre = nombre
        self.esTipado = esTipado


class Programador(Persona):
    def __init__(self, nombre, apellido, lenguaje, esTipado):
        super().__init__(nombre, apellido)
        self.lenguajes = [Lenguaje(lenguaje, esTipado)]

    def agregar_lenguaje(self, lenguaje, esTipado):
        self.lenguajes.append(Lenguaje(lenguaje, esTipado))
    def mostrar_lenguajes(self):
        for lenguaje in self.lenguajes:
            print(lenguaje.nombre)