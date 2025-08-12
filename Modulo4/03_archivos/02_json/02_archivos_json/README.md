# Manejo de JSON en Python

## 1. ¿Qué es JSON?
Formato de texto (JavaScript Object Notation) para intercambiar datos. Similar a dict/list en Python.

## 2. Tipos compatibles
JSON -> Python:
- object -> dict
- array -> list
- string -> str
- number -> int | float
- true/false -> True / False
- null -> None

## 3. Módulo estándar
```python
import json
```

## 4. Rutas con pathlib
```python
from pathlib import Path
ruta = Path(__file__).with_name("datos.json")
```

## 5. Leer un archivo JSON
```python
with ruta.open(encoding="utf-8") as f:
    data = json.load(f)
```
Manejo de errores:
```python
try:
    data = json.load(f)
except json.JSONDecodeError as e:
    print("JSON inválido", e)
```

## 6. Escribir JSON (pretty print)
```python
data = {"nombre": "Ana", "edad": 30}
with ruta.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```
Parámetros útiles:
- indent=2 -> formato legible
- ensure_ascii=False -> mantiene caracteres (tildes, ñ)
- sort_keys=True -> ordena claves

## 7. Convertir entre cadenas y objetos
```python
texto = json.dumps(data)        # dict -> str JSON
obj = json.loads(texto)         # str JSON -> dict
```
Útil para APIs, sockets, logs.

## 8. Actualizar archivo JSON
```python
with ruta.open(encoding="utf-8") as f:
    datos = json.load(f)
datos["activo"] = True
with ruta.open("w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)
```

## 9. Serializar objetos no estándar
```python
from datetime import datetime

def default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError("Tipo no serializable")

json.dumps({"ahora": datetime.now()}, default=default)
```
Deserializar personalizado:
```python
def hook(d):
    if "ahora" in d:
        # intentar parsear
        from datetime import datetime
        try:
            d["ahora"] = datetime.fromisoformat(d["ahora"])
        except: pass
    return d

obj = json.loads(texto, object_hook=hook)
```

## 10. Lectura de archivos grandes (streaming sencillo)
Cuando el archivo es una lista enorme:
```python
import json
with open("grande.json", encoding="utf-8") as f:
    for linea in f:  # si es JSONL (una entidad por línea)
        registro = json.loads(linea)
        # procesar
```
Para JSON estándar muy grande se necesitan librerías como ijson (parsing incremental).

## 11. Validación rápida
```python
try:
    json.loads(texto)
    print("JSON válido")
except json.JSONDecodeError as e:
    print("Error:", e)
```

## 12. Buenas prácticas
- Siempre usar encoding="utf-8".
- Manejar FileNotFoundError y JSONDecodeError.
- No usar eval para JSON.
- Usar indent solo en desarrollo (sin indent produce archivos más pequeños).
- Respaldar antes de sobrescribir archivos importantes.

## 13. Ejemplos incluidos
- 01_leer_json.py -> lectura y extracción de campos.
- 02_escribir_json.py -> escritura formateada.
- datos.json -> archivo de ejemplo.

## 14. Ejecución
```bash
python 01_leer_json.py
python 02_escribir_json.py
```

Listo para reutilizar en otros proyectos.
