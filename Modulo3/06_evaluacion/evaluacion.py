def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista."""
    descripcion = input("Introduce la descripción de la nueva tarea: ")
    if descripcion:
        tareas.append({'descripcion': descripcion, 'completada': False})
        print("¡Tarea agregada con éxito!")
    else:
        print("La descripción de la tarea no puede estar vacía.")

def ver_tareas(tareas):
    """Muestra todas las tareas con su estado."""
    print("\n--- Lista de Tareas ---")
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - [{estado}]")

def marcar_completada(tareas):
    """Marca una tarea como completada."""
    ver_tareas(tareas)
    if not tareas:
        return

    num_input = input("Elige el número de la tarea a marcar como completada: ")
    if num_input.isdigit():
        num_tarea = int(num_input)
        if 1 <= num_tarea <= len(tareas):
            tareas[num_tarea - 1]['completada'] = True
            print("¡Tarea marcada como completada!")
        else:
            print("Número de tarea no válido.")
    else:
        print("Por favor, introduce un número válido.")

def eliminar_tarea(tareas):
    """Elimina una tarea de la lista."""
    ver_tareas(tareas)
    if not tareas:
        return

    num_input = input("Elige el número de la tarea a eliminar: ")
    if num_input.isdigit():
        num_tarea = int(num_input)
        if 1 <= num_tarea <= len(tareas):
            tarea_eliminada = tareas.pop(num_tarea - 1)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
        else:
            print("Número de tarea no válido.")
    else:
        print("Por favor, introduce un número válido.")

def main():
    """Función principal que ejecuta el programa."""
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("¡Gracias por usar el Gestor de Tareas! Adiós.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")


main()
