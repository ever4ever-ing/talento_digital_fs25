cajonera = ["pantalones", "camisetas", "calcetines"]

print(cajonera[0]) #Accedemos al cajón con índice 0. Imprime: "pantalones"

print(cajonera[1]) #Accedemos al cajón con índice 1. Imprime: "camisetas"

print(cajonera[2]) #Accedemos al cajón con índice 2. Imprime: "calcetines"

camisetas = cajonera[1]

cajonera[1] = "sueters" #Cambiamos el valor del cajón con índice 1

print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines']

cajonera.append(camisetas)
print(cajonera)