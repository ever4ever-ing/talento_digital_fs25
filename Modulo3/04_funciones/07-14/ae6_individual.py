cantantes = [
    {"nombre": "Ricky Martin",      "pais": "Puerto Rico"},
    {"nombre": "Chayanne",          "pais": "Puerto Rico"},
    {"nombre": "José José",         "pais": "México"},
    {"nombre": "Juan Luis Guerra",  "pais": "República Dominicana"}
]

# 2 Iterar


def iterarDiccionario(cantantes):
    print("\n=== Nombres de cantantes ===")
    for cantante in cantantes:
        print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

# iterarDiccionario(cantantes)


def iterarDiccionario_v2(lista):
    for diccionario in lista:
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")


iterarDiccionario_v2(cantantes)

# 3 Obtener valores de una lista de diccionarios

# 3.1. Usando un bucle for, operador in, y condicional if


def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])  # Accedo al valor asociado a la llave
        else:
            print(f"La llave '{llave}' no existe.")

# Pregunta1: Como iterar una lista?R: for diccionario in lista:
# Pregunta2: Como evaluo si la llave existe en el diccionario? R: Condicional if


print("-"*30)
iterarDiccionario2("nombre", cantantes)
print("-"*10)
iterarDiccionario2("pais", cantantes)
print("-"*30)

# 3.2. Usando un bucle for y el método get()


def iterarDiccionario3(llave, lista):
    for elemento in lista:
        valor = elemento.get(llave)
        if valor is not None:
            print(valor)
        else:
            print(f"La llave '{llave}' no existe en el diccionario.")


# 3.3. Usando una comprensión de lista
def iterarDiccionario4(llave, lista):
    valores = [x[llave] for x in lista if llave in x]
    for valor in valores:
        print(valor)

# 3.4. Usando un bucle for con manejo de excepciones


def iterarDiccionario5(llave, lista):
    for x in lista:
        try:
            print(x[llave])
        except KeyError:
            print("Llave no encontrada")


# 4 Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, valor in diccionario.items():
        print(len(valor), clave.upper())
        for i in valor:
            print(i)

costa_rica = {

    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

chile = {
    "ciudades": ["Santiago", "Concepción", "Valparaíso"],
    "comidas": ["empanada", "pastel de choclo", "asado"]
}
imprimirInformacion(costa_rica)

print("-"*40)

def imprimirInformacion_j(diccionario):
    for clave, valor in costa_rica.items():
        print("\n"+f"{len(valor)} {clave.upper()}")
        for lista in valor:
            print(lista)

imprimirInformacion_j(chile)
print("-"*40)
def imprimirInformacion_v(diccionario):
    for clave, valor in diccionario.items():
        print(len(valor),clave.upper())
        for elemento in valor:
            print(elemento.capitalize())
imprimirInformacion_v(chile)