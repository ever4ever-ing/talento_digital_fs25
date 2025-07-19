from funciones_mejoradas import (registrar_cita, mostrar_historial, verificar_disponibilidad, mostrar_horarios_disponibles, cancelar_cita, mostrar_citas_del_dia)

# Paso 1: Definición de variables
citas = []
historial = {}
horarios_posibles = ["10:00", "11:00", "12:00", "13:00"]

# Paso 2: Menu de opciones
while True:
    print("\n" + "="*40)
    print("VetCare - Sistema de Gestión de Citas")
    print("="*40)
    print("1. Ver horarios disponibles")
    print("2. Registrar nueva cita")
    print("3. Mostrar historial de mascota")
    print("4. Ver citas del día")
    print("5. Cancelar cita")
    print("6. Salir")
    print("="*40)
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == '1':
        fecha = input("\nIngrese la fecha para consultar (dd/mm/yy): ")
        horarios_disponibles = mostrar_horarios_disponibles(
            citas, fecha, horarios_posibles)

        print(f"\nHorarios disponibles para el {fecha}:")
        if horarios_disponibles:
            for horario in horarios_disponibles:
                print(f"✓ {horario}")
        else:
            print("No hay horarios disponibles para esta fecha")

    elif opcion == '2':
        print("\nRegistro de nueva cita")
        print("-" * 30)

        # Solicitar datos de la cita
        id = input("Ingrese el ID de la mascota: ")
        nombre = input("Nombre de la mascota: ")
        fecha = input("Ingrese la fecha (dd/mm/yy): ")

        # Mostrar horarios disponibles antes de pedir el horario
        horarios_disponibles = mostrar_horarios_disponibles(
            citas, fecha, horarios_posibles)

        if not horarios_disponibles:
            print("No hay horarios disponibles para esta fecha. Intente con otra fecha.")
            continue

        print(f"\nHorarios disponibles para el {fecha}:")
        for i, horario in enumerate(horarios_disponibles, 1):
            print(f"{i}. {horario}")

        try:
            seleccion = int(
                input("\nSeleccione el número del horario deseado: ")) - 1
            if 0 <= seleccion < len(horarios_disponibles):
                horario = horarios_disponibles[seleccion]
            else:
                print("Selección inválida")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido")
            continue

        motivo = input("Ingrese motivo (urgencia, consulta, control): ")
        tutor = input("Ingrese el nombre del tutor: ")

        # Registrar la cita
        registrar_cita(citas, historial, id, nombre,
                        fecha, motivo, tutor, horario)

    elif opcion == '3':
        id_mascota = input("\nIngrese el ID de la mascota: ")
        mostrar_historial(historial, id_mascota)

    elif opcion == '4':
        fecha = input("\nIngrese la fecha a consultar (dd/mm/yy): ")
        mostrar_citas_del_dia(citas, fecha)

    elif opcion == '5':
        print("\nCancelar cita")
        print("-" * 20)
        id_mascota = input("Ingrese el ID de la mascota: ")
        fecha = input("Ingrese la fecha de la cita (dd/mm/yy): ")
        horario = input("Ingrese el horario de la cita: ")

        cancelar_cita(citas, historial, id_mascota, fecha, horario)

    elif opcion == "6":
        print("\nSaliendo del programa VetCare. ¡Hasta luego!")
        break
    else:
        print("\nOpción inválida. Por favor, seleccione una opción del 1 al 6.")
