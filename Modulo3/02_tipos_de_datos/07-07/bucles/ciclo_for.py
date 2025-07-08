print("Range con fin (hasta el 4)")
print("-"*20)
for i in range(4):
    print(i)
    print("Esto es un bucle!")
    print("-"*10)
print("Estoy fuera del bucle")




print("Range con inicio y fin (2 al 8)")
print("-"*20)
for i in range(2, 80):

    print(i)



print("Range con inicio, fin y paso (2 al 12 con paso 3)")
print("-"*20)
for i in range(2, 12, 3):
    print(i)

#ORDEN INVERTIDO
print("Range invertido con inicio, fin y paso (10 al 1 y paso -1)")
print("-"*20)
for i in range(10, 1,-1):
    print(i)

print("Range invertido con inicio, fin y paso (10 al 1 y paso -2)")
print("-"*20)
for i in range(10, 1,-2):
    print(i)


print("Range invertido con inicio, fin y paso (10 al 1 y paso -3)")
print("-"*20)
for i in range(10, 1,-3):
    print(i)

print("Range con flotantes")

for i in range(0, 10):
    valor = i * 0.1
    print(f"{valor:.1f}")

##EXTRA
import numpy as np
print("Range con flotantes usando numpy")
for i in np.arange(0.0, 1.0, 0.1):
    print(f"{i:.1f}")

import numpy as np

for x in np.linspace(0.0, 1.0, num=11):
    print(f"{x:.1f}")

#Iterando strings:
print("Iterando strings:")
print("-"*30)


for letra in 'Python':
    print(letra)
#Imprime: 'P', 'y', 't', 'h', 'o', 'n'
print("-"*30)

palabra= 'Python'
la_te= palabra[2]
print("Letra:",la_te)
#USANDO BREAK
for letra in palabra:
    print(letra)
    if(letra == la_te):
        print("Encontraste la T.")
        break #rompe el ciclo
    print("Seguimos aprendiendo bucles.")

print("Seguimos aprendiendo.")

print("-"*30)

for letra in palabra:
    if(letra == "h"):
        print("Encontre una H.")
        continue #se salta a la sgt iteracion
    print(letra)



