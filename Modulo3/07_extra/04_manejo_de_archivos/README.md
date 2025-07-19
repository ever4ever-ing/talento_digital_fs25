# 📁 Ejemplos de Manejo de Archivos en Python

Este repositorio contiene ejemplos completos y prácticos para trabajar con archivos en Python. Incluye diferentes tipos de archivos y operaciones comunes que encontrarás en el desarrollo de aplicaciones.

## 📋 Tabla de Contenidos

1. [Lectura Básica de Archivos](#1-lectura-básica-de-archivos)
2. [Escritura de Archivos](#2-escritura-de-archivos)
3. [Manejo de Errores](#3-manejo-de-errores)
4. [Trabajar con JSON](#4-trabajar-con-json)
5. [Trabajar con CSV](#5-trabajar-con-csv)
6. [Operaciones con Directorios](#6-operaciones-con-directorios)
7. [Procesamiento de Archivos Grandes](#7-procesamiento-de-archivos-grandes)
8. [Consejos y Mejores Prácticas](#consejos-y-mejores-prácticas)

---

## 1. Lectura Básica de Archivos

### Ejemplo Completo

```python
def ejemplo_lectura_basica():
    """Ejemplo básico de lectura de archivos"""
    print("=== LECTURA BÁSICA ===")
    
    # Crear un archivo de ejemplo
    with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Hola mundo\n")
        archivo.write("Este es un archivo de ejemplo\n")
        archivo.write("Python es genial!")
    
    # Método 1: Leer todo el archivo
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido completo:")
        print(contenido)
    
    print("-" * 40)
    
    # Método 2: Leer línea por línea
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        print("Leyendo línea por línea:")
        for numero_linea, linea in enumerate(archivo, 1):
            print(f"Línea {numero_linea}: {linea.strip()}")
    
    print("-" * 40)
    
    # Método 3: Leer todas las líneas en una lista
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        print("Todas las líneas en lista:")
        for i, linea in enumerate(lineas):
            print(f"[{i}]: {linea.strip()}")
```

### 📝 Métodos de Lectura

| Método | Descripción | Uso Recomendado |
|--------|-------------|-----------------|
| `read()` | Lee todo el archivo | Archivos pequeños |
| `readline()` | Lee línea por línea | Control manual |
| `readlines()` | Lee todas las líneas en lista | Procesamiento posterior |
| `for linea in archivo` | Iteración directa | **Más eficiente** |

---

## 2. Escritura de Archivos

### Ejemplo Completo

```python
def ejemplo_escritura():
    """Ejemplos de escritura en archivos"""
    print("\n=== ESCRITURA DE ARCHIVOS ===")
    
    # Modo 'w' - Sobreescribe el archivo
    datos = ["Primera línea", "Segunda línea", "Tercera línea"]
    
    with open("escritura_ejemplo.txt", "w", encoding="utf-8") as archivo:
        for dato in datos:
            archivo.write(f"{dato}\n")
    
    print("Archivo creado con modo 'w'")
    
    # Modo 'a' - Añade al final del archivo
    with open("escritura_ejemplo.txt", "a", encoding="utf-8") as archivo:
        archivo.write("Línea añadida\n")
        archivo.write("Otra línea más\n")
    
    print("Contenido añadido con modo 'a'")
    
    # Verificar el contenido
    with open("escritura_ejemplo.txt", "r", encoding="utf-8") as archivo:
        print("Contenido final:")
        print(archivo.read())
```

### 📝 Modos de Apertura

| Modo | Descripción | Comportamiento |
|------|-------------|----------------|
| `'w'` | Escritura | Sobreescribe el archivo |
| `'a'` | Añadir | Agrega al final |
| `'x'` | Creación exclusiva | Falla si existe |
| `'r+'` | Lectura y escritura | Debe existir |

---

## 3. Manejo de Errores

### Ejemplo Completo

```python
def ejemplo_manejo_errores():
    """Ejemplo de manejo de errores al trabajar con archivos"""
    print("\n=== MANEJO DE ERRORES ===")
    
    # Intentar leer un archivo que no existe
    try:
        with open("archivo_inexistente.txt", "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("❌ Error: El archivo no existe")
    except PermissionError:
        print("❌ Error: No tienes permisos para acceder al archivo")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    # Verificar si un archivo existe antes de abrirlo
    nombre_archivo = "ejemplo.txt"
    if os.path.exists(nombre_archivo):
        print(f"✅ El archivo '{nombre_archivo}' existe")
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            print("Primeras 50 caracteres:", archivo.read(50))
    else:
        print(f"❌ El archivo '{nombre_archivo}' no existe")
```

### 🚨 Errores Comunes

| Excepción | Causa | Solución |
|-----------|-------|----------|
| `FileNotFoundError` | Archivo no existe | Verificar con `os.path.exists()` |
| `PermissionError` | Sin permisos | Cambiar permisos o ubicación |
| `IOError` | Error de E/S | Verificar disco/conexión |
| `UnicodeDecodeError` | Codificación incorrecta | Especificar `encoding` |

---

## 4. Trabajar con JSON

### Ejemplo Completo

```python
def ejemplo_json():
    """Ejemplo de trabajo con archivos JSON"""
    print("\n=== ARCHIVOS JSON ===")
    
    # Datos de ejemplo
    datos_estudiantes = {
        "estudiantes": [
            {"nombre": "Ana", "edad": 22, "carrera": "Ingeniería"},
            {"nombre": "Carlos", "edad": 24, "carrera": "Medicina"},
            {"nombre": "María", "edad": 23, "carrera": "Derecho"}
        ],
        "curso": "Python Básico",
        "año": 2025
    }
    
    # Escribir JSON
    with open("estudiantes.json", "w", encoding="utf-8") as archivo:
        json.dump(datos_estudiantes, archivo, indent=4, ensure_ascii=False)
    
    print("Archivo JSON creado")
    
    # Leer JSON
    with open("estudiantes.json", "r", encoding="utf-8") as archivo:
        datos_leidos = json.load(archivo)
    
    print("Datos leídos del JSON:")
    print(f"Curso: {datos_leidos['curso']}")
    print("Estudiantes:")
    for estudiante in datos_leidos["estudiantes"]:
        print(f"  - {estudiante['nombre']}, {estudiante['edad']} años, {estudiante['carrera']}")
```

### 📊 Funciones JSON

| Función | Descripción | Uso |
|---------|-------------|-----|
| `json.dump()` | Escribe objeto a archivo | Guardar datos |
| `json.load()` | Lee objeto desde archivo | Cargar datos |
| `json.dumps()` | Convierte a string JSON | APIs/transmisión |
| `json.loads()` | Convierte desde string JSON | Procesar respuestas |

---

## 5. Trabajar con CSV

### Ejemplo Completo

```python
def ejemplo_csv():
    """Ejemplo de trabajo con archivos CSV"""
    print("\n=== ARCHIVOS CSV ===")
    
    # Datos de ejemplo
    datos_productos = [
        ["Producto", "Precio", "Stock"],
        ["Laptop", 899.99, 15],
        ["Mouse", 29.99, 50],
        ["Teclado", 79.99, 30],
        ["Monitor", 299.99, 10]
    ]
    
    # Escribir CSV
    with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos_productos)
    
    print("Archivo CSV creado")
    
    # Leer CSV
    print("Leyendo CSV:")
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(f"  {fila}")
    
    # Leer CSV como diccionario
    print("\nLeyendo CSV como diccionario:")
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(f"  {fila['Producto']}: ${fila['Precio']} (Stock: {fila['Stock']})")
```

### 📈 Clases CSV

| Clase | Descripción | Ventaja |
|-------|-------------|---------|
| `csv.writer()` | Escribe filas como listas | Simple y directo |
| `csv.reader()` | Lee filas como listas | Acceso por índice |
| `csv.DictWriter()` | Escribe usando diccionarios | Más legible |
| `csv.DictReader()` | Lee usando diccionarios | Acceso por nombre |

---

## 6. Operaciones con Directorios

### Ejemplo Completo

```python
def ejemplo_directorios():
    """Ejemplo de operaciones con directorios"""
    print("\n=== OPERACIONES CON DIRECTORIOS ===")
    
    # Directorio actual
    print(f"Directorio actual: {os.getcwd()}")
    
    # Crear directorio
    nombre_directorio = "ejemplo_directorio"
    if not os.path.exists(nombre_directorio):
        os.makedirs(nombre_directorio)
        print(f"Directorio '{nombre_directorio}' creado")
    else:
        print(f"El directorio '{nombre_directorio}' ya existe")
    
    # Listar archivos en el directorio actual
    print("\nArchivos en el directorio actual:")
    for elemento in os.listdir("."):
        if os.path.isfile(elemento):
            tamaño = os.path.getsize(elemento)
            print(f"  📄 {elemento} ({tamaño} bytes)")
        elif os.path.isdir(elemento):
            print(f"  📁 {elemento}/")
    
    # Crear archivo en el subdirectorio
    ruta_archivo = os.path.join(nombre_directorio, "archivo_en_subdirectorio.txt")
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("Este archivo está en un subdirectorio")
    
    print(f"Archivo creado en: {ruta_archivo}")
```

### 📁 Funciones de OS

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `os.getcwd()` | Directorio actual | `/home/user/proyecto` |
| `os.listdir()` | Lista contenido | `['file1.txt', 'dir1']` |
| `os.makedirs()` | Crea directorios | Incluye padres |
| `os.path.join()` | Une rutas | Multiplataforma |
| `os.path.exists()` | Verifica existencia | `True`/`False` |

---

## 7. Procesamiento de Archivos Grandes

### Ejemplo Completo

```python
def ejemplo_archivos_grandes():
    """Ejemplo de procesamiento eficiente de archivos grandes"""
    print("\n=== ARCHIVOS GRANDES ===")
    
    # Crear un archivo grande de ejemplo
    with open("archivo_grande.txt", "w", encoding="utf-8") as archivo:
        for i in range(1000):
            archivo.write(f"Esta es la línea número {i+1}\n")
    
    print("Archivo grande creado (1000 líneas)")
    
    # Procesamiento línea por línea (eficiente para archivos grandes)
    contador_lineas = 0
    palabras_totales = 0
    
    with open("archivo_grande.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            contador_lineas += 1
            palabras_totales += len(linea.split())
    
    print(f"Total de líneas: {contador_lineas}")
    print(f"Total de palabras: {palabras_totales}")
    
    # Leer solo las primeras N líneas
    print("\nPrimeras 5 líneas:")
    with open("archivo_grande.txt", "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo):
            if i >= 5:
                break
            print(f"  {linea.strip()}")
```

### ⚡ Técnicas para Archivos Grandes

| Técnica | Ventaja | Cuándo Usar |
|---------|---------|-------------|
| Iteración línea por línea | Bajo uso de memoria | Archivos > 100MB |
| Procesamiento en chunks | Control de memoria | Datos binarios |
| Generadores | Lazy evaluation | Transformaciones |
| Lectura limitada | Control preciso | Previsualizaciones |

---

## 🎯 Consejos y Mejores Prácticas

### 1. 🔒 Siempre usa Context Managers (`with`)

```python
# ✅ CORRECTO
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
# El archivo se cierra automáticamente

# ❌ INCORRECTO
archivo = open("archivo.txt", "r")
contenido = archivo.read()
archivo.close()  # Puedes olvidar esto
```

### 2. 🌐 Especifica la Codificación

```python
# ✅ CORRECTO
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

# ❌ PROBLEMÁTICO (especialmente en Windows)
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
```

### 3. 🚨 Maneja Excepciones

```python
# ✅ CORRECTO
try:
    with open("archivo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("Sin permisos para leer el archivo")
```

### 4. 📊 Para Archivos Grandes

```python
# ✅ EFICIENTE - Línea por línea
with open("archivo_grande.txt", "r") as archivo:
    for linea in archivo:
        procesar(linea)

# ❌ INEFICIENTE - Carga todo en memoria
with open("archivo_grande.txt", "r") as archivo:
    lineas = archivo.readlines()  # Carga todo
    for linea in lineas:
        procesar(linea)
```

### 5. 🛤️ Trabajar con Rutas

```python
import os
from pathlib import Path

# ✅ MULTIPLATAFORMA
ruta = os.path.join("carpeta", "subcarpeta", "archivo.txt")

# ✅ MODERNO (Python 3.4+)
ruta = Path("carpeta") / "subcarpeta" / "archivo.txt"

# ❌ SOLO UNIX/LINUX
ruta = "carpeta/subcarpeta/archivo.txt"
```

---

## 🚀 Ejecutar los Ejemplos

Para ejecutar todos los ejemplos:

```bash
python main.py
```

Esto creará varios archivos de ejemplo y mostrará la salida de cada función.

### Archivos que se Crearán

- `ejemplo.txt` - Archivo de texto básico
- `escritura_ejemplo.txt` - Ejemplo de escritura
- `estudiantes.json` - Datos en formato JSON
- `productos.csv` - Datos en formato CSV
- `archivo_grande.txt` - Archivo con 1000 líneas
- `ejemplo_directorio/` - Directorio con archivo interno

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Python File Objects](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [JSON Module](https://docs.python.org/3/library/json.html)
- [CSV Module](https://docs.python.org/3/library/csv.html)
- [OS Module](https://docs.python.org/3/library/os.html)

### Bibliotecas Avanzadas
- `pathlib` - Manejo moderno de rutas
- `pandas` - Para archivos CSV/Excel complejos
- `openpyxl` - Para archivos Excel
- `pickle` - Serialización de objetos Python

---

**¡Feliz codificación! 🐍✨**
