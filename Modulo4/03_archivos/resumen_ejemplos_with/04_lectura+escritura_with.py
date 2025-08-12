#Original:
""""
Manzanas: 5
Peras: 3
"""
with open("registro.txt", "r+") as file:
    contenido = file.read()
    file.seek(0)#Para posicionar cursor
    file.write("Uva: 6\n" + contenido)#escribe datos
    print("Registrando nuevos datos.")