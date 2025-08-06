f = None
while True:
    try:
        name_file = input("Ingresa el nombre del archivo: ")
        f = open(name_file, 'r') #ABRIR ARCHIVO
        contenido = f.read() #LECTURA DE ARCHIVO
    except FileNotFoundError:
        print("El archivo no se encuentra.")
    else:
        print("El archivo se leyó correctamente.")
        input("Presiona Enter para continuar...")
    finally:
        print("Cerrando el archivo...")
        if f is not None:
            f.close()  # Este bloque se ejecuta siempre, cerrando el archivo.
