
from datetime import datetime

fechas = [
datetime(2025, 7, 1),
datetime(2023, 12, 25),
datetime(2024, 5, 10)
]

# Ordenar de menor a mayor (más antigua a más reciente)
fechas.sort()

for fecha in fechas:
    print(fecha.strftime("%Y-%m-%d"))
