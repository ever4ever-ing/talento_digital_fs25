import datetime
numeros = [1, 2, "tres"]
# 1. append() - Añadir al final
numeros.append(4)
print(numeros)
# 2. extend() - Añadir múltiples elementos
numeros.extend([5, 6])
print(numeros)
# 3. insert() - Insertar en una posición
numeros.insert(0,0)
print(numeros)
# 4. remove() - Eliminar por valor
tres = numeros.remove("tres") #no permite recuperar
print(numeros)
print(tres)
# 5. pop() - Eliminar por índice y obtener el valor
ultimo_elemento = numeros.pop() #permite recuperar
print(numeros)
penultimo_elemento = numeros.pop(-2)
print(ultimo_elemento)
print(penultimo_elemento)
print(numeros)
# 6. index() - Encontrar la posición de un valor
variable = numeros.index(5)
print(variable)
# 7. sort() - Ordenar (modifica la lista original)
desordenada = [3, 1, 4, 1, 5, 9, 2]
desordenada.sort()
print(desordenada)
# 8. reverse() - Invertir (modifica la lista original)
desordenada.reverse()
print(desordenada)
# 9. copy() - Crear una copia independiente
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(original)
print(copia)



