class Persona:
    def __init__(self, nombre, edad, tamagotchi=None):
        """
        Inicializa una Persona que puede tener un Tamagotchi
        """
        self.nombre = nombre
        self.edad = edad
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        """
        La persona juega con su Tamagotchi
        """
        if self.tamagotchi:
            print(f"{self.nombre} está jugando con {self.tamagotchi.nombre}")
            self.tamagotchi.jugar()
        else:
            print(f"{self.nombre} no tiene un Tamagotchi para jugar")

    def darle_comida(self):
        """
        La persona le da comida a su Tamagotchi
        """
        if self.tamagotchi:
            print(f"{self.nombre} le está dando comida a {self.tamagotchi.nombre}")
            self.tamagotchi.comer()
        else:
            print(f"{self.nombre} no tiene un Tamagotchi para alimentar")

    def curarlo(self):
        """
        La persona cura a su Tamagotchi
        """
        if self.tamagotchi:
            print(f"{self.nombre} está curando a {self.tamagotchi.nombre}")
            self.tamagotchi.curar()
        else:
            print(f"{self.nombre} no tiene un Tamagotchi para curar")
