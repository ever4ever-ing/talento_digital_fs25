# Leer todo el contenido
file = open("mi_archivo.txt", "r")
contenido = file.read()
print("Contenido:", contenido)
file.close()

# Leer una sola línea
file = open("mi_archivo.txt", "r")
linea = file.readline()
print("Linea1:",linea)
linea = file.readline()
print("Linea2:",linea)
linea = file.readline()
print("Linea n:",linea)


print("hola \nhola2")
file.close()


