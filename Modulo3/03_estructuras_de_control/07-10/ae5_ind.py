# Estructuras de datos originales
print("=== Estructuras de datos originales ===")

matriz = [[10, 15, 20], [3, 7, 14]]
print(f"\nMatriz original: {matriz}")

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
print(f"\nCantantes originales: {cantantes}")

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
print(f"\nCiudades originales: {ciudades}")

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
print(f"\nCoordenadas originales: {coordenadas}")

# 1. Cambiar el valor 3 en matriz por 6
matriz[1][0] = 6
print(f"Matriz modificada: {matriz}")

# 2. Cambiar el nombre del primer cantante por "Enrique Martin Morales"
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(f"\nCantantes modificados: {cantantes}")

# 3. En el diccionario ciudades, reemplazar "Cancún" por "Monterrey"
ciudades["México"][2] = "Monterrey"
print(f"\nCiudades modificadas: {ciudades}")

# 4. En la lista coordenadas, cambiar el valor de "latitud" por 9.9355431
coordenadas[0]["latitud"] = 9.9355431
print(f"\nCoordenadas modificadas: {coordenadas}")

# 2
print("\n=== Lista de cantantes ===")
for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

# 3
print("\n=== Nombres de cantantes ===")
for cantante in cantantes:
    print(cantante["nombre"])

print("\n=== Países de cantantes ===")
for cantante in cantantes:
    print(cantante["pais"])

# 4
print("\n=== Recorrer diccionario con listas como valores ===")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave, valor in costa_rica.items():
    print(len(valor), clave.upper())
    for i in valor:
        print(i)