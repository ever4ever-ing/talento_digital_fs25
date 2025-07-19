from funciones_persistencia import (
    cargar_datos, guardar_datos, registrar_cita, mostrar_historial, 
    verificar_disponibilidad, mostrar_horarios_disponibles, cancelar_cita, 
    mostrar_citas_del_dia, validar_fecha, validar_horario, mostrar_estadisticas,
    hacer_backup, validar_fecha_y_hora_futura, limpiar_citas_pasadas, mostrar_info_archivos,
    gestionar_mascotas
)
import sys

def inicializar_sistema():
    """Inicializa el sistema cargando datos existentes"""
    print("=" * 50)
    print("VetCare v3.0 - Sistema de Gestión de Citas")
    print("Con Persistencia de Datos")
    print("=" * 50)
    print("\nInicializando sistema...")
    
    # Cargar datos existentes
    citas, historial = cargar_datos()
    
    print("Sistema inicializado correctamente!")
    return citas, historial

def menu_principal():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("VetCare v3.0 - Sistema de Gestión de Citas")
    print("="*50)
    print("1. Ver horarios disponibles")
    print("2. Registrar nueva cita")
    print("3. Mostrar historial de mascota")
    print("4. Ver citas del día")
    print("5. Cancelar cita")
    print("6. Gestionar mascotas (ver todas/buscar)")
    print("7. Ver estadísticas del sistema")
    print("8. Crear backup de datos")
    print("9. Limpiar citas pasadas")
    print("10. Ver información de archivos")
    print("11. Guardar datos manualmente")
    print("0. Salir")
    print("="*50)

def solicitar_datos_cita(citas, horarios_posibles):
    """Solicita y valida los datos para una nueva cita"""
    print("\nRegistro de nueva cita")
    print("-" * 30)
    
    # Solicitar ID y nombre
    id = input("Ingrese el ID de la mascota: ").strip()
    if not id:
        print("El ID no puede estar vacío.")
        return None
    
    nombre = input("Nombre de la mascota: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return None
    
    # Solicitar y validar fecha
    while True:
        fecha = input("Ingrese la fecha (dd/mm/yy): ").strip()
        es_valida, mensaje = validar_fecha(fecha)
        if es_valida:
            break
        else:
            print(f"Error: {mensaje}")
            print("Ejemplo de fecha válida: 25/12/24")
    
    # Mostrar horarios disponibles
    horarios_disponibles = mostrar_horarios_disponibles(citas, fecha, horarios_posibles)
    
    if not horarios_disponibles:
        print("No hay horarios disponibles para esta fecha.")
        print("Esto puede ser porque:")
        print("- Todos los horarios están ocupados")
        print("- La fecha es hoy y los horarios ya pasaron")
        print("Intente con otra fecha.")
        return None
    
    print(f"\nHorarios disponibles para el {fecha}:")
    for i, horario in enumerate(horarios_disponibles, 1):
        print(f"{i}. {horario}")
    
    # Seleccionar horario
    while True:
        try:
            seleccion = int(input("\nSeleccione el número del horario deseado: ")) - 1
            if 0 <= seleccion < len(horarios_disponibles):
                horario = horarios_disponibles[seleccion]
                break
            else:
                print("Selección inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Solicitar motivo
    motivos_validos = ["urgencia", "consulta", "control", "vacunacion", "cirugia"]
    print(f"\nMotivos disponibles: {', '.join(motivos_validos)}")
    while True:
        motivo = input("Ingrese motivo: ").strip().lower()
        if motivo in motivos_validos:
            break
        else:
            print(f"Motivo inválido. Use uno de: {', '.join(motivos_validos)}")
    
    # Solicitar tutor
    tutor = input("Ingrese el nombre del tutor: ").strip()
    if not tutor:
        print("El nombre del tutor no puede estar vacío.")
        return None
    
    return {
        'id': id,
        'nombre': nombre,
        'fecha': fecha,
        'horario': horario,
        'motivo': motivo,
        'tutor': tutor
    }

def main():
    """Función principal del programa"""
    # Inicializar sistema
    citas, historial = inicializar_sistema()
    horarios_posibles = ["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"]
    
    # Bucle principal del menú
    while True:
        try:
            menu_principal()
            opcion = input("Seleccione una opción (0-11): ").strip()
            
            if opcion == '1':
                # Ver horarios disponibles
                while True:
                    fecha = input("\nIngrese la fecha para consultar (dd/mm/yy): ").strip()
                    es_valida, mensaje = validar_fecha(fecha)
                    if es_valida:
                        break
                    else:
                        print(f"Error: {mensaje}")
                
                horarios_disponibles = mostrar_horarios_disponibles(citas, fecha, horarios_posibles)
                
                print(f"\nHorarios disponibles para el {fecha}:")
                if horarios_disponibles:
                    for horario in horarios_disponibles:
                        print(f"✓ {horario}")
                else:
                    print("No hay horarios disponibles para esta fecha")
                    print("Esto puede ser porque:")
                    print("- Todos los horarios están ocupados")
                    print("- La fecha es hoy y los horarios ya pasaron")
                    
            elif opcion == '2':
                # Registrar nueva cita
                datos_cita = solicitar_datos_cita(citas, horarios_posibles)
                if datos_cita:
                    citas, historial = registrar_cita(
                        citas, historial, 
                        datos_cita['id'], datos_cita['nombre'], 
                        datos_cita['fecha'], datos_cita['motivo'], 
                        datos_cita['tutor'], datos_cita['horario']
                    )
                
            elif opcion == '3':
                # Mostrar historial
                id_mascota = input("\nIngrese el ID de la mascota: ").strip()
                if id_mascota:
                    mostrar_historial(historial, id_mascota)
                else:
                    print("El ID no puede estar vacío.")
                    
            elif opcion == '4':
                # Ver citas del día
                while True:
                    fecha = input("\nIngrese la fecha a consultar (dd/mm/yy): ").strip()
                    es_valida, mensaje = validar_fecha(fecha)
                    if es_valida:
                        break
                    else:
                        print(f"Error: {mensaje}")
                
                mostrar_citas_del_dia(citas, fecha)
                
            elif opcion == '5':
                # Cancelar cita
                print("\nCancelar cita")
                print("-" * 20)
                
                id_mascota = input("Ingrese el ID de la mascota: ").strip()
                if not id_mascota:
                    print("El ID no puede estar vacío.")
                    continue
                
                while True:
                    fecha = input("Ingrese la fecha de la cita (dd/mm/yy): ").strip()
                    es_valida, mensaje = validar_fecha(fecha)
                    if es_valida:
                        break
                    else:
                        print(f"Error: {mensaje}")
                        print("Nota: Puede cancelar citas pasadas si es necesario")
                
                horario = input("Ingrese el horario de la cita: ").strip()
                if not validar_horario(horario, horarios_posibles):
                    print(f"Horario inválido. Use uno de: {', '.join(horarios_posibles)}")
                    continue
                
                citas, historial = cancelar_cita(citas, historial, id_mascota, fecha, horario)
                
            elif opcion == '6':
                # Gestionar mascotas
                gestionar_mascotas(historial)
                
            elif opcion == '7':
                # Ver estadísticas
                mostrar_estadisticas(citas, historial)
                
            elif opcion == '8':
                # Crear backup
                print("\nCreando backup de datos...")
                if hacer_backup():
                    print("Backup creado exitosamente.")
                else:
                    print("Error al crear el backup.")
                    
            elif opcion == '9':
                # Limpiar citas pasadas
                print("\nLimpiando citas pasadas...")
                citas_originales = len(citas)
                citas = limpiar_citas_pasadas(citas)
                
                if len(citas) < citas_originales:
                    if guardar_datos(citas, historial):
                        print(f"Se eliminaron {citas_originales - len(citas)} citas pasadas y se guardaron los cambios.")
                    else:
                        print("Las citas se limpiaron pero hubo un error al guardar.")
                else:
                    print("No se encontraron citas pasadas para eliminar.")
                    
            elif opcion == '10':
                # Ver información de archivos
                mostrar_info_archivos()
                    
            elif opcion == '11':
                # Guardar datos manualmente
                print("\nGuardando datos...")
                if guardar_datos(citas, historial):
                    print("Datos guardados exitosamente.")
                else:
                    print("Error al guardar los datos.")
                    
            elif opcion == '0':
                # Salir
                print("\nGuardando datos antes de salir...")
                if guardar_datos(citas, historial):
                    print("Datos guardados exitosamente.")
                else:
                    print("Advertencia: Error al guardar los datos.")
                
                print("Saliendo del programa VetCare v3.0. ¡Hasta luego!")
                sys.exit(0)
                
            else:
                print("\nOpción inválida. Por favor, seleccione una opción del 0 al 11.")
                
        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Guardando datos...")
            guardar_datos(citas, historial)
            print("Saliendo del programa VetCare v3.0. ¡Hasta luego!")
            sys.exit(0)
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("El programa continuará ejecutándose...")

if __name__ == "__main__":
    main()
