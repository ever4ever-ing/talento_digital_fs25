class Taco:
    def __init__(self, guiso):
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
        
mi_taco = Taco("Al pastor")
nuevo_guiso = input("Ingresa tu guiso:")
mi_taco.guiso = nuevo_guiso # usando setter
print(f"El taco a preparar lleva: {mi_taco.guiso}") #getter