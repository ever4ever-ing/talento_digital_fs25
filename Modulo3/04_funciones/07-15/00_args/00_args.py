#ARGUMENTOS VARIABLES
#Argumentos posicionales variables
#*args permite recibir cualquier cantidad de argumentos posicionales y los agrupa en una tupla.

def suma(*numeros):
    print(type(numeros))
    print(f"Argumentos recibidos: {numeros}")
    resultado = sum(numeros)
    return resultado

variable=suma()
print(suma(1,24))
print("-"*30)


#Argumentos de Palabra Clave variables

#**kwargs permite recibir cualquier cantidad de argumentos nombrados y los agrupa en un diccionario.
def mostrar_info(**datos):
    print(datos)
    print(datos.keys())
    print(datos.values())

mostrar_info(saludo="hola")
mostrar_info(saludo="hola", nombre="mundo")
mostrar_info(nombre='Juan', edad=25, ciudad='Madrid')

#mostrar_info(nombre='Ana', edad=30)

