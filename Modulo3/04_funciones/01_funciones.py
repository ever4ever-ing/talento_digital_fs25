#Crear una funcion para hacer taco, debe devolver un diccionario del taco preparado
def hacer_taco(tortilla, guiso, salsa, complementos):
    print("-"*30)
    print("Calentando la tortilla...")
    print(f"Preparando el guiso: {guiso}")
    print(f"Colocando el guiso en la tortilla de {tortilla}")
    print(f"Poniendo un poco de salsa: {salsa}")
    print(f"Agregando los complementos: {', '.join(complementos)}")
    # Agrega los complementos separados por comas
    taco = {
        "tortilla": tortilla,
        "guiso": guiso,
        "salsa": salsa,
        "complementos": complementos
    }
    return taco

taco=hacer_taco("maíz", "carne molida", "salsa de ají", ["cebolla", "cilantro", "limón"])
taco_piero =  hacer_taco("hallulla", "carne", "ketchup", ["queso amarillo"])
print("Taco piero",taco_piero)

#Hacer una funcion que prepare un completo u otra comida















def hacer_completo(salchicha,pan, palta,tomate):
    print("-"*30)
    print("Calentando la salchicha...")
    print(f"Colocando la salchicha en el pan: {pan}")
    print(f"Agregando palta: {palta}")
    print(f"Agregando tomate: {tomate}")
    completo = {
        "salchicha": salchicha,
        "pan": pan,
        "palta": palta,
        "tomate": tomate
    }
    

hacer_completo("salchicha de pavo", "pan de completo", "palta molida", "tomate picado")
