#Ejercicio_1.Acceder a los todos los elementos iterando sobre la lista
ciudades_principales = ["Santiago", "Valparaíso", "Concepción", "La Serena", "Antofagasta", "Temuco", "Valdivia", "Puerto Montt"]
#Solucion:
for ciudad in range(len(ciudades_principales)):
    print(ciudad, ciudades_principales[ciudad])

print("-"*20)
for ciudad in ciudades_principales:
    print(ciudad)

#3. ITERACIÓN CON ENUMERATE
for indice, ciudad in enumerate(ciudades_principales):
    print(f"Ciudad en el índice {indice}: {ciudad}")

#4. COMBINAR LISTAS:
print("-"*20)
poblaciones = [5614, 296, 216, 334, 221, 175, 150, 123]
ciudades = ["Santiago", "Valparaíso", "Concepción", "Viña del Mar",
            "La Serena", "Temuco", "Rancagua", "Punta Arenas"]

# Creamos una nueva lista con las poblaciones convertidas a millones
poblaciones_en_millones = [poblacion / 1000 for poblacion in poblaciones]

print("Población de ciudades chilenas:")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}: {poblaciones[i]:,} habitantes ({poblaciones_en_millones[i]:.2f} millones)".replace(",", "."))