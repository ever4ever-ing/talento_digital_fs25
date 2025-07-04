#1. Eliminar duplicados de una lista

lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
print(lista_con_duplicados)
lista_sin_duplicados = list(set(lista_con_duplicados))
print(lista_sin_duplicados)
print("-"*30)

#2. Filtrado rápido de elementos únicos
usuarios_activos = {"Ana", "Luis", "Carlos", "Marta"}
#3 Verificar si un usuario está activo (más rápido que con listas)
if "Luis" in usuarios_activos:
    print("Luis está activo")
print("-"*30)
print("Similitud de jaccard")
#Sistemas de recomendación (similitud entre conjuntos)
def jaccard_similitud(set1, set2):
    interseccion = len(set1 & set2)
    union = len(set1 | set2)
    return interseccion / union

intereses_usuario1 = {"python", "data science", "machine learning"}
intereses_usuario2 = {"python", "web development", "data science"}
print(intereses_usuario1)
print(intereses_usuario2)
similitud = jaccard_similitud(intereses_usuario1, intereses_usuario2)

print(f"Similitud: {similitud:.2f}")

print("-"*30)
#4 Búsqueda de palabras clave en textos

palabras_clave = {"python", "programación", "algoritmos"}
texto = "Python es un lenguaje de programación muy popular."
# Convertir el texto a minúsculas y dividirlo en palabras
palabras_en_texto = set(texto.lower().split())
print(palabras_en_texto)
# Verificar coincidencias
coincidencias = palabras_clave & palabras_en_texto
print(coincidencias)

print("-"*30)
#5. Sistema de votaciones (Evitar duplicados)
votantes_registrados = set()

def registrar_voto(rut):
    if rut in votantes_registrados:
        print("¡Ya votaste!")
    else:
        votantes_registrados.add(rut)
        print("Voto registrado.")

registrar_voto("191233211")
registrar_voto("191233212")
registrar_voto("191233213")
registrar_voto("191233211")


"""
Conclusión
Los sets son útiles cuando:
- Necesitas elementos únicos (sin duplicados).
- Quieres verificar pertenencia de forma rápida (elemento in conjunto).
- Realizas operaciones entre conjuntos (unión, intersección, diferencia).
- Trabajas con datos desordenados pero necesitas eficiencia.


"""
