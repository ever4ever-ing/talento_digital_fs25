tupla_letras = ("a", "e", "i", "o", "u")
print(tupla_letras)
print(type(tupla_letras))

tupla_sin_parentesis = "a", "e", "i", "o", "u"
print(tupla_sin_parentesis)

gato = ("Miu", 5, "persa", False)
print(gato)

gato = ("Miu", 5, ['a','b','c'], False)
print(gato)
print(gato[2]) 
print(type(gato[2]))

#gato[0] = "Michi" #No se puede modificar tuplas

gato = gato + ("4.1",)
print(gato)
#gato = gato + ["4.1","4.2"] #No se puede concatenar otro tipo de dato

print(len(gato))
#print(max(gato)) #No compara entre tipos de datos 
print(max(tupla_letras))
print(sorted(tupla_letras))
tupla_num=(1.5,2,3)
print(sum(tupla_num))

