# Lista de excursiones (nombre y cupo) sin validaciones
#Esta version no incluye todas las validaciones
excursiones = [
    {"nombre": "Parque Nacional Villarrica", "cupo": 2, "reservas": []},
    {"nombre": "Parque Nacional Conguillio", "cupo": 2, "reservas": []}
]

while True:
    #MOSTRAMOS LOS CUPOS DISPONIBLES EN LOS PARQUES
    print("\nExcursiones disponibles:")
    for i, ex in enumerate(excursiones, 1):
        print(f"{i}. {ex['nombre']} (Cupos: {ex['cupo']} | Reservados: {len(ex['reservas'])})")

    entrada = input("\nElija excursión (número) o escriba 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break

    opcion = int(entrada)

    nombre = input("Ingrese su nombre: ")
    if len(excursiones[opcion-1]["reservas"]) < excursiones[opcion-1]["cupo"]:
        excursiones[opcion-1]["reservas"].append(nombre)
        print("Reserva realizada.")
    else:
        print("No hay cupos disponibles.")
