platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Chile": "Pastel de Choclo", "Perú": "Ceviche", "Argentina": "Asado"}

#Otra forma de iterar a través de las claves
print("-" * 20)
print("Iterando a través de las claves del diccionario:")
for clave in platillos_tipicos.keys():
    print(clave)

print("-" * 20)
print("Iterando a través de los valores del diccionario:")
#Otra forma de iterar a través de los valores

for valor in platillos_tipicos.values():
    print(valor)

print("-" * 20)
print("Iterando a través de las claves y valores del diccionario:")
for clave, valor in platillos_tipicos.items():
    print(clave, "=", valor)