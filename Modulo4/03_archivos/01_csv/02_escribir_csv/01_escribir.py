import csv

# Datos de ejemplo para escribir en el archivo
bicicletas = [
    ["marca", "modelo", "rodado", "precio"],
    ["Trek", "Marlin 7", 29, 850000],
    ["Giant", "Talon 3", 27.5, 720000],
    ["Scott", "Aspect 950", 29, 900000],
    ["Oxford", "Top Mega", 26, 350000],
    ["Bianchi", "Impulso", 28, 1200000]
]

# Si el archivo bicicletas_nuevo.csv no existe, el modo 'w' en la función open lo creará automáticamente.

# Escribir el archivo bicicletas_nuevo.csv
with open('bicicletas_nuevo.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(bicicletas)

print("Archivo 'bicicletas_nuevo.csv' creado correctamente.")
