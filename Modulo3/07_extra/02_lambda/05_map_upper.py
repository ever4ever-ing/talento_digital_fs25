# Ejemplo 5: usar lambda con map para convertir a mayúsculas
nombres = ['ana', 'juan', 'luis']
mayusculas = list(map(lambda x: x.upper(), nombres))
print(mayusculas)  # Salida: ['ANA', 'JUAN', 'LUIS']

"""
Map permite aplicar un función a cada elemento de un tipo de dato iterable.
"""