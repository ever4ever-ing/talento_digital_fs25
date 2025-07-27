class TarjetaCredito:

   #Declaramos un atributo de clase que se comparte entre todas las instancias de la clase

   banco = "Banco Internacional de Programadores"

   def __init__(self):
       pass
   
tarjeta_de_miyagi = TarjetaCredito()
tarjeta_de_daniel = TarjetaCredito()
tarjeta_de_miyagi.banco = "Banco Nacional de Python"
print(tarjeta_de_miyagi.banco) #Imprime: Banco Nacional de Python
print(tarjeta_de_daniel.banco) #Imprime: Banco Internacional de Programadores
print("-"*30)
TarjetaCredito.banco = "Banco Comercial de Desarrolladores"
print(tarjeta_de_miyagi.banco) #Imprime: Banco Nacional de Python
print(tarjeta_de_daniel.banco) #Imprime: Banco Comercial de Desarrolladores
tarjeta_jackie = TarjetaCredito()
print(tarjeta_jackie.banco) 