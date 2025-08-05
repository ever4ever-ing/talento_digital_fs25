class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=80):
        """
        Inicializa un Tamagotchi con valores por defecto para salud, felicidad y energía
        """
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia
    
    def jugar(self):
        """
        Incrementa la felicidad en 10, disminuye la salud en 5
        """
        self.felicidad += 10
        self.salud -= 5
        print(f"{self.nombre} está jugando! Felicidad: {self.felicidad}, Salud: {self.salud}")
    
    def comer(self):
        """
        Incrementa la felicidad en 5, aumenta la salud en 10
        """
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} está comiendo! Felicidad: {self.felicidad}, Salud: {self.salud}")
    
    def curar(self):
        """
        Incrementa la salud en 20, disminuye la felicidad en 5
        """
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} está siendo curado! Salud: {self.salud}, Felicidad: {self.felicidad}")
    
    def mostrar_estado(self):
        """
        Muestra el estado actual del Tamagotchi
        """
        print(f"\n=== Estado de {self.nombre} ===")
        print(f"Color: {self.color}")
        print(f"Salud: {self.salud}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Energía: {self.energia}")
        print("========================\n")


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


# Creando instancias y probando el funcionamiento
if __name__ == "__main__":
    # Crear una instancia de Tamagotchi
    mi_tamagotchi = Tamagotchi("Pikachu", "amarillo")
    
    # Crear una instancia de Persona y asignarle el Tamagotchi
    persona = Persona("Ana", 25, mi_tamagotchi)
    
    print(f"¡Hola! Soy {persona.nombre} y tengo {persona.edad} años.")
    print(f"Mi Tamagotchi se llama {persona.tamagotchi.nombre} y es de color {persona.tamagotchi.color}")
    
    # Mostrar estado inicial
    persona.tamagotchi.mostrar_estado()
    
    # La persona interactúa con su Tamagotchi
    print("=== Interacciones con el Tamagotchi ===")
    
    # Darle comida
    persona.darle_comida()
    
    # Jugar con él
    persona.jugar_con_tamagotchi()
    
    # Curarlo
    persona.curarlo()
    
    # Mostrar estado final
    persona.tamagotchi.mostrar_estado()
    
    # Más interacciones para ver los cambios
    print("=== Más interacciones ===")
    persona.jugar_con_tamagotchi()
    persona.darle_comida()
    persona.tamagotchi.mostrar_estado()