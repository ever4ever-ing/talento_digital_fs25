import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def escribir_csv(ruta, datos):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)
    print("Archivo CSV creado")

def leer_csv(ruta):
    print("Leyendo CSV:")
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(f"  {fila}")
    print("\nLeyendo CSV como diccionario:")
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(f"  {fila['Producto']}: ${fila['Precio']} (Stock: {fila['Stock']})")


print("\n=== ARCHIVOS CSV ===")
datos_productos = [
        ["Producto", "Precio", "Stock"],
        ["Laptop", 899.99, 15],
        ["Mouse", 29.99, 50],
        ["Teclado", 79.99, 30],
        ["Monitor", 299.99, 10]
    ]
ruta_csv = os.path.join(BASE_DIR, "productos.csv")
escribir_csv(ruta_csv, datos_productos)
leer_csv(ruta_csv)

