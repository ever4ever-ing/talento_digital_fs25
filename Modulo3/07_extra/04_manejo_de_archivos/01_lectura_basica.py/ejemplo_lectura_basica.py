import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def leer_todo_el_archivo(ruta):
    """Lee todo el contenido del archivo y lo imprime."""
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido completo:")
        print(contenido)
    print("-" * 40)

def leer_linea_por_linea(ruta):
    """Lee el archivo línea por línea e imprime cada línea con su número."""
    with open(ruta, "r", encoding="utf-8") as archivo:
        print("Leyendo línea por línea:")
        for numero_linea, linea in enumerate(archivo, 1):
            print(f"Línea {numero_linea}: {linea.strip()}")
    print("-" * 40)

def leer_todas_las_lineas_en_lista(ruta):
    """Lee todas las líneas del archivo y las devuelve en una lista."""
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        print("Todas las líneas en lista:")
        for i, linea in enumerate(lineas):
            print(f"[{i}]: {linea.strip()}")

print("=== LECTURA BÁSICA ===")
ruta_ejemplo = os.path.join(BASE_DIR, "ejemplo.txt")
leer_todo_el_archivo(ruta_ejemplo)
leer_linea_por_linea(ruta_ejemplo)
leer_todas_las_lineas_en_lista(ruta_ejemplo)

