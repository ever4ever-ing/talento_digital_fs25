from Tarjeta import TarjetaCredito
class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.tarjeta = TarjetaCredito(0, 20000, 0.015) #Instancia de TarjetaCredito con saldo inicial 0,
       #limite 20000 y tasa de interes 0.015

miyagi = Usuario("Naruyashi", "Miyagi", "karate@gmail.com")
miyagi.tarjeta.hacer_compra(5000)  # Realiza una compra de 5000
print(f"Saldo a pagar de {miyagi.nombre} {miyagi.apellido}: {miyagi.tarjeta.saldo_pagar}")