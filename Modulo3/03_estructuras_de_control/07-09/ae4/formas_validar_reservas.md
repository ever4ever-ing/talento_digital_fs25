# Alternativas para validar y registrar reservas en excursiones

En el código v3 se utiliza:

```python
if len(excursiones[opcion-1]["reservas"]) < excursiones[opcion-1]["cupo"]:
    excursiones[opcion-1]["reservas"].append(nombre)
    print("Reserva realizada.")
else:
    print("No hay cupos disponibles.")
```

A continuación, se presentan otras formas de realizar la validación y el registro de reservas:

---

## 1. Usando una variable auxiliar para la excursión seleccionada

```python
excursion = excursiones[opcion-1]
if len(excursion["reservas"]) < excursion["cupo"]:
    excursion["reservas"].append(nombre)
    print("Reserva realizada.")
else:
    print("No hay cupos disponibles.")
```

---

## 2. Usando una función para gestionar la reserva

```python
def reservar(excursion, nombre):
    if len(excursion["reservas"]) < excursion["cupo"]:
        excursion["reservas"].append(nombre)
        print("Reserva realizada.")
    else:
        print("No hay cupos disponibles.")

reservar(excursiones[opcion-1], nombre)
```

---

## 3. Usando un operador ternario para el mensaje

```python
if len(excursiones[opcion-1]["reservas"]) < excursiones[opcion-1]["cupo"]:
    excursiones[opcion-1]["reservas"].append(nombre)
    mensaje = "Reserva realizada."
else:
    mensaje = "No hay cupos disponibles."
print(mensaje)
```

---

## 4. Usando una excepción personalizada (avanzado)

```python
class CupoLlenoError(Exception):
    pass

try:
    if len(excursiones[opcion-1]["reservas"]) >= excursiones[opcion-1]["cupo"]:
        raise CupoLlenoError("No hay cupos disponibles.")
    excursiones[opcion-1]["reservas"].append(nombre)
    print("Reserva realizada.")
except CupoLlenoError as e:
    print(e)
```

---

Cada una de estas alternativas es válida y puede usarse según el contexto, la complejidad del programa y las preferencias del programador.
