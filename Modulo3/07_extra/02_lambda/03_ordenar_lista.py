# Ejemplo 3: usar lambda con sorted para ordenar por la segunda letra
palabras = ['gato', 'perro', 'loro']
ordenadas = sorted(palabras, key=lambda x: x[1])
print(ordenadas) 