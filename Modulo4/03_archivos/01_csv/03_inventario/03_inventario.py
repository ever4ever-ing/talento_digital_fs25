import csv
import os

ARCHIVO_CSV = "inventario_bicicletas.csv"
CAMPOS = ['id', 'marca', 'modelo', 'tipo', 'precio', 'color']

def inicializar_archivo():
    """Crea el archivo CSV si no existe"""
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()

def agregar_bicicleta():
    """Añade una bicicleta al inventario"""
    print("\nREGISTRAR NUEVA BICICLETA")
    bicicleta = {campo: input(f"{campo.capitalize()}: ") for campo in CAMPOS}
    
    with open(ARCHIVO_CSV, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writerow(bicicleta)
    print("¡Bicicleta registrada!")

def mostrar_inventario():
    """Muestra todas las bicicletas"""
    print("\nINVENTARIO DE BICICLETAS")
    try:
        with open(ARCHIVO_CSV, 'r') as f:
            reader = csv.DictReader(f)
            for idx, bici in enumerate(reader, 1):
                print(f"{idx}. {bici['marca']} {bici['modelo']} - ${bici['precio']}")
    except FileNotFoundError:
        print("No hay bicicletas registradas.")

def buscar_bicicleta():
    """Busca bicicletas por marca"""
    marca = input("\nBuscar por marca: ").lower()
    encontradas = False
    
    with open(ARCHIVO_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for bici in reader:
            if marca in bici['marca'].lower():
                print(f"\nID: {bici['id']}")
                print(f"Marca/Modelo: {bici['marca']} {bici['modelo']}")
                print(f"Tipo: {bici['tipo']} | Color: {bici['color']}")
                print(f"Precio: ${bici['precio']}")
                encontradas = True
    
    if not encontradas:
        print("No se encontraron bicicletas de esa marca.")

def menu():
    """Muestra el menú principal"""
    print("\nSISTEMA DE BICICLETAS")
    print("1. Registrar nueva bicicleta")
    print("2. Ver inventario completo")
    print("3. Buscar por marca")
    print("4. Salir")

def main():
    inicializar_archivo()
    
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_bicicleta()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_bicicleta()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()