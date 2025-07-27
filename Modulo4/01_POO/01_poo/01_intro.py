#Auto
"""
Carro:
Atributos: marca, modelo, color.
"""
class Auto:
    #metodo constructor
    def __init__(self, marca, modelo, color): 
        self.marca = marca
        self.modelo = modelo
        self.color = color
    #metodos
    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")
        if(self.marca == "Toyota"):
            print("Bruuuuuum!")
        elif(self.marca == "Audi"):
            print("Niuuuuuuuum!")
    def frenar(self):
        print(f"{self.marca} {self.modelo} está frenando.")
    def encender_luces(self):
        print(f"Luces de {self.marca} {self.modelo} encendidas.")

mi_auto_1 = Auto("Toyota","Corolla","Gris")
mi_auto_2 = Auto("Audi","R8","Negro")

print(type(mi_auto_1)) #Inspeccionando clase
mi_auto_1.acelerar() #Llamando al método acelerar
print("Es de color:",mi_auto_1.color) #Accediendo a un atributo

print("-"*20)
mi_auto_2.acelerar()
mi_auto_2.encender_luces()

#Celular

class Celular:
    #Constructor
    def __init__(self, marca, tamano_pantalla, capacidad_almacenamiento):
        self.marca = marca
        self.tamano_pantalla = tamano_pantalla
        self.capacidad_almacenamiento = capacidad_almacenamiento
    #Métodos
    def llamar(self, numero):
        print(f"Llamando al {numero} desde {self.marca}.")
    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero}: {mensaje}")
    def tomar_foto(self, capacidad_almacenamiento):
        if capacidad_almacenamiento > 0:
            print(f"Tomando foto con {self.marca}.")
        else:
            print(f"No hay suficiente espacio en {self.marca} para tomar la foto.")
    def programar_alarma(self,hora):
        print(f"Alarma programada en {self.marca}. Hora: {hora}")
    def desbloquear(self,huella):
        if huella:
            print(f"{self.marca} desbloqueado con huella.")
        else:
            print(f"{self.marca} no se pudo desbloquear. Huella no reconocida.")

print("-"*20)
mi_celular = Celular("Samsung", "6.5 pulgadas", "128GB")#instancia de la clase Celular
mi_celular.llamar("923456789")
mi_celular.programar_alarma("08:00 AM")
mi_celular.desbloquear(True)







#Persona


#Usuario






"""



Métodos: acelerar, frenar, encender luces.

Celular:

Atributos: marca, tamaño de pantalla, capacidad de almacenamiento.

Métodos: llamar, enviar mensajes, tomar fotos.

Usuario en una aplicación:

Atributos: nombre, correo electrónico, contraseña.

Métodos: iniciar sesión, publicar un comentario, editar perfil.
"""