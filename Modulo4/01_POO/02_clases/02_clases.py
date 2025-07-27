class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):  # recibe como argumento el monto de la compra
        self.saldo_pagar += monto

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")

daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
lista = list()
dict = dict()

print(miyagi.nombre)  # Imprime: Nariyoshi
print(daniel.nombre)  # Imprime: Nariyoshi

miyagi.hacer_compra(1000)  # Miyagi hace una compra de 1000
miyagi.hacer_compra(5000)  # Miyagi hace otra compra de 5000
print(miyagi.saldo_pagar)  # Imprime: 6000

daniel.hacer_compra(2000)  # Daniel hace una compra de 2000
print(daniel.saldo_pagar)  # Imprime: 2000