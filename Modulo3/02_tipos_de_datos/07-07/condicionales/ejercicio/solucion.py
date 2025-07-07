
material = input("Material (cuero/tela/sintético): ").lower()
precio = float(input("Precio ($): "))
garantia = int(input("Garantía (años): "))

if material == "cuero" and precio > 100000 and garantia > 1:
    # Alta calidad (cumple los 3 criterios )
    print(" Alta calidad: Excelentes materiales, durabilidad y confianza.")
elif (material == "tela" and precio >= 50000) or (garantia >= 1): 
    # Calidad media (al menos 2 criterios medios/altos )
    print(" Calidad media: Al menos dos criterios.")
else:                         
    # Baja calidad (no cumple requisitos )
    print(" Baja calidad: No cumple con los estándares mínimos.")
