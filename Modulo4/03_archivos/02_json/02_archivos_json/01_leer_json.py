# Importa el módulo estándar para trabajar con JSON (parsear y serializar).
import json
# Importa Path para manejar rutas de forma más segura y portable.
from pathlib import Path

# Ruta al archivo JSON (mismo directorio que este script)
# Construye la ruta al archivo datos.json en el mismo folder del script.
RUTA_JSON = Path(__file__).with_name("datos.json")


def leer_json(ruta: Path):
    """Lee un archivo JSON y muestra algunos campos básicos."""
    try:
        # Abre el archivo en modo lectura de texto usando codificación UTF-8.
        with ruta.open(encoding="utf-8") as f:
            # Convierte el contenido JSON del archivo a un diccionario (u otras estructuras).
            data = json.load(f)
        # Muestra el objeto completo (dict).
        print("Contenido completo:", data)
        # Accede de forma segura a la clave 'nombre'.
        print("Nombre:", data.get("nombre"))
        # Accede de forma segura a la clave 'edad'.
        print("Edad:", data.get("edad"))
        # Une la lista de hobbies (si existe) en una cadena separada por comas. Si no existe, usa lista vacía.
        print("Hobbies:", ", ".join(data.get("hobbies", [])))
        return data  # Devuelve el diccionario para posible reutilización.
    except FileNotFoundError:
        # Se ejecuta si el archivo no existe en la ruta indicada.
        print(f"Archivo no encontrado: {ruta}")

# Punto de entrada cuando se ejecuta directamente el script.
if __name__ == "__main__":
    leer_json(RUTA_JSON)
