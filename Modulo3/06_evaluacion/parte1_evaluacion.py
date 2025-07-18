def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
def agregar_tarea(tareas):
    pass
def ver_tareas(tareas):
    pass
def marcar_completada(tareas):
    pass
def eliminar_tarea(tareas):
    pass

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
