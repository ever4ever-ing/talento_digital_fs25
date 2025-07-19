from datetime import date, timedelta

# Sumar o restar días a una fecha
hoy = date.today()
manana = hoy + timedelta(days=1)
ayer = hoy - timedelta(days=1)
print(f"Hoy: {hoy}")
print(f"Mañana: {manana}")
print(f"Ayer: {ayer}")
ayer = hoy - timedelta(days=2)
print(f"Anteayer (dos días atrás): {ayer}")