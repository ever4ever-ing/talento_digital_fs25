
# BREAK
print("BREAK")
for i in range(7):
    print(i)
    for letra in "detente":
        if letra == "n":
            break
        print("\t |", letra)

print("-"*30)
# CONTINUE
print("CONTINUE")
for letra in "detente":
    if letra == "n":
        continue
    # ------------------   NO SE EJECUTA
    print(letra)


# BREAK & ELSE

print("BREAK & ELSE")
x = 6

while x > 2:
    print(x)
    x -= 1
    if x == 3:
        break
else:  # Recuerda: Solo se ejecuta en una salida normal, NO en un break
    print("Sentencia final")

print("-"*30)

x = 3

while x > 2:
    print(x)
    x -= 1
    if x == 3:
        break
else:  # Recuerda: Solo se ejecuta en una salida normal, NO en un break
    print("Sentencia final")
