a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("a:", a)
print("b",b)

# Unión
print("Union:")
print(a | b) 
# Intersección
print("Intersección:")
print(a & b)  # {3, 4}
print("Diferencia:")
# Diferencia (elementos en a que no están en b)
print(a - b)
# Diferencia simétrica (elementos que están en a o b pero no en ambos)
print("Diferencia simetrica:")
print(a ^ b) 
