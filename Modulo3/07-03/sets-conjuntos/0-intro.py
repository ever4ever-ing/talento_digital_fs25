"""
SETS (CONJUNTOS)
- Se crean con {}
- Son una estructura de datos que permite almacenar elementos únicos y no ordenados.
- Son mutables.
- Optimizados para operaciones de pertenencia.
"""

mi_set = set()
mi_set2 = {} # Esto no es un set
print(type(mi_set2))
print(type(mi_set))

frutas = {"manzana","mango","platano","palta","naranja"}

fruta= {"manzana": 1, "naranja": 3}# Esto es diccionario con clave-valor
print(frutas)

#Añadiendo elementos
#No puedes predecir en qué posición quedará almacenado.
frutas.add("kiwi")
print(frutas)
frutas.add("manzana")
print(frutas)
""" 
Los sets están implementados con una tabla hash, lo que los hace muy eficientes para verificar si un elemento existe (if x in mi_set es muy rápido), pero no conservan el orden de inserción.
"""
#Eliminar elementos:
frutas.remove("platano")
print(frutas) 
#frutas.remove("papaya")  # Lanza KeyError si no existe
print(frutas)
frutas.discard("piña") # No lanza error si no existe
print(frutas)
