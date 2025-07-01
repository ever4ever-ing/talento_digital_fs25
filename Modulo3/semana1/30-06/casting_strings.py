tiempo_preparacion = 1

tiempo_horneado = "2"

#tiempo_total = tiempo_preparacion + tiempo_horneado 

tiempo_total = tiempo_preparacion + int(tiempo_horneado) #Imprime: 3
print(f"El tiempo total de la receta es: {tiempo_total} horas")