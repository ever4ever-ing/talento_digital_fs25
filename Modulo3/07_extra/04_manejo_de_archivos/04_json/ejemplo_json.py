import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def escribir_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print("Archivo JSON creado")


def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos_leidos = json.load(archivo)
    print("Datos leídos del JSON:")
    print(f"Curso: {datos_leidos['curso']}")
    print("Estudiantes:")
    for estudiante in datos_leidos["estudiantes"]:
        print(
            f"  - {estudiante['nombre']}, {estudiante['edad']} años, {estudiante['carrera']}")



print("\n=== ARCHIVOS JSON ===")
datos_estudiantes = {
    "estudiantes": [
            {"nombre": "Ana", "edad": 22, "carrera": "Ingeniería"},
            {"nombre": "Carlos", "edad": 24, "carrera": "Medicina"},
            {"nombre": "María", "edad": 23, "carrera": "Derecho"}
        ],
        "curso": "Python Básico",
        "año": 2025
    }
ruta_json = os.path.join(BASE_DIR, "estudiantes.json")
escribir_json(ruta_json, datos_estudiantes)
leer_json(ruta_json)
