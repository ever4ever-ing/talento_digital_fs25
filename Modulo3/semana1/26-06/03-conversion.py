#Las conversiones (int(), str(), etc.) son como disfraces.

edad = 28
edad_txt= str(edad)
print("Tengo "+edad_txt+" años.")


# De str a int (texto a número)  
puntaje = "70"
bonus = float(puntaje) * 1.1
print("Tu puntaje final es:", bonus)

# De float a int
peso = 2.9
peso_entero = int(peso)
print(peso_entero)


#booleano

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool("Hola"))
print(bool("Chao"))
