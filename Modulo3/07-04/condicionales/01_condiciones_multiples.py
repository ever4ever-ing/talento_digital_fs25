"""
Operadores lógicos
AND, OR, NOT
"""
#1. AND: (ambas condiciones deben ser verdaderas)
print("-"*30)
print("AND: (ambas condiciones deben ser verdaderas)")
fruta = "manzana"
color = "rojo"
dulce = True
if fruta == "manzana" and color == "rojo" and dulce:
    print("Es una manzana dulce de color rojo ")
else:
    print("No es un manzana dulce de color rojo ")
#2. OR  (al menos una condición debe ser verdadera)
print("-"*30)
print("OR  (al menos una condición debe ser verdadera)")
fruta = "kiwi"
if fruta == "kiwi" or fruta == "mandarina" or fruta=="guayaba":
    print("Esta fruta tiene mucha vitamina C")
else:
    print("No tiene tanta vitamina C.")

#3. Usando not (invierte el valor de la condición)
print("-"*30)
print(" Usando not (invierte el valor de la condición)")
fruta = "naranja"
if not fruta == "manzana":
    print("No es una manzana, es una", fruta)
else:
    print("Es una manzana.")
#4. Combinando and, or y not
#Actividad: Combinar operadores logicos en un condicional if
print("-"*30)
print("Combinando and, or y not")
fruta = "arandano"
verde = False
precio = 1800
if (fruta == "arandano" or fruta == "mora") and not verde and (precio < 2000):
    print("¡Oferta! Puedes comprar estas frutas frescas y baratas.")
else:
    print("No aplica la oferta.")


####

print("-"*30)
paltas_precio = 3990
cantidad_kilos = 0
suavidad= False
duras= True
tomates_precio = 2000
if paltas_precio < 4990 and not duras or tomates_precio < 2500:
    print("Se hacen completos.")
else:
    print("No se hacen completos hoy.")

####
print("-"*30)
fruta = "pera"
costo = "alto"
tiempo_entrega = 60
if not costo == "bajo" and fruta == "pera"  and (tiempo_entrega < 50):
    print ("comprar peras")
else:
    print("seguir buscando")