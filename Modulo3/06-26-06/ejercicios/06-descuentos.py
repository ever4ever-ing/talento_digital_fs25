"""
Define las variables con los siguientes datos:
Precio original de un pantalón: $4599.
Precio original de unos zapatos: $7999.
Porcentaje de descuento para ropa: 20%.
Porcentaje de descuento para calzado: 15%.
Calcula el precio final para cada producto aplicando su respectivo descuento.
Pista: El precio final se calcula como precio_original * (1 - descuento / 100).
Muestra los precios finales en la consola. 
Bonus:
Calcula el ahorro total sumando la cantidad que te ahorraste en cada producto.
Muestra el ahorro total en la consola con el siguiente formato: ¡Ahorraste $ahorro_total en total!

"""
# Precios originales (float)
precio_pantalon = 4599  
precio_zapatos = 7999  
# Descuentos (int convertido a float para cálculos)
descuento_ropa = 20  # 20%
descuento_calzado = 15  # 15%
#Calculo
precio_final_ropa = round(precio_pantalon * (1 - descuento_ropa / 100))
precio_final_calzado = round(precio_zapatos * (1 - descuento_calzado / 100))
# Resultado (str + float redondeado)
print(f" El pantalón cuesta ${precio_final_ropa} (antes ${precio_pantalon})")  
print(f" Los zapatos cuestan ${precio_final_calzado} (antes ${precio_zapatos})")
##BONUS
ahorro_ropa = precio_pantalon - precio_final_ropa
ahorro_calzado = precio_zapatos - precio_final_calzado
ahorro_total = ahorro_ropa + ahorro_calzado
print(f"¡Ahorraste ${ahorro_total} en total!")