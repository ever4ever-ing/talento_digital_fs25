#Manejo de inventario con csv
import csv
import os
from datetime import datetime 
from pathlib import Path
import shutil

RUTA_ARCHIVO = Path("inventario.csv")

BACKUP_DIR = Path("backups")


class ManejoInventario:
    def __init__(self):
        self.archivo_nombre = "inventario.csv"
        self.encabezados_defecto = ["Nombre", "Precio", "Cantidad", "Talla"]
        self.menu ="""
        "Elige una opción."\n
        "1: Ver el inventario"
        "2: Añadir texto al inventario sobreescribiendo"
        "3: Añadir texto al inventario nuevo sin sobreescribir"
        "4: Modificar productos existentes en el inventario."
        "5: Obtener atributos del archivo: Ver información sobre el archivo como el tamaño y la fecha de última modificación."
        "6: Leer un producto específico: Buscar por nombre o ID y mostrar los detalles del producto."
        "7: Eliminar un producto: Eliminar un producto del inventario."
        "8: Hacer backup."
        "9: Cerrar archivos"
        """

    def inicializar_archivo_con_encabezados(self):
        """Crea el archivo con encabezados si no existe"""
        if not Path(self.archivo_nombre).exists():
            with open(self.archivo_nombre, 'w', newline='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                escritor.writerow(self.encabezados_defecto)
            print("Archivo de inventario creado con encabezados.")

    def mostrar_menu(self):
        print(self.menu)
        while True:  # Bucle hasta obtener entrada válida
            try:
                numero = int(input("Lee las opciones y elige un número: "))
                return numero
            except ValueError:
                print("Por favor, ingresa un número válido.")
                # Continúa el bucle para pedir entrada nuevamente
                
    def ver_inventario(self):
        """Opción 1: Ver inventario"""
        try:
            with open(self.archivo_nombre, "r", encoding='utf-8') as file:
                contenido = file.read()
                if contenido:
                    print("Inventario actual")
                    print(contenido)
                else:
                    print("El inventario está vacío.")
        except FileNotFoundError:
             print("El archivo de inventario no existe. Se creará automáticamente al agregar productos.")

    def reemplazar_info(self, texto):
        """Opción 2: Sobreescribir inventario"""
        try: 
            with open(self.archivo_nombre, "w", newline ='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                # Escribir encabezados primero
                escritor.writerow(self.encabezados_defecto)
                
                # Dividir por líneas y escribir cada línea como fila
                lineas = texto.strip().split('\n')
                for linea in lineas:
                    if linea.strip(): 
                        escritor.writerow(linea.split(','))
                print("Inventario reemplazado exitosamente (encabezados preservados).")
        except Exception as e:
            print(f"Error al reemplazar el inventario: {e}")
                  
    def añadir_texto(self, texto):
            """Opción 3: Añadir al inventario sin sobreescribir"""
            try:
                with open(self.archivo_nombre, "a", newline= '', encoding = 'utf-8') as file:
                    escritor = csv.writer(file)
                    #Dividir por líneas y escribir cada línea como fila
                    lineas = texto.strip().split('\n')
                    for linea in lineas:
                        if linea.strip(): 
                        #Solo escribir líneas no vacías
                            escritor.writerow(linea.split(','))
                    print("Texto añadido al inventario exitosamente.")
            except Exception as e:
                print(f"Error al añadir texto al inventario: {e}")
    
    def editar_producto(self):
        """Opción 4: Modificar y consultar productos existentes en el inventario"""
        encabezados_defecto = ["Nombre", "Precio", "Cantidad", "Talla"]
        nombre_buscar = input("Ingrese el nombre del producto a editar: ")
        encontrado = False
        
        try:
            with open(self.archivo_nombre, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                
                try:
                    primera_fila = next(lector)
                    # Si el segundo campo es numérico, son datos; si no, son encabezados
                    if len(primera_fila) > 1 and primera_fila[1].replace('.', '').isdigit():
                        encabezados = encabezados_defecto
                        filas = [primera_fila] + list(lector)
                    else:
                        encabezados = primera_fila
                        filas = list(lector)
                except StopIteration:
                    print("El archivo está vacío.")
                    return
                    
                # Buscar y editar producto
                for i, fila in enumerate(filas):
                    if fila[0] == nombre_buscar:
                        print(f"Producto encontrado: {dict(zip(encabezados, fila))}")
                        nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para no cambiar): ")
                        nuevo_precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
                        nuevo_cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
                        nuevo_talla = input("Ingrese la nueva talla (dejar en blanco para no cambiar): ")

                        if nuevo_nombre: fila[0] = nuevo_nombre
                        if nuevo_precio: fila[1] = nuevo_precio
                        if nuevo_cantidad: fila[2] = nuevo_cantidad
                        if nuevo_talla: fila[3] = nuevo_talla

                        filas[i] = fila
                        encontrado = True
                        break
                        
        except FileNotFoundError:
            print("El archivo no existe.")
            return
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return

        # GUARDAR CAMBIOS
        if encontrado:
            with open(self.archivo_nombre, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(encabezados)
                escritor.writerows(filas)
                print("Producto editado con éxito.")
        else:
            print("Producto no encontrado.")

    def obtener_atributos_archivo(self):
        """Opción 5: Obtener información del archivo"""
        try:
            stats = os.stat(self.archivo_nombre)
            tamaño = stats.st_size
            fecha_modificacion = datetime.fromtimestamp(stats.st_mtime)
            
            print(f"\n--- INFORMACIÓN DEL ARCHIVO ---")
            print(f"Nombre: {self.archivo_nombre}")
            print(f"Tamaño: {tamaño} bytes")
            fecha_simple = fecha_modificacion.date()  # Solo la fecha, sin hora
            print(f"Última modificación: {fecha_simple}")
        except FileNotFoundError:
            print("El archivo de inventario no existe.")
        except Exception as e:
            print(f"Error al obtener información del archivo: {e}")


    def buscar_producto(self, nombre_producto):
        """Opción 6: Buscar un producto específico"""
        try:
            with open(self.archivo_nombre, "r", encoding='utf-8') as file:
                lector = csv.reader(file)
                encontrado = False
                for fila in lector:
                    if fila and nombre_producto.lower() in fila[0].lower():
                        print(f"Producto encontrado: {', '.join(fila)}")
                        encontrado = True
                
                if not encontrado:
                    print(f"No se encontró el producto '{nombre_producto}'")
        except FileNotFoundError:
            print("El archivo de inventario no existe.")
        except Exception as e:
            print(f"Error al buscar el producto: {e}")   

    def crear_backup(self):
        """Opción 9: Crear backup del inventario"""
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    
    # Verificar que el archivo existe antes de hacer backup
        if not RUTA_ARCHIVO.exists():
            print("No se puede crear backup: el archivo de inventario no existe.")
            return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = BACKUP_DIR / f"inventario_backup_{timestamp}.csv"
    
    try:
        shutil.copy(RUTA_ARCHIVO, destino)
        print(f"Backup creado exitosamente en: {destino}")
    except Exception as e:
        print(f"Error al crear backup: {e}")
    else:
        print("Backup generado correctamente.")



    def eliminar_producto(self):
        """Opción 7: Eliminar un producto del inventario"""
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        
        try:
            with open(self.archivo_nombre, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                encabezados = next(lector)  # Leer encabezados
                filas = list(lector)
                
                # Buscar producto a eliminar
            for i, fila in enumerate(filas):
                if fila and fila[0] == nombre_eliminar:
                    print(f"\nProducto encontrado: {dict(zip(encabezados, fila))}")
                    confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ")
                        
                    if confirmacion.lower() in ['s', 'si', 'sí', 'yes', 'y']:
                        filas.pop(i)
                        encontrado = True
                            
                            # Guardar cambios
                        with open(self.archivo_nombre, 'w', newline='', encoding='utf-8') as archivo:
                            escritor = csv.writer(archivo)
                            escritor.writerow(encabezados)
                            escritor.writerows(filas)
                            
                        print("Producto eliminado exitosamente.")
                    else:
                        print("Eliminación cancelada.")
                    break
                
            if not encontrado:
                print("Producto no encontrado.")
                    
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")


    def ejecutar(self):
        print("Sistema de manejo de inventario")
        # Inicializar archivo con encabezados si no existe
        self.inicializar_archivo_con_encabezados()  # ← AQUÍ se ejecuta
    
        while True:  # Luego empieza el bucle del menú    
            while True:
                numero = self.mostrar_menu()
                
                if numero == 1:
                    self.ver_inventario()
                
                elif numero == 2:
                    texto = input("Ingresa el texto para reemplazar el inventario (separa productos por líneas y campos por comas):\n")
                    self.reemplazar_info(texto)
                
                elif numero == 3:
                    texto = input("Ingresa el texto para añadir al inventario (separa productos por líneas y campos por comas):\n")
                    self.añadir_texto(texto)
                
                elif numero == 4:
                    
                    self.editar_producto()         

                elif numero == 5:
                    self.obtener_atributos_archivo()
                
                elif numero == 6:
                    nombre = input("Ingresa el nombre del producto a buscar: ")
                    self.buscar_producto(nombre)
                
                elif numero == 7:
                    self.eliminar_producto()

                elif numero == 8:
                    self.crear_backup()

                elif numero == 9:
                    print("¡Hasta luego!")
                    break

                else:
                    print("Opción no válida. Por favor, elige un número del 1 al 9.")
            
if __name__ == "__main__":
    
    inventario = ManejoInventario()
    inventario.ejecutar() 
