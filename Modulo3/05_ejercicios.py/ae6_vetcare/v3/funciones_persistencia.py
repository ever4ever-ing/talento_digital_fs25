import json
import os
from datetime import datetime

# Obtener el directorio donde está este archivo
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Archivos de datos (siempre relativos al directorio del script)
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
ARCHIVO_CITAS = os.path.join(DATA_DIR, "citas.json")
ARCHIVO_HISTORIAL = os.path.join(DATA_DIR, "historial.json")

# Crear directorio de datos si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    print(f"Directorio de datos creado en: {DATA_DIR}")

def cargar_datos():
    """Carga los datos de citas e historial desde archivos JSON"""
    citas = []
    historial = {}
    
    print(f"Cargando datos desde la carpeta: {DATA_DIR}")
    
    # Cargar citas
    if os.path.exists(ARCHIVO_CITAS):
        try:
            with open(ARCHIVO_CITAS, 'r', encoding='utf-8') as archivo:
                citas = json.load(archivo)
            print(f"Datos de citas cargados: {len(citas)} citas encontradas")
            
            # Limpiar citas pasadas automáticamente
            citas_originales = len(citas)
            citas = limpiar_citas_pasadas(citas)
            
            # Si se eliminaron citas, guardar los datos actualizados
            if len(citas) < citas_originales:
                with open(ARCHIVO_CITAS, 'w', encoding='utf-8') as archivo:
                    json.dump(citas, archivo, indent=2, ensure_ascii=False)
                    
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error al cargar el archivo de citas, iniciando con lista vacía")
            citas = []
    else:
        print("No se encontró archivo de citas previo, iniciando con lista vacía")
    
    # Cargar historial
    if os.path.exists(ARCHIVO_HISTORIAL):
        try:
            with open(ARCHIVO_HISTORIAL, 'r', encoding='utf-8') as archivo:
                historial = json.load(archivo)
            print(f"Historial cargado: {len(historial)} mascotas en el historial")
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error al cargar el archivo de historial, iniciando con diccionario vacío")
            historial = {}
    else:
        print("No se encontró archivo de historial previo, iniciando con diccionario vacío")
    
    return citas, historial

def guardar_datos(citas, historial):
    """Guarda los datos de citas e historial en archivos JSON"""
    try:
        # Guardar citas
        with open(ARCHIVO_CITAS, 'w', encoding='utf-8') as archivo:
            json.dump(citas, archivo, indent=2, ensure_ascii=False)
        
        # Guardar historial
        with open(ARCHIVO_HISTORIAL, 'w', encoding='utf-8') as archivo:
            json.dump(historial, archivo, indent=2, ensure_ascii=False)
        
        print(f"Datos guardados exitosamente en: {DATA_DIR}")
        return True
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        return False

def verificar_disponibilidad(citas, fecha, horario):
    """Verifica si un horario está disponible en una fecha específica"""
    for cita in citas:
        if cita['fecha'] == fecha and cita['horario'] == horario:
            return False
    return True

def mostrar_horarios_disponibles(citas, fecha, horarios_posibles):
    """Muestra los horarios disponibles para una fecha específica, excluyendo horarios pasados"""
    horarios_disponibles = []
    fecha_actual = datetime.now()
    
    try:
        fecha_cita = datetime.strptime(fecha, '%d/%m/%y')
        es_hoy = fecha_cita.date() == fecha_actual.date()
        
        for horario in horarios_posibles:
            # Verificar disponibilidad (no ocupado)
            if verificar_disponibilidad(citas, fecha, horario):
                # Si es hoy, verificar que el horario no haya pasado
                if es_hoy:
                    hora_cita = datetime.strptime(f"{fecha} {horario}", '%d/%m/%y %H:%M')
                    if hora_cita > fecha_actual:
                        horarios_disponibles.append(horario)
                else:
                    # Si es una fecha futura, todos los horarios son válidos
                    horarios_disponibles.append(horario)
    except ValueError:
        # Si hay error en el formato de fecha, devolver lista vacía
        pass
    
    return horarios_disponibles

def validar_fecha(fecha_str):
    """Valida que la fecha tenga el formato correcto dd/mm/yy y sea futura"""
    try:
        fecha_cita = datetime.strptime(fecha_str, '%d/%m/%y')
        fecha_actual = datetime.now()
        
        # Comparar solo las fechas (sin horas)
        if fecha_cita.date() < fecha_actual.date():
            return False, "La fecha no puede ser en el pasado"
        return True, "Fecha válida"
    except ValueError:
        return False, "Formato de fecha inválido. Use dd/mm/yy"

def validar_fecha_y_hora_futura(fecha_str, horario_str):
    """Valida que la fecha y hora sean futuras"""
    try:
        # Combinar fecha y hora
        fecha_hora_str = f"{fecha_str} {horario_str}"
        fecha_hora_cita = datetime.strptime(fecha_hora_str, '%d/%m/%y %H:%M')
        fecha_hora_actual = datetime.now()
        
        if fecha_hora_cita <= fecha_hora_actual:
            return False, "La fecha y hora no pueden ser en el pasado"
        return True, "Fecha y hora válidas"
    except ValueError:
        return False, "Error al validar fecha y hora"

def validar_horario(horario, horarios_posibles):
    """Valida que el horario esté dentro de los horarios permitidos"""
    return horario in horarios_posibles

def registrar_cita(citas, historial, id, nombre_mascota, fecha, motivo, tutor, horario):
    """Registra una nueva cita y guarda los datos automáticamente"""
    print("\nVerificando disponibilidad y validando fecha/hora...")
    
    # Verificar que la fecha y hora sean futuras
    es_valida, mensaje = validar_fecha_y_hora_futura(fecha, horario)
    if not es_valida:
        print(f"Error: {mensaje}")
        return citas, historial
    
    # Verificar si el horario está disponible
    if not verificar_disponibilidad(citas, fecha, horario):
        print(f"El horario {horario} del {fecha} ya está ocupado.")
        return citas, historial
    
    print("Horario disponible. Registrando cita...")
    
    # Crear objeto cita con timestamp
    cita = {
        "id": id,
        "nombre_mascota": nombre_mascota,
        "fecha": fecha,
        "motivo": motivo,
        "tutor": tutor,
        "horario": horario,
        "fecha_registro": datetime.now().strftime('%d/%m/%y %H:%M:%S')
    }
    
    # Agregar a la lista de citas
    citas.append(cita)
    
    # Agregar al historial
    if id not in historial:
        historial[id] = []
    historial[id].append(cita)
    
    # Guardar datos automáticamente
    if guardar_datos(citas, historial):
        print(f"Cita registrada para {nombre_mascota} el {fecha} a las {horario} por {motivo}.")
    else:
        print("Cita registrada pero hubo un error al guardar los datos.")
    
    return citas, historial

def cancelar_cita(citas, historial, id_mascota, fecha, horario):
    """Cancela una cita específica y guarda los cambios"""
    cita_encontrada = False
    
    # Buscar y eliminar de la lista de citas
    for i, cita in enumerate(citas):
        if (cita['id'] == id_mascota and 
            cita['fecha'] == fecha and 
            cita['horario'] == horario):
            cita_cancelada = citas.pop(i)
            cita_encontrada = True
            break
    
    # Buscar y eliminar del historial
    if id_mascota in historial:
        for i, cita in enumerate(historial[id_mascota]):
            if (cita['fecha'] == fecha and 
                cita['horario'] == horario):
                historial[id_mascota].pop(i)
                # Si no quedan más citas, eliminar la mascota del historial
                if not historial[id_mascota]:
                    del historial[id_mascota]
                break
    
    if cita_encontrada:
        # Guardar cambios automáticamente
        if guardar_datos(citas, historial):
            print(f"Cita cancelada exitosamente para el {fecha} a las {horario}")
        else:
            print("Cita cancelada pero hubo un error al guardar los cambios.")
    else:
        print("No se encontró la cita especificada")
    
    return citas, historial

def mostrar_historial(historial, id_mascota):
    """Muestra el historial de citas de una mascota"""
    if id_mascota in historial:
        print(f"\nHistorial de citas para la mascota ID: {id_mascota}")
        print("-" * 60)
        for i, cita in enumerate(historial[id_mascota], 1):
            nombre_mascota = cita['nombre_mascota']
            print(f"Cita #{i}:")
            print(f"  Nombre: {nombre_mascota}")
            print(f"  Fecha: {cita['fecha']}")
            print(f"  Horario: {cita['horario']}")
            print(f"  Motivo: {cita['motivo']}")
            print(f"  Tutor: {cita['tutor']}")
            if 'fecha_registro' in cita:
                print(f"  Registrada: {cita['fecha_registro']}")
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
    print("-" * 60)
    
    # Ordenar las citas por horario
    citas_del_dia.sort(key=lambda x: x['horario'])
    
    for i, cita in enumerate(citas_del_dia, 1):
        print(f"Cita #{i}:")
        print(f"  {cita['horario']} - {cita['nombre_mascota']} (ID: {cita['id']})")
        print(f"  Tutor: {cita['tutor']}")
        print(f"  Motivo: {cita['motivo']}")
        if 'fecha_registro' in cita:
            print(f"  Registrada: {cita['fecha_registro']}")
        print("-" * 30)

def mostrar_estadisticas(citas, historial):
    """Muestra estadísticas generales del sistema"""
    print("\nEstadísticas del Sistema VetCare")
    print("=" * 40)
    print(f"Total de citas activas: {len(citas)}")
    print(f"Total de mascotas registradas: {len(historial)}")
    
    if citas:
        # Contar citas por motivo
        motivos = {}
        for cita in citas:
            motivo = cita['motivo']
            motivos[motivo] = motivos.get(motivo, 0) + 1
        
        print("\nCitas por motivo:")
        for motivo, cantidad in motivos.items():
            print(f"  {motivo}: {cantidad}")
        
        # Mostrar próximas citas (ordenadas por fecha)
        citas_ordenadas = sorted(citas, key=lambda x: datetime.strptime(x['fecha'], '%d/%m/%y'))
        print(f"\nPróxima cita: {citas_ordenadas[0]['fecha']} a las {citas_ordenadas[0]['horario']}")
        print(f"Mascota: {citas_ordenadas[0]['nombre_mascota']} (ID: {citas_ordenadas[0]['id']})")

def mostrar_todas_las_mascotas(historial):
    """Muestra todas las mascotas registradas en el sistema"""
    if not historial:
        print("No hay mascotas registradas en el sistema.")
        return
    
    print(f"\nTodas las Mascotas Registradas ({len(historial)} mascotas)")
    print("=" * 60)
    
    mascotas_info = []
    for id_mascota, citas_mascota in historial.items():
        if citas_mascota:  # Si tiene al menos una cita
            # Obtener información de la mascota de la primera cita
            primera_cita = citas_mascota[0]
            nombre = primera_cita['nombre_mascota']
            tutor = primera_cita['tutor']
            total_citas = len(citas_mascota)
            
            # Encontrar la fecha más reciente
            fechas = [datetime.strptime(cita['fecha'], '%d/%m/%y') for cita in citas_mascota]
            fecha_mas_reciente = max(fechas).strftime('%d/%m/%y')
            
            mascotas_info.append({
                'id': id_mascota,
                'nombre': nombre,
                'tutor': tutor,
                'total_citas': total_citas,
                'ultima_cita': fecha_mas_reciente
            })
    
    # Ordenar por nombre de mascota
    mascotas_info.sort(key=lambda x: x['nombre'].lower())
    
    for i, mascota in enumerate(mascotas_info, 1):
        print(f"{i}. ID: {mascota['id']}")
        print(f"   Nombre: {mascota['nombre']}")
        print(f"   Tutor: {mascota['tutor']}")
        print(f"   Total de citas: {mascota['total_citas']}")
        print(f"   Última cita: {mascota['ultima_cita']}")
        print("-" * 30)

def buscar_mascota_por_nombre(historial, nombre_busqueda):
    """Busca mascotas por nombre (búsqueda parcial)"""
    nombre_busqueda = nombre_busqueda.lower().strip()
    mascotas_encontradas = []
    
    for id_mascota, citas_mascota in historial.items():
        if citas_mascota:
            nombre_mascota = citas_mascota[0]['nombre_mascota'].lower()
            if nombre_busqueda in nombre_mascota:
                mascotas_encontradas.append({
                    'id': id_mascota,
                    'nombre': citas_mascota[0]['nombre_mascota'],
                    'tutor': citas_mascota[0]['tutor'],
                    'total_citas': len(citas_mascota)
                })
    
    return mascotas_encontradas

def buscar_mascota_por_tutor(historial, tutor_busqueda):
    """Busca mascotas por nombre del tutor (búsqueda parcial)"""
    tutor_busqueda = tutor_busqueda.lower().strip()
    mascotas_encontradas = []
    
    for id_mascota, citas_mascota in historial.items():
        if citas_mascota:
            tutor = citas_mascota[0]['tutor'].lower()
            if tutor_busqueda in tutor:
                mascotas_encontradas.append({
                    'id': id_mascota,
                    'nombre': citas_mascota[0]['nombre_mascota'],
                    'tutor': citas_mascota[0]['tutor'],
                    'total_citas': len(citas_mascota)
                })
    
    return mascotas_encontradas

def mostrar_resultados_busqueda(mascotas_encontradas, tipo_busqueda, termino_busqueda):
    """Muestra los resultados de búsqueda de mascotas"""
    if not mascotas_encontradas:
        print(f"No se encontraron mascotas con {tipo_busqueda} que contenga '{termino_busqueda}'")
        return
    
    print(f"\nResultados de búsqueda por {tipo_busqueda}: '{termino_busqueda}'")
    print(f"Se encontraron {len(mascotas_encontradas)} mascota(s)")
    print("-" * 50)
    
    for i, mascota in enumerate(mascotas_encontradas, 1):
        print(f"{i}. ID: {mascota['id']} - {mascota['nombre']}")
        print(f"   Tutor: {mascota['tutor']}")
        print(f"   Total de citas: {mascota['total_citas']}")
        print("-" * 30)

def gestionar_mascotas(historial):
    """Función principal para gestionar y buscar mascotas"""
    while True:
        print("\nGestión de Mascotas")
        print("=" * 30)
        print("1. Ver todas las mascotas")
        print("2. Buscar por nombre de mascota")
        print("3. Buscar por nombre del tutor")
        print("4. Volver al menú principal")
        print("-" * 30)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            mostrar_todas_las_mascotas(historial)
            
        elif opcion == '2':
            nombre = input("\nIngrese el nombre (o parte del nombre) de la mascota: ").strip()
            if nombre:
                mascotas = buscar_mascota_por_nombre(historial, nombre)
                mostrar_resultados_busqueda(mascotas, "nombre", nombre)
            else:
                print("El nombre no puede estar vacío.")
                
        elif opcion == '3':
            tutor = input("\nIngrese el nombre (o parte del nombre) del tutor: ").strip()
            if tutor:
                mascotas = buscar_mascota_por_tutor(historial, tutor)
                mostrar_resultados_busqueda(mascotas, "tutor", tutor)
            else:
                print("El nombre del tutor no puede estar vacío.")
                
        elif opcion == '4':
            break
            
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")

def mostrar_info_archivos():
    """Muestra información sobre los archivos de datos"""
    print("\nInformación de Archivos de Datos")
    print("=" * 40)
    print(f"Carpeta de datos: {DATA_DIR}")
    
    # Información del archivo de citas
    if os.path.exists(ARCHIVO_CITAS):
        stat_citas = os.stat(ARCHIVO_CITAS)
        tamaño_citas = stat_citas.st_size
        fecha_mod_citas = datetime.fromtimestamp(stat_citas.st_mtime).strftime('%d/%m/%y %H:%M:%S')
        print(f"Archivo de citas: {ARCHIVO_CITAS}")
        print(f"  Tamaño: {tamaño_citas} bytes")
        print(f"  Última modificación: {fecha_mod_citas}")
    else:
        print(f"Archivo de citas: {ARCHIVO_CITAS} (no existe)")
    
    # Información del archivo de historial
    if os.path.exists(ARCHIVO_HISTORIAL):
        stat_historial = os.stat(ARCHIVO_HISTORIAL)
        tamaño_historial = stat_historial.st_size
        fecha_mod_historial = datetime.fromtimestamp(stat_historial.st_mtime).strftime('%d/%m/%y %H:%M:%S')
        print(f"Archivo de historial: {ARCHIVO_HISTORIAL}")
        print(f"  Tamaño: {tamaño_historial} bytes")
        print(f"  Última modificación: {fecha_mod_historial}")
    else:
        print(f"Archivo de historial: {ARCHIVO_HISTORIAL} (no existe)")
    
    # Listar archivos de backup
    if os.path.exists(DATA_DIR):
        archivos_backup = [f for f in os.listdir(DATA_DIR) if f.startswith('backup_')]
        if archivos_backup:
            print(f"\nArchivos de backup encontrados: {len(archivos_backup)}")
            for backup in sorted(archivos_backup)[-3:]:  # Mostrar solo los 3 más recientes
                print(f"  {backup}")
        else:
            print("\nNo se encontraron archivos de backup")

def limpiar_citas_pasadas(citas):
    """Elimina automáticamente las citas que ya pasaron"""
    fecha_hora_actual = datetime.now()
    citas_futuras = []
    citas_eliminadas = 0
    
    for cita in citas:
        try:
            fecha_hora_cita = datetime.strptime(f"{cita['fecha']} {cita['horario']}", '%d/%m/%y %H:%M')
            if fecha_hora_cita > fecha_hora_actual:
                citas_futuras.append(cita)
            else:
                citas_eliminadas += 1
        except ValueError:
            # Si hay error en el formato, conservar la cita
            citas_futuras.append(cita)
    
    if citas_eliminadas > 0:
        print(f"Se eliminaron automáticamente {citas_eliminadas} citas pasadas del sistema")
    
    return citas_futuras

def hacer_backup():
    """Crea una copia de respaldo de los datos con timestamp"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    try:
        # Backup de citas
        if os.path.exists(ARCHIVO_CITAS):
            backup_citas = os.path.join(DATA_DIR, f"backup_citas_{timestamp}.json")
            with open(ARCHIVO_CITAS, 'r', encoding='utf-8') as origen:
                with open(backup_citas, 'w', encoding='utf-8') as destino:
                    destino.write(origen.read())
        
        # Backup de historial
        if os.path.exists(ARCHIVO_HISTORIAL):
            backup_historial = os.path.join(DATA_DIR, f"backup_historial_{timestamp}.json")
            with open(ARCHIVO_HISTORIAL, 'r', encoding='utf-8') as origen:
                with open(backup_historial, 'w', encoding='utf-8') as destino:
                    destino.write(origen.read())
        
        print(f"Backup creado exitosamente con timestamp: {timestamp}")
        print(f"Archivos guardados en: {DATA_DIR}")
        return True
    except Exception as e:
        print(f"Error al crear backup: {e}")
        return False
