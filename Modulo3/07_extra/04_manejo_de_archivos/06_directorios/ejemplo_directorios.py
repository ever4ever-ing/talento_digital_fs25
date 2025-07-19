import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def crear_directorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Directorio '{ruta}' creado")
    else:
        print(f"El directorio '{ruta}' ya existe")

def listar_archivos(ruta):
    print("\nArchivos en el directorio actual:")
    for elemento in os.listdir(ruta):
        ruta_elemento = os.path.join(ruta, elemento)
        if os.path.isfile(ruta_elemento):
            tamaño = os.path.getsize(ruta_elemento)
            print(f"  [A] {elemento} ({tamaño} bytes)")
        elif os.path.isdir(ruta_elemento):
            print(f"  [D] {elemento}/")

def crear_archivo_en_subdirectorio(ruta_directorio, nombre_archivo):
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("Este archivo está en un subdirectorio")
    print(f"Archivo creado en: {ruta_archivo}")

def ejemplo_directorios():
    print("\n=== OPERACIONES CON DIRECTORIOS ===")
    print(f"Directorio actual: {os.getcwd()}")
    nombre_directorio = os.path.join(BASE_DIR, "ejemplo_directorio")
    crear_directorio(nombre_directorio)
    listar_archivos(BASE_DIR)
    crear_archivo_en_subdirectorio(nombre_directorio, "archivo_en_subdirectorio.txt")

if __name__ == "__main__":
    ejemplo_directorios()
