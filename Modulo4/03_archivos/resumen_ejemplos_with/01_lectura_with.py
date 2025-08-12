try:
    with open("mi_archivo0.txt", "r") as file:
        contenido = file.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")