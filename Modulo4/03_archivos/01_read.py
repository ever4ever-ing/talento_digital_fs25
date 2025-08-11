# Abrir un archivo para leer
file = open("mi_archivo.txt", "r")

# Leer todo el contenido del archivo
contenido = file.read()
print(contenido)
# Cerrar el archivo después de usarlo
file.close()
