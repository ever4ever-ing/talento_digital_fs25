# Programa para iterar sobre una lista de volcanes chilenos

# Lista de volcanes de Chile
volcanes = [
    {"nombre": "Villarrica", "altura": 2847, "region": "Araucanía", "activo": True},
    {"nombre": "Osorno", "altura": 2652, "region": "Los Lagos", "activo": True},
    {"nombre": "Llaima", "altura": 3125, "region": "Araucanía", "activo": True},
    {"nombre": "Lonquimay", "altura": 2865, "region": "Araucanía", "activo": True},
    {"nombre": "Calbuco", "altura": 2003, "region": "Los Lagos", "activo": True},
    {"nombre": "Puntiagudo", "altura": 2190, "region": "Los Lagos", "activo": False},
    {"nombre": "Descabezado Grande", "altura": 3953, "region": "Maule", "activo": True},
    {"nombre": "Nevados de Chillán", "altura": 3212, "region": "Ñuble", "activo": True}
]

print("===== Listado de volcanes chilenos =====")

# Método 1: Iteración básica con bucle for
print("\n1. Iteración con bucle for tradicional:")
for volcan in volcanes:
    print(f"El volcán {volcan['nombre']} tiene una altura de {volcan['altura']} metros.")

# Método 2: Iteración con índices
print("\n2. Iteración con índices:")
for i in range(len(volcanes)):
    volcan = volcanes[i]
    print(f"{i+1}. {volcan['nombre']} - Ubicado en la región de {volcan['region']}")

# Método 3: Iteración con enumerate
print("\n3. Iteración con enumerate:")
for indice, volcan in enumerate(volcanes):
    estado = "activo" if volcan["activo"] else "inactivo"
    print(f"Volcán #{indice+1}: {volcan['nombre']} - Estado: {estado}")

# Método 4: Filtrar volcanes activos
print("\n4. Solo volcanes activos:")
volcanes_activos = [v for v in volcanes if v["activo"]]
for volcan in volcanes_activos:
    print(f"El volcán {volcan['nombre']} está activo y tiene {volcan['altura']} metros de altura.")

# Método 5: Agrupar volcanes por región
print("\n5. Volcanes agrupados por región:")
regiones = {}
for volcan in volcanes:
    region = volcan["region"]
    if region not in regiones:
        regiones[region] = []
    regiones[region].append(volcan["nombre"])

for region, lista_volcanes in regiones.items():
    volcanes_str = ", ".join(lista_volcanes)
    print(f"Región de {region}: {volcanes_str}")

# Método 6: Usar while para iterar
print("\n6. Iteración con bucle while:")
i = 0
while i < len(volcanes):
    volcan = volcanes[i]
    print(f"Volcán: {volcan['nombre']} - Altura: {volcan['altura']} metros")
    i += 1

# Método 7: Encontrar el volcán más alto
print("\n7. El volcán más alto:")
volcan_mas_alto = max(volcanes, key=lambda x: x["altura"])
print(f"El volcán más alto es {volcan_mas_alto['nombre']} con {volcan_mas_alto['altura']} metros.")

# Método 8: Ordenar volcanes por altura (de mayor a menor)
print("\n8. Volcanes ordenados por altura (de mayor a menor):")
volcanes_ordenados = sorted(volcanes, key=lambda x: x["altura"], reverse=True)
for volcan in volcanes_ordenados:
    print(f"{volcan['nombre']} - {volcan['altura']} metros")
