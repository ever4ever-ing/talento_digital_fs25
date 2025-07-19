import os

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Archivo '{nombre_archivo}' leído correctamente:")
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
    except PermissionError:
        print(f"Error: Sin permisos para leer '{nombre_archivo}'")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

print("\nRuta de ejecución (directorio de trabajo):", os.getcwd())
print("\nRuta del archivo actual:", os.path.abspath(__file__))
print("\nDirectorio del archivo actual:", os.path.dirname(__file__))
print("\nNombre del archivo:", os.path.basename(__file__))
print("-" * 50)
leer_archivo(os.path.dirname(__file__)+"/01_try_except.py")

