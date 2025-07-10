# Alternativas para mostrar la lista de excursiones en Python

En el código v3 se utiliza:

```python
for i, ex in enumerate(excursiones, 1):
    print(f"{i}. {ex['nombre']} (Cupos: {ex['cupo']} | Reservados: {len(ex['reservas'])})")
```

A continuación, se presentan otras formas de lograr el mismo resultado:

---

## 1. Usando un bucle `for` clásico con índices

```python
for i in range(len(excursiones)):
    ex = excursiones[i]
    print(f"{i+1}. {ex['nombre']} (Cupos: {ex['cupo']} | Reservados: {len(ex['reservas'])})")
```

---

## 2. Usando una función para mostrar excursiones

```python
def mostrar_excursiones(lista):
    for idx, ex in enumerate(lista, 1):
        print(f"{idx}. {ex['nombre']} (Cupos: {ex['cupo']} | Reservados: {len(ex['reservas'])})")

mostrar_excursiones(excursiones)
```

---

## 3. Usando comprensión de listas y `join`

```python
lineas = [
    f"{i+1}. {ex['nombre']} (Cupos: {ex['cupo']} | Reservados: {len(ex['reservas'])})"
    for i, ex in enumerate(excursiones)
]
print("\n".join(lineas))
```

---

## 4. Usando un bucle `while`

```python
i = 0
while i < len(excursiones):
    ex = excursiones[i]
    print(f"{i+1}. {ex['nombre']} (Cupos: {ex['cupo']} | Reservados: {len(ex['reservas'])})")
    i += 1
```

---

Cada una de estas alternativas es válida y puede usarse según el contexto o preferencia del programador.
