import csv

class SinDatosError(Exception):
    """Excepción personalizada para datos vacíos"""
    pass

bicicletas = [
    ["marca", "modelo", "rodado", "precio"],
    # Puedes comentar todas las filas siguientes para probar la excepción personalizada
    ["Trek", "Marlin 7", 29, 850000],
    ["Giant", "Talon 3", 27.5, 720000],
    ["Scott", "Aspect 950", 29, 900000],
    ["Oxford", "Top Mega", 26, 350000],
    ["Bianchi", "Impulso", 28, 1200000]
]

try:
    if len(bicicletas) <= 1:
        raise SinDatosError("No hay datos de bicicletas para escribir en el archivo.")
    with open('bicicletas_personalizada.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(bicicletas)
    print("Archivo 'bicicletas_personalizada.csv' creado correctamente.")
except SinDatosError as sde:
    print(f"Error personalizado: {sde}")
except PermissionError:
    print("No tienes permisos para escribir el archivo.")
except Exception as e:
    print(f"Ocurrió un error al escribir el archivo: {e}")
