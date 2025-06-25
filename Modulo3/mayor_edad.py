"""
Este programa analiza si la persona cumple la mayoria de edad
"""

import keyword
print(keyword.kwlist)

edad = 0
edad = float(input("Ingresa tu edad: "))

if edad >= 18:
    print("Es mayor de edad")
elif edad >= 17.5:
    print("Pronto seras mayor de edad.")
else:
    print("No es mayor de edad.")
