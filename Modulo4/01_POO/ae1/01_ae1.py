class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
    def ocupar(self):
        self.ocupada = True
    def liberar(self):
        self.ocupada = False

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.platos = []
    def agregar_plato(self, plato):
        self.platos.append(plato)
    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)
    
    
    
    
    
# Uso
mesa1 = Mesa(1, 4)# Creando objeto Mesa con número 1 y capacidad 4
plato1 = Plato("Hamburguesa", 8500)# Creando objeto Plato con nombre "Hamburguesa" y precio 8.5
plato2 = Plato("Ensalada", 5000)
mesa1.ocupar()# llamando al método ocupar
pedido1 = Pedido(mesa1)
pedido1.agregar_plato(plato1)#Recibe un objeto de clase Plato
pedido1.agregar_plato(plato2)
total = pedido1.calcular_total()
print(f"Total a pagar: ${total}")
mesa1.liberar()