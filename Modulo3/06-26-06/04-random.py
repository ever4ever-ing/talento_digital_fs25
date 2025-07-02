import random
# Ejemplo 1: Dado de 6 caras 
dado = random.randint(1,6)
i = 0
while(i<3):
    break
    intento = input("Introduce un numero:")
    if intento == dado:
        print(f"Adivinaste: {dado}")
        break
    else:
        print(f"Lo siento, intenta nuevamene.")
        i+=1
print(f"Juego finalizado. (El numero era:{dado})")

amigos = ["Ana", "Luis", "Carlos", "Mía","Peter"] #Listas
ganador = random.choice(amigos)
print(f"🎉 ¡{ganador} paga la pizza! 🍕")  


# Ejemplo 3: Mezclar una lista (como barajar cartas)

cartas = ["A♠", "K♥", "Q♦", "J♣"]
random.shuffle(cartas)
print("Cartas mezcladas:", cartas) 

