import csv

bicicletas = [
    ["marca", "modelo", "rodado", "precio"],
    ["Trek", "Marlin 7", 29, 850000],
    ["Giant", "Talon 3", 27.5, 720000],
    ["Scott", "Aspect 950", 29, 900000],
    ["Oxford", "Top Mega", 26, 350000],
    ["Bianchi", "Impulso", 28, 1200000]
]

try:
    with open('bicicletas_excepciones.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(bicicletas)
    print("Archivo 'bicicletas_excepciones.csv' creado correctamente.")
except PermissionError:
    print("No tienes permisos para escribir el archivo.")
except Exception as e:
    print(f"Ocurrió un error al escribir el archivo: {e}")
