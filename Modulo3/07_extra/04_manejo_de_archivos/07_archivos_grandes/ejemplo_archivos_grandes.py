import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ejemplo_archivos_grandes():
    print("\n=== ARCHIVOS GRANDES ===")
    ruta_grande = os.path.join(BASE_DIR, "archivo_grande.txt")
    with open(ruta_grande, "w", encoding="utf-8") as archivo:
        for i in range(1000):
            archivo.write(f"Esta es la línea número {i+1}\n")
    print("Archivo grande creado (1000 líneas)")
    contador_lineas = 0
    palabras_totales = 0
    with open(ruta_grande, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            contador_lineas += 1
            palabras_totales += len(linea.split())
    print(f"Total de líneas: {contador_lineas}")
    print(f"Total de palabras: {palabras_totales}")
    print("\nPrimeras 5 líneas:")
    with open(ruta_grande, "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo):
            if i >= 5:
                break
            print(f"  {linea.strip()}")

if __name__ == "__main__":
    ejemplo_archivos_grandes()
