# Alimentos favoritos de un grupo de estudiantes
estudiantes = {"pizza", "hamburguesa", "sushi", "tacos", "ensalada"}
# Alimentos favoritos de un grupo de deportistas
deportistas = {"pollo", "ensalada", "sushi", "batidos", "huevos"}


# 1. Alimentos comunes en ambos grupos (intersección)
comidas_comunes = estudiantes & deportistas
print("Alimentos que les gustan a ambos grupos:", comidas_comunes)  
# 2. Alimentos únicos de los estudiantes (diferencia)
solo_estudiantes = estudiantes - deportistas
print("Alimentos que solo les gustan a los estudiantes:", solo_estudiantes)  
# 3. Alimentos únicos de los deportistas (diferencia)
solo_deportistas = deportistas - estudiantes
print("Alimentos que solo les gustan a los deportistas:", solo_deportistas) 
# 4. Todos los alimentos únicos (sin repeticiones en ningún grupo)
todos_unicos = estudiantes ^ deportistas
print("Alimentos que no comparten:", todos_unicos)
# 5. Todos los alimentos mencionados (unión)
todos_los_alimentos = estudiantes | deportistas
print("Todos los alimentos mencionados:", todos_los_alimentos)  