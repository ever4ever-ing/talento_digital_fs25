# Solo una excursión
cupo = 2
reservas = []

print("Excursión: Parque Nacional Villarica")
print(f"Cupo disponible: {cupo}")

while len(reservas) < cupo:
    nombre = input("Ingrese su nombre para reservar: ")
    reservas.append(nombre)
    print("Reserva realizada.")
    print(f"Cupos restantes: {cupo - len(reservas)}")

print("Excursión llena. No se aceptan más reservas.")





"""
TIP1: USAR
while True:
    entrada = input("Elija excursión o 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break
"""


"""
TIP2:
excursiones = [
    {"nombre": "Parque Nacional Villarrica", "cupo": 2, "reservas": []},
    {"nombre": "Parque Nacional Conguillio", "cupo": 2, "reservas": []}
]
"""