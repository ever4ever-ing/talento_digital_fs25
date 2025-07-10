# Métodos para listas y diccionarios 


<span style="color:#2d7dd2; font-weight:bold;">▸ Métodos para Listas</span>

<span style="color:#2d7dd2;">▸ Acceso a elementos</span>
- `lista[indice]` — Accede al elemento en la posición especificada (comienza en 0)
- `lista[-indice]` — Accede desde el final (`-1` es el último elemento)
- `lista[inicio:fin]` — *Slice*: devuelve sublista desde `inicio` hasta `fin-1`
- `lista[inicio:fin:paso]` — *Slice* con paso especificado

<span style="color:#2d7dd2;">▸ Modificación de listas</span>
- `lista.append(elemento)` — Añade un elemento al final
- `lista.insert(indice, elemento)` — Inserta elemento en posición específica
- `lista.extend(iterable)` — Añade todos los elementos del iterable
- `lista[indice] = valor` — Modifica el elemento en la posición dada
- `lista[inicio:fin] = nueva_lista` — Modifica un segmento de la lista
- `lista.remove(elemento)` — Elimina la primera ocurrencia del elemento
- `lista.pop([indice])` — Elimina y devuelve elemento en posición (o último si no se especifica)
- `lista.clear()` — Elimina todos los elementos
- `lista.reverse()` — Invierte el orden de la lista *in-place*
- `lista.sort(key=None, reverse=False)` — Ordena la lista *in-place*

<span style="color:#2d7dd2;">▸ Búsqueda e información</span>
- `lista.index(elemento[, inicio[, fin]])` — Devuelve índice de la primera ocurrencia
- `lista.count(elemento)` — Cuenta ocurrencias del elemento
- `len(lista)` — Devuelve longitud de la lista
- `elemento in lista` — Verifica si el elemento está en la lista

---

<span style="color:#2d7dd2; font-weight:bold;">▸ Métodos para Diccionarios</span>

<span style="color:#2d7dd2;">▸ Acceso a elementos</span>
- `diccionario[clave]` — Accede al valor asociado a la clave
- `diccionario.get(clave[, valor_por_defecto])` — Accede al valor sin error si no existe
- `diccionario.keys()` — Devuelve vista de las claves
- `diccionario.values()` — Devuelve vista de los valores
- `diccionario.items()` — Devuelve vista de pares (clave, valor)

<span style="color:#2d7dd2;">▸ Modificación de diccionarios</span>
- `diccionario[clave] = valor` — Añade o modifica entrada
- `diccionario.update(otro_diccionario)` — Actualiza con pares de otro diccionario
- `diccionario.setdefault(clave[, valor_por_defecto])` — Obtiene valor o lo establece si no existe
- `diccionario.pop(clave[, valor_por_defecto])` — Elimina clave y devuelve su valor
- `diccionario.popitem()` — Elimina y devuelve par (clave, valor) (LIFO)
- `diccionario.clear()` — Elimina todos los elementos

<span style="color:#2d7dd2;">▸ Búsqueda e información</span>
- `clave in diccionario` — Verifica si la clave existe
- `len(diccionario)` — Devuelve número de pares clave-valor

---

<span style="color:#2d7dd2; font-weight:bold;">▸ Operaciones comunes</span>
- **Copiar:** `copia = lista.copy()` o `copia = diccionario.copy()`
- **Crear:** `lista = list()` o `lista = []`, `dic = dict()` o `dic = {}`
- **Iterar:**
  - `for elemento in lista:`
  - `for clave in diccionario:`
  - `for clave, valor in diccionario.items():`
