# 🐍 Excepciones en Python - Guía Completa

Este documento contiene ejemplos prácticos y explicaciones detalladas sobre el manejo de excepciones en Python.

## 📋 Contenido de los ejemplos:

### 1. **Manejo básico** - `try/except` simple
Conceptos fundamentales del manejo de excepciones usando la estructura básica `try/except`.

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"10 dividido por {numero} es: {resultado}")
except ValueError:
    print("Error: No ingresaste un número válido")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
```

**Conceptos clave:**
- `try`: Bloque donde se ejecuta el código que puede generar una excepción
- `except`: Bloque que maneja una excepción específica
- Captura de excepciones específicas (`ValueError`, `ZeroDivisionError`)

---

### 2. **Múltiples excepciones** - Capturar diferentes tipos de errores
Técnicas para manejar varios tipos de excepciones en un solo bloque.

```python
try:
    lista = [1, 2, 3]
    indice = int(input("Ingresa un índice (0-2): "))
    print(f"Elemento en índice {indice}: {lista[indice]}")
except (ValueError, IndexError) as e:
    print(f"Error: {e}")
```

**Conceptos clave:**
- Captura múltiple con tupla: `except (Excepcion1, Excepcion2)`
- Uso de `as e` para acceder al objeto de excepción
- Manejo unificado de diferentes tipos de errores

---

### 3. **Bloques `else` y `finally`** - Control de flujo completo
Control completo del flujo de ejecución con todos los bloques disponibles.

```python
try:
    # Código que puede fallar
    print("Intentando ejecutar código...")
except Exception:
    print("Error: Algo salió mal")
else:
    print("Bloque else: Se ejecuta si NO hay excepciones")
finally:
    print("Bloque finally: Siempre se ejecuta")
```

**Conceptos clave:**
- `else`: Se ejecuta solo si no hay excepciones
- `finally`: Siempre se ejecuta, haya o no excepciones
- Útil para limpieza de recursos (cerrar archivos, conexiones, etc.)

---

### 4. **Excepciones comunes**

#### 📌 **IndexError** - Índice fuera de rango
```python
try:
    lista = [1, 2, 3]
    print(lista[5])  # Índice fuera de rango
except IndexError as e:
    print(f"Error de índice: {e}")
```

#### 📌 **KeyError** - Clave no encontrada en diccionario
```python
try:
    diccionario = {"nombre": "Juan", "edad": 30}
    print(diccionario["apellido"])  # Clave no existe
except KeyError as e:
    print(f"Error de clave: {e}")
```

#### 📌 **TypeError** - Error de tipos incompatibles
```python
try:
    resultado = "texto" + 5  # No se puede sumar string con int
except TypeError as e:
    print(f"Error de tipo: {e}")
```

#### 📌 **AttributeError** - Método/atributo inexistente
```python
try:
    numero = 42
    numero.append(1)  # Los enteros no tienen método append
except AttributeError as e:
    print(f"Error de atributo: {e}")
```

**Cuándo ocurren:**
- **IndexError**: Acceder a índices que no existen en listas/tuplas
- **KeyError**: Buscar claves inexistentes en diccionarios
- **TypeError**: Operaciones entre tipos incompatibles
- **AttributeError**: Usar métodos/propiedades que no existen en un objeto

---

### 5. **Excepciones personalizadas** - Crear tus propias excepciones
Desarrollo de excepciones específicas para tu aplicación.

```python
class EdadInvalidaError(Exception):
    """Excepción personalizada para edad inválida"""
    def __init__(self, edad, mensaje="Edad no válida"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError(edad, "La edad no puede ser negativa")
    elif edad > 150:
        raise EdadInvalidaError(edad, "La edad no puede ser mayor a 150 años")
    return True
```

**Conceptos clave:**
- Herencia de la clase `Exception`
- Constructor personalizado con parámetros específicos
- Uso de `raise` para lanzar excepciones personalizadas
- Documentación con docstrings

---

### 6. **Simulador bancario** - Ejemplo práctico con excepciones
Implementación práctica de un sistema que usa excepciones para validaciones.

```python
class SaldoInsuficienteError(Exception):
    """Excepción para saldo insuficiente"""
    pass

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar la operación")
        self.saldo -= cantidad
        return self.saldo
```

**Casos de uso:**
- Validación de datos de entrada
- Control de lógica de negocio
- Prevención de estados inválidos
- Comunicación clara de errores al usuario

---

### 7. **Manejo de archivos** - Errores comunes con archivos
Gestión robusta de operaciones con archivos del sistema.

```python
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
    except PermissionError:
        print(f"Error: Sin permisos para leer '{nombre_archivo}'")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None
```

**Excepciones comunes en archivos:**
- `FileNotFoundError`: Archivo no existe
- `PermissionError`: Sin permisos de acceso
- `IOError`: Errores generales de entrada/salida
- `UnicodeDecodeError`: Problemas de codificación

---

### 8. **Re-lanzar excepciones** - Usar `raise` sin argumentos
Técnica para capturar, procesar y re-lanzar excepciones.

```python
def dividir_numeros(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error capturado en la función")
        raise  # Re-lanza la excepción

try:
    resultado = dividir_numeros(10, 0)
except ZeroDivisionError:
    print("Error capturado en el nivel superior")
```

**Cuándo usar:**
- Logging de errores en diferentes niveles
- Procesamiento intermedio de excepciones
- Mantener el stack trace original
- Delegar el manejo final a otro nivel

---

### 9. **Jerarquía de excepciones** - Múltiples `except` ordenados
Orden estratégico de bloques `except` para manejo específico y general.

```python
def procesar_datos(datos):
    try:
        # Procesamiento de datos
        if not datos:
            raise ValueError("Los datos están vacíos")
        if len(datos) > 100:
            raise MemoryError("Demasiados datos para procesar")
        return f"Procesados {len(datos)} elementos"
    except ValueError as e:
        print(f"Error de valor: {e}")
    except MemoryError as e:
        print(f"Error de memoria: {e}")
    except Exception as e:  # Captura general al final
        print(f"Error general: {e}")
```

**Reglas importantes:**
- Excepciones específicas primero
- Excepciones generales al final
- `Exception` captura casi todas las excepciones
- El orden importa: Python usa el primer `except` que coincida

---

### 10. **Assertions** - Verificaciones con `assert`
Herramienta para verificaciones de desarrollo y debugging.

```python
def calcular_promedio(numeros):
    assert len(numeros) > 0, "La lista no puede estar vacía"
    assert all(isinstance(n, (int, float)) for n in numeros), "Todos los elementos deben ser números"
    return sum(numeros) / len(numeros)

try:
    promedio = calcular_promedio([10, 20, 30])
    print(f"Promedio: {promedio}")
    
    promedio2 = calcular_promedio([])  # Causará AssertionError
except AssertionError as e:
    print(f"Error de aserción: {e}")
```

**Características de `assert`:**
- Se deshabilita con la flag `-O` (optimización)
- Ideal para verificaciones de desarrollo
- No debe usarse para validación de entrada del usuario
- Lanza `AssertionError` cuando la condición es falsa

---

## 🚀 **Mejores Prácticas**

### ✅ **Recomendaciones:**
- Captura excepciones específicas, no `Exception` genérica
- Usa mensajes de error descriptivos
- Documenta las excepciones que puede lanzar una función
- Limpia recursos en bloques `finally`
- Crea excepciones personalizadas para tu dominio

### ❌ **Evita:**
- `except:` sin especificar la excepción
- Capturar y silenciar excepciones sin razón
- Usar excepciones para controlar flujo normal
- `assert` para validación de entrada del usuario

---

## 📖 **Jerarquía de Excepciones en Python**

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- ValueError
      +-- TypeError
      +-- AttributeError
      +-- FileNotFoundError
      +-- PermissionError
      +-- ...
```

---

## 🎯 **Ejemplos de Uso Práctico**

### 📝 **Validación de entrada:**
```python
def obtener_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if 0 <= edad <= 120:
                return edad
            else:
                print("La edad debe estar entre 0 y 120 años")
        except ValueError:
            print("Por favor, ingresa un número válido")
```

### 🔄 **Reintentos automáticos:**
```python
import time

def conectar_servidor(max_intentos=3):
    for intento in range(max_intentos):
        try:
            # Simular conexión
            if intento < 2:  # Simular fallo
                raise ConnectionError("No se pudo conectar")
            return "Conectado exitosamente"
        except ConnectionError as e:
            print(f"Intento {intento + 1} falló: {e}")
            if intento < max_intentos - 1:
                time.sleep(1)  # Esperar antes del siguiente intento
    return "Error: No se pudo conectar después de todos los intentos"
```

---

## 📚 **Recursos Adicionales**

- [Documentación oficial de Python - Excepciones](https://docs.python.org/3/tutorial/errors.html)
- [PEP 8 - Convenciones para excepciones](https://pep8.org/#programming-recommendations)
- [Excepciones built-in de Python](https://docs.python.org/3/library/exceptions.html)

---

*💡 **Consejo:** Practica estos ejemplos modificando los valores y observando cómo se comportan las diferentes excepciones. El manejo adecuado de excepciones es crucial para crear aplicaciones robustas y confiables.*
