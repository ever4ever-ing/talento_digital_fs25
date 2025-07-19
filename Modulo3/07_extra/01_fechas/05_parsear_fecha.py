from datetime import datetime

# Parsear un string a fecha
fecha_str = "25/12/2025"
fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
print(f"Fecha parseada: {fecha}")
