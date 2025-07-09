tupla = ('fresa', 'manzana', 'cereza')
print("-" * 20)
print("Usando range: ")
for i in range( len(tupla) ):
    print(i, tupla[i])

print("-" * 40)
print("Usando In: ")

for fruta in tupla:

    print(fruta)