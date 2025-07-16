# Usando argumentos variables en una función para hacer una pizza

def hacer_pizza(tamaño, *ingredientes):
    print(f"\nHaciendo una pizza {tamaño} con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")











    """
    Imprime el tipo de pizza y sus ingredientes.

    Parámetros:
        tamaño (str o int): Tamaño de la pizza.
        *ingredientes (str): Ingredientes de la pizza.

    Retorna:
        None
    """