from pathlib import Path
import csv

RUTA_ARCHIVO = Path("inventario.csv")
# Encabezados de las columnas del CSV
ENCABEZADOS = ["Nombre", "Precio", "Cantidad", "Talla"]



def inicializar_archivo(ruta_dinamica: Path, campos: list):
    with open(ruta_dinamica, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)  # Definir el objeto DictWriter
        writer.writeheader() # Escribimos la cabecera del archivo
        print("Archivo inicializado")
        
def agregar_producto(nombre, precio, cantidad, talla):
    with open(RUTA_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([nombre, precio, cantidad, talla])

def mostrar_inventario():
    print("\nMostrando inventario:")
    print("="*30)
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            print(f"Encabezados: {encabezados}")
            print("Datos:")
            for fila in lector:
                print(fila)
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            for fila in lector:
                if fila[0] == nombre_buscar:
                    print(f"Producto encontrado: {dict(zip(encabezados, fila))}") #zip es para combinar encabezados y valores
                    encontrado = True
                    break
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    if not encontrado:
        print("Producto no encontrado.")

def editar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a editar: ")
    encontrado = False
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)
            filas = list(lector)
            for i, fila in enumerate(filas):
                if fila[0] == nombre_buscar:
                    print(f"Producto encontrado: {dict(zip(encabezados, fila))}")
                    nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para no cambiar): ")
                    nuevo_precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
                    nuevo_cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
                    nuevo_talla = input("Ingrese la nueva talla (dejar en blanco para no cambiar): ")

                    if nuevo_nombre:
                        fila[0] = nuevo_nombre
                    if nuevo_precio:
                        fila[1] = nuevo_precio
                    if nuevo_cantidad:
                        fila[2] = nuevo_cantidad
                    if nuevo_talla:
                        fila[3] = nuevo_talla

                    filas[i] = fila
                    encontrado = True
                    break
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

    if encontrado:
        with open(RUTA_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados)
            escritor.writerows(filas)
            print("Producto editado con éxito.")
    else:
        print("Producto no encontrado.")
        
        
def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar inventario")
        print("2. Buscar producto")
        print("3. Editar producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            editar_producto()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    inicializar_archivo(RUTA_ARCHIVO, ENCABEZADOS)
    agregar_producto("camiseta", 90, 3, "Talla M")
    agregar_producto("pantalón", 120, 5, "Talla L")
    agregar_producto("zapatos", 150, 2, "Talla 42")
    menu()
