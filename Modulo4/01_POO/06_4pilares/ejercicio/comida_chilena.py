from abc import ABC, abstractmethod
#clase abstracta es una clase que no puede ser instanciada directamente,
#sino que debe ser heredada por otras clases.
class ComidaChilena(ABC):
    def __init__(self, nombre, ingredientes):
        self.__nombre = nombre
        self.ingredientes = ingredientes
    @abstractmethod #metodo abstracto es un metodo que no tiene implementacion
    def preparar(self):
        pass
    @property #getters
    def nombre(self):
        return self.__nombre
    @nombre.setter #setters
    def nombre(self, value):
        self.__nombre = value
    @property #getters
    def ingredientes(self):
        return self._ingredientes
    @ingredientes.setter #setters
    def ingredientes(self, value):
        self._ingredientes = value

class Completo(ComidaChilena):
    def __init__(self):
        super().__init__("Completo", ["pan", "salchicha", "palta", "mayonesa", "tomate"])

    def preparar(self):
        super().preparar()
        print(f"Preparando {self.nombre}")

class CompletoItaliano(Completo):
    def __init__(self):
        super().__init__()
        self.nombre = "Completo Italiano"
        self.ingredientes.append(["palta", "mayonesa", "tomate"])
    def preparar(self):
        print("Preparando un completo italiano.")
        
mi_completo = CompletoItaliano()
mi_completo.preparar()
        
        

class PorotosConRienda(ComidaChilena):
    def __init__(self):
        super().__init__("Porotos con rienda", ["porotos", "choclo", "longaniza", "cebolla", "tallarines","zapallo", "merken", "ajo"])
    def preparar(self):
        super().preparar()
        print("Cocinando porotos con choclo, longaniza, cebolla, tallarines y zapallo.")
        
class PastelDeChoclo(ComidaChilena):
    def __init__(self):
        super().__init__("Pastel de choclo", ["choclo", "carne molida", "cebolla", "huevo duro", "aceitunas", "azúcar", "queso"])
    def preparar(self):
        super().preparar()
        print("Preparando pastel de choclo con carne molida, cebolla, huevo duro, aceitunas y azúcar.")
    
class Curanto(ComidaChilena):
    def __init__(self):
        super().__init__("Curanto", ["mariscos", "carne", "papas", "choclo", "almejas", "chorizo","nalca", "cilantro"])
    def preparar(self):
        super().preparar()
        print("Cocinando curanto con mariscos, carne, papas, choclo, almejas, chorizo, nalca y cilantro.")