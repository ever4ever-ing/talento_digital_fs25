import os
nombre_archivo = 'archivo1.txt'
ruta_dinamica = os.path.join('.', nombre_archivo) 
print("Ruta dinámica:", ruta_dinamica)
try:
    with open(ruta_dinamica, 'r') as f:  # No se necesita f.close()
        contenido = f.read()
        print("El contenido:",contenido)
except FileNotFoundError:
    print("El archivo no se encuentra.")
else:
    print("El archivo se leyó correctamente.")