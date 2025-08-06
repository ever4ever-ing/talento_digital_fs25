try:
    with open('./archivo1.txt', 'r') as f:  # No se necesita f.close()
        contenido = f.read()
        print("El contenido:",contenido)
except FileNotFoundError:
    print("El archivo no se encuentra.")
else:
    print("El archivo se leyó correctamente.")