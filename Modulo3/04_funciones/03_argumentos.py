def buenos_dias(nombre="alegría", cantidad=4):
    texto = ("\nBuenos días "+nombre ) *cantidad
    print(("\nBuenos días "+nombre) * cantidad)
    return texto

texto1 = buenos_dias()

texto2 = buenos_dias("al amor")

print("El texto es:",texto1)

buenos_dias(nombre="a la vida")
buenos_dias(cantidad=3)

buenos_dias(nombre="señor Sol", cantidad=2)
buenos_dias("x",5)
