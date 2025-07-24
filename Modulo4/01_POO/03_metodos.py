class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):  # recibe como argumento el monto de la compra
        self.saldo_pagar += monto
        return self # permite el encadenamiento de métodos, devuelve todo el objeto Usuario
    def mostrar_saldo(self):
        print(f"Saldo a pagar de {self.nombre}: {self.saldo_pagar}")
        return self # devuelve el saldo a pagar del usuario

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")

daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
lista = list()
dict = dict()

print(miyagi.nombre)  # Imprime: Nariyoshi
print(daniel.nombre)  # Imprime: Nariyoshi

miyagi.hacer_compra(1000).hacer_compra(5000).mostrar_saldo()  # Miyagi hace una compra de 1000 y otra de 5000

