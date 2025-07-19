import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def escribir_archivo_w(ruta, lineas):
    """Escribe líneas en un archivo, creando uno nuevo si no existe."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(f"{linea}\n")
    print("Archivo creado con modo 'w'")

def escribir_archivo_a(ruta, lineas):
    """Añade contenido a un archivo existente o crea uno nuevo si no existe."""
    with open(ruta, "a", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(f"{linea}\n")
    print("Contenido añadido con modo 'a'")

def mostrar_contenido(ruta):
    """Muestra el contenido de un archivo."""
    with open(ruta, "r", encoding="utf-8") as archivo:
        print("Contenido final:")
        print(archivo.read())

def ejemplo_escritura():
    """Ejemplo de escritura en archivos."""
    print("\n=== ESCRITURA DE ARCHIVOS ===")
    ruta_escritura = os.path.join(BASE_DIR, "escritura_ejemplo.txt")
    escribir_archivo_w(ruta_escritura, ["Primera línea", "Segunda línea", "Tercera línea"])
    escribir_archivo_a(ruta_escritura, ["Línea añadida", "Otra línea más"])
    mostrar_contenido(ruta_escritura)

if __name__ == "__main__":
    ejemplo_escritura()
