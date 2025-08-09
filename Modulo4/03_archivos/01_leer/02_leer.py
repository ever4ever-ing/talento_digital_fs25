import csv

try:
    with open('bicicletas_nuevo.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector)
        print(f"Encabezados: {encabezados}")
        print("Datos:")
        for fila in lector:
            print(fila)
except FileNotFoundError:
    print("El archivo 'bicicletas_nuevo.csv' no existe.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
