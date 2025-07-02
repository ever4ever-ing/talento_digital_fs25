"""
Características de los datos primitivos en Python:
-Inmutables: No se pueden modificar después de ser creados.
-Simples: Representan un solo valor.
-Eficientes: Usan menos memoria y son más rápidos de procesar.

Booleanos: True o False
Númericos:  Int, float
Texto: Str


"""
#Booleanos
notificaciones_activadas = True
if(notificaciones_activadas):
    print("Notificaciones  activadas 🔔")

es_fin_de_semana = False
#El if espera siempre un valor True
if(es_fin_de_semana):
    print("A descansar!")
else:
    print("A trabajar!")

# Númericos

edad = 28
temperatura = 7.5


#Cadenas de texto

nombre = "Skillnest"
mensaje = "Hola mundo!"

#None : Representa la ausencia de valor o un valor nulo

resultado = None
print("id de variable resultado:", id(resultado))
#id() devuelve un identificador único para un objeto, que representa su dirección en memoria
suma = 1+1 
resultado = suma
print("id de variable resultado al modificar:", id(resultado))
print(resultado)








