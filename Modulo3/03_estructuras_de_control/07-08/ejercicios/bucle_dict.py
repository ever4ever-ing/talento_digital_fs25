santiago = {
    "nombre": "Santiago", 
    "region": "Metropolitana", 
    "poblacion": 5614000, 
    "altitud": 570,  # metros sobre el nivel del mar
    "fundacion": 1541  # año de fundación
}

print("-"*20)
#ITERACIÓN A TRAVÉS DE LAS CLAVES
for clave in santiago:
    print(clave)
print("-"*10)
for clave in santiago.keys():
    print(clave)

print("-"*20)
#ITERACION A TRAVÉS DE LOS VALORES
for valor in santiago.values():
    print(valor)

print("-"*20)
#ITERACIÓN A TRAVÉS DE CLAVES Y VALORES (ITEMS)
for clave, valor in santiago.items():
    print(f"{clave}: {valor}")