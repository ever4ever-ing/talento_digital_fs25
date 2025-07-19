import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ejemplo_manejo_errores():
    print("\n=== MANEJO DE ERRORES ===")
    ruta_inexistente = os.path.join(BASE_DIR, "archivo_inexistente.txt")
    try:
        with open(ruta_inexistente, "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("Error: El archivo no existe")
    except PermissionError:
        print("Error: No tienes permisos para acceder al archivo")
    except Exception as e:
        print(f"Error inesperado: {e}")
    nombre_archivo = os.path.join(BASE_DIR, "ejemplo.txt")
    if os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' existe")
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            print("Primeras 50 caracteres:", archivo.read(50))
    else:
        print(f"El archivo '{nombre_archivo}' no existe")

if __name__ == "__main__":
    ejemplo_manejo_errores()
