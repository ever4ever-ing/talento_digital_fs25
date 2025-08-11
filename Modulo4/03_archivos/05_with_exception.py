try:
    # Intentar abrir un archivo
    with open("mi_archivo.txt", "r") as file:
        contenido = file.read()
        print("Archivo leído correctamente.")
except FileNotFoundError:
    print("El archivo no existe.")
except IOError:
    print("Hubo un error al intentar leer el archivo.")
