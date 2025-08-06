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
        if self.salud <= 5:
            print(f"{self.nombre} está demasiado enfermo para jugar.")
            return self
        else:
            self.felicidad += 10
            self.salud -= 5
            print(
                f"{self.nombre} juega. Felicidad: {self.felicidad}, Salud: {self.salud}")
            return self

    def comer(self):
        """
        Incrementa la felicidad en 5, aumenta la salud en 10
        """
        self.felicidad += 5
        self.salud += 10
        print(
            f"{self.nombre} está comiendo! Felicidad: {self.felicidad}, Salud: {self.salud}")

    def curar(self):
        """
        Incrementa la salud en 20, disminuye la felicidad en 5
        """
        self.salud += 20
        self.felicidad -= 5
        print(
            f"{self.nombre} está siendo curado! Salud: {self.salud}, Felicidad: {self.felicidad}")

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

class Gozarutchi (Tamagotchi):
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=80):
        super().__init__(nombre, color, salud, felicidad, energia)
        self.tipo = "Gozarutchi"
        self.habilidad_especial = "Arrojar shuriken"
        self.clase_social = "Guerrero"
        self.inteligencia = 40

    def usar_habilidad_especial(self):
        print(f"{self.nombre} está usando su habilidad especial: {self.habilidad_especial}!")
        self.felicidad += 15
        self.energia -= 10
        print(
            f"Felicidad: {self.felicidad}, Energía: {self.energia}")