# Módulo estándar para trabajar con datos en formato JSON (serializar/deserializar)
import json
from pathlib import Path  # Para manejar rutas de archivos de forma portable

# Ruta al archivo JSON que contiene los asistentes al evento
RUTA_ASISTENTES = Path(__file__).with_name("asistentes.json")

def leer_asistentes_simple(ruta: Path):
    """Lee el archivo JSON e imprime 'nombre - rol' por asistente."""
    try:
        with ruta.open(encoding="utf-8") as f:
            data = json.load(f)
        for persona in data.get("asistentes", []):
            nombre = persona.get("nombre", "(sin nombre)")
            rol = persona.get("rol", "(sin rol)")
            print(f"{nombre} - {rol}")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
    except json.JSONDecodeError as e:
        print(f"JSON inválido: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    leer_asistentes_simple(RUTA_ASISTENTES)
