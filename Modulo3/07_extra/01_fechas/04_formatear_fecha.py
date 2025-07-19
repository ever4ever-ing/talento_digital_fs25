from datetime import datetime

# Formatear una fecha a string
now = datetime.now()
formato = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha formateada: {formato}")

formato2 = now.strftime("%H:%M:%S")
print(f"Fecha formateada: {formato2}")
