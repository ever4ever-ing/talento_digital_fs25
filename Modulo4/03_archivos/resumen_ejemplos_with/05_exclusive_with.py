try:
    with open("config.json", "x") as file:
        file.write('{"usuario": "admin"}')
    print("Archivo creado")
except FileExistsError:
    print("Error: El archivo ya existe")