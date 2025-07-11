# Programa para iterar sobre un diccionario de parques nacionales chilenos
"""
Diferentes métodos para iterar sobre diccionarios:
Iteración sobre claves (.keys()): Recorre los nombres de los parques

Iteración sobre valores (.values()): Recorre la información de cada parque sin saber sus nombres

Iteración sobre pares clave-valor (.items()): Recorre nombres y datos a la vez

Iteración anidada: Muestra cómo acceder a las listas dentro del diccionario (características de cada parque)

Filtrado con comprensión de diccionarios: Filtra parques con más de 100,000 visitantes

Cálculo de estadísticas:

Superficie total protegida
Total de visitantes anuales
Parque más antiguo
Parque más grande
Uso de get(): Demuestra cómo acceder de forma segura a claves que podrían no existir en el diccionario

Agrupación por región: Reorganiza los datos para agrupar parques por su región

"""
# Diccionario de parques nacionales de Chile
parques_nacionales = {
    "Torres del Paine": {
        "region": "Magallanes",
        "superficie": 227298,  # hectáreas
        "año_creacion": 1959,
        "caracteristicas": ["montañas", "lagos", "glaciares", "fauna"],
        "visitantes_anuales": 252000
    },
    "Conguillío": {
        "region": "Araucanía",
        "superficie": 60832,  # hectáreas
        "año_creacion": 1950,
        "caracteristicas": ["volcán Llaima", "araucarias", "lagos", "bosques"],
        "visitantes_anuales": 132000
    },
    "Pan de Azúcar": {
        "region": "Atacama",
        "superficie": 43754,  # hectáreas
        "año_creacion": 1985,
        "caracteristicas": ["desierto", "costa", "fauna marina", "cactus"],
        "visitantes_anuales": 35000
    },
    "Vicente Pérez Rosales": {
        "region": "Los Lagos",
        "superficie": 253780,  # hectáreas
        "año_creacion": 1926,
        "caracteristicas": ["volcán Osorno", "lago Todos los Santos", "saltos del Petrohué", "bosques"],
        "visitantes_anuales": 400000
    },
    "Rapa Nui": {
        "region": "Valparaíso (Isla de Pascua)",
        "superficie": 7130,  # hectáreas
        "año_creacion": 1935,
        "caracteristicas": ["moáis", "cráteres volcánicos", "cultura polinésica", "arqueología"],
        "visitantes_anuales": 120000
    },
    "Lauca": {
        "region": "Arica y Parinacota",
        "superficie": 137883,  # hectáreas
        "año_creacion": 1970,
        "caracteristicas": ["altiplano", "lagos", "fauna andina", "volcanes"],
        "visitantes_anuales": 45000
    }
}

print("===== Parques Nacionales de Chile =====")

# Método 1: Iteración básica sobre las claves (nombres de parques)
print("\n1. Lista de parques nacionales:")
for nombre_parque in parques_nacionales.keys():
    print(f"- {nombre_parque}")

# Método 2: Iteración sobre valores
print("\n2. Información detallada de cada parque:")
for info_parque in parques_nacionales.values():
    print(f"Parque en región de {info_parque['region']} - {info_parque['superficie']} hectáreas")

# Método 3: Iteración sobre pares clave-valor
print("\n3. Nombres y año de creación:")
for nombre, info in parques_nacionales.items():
    print(f"{nombre} - Fundado en {info['año_creacion']}")

# Método 4: Iteración anidada para acceder a listas dentro del diccionario
print("\n4. Características principales de cada parque:")
for nombre, info in parques_nacionales.items():
    print(f"{nombre}:")
    for caracteristica in info["caracteristicas"]:
        print(f"  - {caracteristica}")

        # Ejemplo: Acceder a la región de cada parque
        print("\nAcceso a la región de cada parque:")
        for nombre, info in parques_nacionales.items():
            print(f"{nombre} está en la región de {info['region']}")

# Método 5: Filtrado de parques por criterio (más de 100,000 visitantes)
print("\n5. Parques con más de 100,000 visitantes anuales:")
parques_populares = {nombre: info for nombre, info in parques_nacionales.items() 
                    if info["visitantes_anuales"] > 100000}

for nombre, info in parques_populares.items():
    print(f"{nombre} - {info['visitantes_anuales']} visitantes al año")

# Método 6: Cálculo de estadísticas
print("\n6. Estadísticas:")
total_superficie = sum(info["superficie"] for info in parques_nacionales.values())
total_visitantes = sum(info["visitantes_anuales"] for info in parques_nacionales.values())
parque_mas_antiguo = min(parques_nacionales.items(), key=lambda x: x[1]["año_creacion"])
parque_mas_grande = max(parques_nacionales.items(), key=lambda x: x[1]["superficie"])

print(f"Superficie total protegida: {total_superficie} hectáreas")
print(f"Total de visitantes anuales: {total_visitantes}")
print(f"Parque más antiguo: {parque_mas_antiguo[0]} ({parque_mas_antiguo[1]['año_creacion']})")
print(f"Parque más grande: {parque_mas_grande[0]} ({parque_mas_grande[1]['superficie']} hectáreas)")

# Método 7: Uso de get() para acceso seguro
print("\n7. Acceso seguro a datos con get():")
for nombre in ["Torres del Paine", "El Morado", "Conguillío"]:
    # get() devuelve None o un valor por defecto si la clave no existe
    parque = parques_nacionales.get(nombre, {"region": "No encontrado", "año_creacion": "N/A"})
    print(f"{nombre} - Región: {parque['region']} - Año: {parque.get('año_creacion', 'No disponible')}")

# Método 8: Agrupación por región
print("\n8. Parques agrupados por región:")
parques_por_region = {}
for nombre, info in parques_nacionales.items():
    region = info["region"]
    if region not in parques_por_region:
        parques_por_region[region] = []
    parques_por_region[region].append(nombre)

for region, lista_parques in parques_por_region.items():
    parques_str = ", ".join(lista_parques)
    print(f"Región de {region}: {parques_str}")
