while True:
    try:
        lista = [1, 2, 3]
        indice = int(input("Ingresa un índice (0-2): "))
        print(f"Elemento en índice {indice}: {lista[indice]}")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")