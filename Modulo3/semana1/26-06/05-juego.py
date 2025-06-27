import random

numero_secreto = random.randint(1, 10)
intento = int(input("Adivina un número del 1 al 10: "))

if intento == numero_secreto:
    print("¡Ganaste! 🎊")
else:
    print(f"¡Perdiste! El número era {numero_secreto} 😅")