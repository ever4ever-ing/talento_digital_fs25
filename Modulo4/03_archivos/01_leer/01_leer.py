import csv

# Leer el archivo bicicletas.csv de forma sencilla
with open('bicicletas1.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo) #delimiter=";" en caso de que sea con ;
    encabezados = next(lector)# con next se obtiene la primera fila
    print(f"Encabezados: {encabezados}")
    print("Datos:")
    for fila in lector: # Iterar sobre las filas restantes
        print(fila)
