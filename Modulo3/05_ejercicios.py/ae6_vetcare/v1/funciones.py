def registrar_cita(citas,historial,id,nombre_mascota,fecha,motivo,tutor,horario):
    print("\nRegistrando cita")
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
        for cita in historial[id_mascota]:
            nombre_mascota = cita['nombre_mascota']
            print(f"Nombre: {nombre_mascota}")
            print(f"- Fecha: {cita['fecha']}, Motivo: {cita['motivo']}, Tutor: {cita['tutor']}, Horario: {cita['horario']}")
    else:
        print(f"No hay historial para {nombre_mascota}.")
