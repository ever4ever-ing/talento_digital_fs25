for i in range(3):  # Bucle externo
    for j in range(2):  # Bucle interno
        print(f"i: {i}, j: {j}")

print("-"*30)

matriz = [[1, 2], [3, 4]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        # Recorre las columnas de cada fila
        print(matriz[i][j], end=' ')
    print()

print("-"*30)

matriz_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz_3x3:
    for elemento in fila:
        print(elemento, end=' ')
    print()