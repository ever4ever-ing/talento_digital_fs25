# Importa el módulo estándar para trabajar con JSON (parsear y serializar).
import json
# Importa Path para manejar rutas de forma más segura y portable.
from pathlib import Path

# Ruta al archivo JSON (mismo directorio que este script)
# Construye la ruta al archivo datos.json en el mismo folder del script.
ruta = Path(__file__).with_name("datos.json")

try:
    # Abre el archivo en modo lectura de texto usando codificación UTF-8.
    with ruta.open(encoding="utf-8") as f:
        # Convierte el contenido JSON del archivo a un diccionario (u otras estructuras).
        data = json.load(f)
    # Muestra el objeto completo (dict).
    print("Contenido completo:", data)
    # Accede de forma segura a la clave 'nombre'.
    print("Nombre:", data.get("nombre"))
except FileNotFoundError:
    # Se ejecuta si el archivo no existe en la ruta indicada.
    print(f"Archivo no encontrado: {ruta}")
