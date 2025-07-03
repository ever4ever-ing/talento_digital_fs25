"""
Diccionarios (dict)
Mutables: Se pueden modificar después de su creación.
Clave-Valor: Almacenan pares de clave-valor únicos.
Sintaxis: Se definen con llaves {} o dict().

"""

print("\n DICCIONARIOS")
print("-" * 40)
# 1. CREACIÓN DE DICCIONARIOS

diccionario_vacio = {}
diccionario_vacio2 = dict()


# Diccionario con datos iniciales
persona = {
    "nombre": "Everardo",
    "edad": 28,
    "ciudad": "Temuco"
}

dato = [("a", 1), ("b", 2), ("c", 3)]
diccionario= dict(dato)
print(type(diccionario))
print(diccionario)

lista= [["a",1],["b",2]]
diccionario_lista= dict(lista)


#Acceso y modificacion

print("-" * 40)
print("Acceso y modificacion")

mascota= {
    "nombre": "Ratanaz",
    "edad": 7,
    "especie": "Gato",
    "color": "gris"
}
# Acceso directo
print("Edad es ", mascota["edad"])
# Acceso con get()
print("Edad es ", mascota.get("edad"))
print("Telefono contacto es ",
    mascota.get("contacto", -1))
print("Color es ",mascota.get("color"))
# Modificar valores existentes
mascota["edad"]= 8
print(mascota.get("edad"))
mascota.update({"edad":9})
print(mascota.get("edad"))
#Agregar nuevo par clave-valor
print(mascota)
mascota["contacto"]= "+56912345678"
print(mascota)
#Eliminar número
del mascota["contacto"]
print(mascota)






