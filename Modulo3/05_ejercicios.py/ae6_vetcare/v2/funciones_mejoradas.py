def verificar_disponibilidad(citas, fecha, horario):
    """Verifica si un horario está disponible en una fecha específica"""
    for cita in citas:
        if cita['fecha'] == fecha and cita['horario'] == horario:
            return False
    return True

def mostrar_horarios_disponibles(citas, fecha, horarios_posibles):
    """
    Muestra los horarios disponibles para una fecha específica.
    Parametros: citas (list): Lista de citas registradas
                fecha (str): Fecha para la cual se desean los horarios disponibles
                horarios_posibles (list): Lista de horarios posibles
    Retorna: 
    list: Lista de horarios disponibles para la fecha especificada
    
    """
    horarios_disponibles = []
    for horario in horarios_posibles:
        if verificar_disponibilidad(citas, fecha, horario):
            horarios_disponibles.append(horario)
    return horarios_disponibles

def cancelar_cita(citas, historial, id_mascota, fecha, horario):
    """Cancela una cita específica"""
    cita_encontrada = False
    
    # Buscar y eliminar de la lista de citas
    for i, cita in enumerate(citas):
        if (cita['id'] == id_mascota and 
            cita['fecha'] == fecha and 
            cita['horario'] == horario):
            citas.pop(i)
            cita_encontrada = True
            break
    
    # Buscar y eliminar del historial
    if id_mascota in historial:
        for i, cita in enumerate(historial[id_mascota]):
            if (cita['fecha'] == fecha and 
                cita['horario'] == horario):
                historial[id_mascota].pop(i)
                break
    
    if cita_encontrada:
        print(f"Cita cancelada exitosamente para el {fecha} a las {horario}")
    else:
        print("No se encontró la cita especificada")
    
    return citas, historial

def registrar_cita(citas,historial,id,nombre_mascota,fecha,motivo,tutor,horario):
    print("\nVerificando disponibilidad...")
    
    # Verificar si el horario está disponible
    if not verificar_disponibilidad(citas, fecha, horario):
        print(f"El horario {horario} del {fecha} ya está ocupado.")
        return citas, historial
    
    print("Horario disponible. Registrando cita...")
    cita = {
        "id": id,
        "nombre_mascota": nombre_mascota,
        "fecha": fecha,
        "motivo": motivo,
        "tutor": tutor,
        "horario":horario,
    }
    citas.append(cita)
    if id not in historial:
        historial[id] = [] # Inicializar lista si no existe
    historial[id].append(cita) #Agregar cita al historial
    print(f"Cita registrada para {nombre_mascota} el {fecha} a las {horario} por {motivo}.")
    return citas, historial

def mostrar_historial(historial, id_mascota):
    if id_mascota in historial:
        print(f"\nHistorial de citas para la mascota ID: {id_mascota}")
        print("-" * 50)
        for cita in historial[id_mascota]:
            nombre_mascota = cita['nombre_mascota']
            print(f"Nombre: {nombre_mascota}")
            print(f"Fecha: {cita['fecha']}")
            print(f"Horario: {cita['horario']}")
            print(f"Motivo: {cita['motivo']}")
            print(f"Tutor: {cita['tutor']}")
            print("-" * 30)
    else:
        print(f"No hay historial para la mascota con ID: {id_mascota}")

def mostrar_citas_del_dia(citas, fecha):
    """Muestra todas las citas programadas para una fecha específica"""
    citas_del_dia = [cita for cita in citas if cita['fecha'] == fecha]
    
    if not citas_del_dia:
        print(f"No hay citas programadas para el {fecha}")
        return
    
    print(f"\nCitas programadas para el {fecha}:")
    print("-" * 50)
    
    # Ordenar las citas por horario
    citas_del_dia.sort(key=lambda x: x['horario'])#Ordenar por horario 
    
    for cita in citas_del_dia:
        print(f"{cita['horario']} - {cita['nombre_mascota']} (ID: {cita['id']})")
        print(f"   Tutor: {cita['tutor']}")
        print(f"   Motivo: {cita['motivo']}")
        print("-" * 30)
