# Programa para iterar sobre una lista de volcanes chilenos

# Lista simple de volcanes de Chile
volcanes = ["Villarrica", "Osorno", "Llaima", "Lonquimay", "Calbuco", "Puntiagudo", "Descabezado Grande", "Nevados de Chillán"]


print("===== Listado de volcanes chilenos =====")
# Método 1: Iteración básica con bucle for
print("\n1. Iteración con bucle for tradicional:")
for volcan in volcanes:
    print(f"Volcán: {volcan}")

# Método 2: Iteración con índices
print("\n2. Iteración con índices:")
for i in range(len(volcanes)):
    print(f"{i+1}. {volcanes[i]}")

# Método 3: Iteración con enumerate
print("\n3. Iteración con enumerate:")
for i, v in enumerate(volcanes):
    print(i, v)

# Método 4: Filtrar volcanes que empiezan con 'P'
print("\n4. Solo volcanes que empiezan con 'P':")
volcanes_con_p = [v for v in volcanes if v.startswith("P")]
for volcan in volcanes_con_p:
    print(f"Volcán que empieza con P: {volcan}")

# Método 5: Agrupar volcanes por la primera letra
print("\n5. Volcanes agrupados por primera letra:")
letras = {}
for volcan in volcanes:
    primera_letra = volcan[0]
    if primera_letra not in letras:
        letras[primera_letra] = []
    letras[primera_letra].append(volcan)

for letra, lista_volcanes in letras.items():
    volcanes_str = ", ".join(lista_volcanes)
    print(f"Letra {letra}: {volcanes_str}")

# Método 5: Usar while para iterar
print("\n6. Iteración con bucle while:")
i = 0
while i < len(volcanes):
    print(f"Volcán {i+1}: {volcanes[i]}")
    i += 1

# Método 7: Encontrar el volcán más largo (nombre)
print("\n7. El volcán con el nombre más largo:")
volcan_mas_largo = max(volcanes, key=len)
print(f"El volcán con el nombre más largo es {volcan_mas_largo} con {len(volcan_mas_largo)} letras.")

# Método 8: Ordenar volcanes alfabéticamente
print("\n8. Volcanes ordenados alfabéticamente:")
volcanes_ordenados = sorted(volcanes)
for volcan in volcanes_ordenados:
    print(f"- {volcan}")
