# Escribir en un archivo
file = open("mi_archivo.txt", "w")
file.write("Esto es una nueva línea de texto. ")
file.close()

# Añadir contenido a un archivo existente
file = open("mi_archivo.txt", "a")
file.write("Añadiendo otra línea al final.")
file.close()
