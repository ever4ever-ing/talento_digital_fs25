def saludar(nombre: str = "Mundo") -> None:
    print(f"Hola, {nombre}!")


def sumar(a: int = 1, b: int = 1) -> int:
    print(f"La suma de {a} y {b} es: {a + b}")
    return a + b

saludar()
sumar(1,2)
sumar(5, 10)





def cantar_cueca(flor: str ="Rosa", veces: int =1) -> None:
    print((f"La {flor}, la {flor} con el Clavel, mi vida hicieron, hicieron un juramento. \n") * veces)

cantar_cueca("Azucena", 3)
