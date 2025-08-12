import csv
from pathlib import Path

nombre_archivo = 'inventario_bicicletas.csv'
ruta_dinamica = Path('./') / nombre_archivo
campos = ["marca", "modelo", "aro", "precio"]

def inicializar_archivo(ruta_dinamica: Path, campos: list):
    with open(ruta_dinamica, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)  # Definir el objeto DictWriter
        writer.writeheader() # Escribimos la cabecera del archivo
        print(f"Archivo '{nombre_archivo}' inicializado correctamente.")

def agregar_bicicleta(ruta_dinamica: Path):
    try:
        marca = input("Ingrese la marca de la bicicleta: ")
        modelo = input("Ingrese el modelo de la bicicleta: ")
        aro = input("Ingrese el aro de la bicicleta: ")
        precio = input("Ingrese el precio de la bicicleta: ")
    except ValueError as e:
        print("Error: ", e)
        return  # Detener la ejecución de la función si hay un error

    bicicleta = [marca.lower(), modelo.lower(), aro.lower(), precio.lower()]

    with open(ruta_dinamica, 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(bicicleta)
        print("Bicicleta agregada correctamente.")

def mostrar_inventario(ruta_dinamica: Path):

    with open(ruta_dinamica, 'r', newline='', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Saltar la cabecera
        print("===== Inventario =====")
        for fila in reader:
            print(f"Marca: {fila[0]}, Modelo: {fila[1]}, Aro: {fila[2]}, Precio: {fila[3]}")

def menu():
    print("\n===== Menú =====")
    print("1. Agregar bicicleta")
    print("2. Mostrar inventario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

if __name__ == "__main__":
    print("\n===== Sistema de inventario =====")
    inicializar_archivo(ruta_dinamica, campos)
    while True:
        opcion = menu()
        if opcion == "1":
            agregar_bicicleta(ruta_dinamica)
        elif opcion == "2":
            mostrar_inventario(ruta_dinamica)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")