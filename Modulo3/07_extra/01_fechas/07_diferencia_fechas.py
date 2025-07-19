from datetime import date
# Diferencia entre fechas
fecha1 = date(2025, 7, 18)
fecha2 = date(2025, 8, 1)
diferencia = fecha2 - fecha1
print(f"Días de diferencia: {diferencia.days}")
print(f"Meses de diferencia: {diferencia.days // 30}")#  división entera
print(f"Años de diferencia: {diferencia.days // 365}") #  división entera
print(f"Minutos de diferencia: {diferencia.total_seconds() // 60}")
print(f"Horas de diferencia: {diferencia.total_seconds() // 3600}")