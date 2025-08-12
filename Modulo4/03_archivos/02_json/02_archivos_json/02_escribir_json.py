import json
from pathlib import Path

RUTA_SALIDA = Path(__file__).with_name("salida.json")

def escribir_json(data: dict, ruta: Path):
    """Escribe un diccionario a un archivo JSON con formato legible."""
    try:
        with ruta.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Archivo JSON escrito en: {ruta}")
    except Exception as e:
        print(f"Error al escribir JSON: {e}")

if __name__ == "__main__":
    datos = {
        "nombre": "Ana",
        "edad": 30,
        "hobbies": ["leer", "correr", "cine"],
        "activo": True
    }
    escribir_json(datos, RUTA_SALIDA)
