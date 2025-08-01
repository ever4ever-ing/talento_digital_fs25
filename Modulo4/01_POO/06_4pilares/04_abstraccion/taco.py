class Taco:
    def __init__(self, guiso): 
        #encapsulamiento
        self.__guiso = guiso  # privado
        self.tortilla = "maiz"  # publico  
    @property # getter: permite acceso a datos
    def guiso(self):
        return self.__guiso
    @guiso.setter # setter: define atributo
    def guiso(self, nuevo_guiso):
        if not isinstance(nuevo_guiso, str):
            print("Error")
            raise ValueError("El guiso debe ser una cadena de texto")
        self.__guiso = nuevo_guiso
        
    def prepararlo(self):
        print(f"Haciendo un taco de {self.__guiso}")
        print("¡Calentando el taquito!")

    def servir(self):
        print("Tomamos un plato plano y colocamos el platillo")
        
class Enchilada(Taco):
   def __init__(self, guiso):
       super().__init__(guiso)
       self.salsa = "verde"

   def hacer_enchilada(self):
       super().prepararlo() #Herencia
       print("Agregamos la salsa a nuestro taco y ahora es enchilada")

   def servir(self): #polimorfismo
       print("Tomamos un plato grande, colocamos el platillo y adornamos con cilantro")

#Abstraccion   
class Comensal:
   def __init__(self, nombre):
       self.nombre = nombre
       self.taco = Taco("carne")
   def comer_taco(self):
       self.taco.prepararlo()
       self.taco.servir()
       print("Me como mi delicioso taco")