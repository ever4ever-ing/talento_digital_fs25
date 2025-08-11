with open("mi_archivo.txt", "r+") as file:
    contenido = file.read()
    print(contenido)
    file.write("Añadiendo otra línea al final.")
    print(contenido)

#contenido = file.read()