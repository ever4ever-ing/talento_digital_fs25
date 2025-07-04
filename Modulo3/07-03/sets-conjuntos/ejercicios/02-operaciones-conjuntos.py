"""
Ejercicio 2:
Dadas dos listas de números, encuentra:

-Los números comunes en ambas listas
-Los números únicos de cada lista

"""
lista1 = [1, 2, 3, 4, 5, 5]
lista2 = [4, 5, 6, 7, 8]
#transformacion
set1 = set(lista1)
set2 = set(lista2)
print("set1:",set1)
print("set2:",set2)
ambas = set1 & set2
unicos_lista1= set1 - set2
unicos_lista2 = set2 - set1
print("Los números comunes en ambas listas", ambas)
print("Únicamente en lista 1:", unicos_lista1)
print("Únicamente en lista 2:", unicos_lista2)
