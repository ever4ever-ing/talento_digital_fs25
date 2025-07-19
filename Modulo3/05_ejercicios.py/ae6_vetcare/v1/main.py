from v1.funciones import registrar_cita, mostrar_historial #Paso 4: Modularización 

# Paso 1:Definición de variables
citas = []
historial = {}
horarios_posibles = ["10:00", "11:00", "12:00", "13:00"]
#Posible mejora: Definir horarios por día
disponibilidad_semanal= {
    "lunes": ["10:00","11:00", "12:00", "13:00"],
    "martes": ["10:00", "11:00", "12:00", "13:00"],
    "miércoles": ["10:00", "11:00", "12:00", "13:00"],
    "jueves": ["10:00", "11:00", "12:00", "13:00"],
    "viernes": ["10:00", "11:00", "12:00", "13:00"],
    "sábado": ["10:00", "11:00", "12:00", "13:00"],
}
# Paso 2: Menu de opciones
while True:
    print("\n--- VetCare ---")
    print("1. Ver horarios disponibles")
    print("2. Registrar nueva cita")
    print("3. Mostrar historial de mascota")
    print("4. Salir\n")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        print("\nHorarios disponibles:")
        for horario in horarios_posibles:
            print(f"- {horario}")
    elif opcion == '2':
        id = input("\nIngrese el ID de la mascota:")
        nombre= input("\nNombre de la mascota:")
        fecha=input("Ingrese la fecha (dd/mm/yy):")
        motivo= input("Ingrese motivo(urgencia, consulta, control):")
        tutor = input("Ingrese el nombre del tutor:")
        horario = input("Ingrese el horario:(10:00)")
        #Paso 3: Definición de funciones
        registrar_cita(citas,historial,id,nombre,fecha,motivo,tutor,horario)
    elif opcion == '3':
        mostrar_historial(historial, input("\nIngrese el ID de la mascota: "))
    elif opcion == "4":
        print("\nSaliendo del programa, adiós")
        break
    else:
        print("\nOpción inválida.")
