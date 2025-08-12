"""
Sobreescribe lo existente.
"""
with open("datos.txt", "w") as file:
    file.write("notas_actualizas: 7.0 , 6.5, 6.9")
    print("Se ha sobreescrito el archivo.")