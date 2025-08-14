from pathlib import Path
import shutil
from datetime import datetime

RUTA_ARCHIVO = Path("inventario.txt")
BACKUP_DIR = Path("backups")

def agregar_producto():
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    talla = input("Talla: ")
    with RUTA_ARCHIVO.open("a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad},{talla}\n")
    print("Producto registrado.")

def mostrar_inventario():
    print("\nInventario completo")
    if not RUTA_ARCHIVO.exists():
        print("No hay productos registrados.")
        return
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        lineas = [l.strip() for l in f if l.strip()]
    if not lineas:
        print("No hay productos registrados.")
        return
    print(f"{'Nombre':<20} {'Precio':<12} {'Cantidad':<10} {'Talla':<10}")
    print("-" * 60)
    for linea in lineas:
        partes = linea.split(",")
        if len(partes) == 4:
            print(f"{partes[0]:<20} {partes[1]:<12} {partes[2]:<10} {partes[3]:<10}")

def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    if not RUTA_ARCHIVO.exists():
        print("No hay productos registrados.")
        return
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 4 and partes[0].lower() == nombre.lower():
                print(f"Producto encontrado: Nombre={partes[0]}, Precio={partes[1]}, Cantidad={partes[2]}, Talla={partes[3]}")
                return
    print("Producto no encontrado.")

def modificar_producto():
    nombre = input("Nombre del producto a modificar: ")
    if not RUTA_ARCHIVO.exists():
        print("No hay productos registrados.")
        return
    nuevas = []
    modificado = False
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 4 and partes[0].lower() == nombre.lower():
                print(f"Actual: Nombre={partes[0]}, Precio={partes[1]}, Cantidad={partes[2]}, Talla={partes[3]}")
                nuevo_nombre = input(f"Nuevo nombre [{partes[0]}]: ") or partes[0]
                nuevo_precio = input(f"Nuevo precio [{partes[1]}]: ") or partes[1]
                nuevo_cantidad = input(f"Nueva cantidad [{partes[2]}]: ") or partes[2]
                nuevo_talla = input(f"Nueva talla [{partes[3]}]: ") or partes[3]
                nuevas.append(f"{nuevo_nombre},{nuevo_precio},{nuevo_cantidad},{nuevo_talla}\n")
                modificado = True
            else:
                nuevas.append(linea)
    with RUTA_ARCHIVO.open("w", encoding="utf-8") as f:
        f.writelines(nuevas)
    if modificado:
        print("Producto modificado.")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    if not RUTA_ARCHIVO.exists():
        print("No hay productos registrados.")
        return
    nuevas = []
    eliminado = False
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 4 and partes[0].lower() == nombre.lower():
                eliminado = True
                continue
            nuevas.append(linea)
    with RUTA_ARCHIVO.open("w", encoding="utf-8") as f:
        f.writelines(nuevas)
    if eliminado:
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def crear_backup():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = BACKUP_DIR / f"inventario_backup_{timestamp}.txt"
    shutil.copy(RUTA_ARCHIVO, destino)
    print(f"Backup creado en: {destino}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Registrar nuevo producto")
        print("2. Consultar inventario completo")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Crear backup del inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            crear_backup()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
