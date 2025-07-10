# Lista de excursiones (nombre y cupo)
excursiones = [
    {"nombre": "Parque Nacional Villarrica", "cupo": 2, "reservas": []},
    {"nombre": "Parque Nacional Conguillio", "cupo": 2, "reservas": []}
]

# Mostrar excursiones y reservar en bucle
while True:
    print("\nExcursiones disponibles:")
    for i, ex in enumerate(excursiones, 1):
        print(f"{i}. {ex['nombre']} (Cupos: {ex['cupo']} | Reservados: {len(ex['reservas'])})")
    entrada = input("\nElija excursión (número) o escriba 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break
    if not entrada.isdigit():
        print("Por favor, ingrese un número válido.")
        continue
    opcion = int(entrada)
    if opcion < 1 or opcion > len(excursiones):
        print("Opción inválida.")
        continue
    nombre = input("Ingrese su nombre: ")
    if len(excursiones[opcion-1]["reservas"]) < excursiones[opcion-1]["cupo"]:
        excursiones[opcion-1]["reservas"].append(nombre)
        print("Reserva realizada.")
    else:
        print("No hay cupos disponibles.")
