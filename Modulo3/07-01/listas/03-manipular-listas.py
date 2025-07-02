cajonera = ["pantalones", "camisetas", "calcetines"]
camisetas = cajonera[1]
cajonera[1] = "sueters" #Cambiamos el valor del cajón con índice 1
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines']
cajonera.append(camisetas)
print(cajonera)
cajonera.insert(1,"vestidos")
cajonera.insert(4,"vestidos") # Inserta en una posicion un elemento
print(cajonera)
cajonera.remove("vestidos") #Elimina la primera ocurrencia
print(cajonera)
cajonera.pop(3)
print(cajonera)
lista_compras = ['botas', 'bufanda', 'guantes']
cajonera.append(lista_compras)
print(cajonera)
print(lista_compras[2])
print(cajonera[4])
print(type(lista_compras[2]))
cajonera[4].remove("guantes") #Eliminando un elemento de la lista de compras dentro de cajonera
print(cajonera)
#print(cajonera)
cajonera[4].insert(1,"paraguas")
print(cajonera)
