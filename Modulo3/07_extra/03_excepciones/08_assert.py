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

"""
Las aserciones son declaraciones que verifican si una condición es verdadera. Si la condición es falsa, Python lanza una excepción AssertionError.
¿Cuándo usar assert?
- Para validaciones durante desarrollo: Verificar condiciones que deberían ser siempre verdaderas
- Para debugging: Detectar errores de lógica
"""