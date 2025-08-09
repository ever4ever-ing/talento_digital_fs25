import csv

class ArchivoVacioError(Exception):
    """Excepción personalizada para archivo vacío"""
    pass

try:
    with open('bicicletas_excepciones.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        filas = list(lector)
        if len(filas) == 0:
            raise ArchivoVacioError("El archivo está vacío.")
        encabezados = filas[0]
        print(f"Encabezados: {encabezados}")
        print("Datos:")
        for fila in filas[1:]:
            print(fila)
except FileNotFoundError:
    print("El archivo 'bicicletas_excepciones.csv' no existe.")
except ArchivoVacioError as ave:
    print(f"Error personalizado: {ave}")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
