def procesar_datos(datos):
    try:
        # Procesamiento de datos
        if not datos:
            raise ValueError("Los datos están vacíos")
        if len(datos) > 100:
            raise MemoryError("Demasiados datos para procesar")
        # Intentar acceder al primer elemento (puede causar otros errores)
        primer_elemento = datos[0]
        print(f"Procesando datos... Primer elemento: {primer_elemento}")
        return f"Procesados {len(datos)} elementos"
    except ValueError as e:
        print(f"Error de valor específico: {e}")
    except MemoryError as e:
        print(f"Error de memoria específico: {e}")
    except TypeError as e:
        print(f"Error de tipo específico: {e}")
    except Exception as e:  # Captura cualquier otra excepción no prevista
        print(f"Error general no específico: {type(e).__name__}: {e}")
        print("Este bloque captura errores que no fueron previstos en los except anteriores")

procesar_datos([])  # Lanza ValueError
procesar_datos(["a"] * 101)  # Lanza MemoryError
procesar_datos(None)  # Lanza Exception general (TypeError al intentar len(None))
procesar_datos(["Datos", "válidos"])  # Procesa correctamente

# Ejemplo Exception as e (error general)
print("\n--- Exception general ---")
procesar_datos({"no": "es lista"})  # TypeError: object of type 'dict' has no len()
procesar_datos(set([1, 2, 3]))  # Podría funcionar o no dependiendo del procesamiento

"""
Exception (más general)
    ├── ValueError (específica)
    ├── MemoryError (específica)  
    ├── TypeError (específica)
    └── Otras excepciones no previstas

El except Exception as e siempre debe ir al final porque captura cualquier excepción que no haya sido manejada por los bloques except más específicos anteriores. Esto asegura que el programa no se rompa por errores inesperados.

"""
