# Ejercicio: Evaluación de Calidad de Zapatillas (Condicionales en Python)

## Contexto

Eres un analista en una tienda deportiva y debes crear un programa en Python que evalúe la calidad de unas zapatillas basándose en 3 factores clave:

* **Material de fabricación**
* **Precio**
* **Tiempo de garantía**

## Clasificación de Calidad

La calidad se clasificará en:

* ✅ **Alta calidad** (Cumple con los mejores estándares)
* 🔄 **Calidad media** (Aceptable, pero con algunas limitaciones)
* ❌ **Baja calidad** (No cumple con los requisitos mínimos)

## Tabla de Criterios de Evaluación

| Factor | Alta Calidad (⭐) | Calidad Media (➖) | Baja Calidad (✖) |
|--------|-----------------|-------------------|------------------|
| Material | Cuero | Tela | Sintético |
| Precio | > $100.000 | $50.000 - $100.000 | < $50.000 |
| Garantía | > 1 año | 1 año | < 1 año o sin garantía |

## Requisitos del Programa

El usuario debe ingresar:

1. **Material** (cuero, tela o sintético)
2. **Precio** (número positivo)
3. **Garantía** (en años, número entero)

El programa debe evaluar los datos y mostrar uno de estos mensajes:

* **"⭐ Alta calidad:** Excelentes materiales, durabilidad y confianza."
* **"➖ Calidad media:** Buen equilibrio entre precio y calidad."
* **"✖ Baja calidad:** No cumple con los estándares mínimos."