class Tamagotchi:
    def __init__(self, nombre, color, salud, felicidad, energia):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia
    def jugar(self):
        if self.salud <= 5:
            print(f"{self.nombre} está demasiado enfermo para jugar.")
            return self
        else:
            self.felicidad += 10
            self.salud -= 5
            print(f"{self.nombre} juega. Felicidad: {self.felicidad}, Salud: {self.salud}")
            return self
    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} come. Felicidad: {self.felicidad}, Salud: {self.salud}")
        return self

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi
    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()
    def darle_comida(self):
        self.tamagotchi.comer()




# Métodos:

    # jugar_con_tamagotchi(): juega e invoca el método de tamagotchi jugar()
    # darle_comida(): le da de comer su tamagotchi invocando al método de tamagotchi comer()
    # curarlo(): sana las heridas de su tamagotchi invocando al método de tamagotchi curar()


# Métodos:
# jugar(): incrementa la felicidad el 10, disminuye la salud en 5
# comer(): incrementa la felicidad en 5, aumenta la salud en 10
# curar(): incrementa la saludo en 20, disminuye la felicidad en 5
