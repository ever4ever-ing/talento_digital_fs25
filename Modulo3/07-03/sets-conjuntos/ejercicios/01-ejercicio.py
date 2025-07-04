"""
Ejercicio 1
Crea un set con los días de la semana. Luego:
Añade "domingo" si no está presente
Elimina un día cualquiera
Verifica si "lunes" está en el set

"""
#Solucion:
dias = {"lunes","martes","miercoles","jueves","viernes","sabado"}
dias.add("domingo")
print(dias)
dias.remove("lunes")
print(dias)
print("lunes" in dias)
