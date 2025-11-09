# ====================================================================================
# Archivo: inventario_moda_xpress.py
# Descripción: Sistema de gestión de inventario para una tienda de ropa.
# Autores: Milenka, Tomason, Raul, Felipe, Jonathan
# ====================================================================================

import os
import shutil
import csv
from datetime import datetime

# Definición de las constantes para los archivos y el directorio de backups
# Usamos un archivo .csv ya que es la forma más estructurada de manejar estos datos
INVENTARIO_FILE = 'inventario.csv'
BACKUP_DIR = 'backups'
ENCABEZADOS = ['Nombre', 'Precio', 'Cantidad', 'Talla']

def inicializar_inventario():
    """
    Función para crear el archivo de inventario inicial si no existe,
    y llenarlo con los datos de ejemplo.
    """
    if not os.path.exists(INVENTARIO_FILE):
        try:
            with open(INVENTARIO_FILE, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(ENCABEZADOS)  # Escribimos los encabezados
                # Escribimos los datos iniciales
                writer.writerow(['Camiseta Azul', '15 USD', '50', 'M'])
                writer.writerow(['Pantalón Negro', '25 USD', '30', 'L'])
                writer.writerow(['Chaqueta Roja', '40 USD', '20', 'S'])
                writer.writerow(['Zapatillas Deportivas', '60 USD', '10', '42'])
                writer.writerow(['Gorra Blanca', '10 USD', '100', 'Talla Única'])
            print("✅  Archivo de inventario inicial creado exitosamente.")
        except IOError as e:
            print(f"⚠️  Error al inicializar el archivo: {e}")

def consultar_inventario():
    """
    Lee y muestra todo el contenido del inventario, con un formato de tabla.
    """
    try:
        with open(INVENTARIO_FILE, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            # Imprimimos los encabezados
            print("\n🛍️  Inventario Completo de Moda Xpress 🛍️")
            print(" | ".join(next(lector)))
            print("=" * 50 + "\n")
            # Imprimimos las filas
            for fila in lector:
                print(" | ".join(fila))
    except FileNotFoundError:
        print("\n⚠️  Error: El archivo de inventario no existe.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error al leer el archivo: {e}")

def buscar_producto():
    """
    Busca y muestra los detalles de un producto específico por nombre.
    """
    nombre_producto = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = False
    try:
        with open(INVENTARIO_FILE, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            print("\n🛒  Detalles del Producto 🛒")
            for producto in lector:
                if producto['Nombre'].lower() == nombre_producto.lower():
                    print(f"Nombre: {producto['Nombre']}")
                    print(f"Precio: {producto['Precio']}")
                    print(f"Cantidad: {producto['Cantidad']}")
                    print(f"Talla: {producto['Talla']}")
                    encontrado = True
                    break
        if not encontrado:
            print(f"\n⚠️  Producto '{nombre_producto}' no encontrado en el inventario.")
    except FileNotFoundError:
        print("\n⚠️  Error: El archivo de inventario no existe.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error al buscar el producto: {e}")

def agregar_producto():
    """
    Registra un nuevo producto en el inventario usando el modo 'a'.
    """
    nombre = input("Ingrese nombre de SKU: ").strip()
    precio = input("Ingrese precio del producto (ej. 25 USD): ").strip()
    cantidad = input("Ingrese cantidad de SKU: ").strip()
    talla = input("Ingrese talla de SKU: ").strip()
    
    nuevo_producto = [nombre, precio, cantidad, talla]
    
    try:
        with open(INVENTARIO_FILE, "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(nuevo_producto)
        print("\n✅  SKU ingresado correctamente.")
    except Exception as e:
        print(f"\n⚠️  Error al ingresar SKU: {e}")

def modificar_producto():
    """
    Modifica los datos de un producto ya existente.
    """
    nombre_modificar = input("Ingrese el nombre del producto a modificar: ").strip()
    filas_actualizadas = []
    encontrado = False
    try:
        with open(INVENTARIO_FILE, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            filas_actualizadas.append(encabezados)
            for fila in lector:
                if fila[0].lower() == nombre_modificar.lower():
                    print(f"\n✅  Producto encontrado: {fila}")
                    fila[0] = input(f"Nuevo nombre (enter para no cambiar): ") or fila[0]
                    fila[1] = input(f"Nuevo precio (enter para no cambiar): ") or fila[1]
                    fila[2] = input(f"Nueva cantidad (enter para no cambiar): ") or fila[2]
                    fila[3] = input(f"Nueva talla (enter para no cambiar): ") or fila[3]
                    print(f"✅  Producto modificado: {fila}")
                    encontrado = True
                filas_actualizadas.append(fila)

        if encontrado:
            with open(INVENTARIO_FILE, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(filas_actualizadas)
            print(f"\n✅  Producto '{nombre_modificar}' modificado con éxito.")
        else:
            print(f"\n⚠️  Producto '{nombre_modificar}' no encontrado.")
    except FileNotFoundError:
        print("\n⚠️  Error: El archivo de inventario no existe.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error al modificar el producto: {e}")

def eliminar_producto():
    """
    Elimina un producto del inventario.
    """
    nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()
    filas_conservar = []
    encontrado = False
    try:
        with open(INVENTARIO_FILE, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            filas_conservar.append(encabezados)
            for fila in lector:
                if fila[0].lower() == nombre_eliminar.lower():
                    print(f"\n✅  Producto '{fila[0]}' se eliminará.")
                    encontrado = True
                else:
                    filas_conservar.append(fila)
        
        if encontrado:
            with open(INVENTARIO_FILE, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(filas_conservar)
            print(f"\n✅  Producto '{nombre_eliminar}' eliminado exitosamente.")
        else:
            print(f"\n⚠️  Producto '{nombre_eliminar}' no encontrado.")
    except FileNotFoundError:
        print("\n⚠️  Error: El archivo de inventario no existe.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error al eliminar el producto: {e}")

def obtener_atributos():
    """
    Visualiza los detalles de un producto específico y los atributos del archivo.
    (Implementación de la tarea de Visualizar y Atributos)
    """
    try:
        stats = os.stat(INVENTARIO_FILE)
        print("\nℹ️  Atributos del Archivo de Inventario ℹ️")
        print(f"Tamaño del archivo: {stats.st_size} bytes")
        fecha_modificacion = datetime.fromtimestamp(stats.st_mtime)
        print(f"Última modificación: {fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S')}")
    except FileNotFoundError:
        print("\n⚠️  Error: El archivo de inventario no existe.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error al obtener atributos: {e}")

def crear_backup():
    """
    Crea una copia de seguridad del archivo de inventario.
    """
    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nombre_backup = f'inventario_backup_{timestamp}.csv'
        shutil.copy(INVENTARIO_FILE, os.path.join(BACKUP_DIR, nombre_backup))
        print(f"\n✅  Copia de seguridad '{nombre_backup}' creada exitosamente en la carpeta '{BACKUP_DIR}'.")
    except FileNotFoundError:
        print("\n⚠️  Error: El archivo de inventario no existe.")
    except Exception as e:
        print(f"\n⚠️  Error al crear la copia de seguridad: {e}")

def renombrar_producto():
    """
    Modifica los datos de un producto ya existente.
    """
    nombre_modificar = input("Ingrese el nombre del producto a modificar: ").strip()
    filas_actualizadas = []
    encontrado = False
    try:
        with open(INVENTARIO_FILE, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            filas_actualizadas.append(encabezados)
            for fila in lector:
                if fila[0].lower() == nombre_modificar.lower():
                    print(f"\n✅  Producto encontrado: {fila}")
                    fila[0] = input(f"Nuevo nombre (enter para no cambiar): ") or fila[0]
                    print(f"✅  Producto modificado: {fila}")
                    encontrado = True
                filas_actualizadas.append(fila)

        if encontrado:
            with open(INVENTARIO_FILE, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(filas_actualizadas)
            print(f"\n✅  Producto '{nombre_modificar}' modificado con éxito.")
        else:
            print(f"\n⚠️  Producto '{nombre_modificar}' no encontrado.")
    except FileNotFoundError:
        print("\n⚠️  Error: El archivo de inventario no existe.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error al modificar el producto: {e}")
        """
    Cambia el nombre de un artículo en el inventario.
    Aclaro: la solicitud de la tarea es cambiar el nombre de un "artículo", no el archivo.
    """

def mostrar_menu():
    """Muestra el menú de opciones al usuario, con emojis para un mejor estilo."""
    print("\n" + "👕👖🧥👟🧢" * 5 + "\n")
    print("📦  Sistema de Inventario 'Moda Xpress' 📦")
    print("=" * 50 + "\n")
    print("1. Consultar inventario completo")
    print("2. Buscar un producto específico")
    print("3. Registrar un nuevo producto")
    print("4. Modificar un producto existente")
    print("5. Eliminar un producto")
    print("6. Obtener atributos del archivo de inventario")
    print("7. Crear una copia de seguridad del inventario")
    print("8. Renombrar un producto")
    print("9. Salir")
    print("\n" + "👕👖🧥👟🧢" * 5 + "\n")

def main():
    """Función principal que ejecuta el sistema."""
    inicializar_inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            consultar_inventario()
        elif opcion == '2':
            buscar_producto()
        elif opcion == '3':
            agregar_producto()
        elif opcion == '4':
            modificar_producto()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            obtener_atributos()
        elif opcion == '7':
            crear_backup()
        elif opcion == '8':
            # Renombrar un producto (como se pidió en la consigna)
            renombrar_producto()
        elif opcion == '9':
            print("Saliendo del sistema ¡Gracias por usar 'Moda Xpress'!")
            break
        else:
            print("⚠️  Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
