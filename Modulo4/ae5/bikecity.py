"""
Sistema de Reservas BIKECITY 
Manejo de renta de bicicletas urbanas con manejo robusto de excepciones
"""

from datetime import datetime, timedelta

# ============== EXCEPCION PERSONALIZADA ==============

class SystemError(Exception):
    """Excepcion personalizada para errores especificos del sistema de reservas"""
    def __init__(self, mensaje, codigo_error=None):
        self.codigo_error = codigo_error
        super().__init__(mensaje)

# ============== CLASES DEL SISTEMA ==============

class Bicicleta:
    def __init__(self, id_bici, modelo, precio_hora=5000):
        self.id = id_bici
        self.modelo = modelo
        self.precio_hora = precio_hora
        self.disponible = True
        self.estado = "Bueno"  # Bueno, Malo, Mantenimiento
        
    def __str__(self):
        estado_disp = "Disponible" if self.disponible else "No disponible"
        return f"Bicicleta {self.id} - {self.modelo} - {estado_disp} ({self.estado})"

class Cliente:
    def __init__(self, id_cliente, nombre, telefono, email=""):
        self.id = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.fecha_registro = datetime.now()
        self.reservas_historicas = []
        
    def __str__(self):
        return f"Cliente {self.id} - {self.nombre} - Tel: {self.telefono}"

class Reserva:
    def __init__(self, id_reserva, cliente_id, bicicleta_id, horas):
        self.id = id_reserva
        self.cliente_id = cliente_id
        self.bicicleta_id = bicicleta_id
        self.horas = horas
        self.fecha_reserva = datetime.now()
        self.fecha_limite = self.fecha_reserva + timedelta(hours=1)  # 1 hora para recoger
        self.estado = "Pendiente"  # Pendiente, Activa, Completada, Cancelada
        self.monto = 0
        
    def __str__(self):
        return f"Reserva {self.id} - Cliente: {self.cliente_id} - Estado: {self.estado} - Monto: ${self.monto}"

class SistemaBikeCity:
    def __init__(self):
        self.bicicletas = {}
        self.clientes = {}
        self.reservas = {}
        self.reservas_activas = {}  # cliente_id -> reserva_id
        self.contador_reservas = 1
        
    def agregar_cliente(self, cliente):
        """Agrega un cliente al sistema con validaciones"""
        try:
            if not isinstance(cliente, Cliente):
                raise TypeError("Debe ser una instancia de Cliente")
            
            if cliente.id in self.clientes:
                raise SystemError(f"Cliente {cliente.id} ya existe", "DUPLICADO")
                
            self.clientes[cliente.id] = cliente
            print(f"Cliente {cliente.id} - {cliente.nombre} agregado exitosamente")
            
        except (TypeError, SystemError) as e:
            print(f"Error: {e}")
            raise
        finally:
            print("Operacion de agregar cliente finalizada")
        
    def agregar_bicicleta(self, bicicleta):
        """Agrega una bicicleta al sistema con validaciones"""
        try:
            if not isinstance(bicicleta, Bicicleta):
                raise TypeError("Debe ser una instancia de Bicicleta")
            
            if bicicleta.id in self.bicicletas:
                raise SystemError(f"Bicicleta {bicicleta.id} ya existe", "DUPLICADA")
                
            self.bicicletas[bicicleta.id] = bicicleta
            print(f"Bicicleta {bicicleta.id} agregada exitosamente")
            
        except (TypeError, SystemError) as e:
            print(f"Error: {e}")
            raise
        finally:
            print(f"Operacion de agregar bicicleta finalizada")
    
    def crear_reserva(self, cliente_id, bicicleta_id, horas):
        """Crear reserva con manejo multiple de excepciones"""
        
        try:
            # Validaciones basicas - pueden generar ValueError/TypeError
            if not cliente_id or not isinstance(cliente_id, str):
                raise ValueError("ID de cliente invalido")
            
            if not isinstance(horas, (int, float)) or horas <= 0:
                raise ValueError("Horas debe ser numero positivo")
            
            # Verificar existencia del cliente
            if cliente_id not in self.clientes:
                raise KeyError(f"Cliente {cliente_id} no existe en el sistema")
            
            # Verificar existencia - puede generar KeyError
            if bicicleta_id not in self.bicicletas:
                raise KeyError(f"Bicicleta {bicicleta_id} no existe")
            
            # Verificar reservas duplicadas - caso especifico de negocio
            if cliente_id in self.reservas_activas:
                reserva_previa = self.reservas[self.reservas_activas[cliente_id]]
                raise SystemError(
                    f"Cliente {cliente_id} ya tiene reserva activa (ID: {reserva_previa.id})", 
                    "RESERVA_DUPLICADA"
                )
            
            # Verificar disponibilidad
            bicicleta = self.bicicletas[bicicleta_id]
            if not bicicleta.disponible:
                raise SystemError(
                    f"Bicicleta {bicicleta_id} no disponible ({bicicleta.estado})", 
                    "NO_DISPONIBLE"
                )
            
            # Crear y calcular reserva
            reserva = Reserva(self.contador_reservas, cliente_id, bicicleta_id, horas)
            reserva.monto = horas * bicicleta.precio_hora
            
            # Registrar en sistema
            self.reservas[reserva.id] = reserva
            self.reservas_activas[cliente_id] = reserva.id
            self.clientes[cliente_id].reservas_historicas.append(reserva.id)
            bicicleta.disponible = False
            self.contador_reservas += 1
            
            print(f"Reserva {reserva.id} creada - Monto: ${reserva.monto:,.0f}")
            print(f"Recoger antes de: {reserva.fecha_limite.strftime('%H:%M')}")
            return reserva.id
            
        except ValueError as e:
            print(f"Error de validacion: {e}")
            raise
        except KeyError as e:
            print(f"Error de datos: {e}")
            raise
        except SystemError as e:
            print(f"Error de negocio: {e}")
            if e.codigo_error == "RESERVA_DUPLICADA":
                print("Sugerencia: Complete o cancele la reserva actual primero")
            raise
        except Exception as e:
            print(f"Error inesperado: {e}")
            raise
        finally:
            # Acciones de limpieza
            if 'reserva' in locals():
                print(f"Registro: Operacion de reserva {reserva.id} procesada")
            else:
                print("Registro: Operacion de reserva fallo")
            conexion_activa = False
            print("Limpieza: Conexion cerrada")
    
    def procesar_pago(self, reserva_id, monto_pagado):
        """Procesar pago con validacion de montos"""
        try:
            if reserva_id not in self.reservas:
                raise KeyError(f"Reserva {reserva_id} no encontrada")
            
            reserva = self.reservas[reserva_id]
            
            if reserva.estado != "Pendiente":
                raise SystemError(f"Reserva en estado {reserva.estado}, no se puede pagar", "ESTADO_INVALIDO")
            
            # Validar monto exacto para evitar errores de calculo
            if monto_pagado != reserva.monto:
                raise SystemError(
                    f"Monto incorrecto: esperado ${reserva.monto}, recibido ${monto_pagado}", 
                    "MONTO_INCORRECTO"
                )
            
            reserva.estado = "Activa"
            print(f"Pago procesado - Reserva {reserva_id} activada")
            
        except (KeyError, SystemError) as e:
            print(f"Error en pago: {e}")
            raise
        finally:
            print("Transaccion de pago finalizada")
    
    def completar_reserva(self, reserva_id):
        """Completar reserva y liberar bicicleta"""
        try:
            reserva = self.reservas[reserva_id]
            
            if reserva.estado != "Activa":
                raise SystemError(f"Reserva debe estar activa, esta: {reserva.estado}", "ESTADO_INVALIDO")
            
            # Liberar bicicleta
            self.bicicletas[reserva.bicicleta_id].disponible = True
            reserva.estado = "Completada"
            del self.reservas_activas[reserva.cliente_id]
            
            print(f"Reserva {reserva_id} completada - Bicicleta liberada")
            
        except KeyError:
            raise SystemError(f"Reserva {reserva_id} no encontrada", "NO_EXISTE")
        except SystemError as e:
            print(f"Error: {e}")
            raise
        finally:
            print("Operacion de completar finalizada")
    
    def verificar_vencidas(self):
        """Verificar y cancelar reservas no recogidas a tiempo"""
        ahora = datetime.now()
        vencidas = []
        
        try:
            for reserva in self.reservas.values():
                if reserva.estado == "Pendiente" and ahora > reserva.fecha_limite:
                    vencidas.append(reserva.id)
            
            for reserva_id in vencidas:
                try:
                    reserva = self.reservas[reserva_id]
                    self.bicicletas[reserva.bicicleta_id].disponible = True
                    reserva.estado = "Cancelada"
                    if reserva.cliente_id in self.reservas_activas:
                        del self.reservas_activas[reserva.cliente_id]
                    print(f"Reserva {reserva_id} cancelada por vencimiento")
                except Exception as e:
                    print(f"Error cancelando reserva vencida {reserva_id}: {e}")
            
            if not vencidas:
                print("No hay reservas vencidas")
                
        except Exception as e:
            print(f"Error verificando vencidas: {e}")
        finally:
            print(f"Verificacion completada: {len(vencidas)} reservas procesadas")
    
    def mostrar_estado(self):
        """Mostrar estado actual del sistema"""
        print("\n" + "="*40)
        print("ESTADO SISTEMA BIKECITY")
        print("="*40)
        
        print(f"\nCLIENTES ({len(self.clientes)}):")
        for cliente in self.clientes.values():
            print(f"  {cliente}")
        
        print(f"\nBICICLETAS ({len(self.bicicletas)}):")
        for bici in self.bicicletas.values():
            print(f"  {bici}")
        
        print(f"\nRESERVAS ACTIVAS ({len(self.reservas_activas)}):")
        for cliente_id, reserva_id in self.reservas_activas.items():
            reserva = self.reservas[reserva_id]
            cliente_nombre = self.clientes[cliente_id].nombre
            print(f"  {reserva} - {cliente_nombre}")


def inicializar_sistema():
    """Inicializar sistema con clientes y bicicletas por defecto"""
    sistema = SistemaBikeCity()
    
    # Clientes por defecto
    clientes = [
        Cliente("CLI001", "Juan Perez", "987654321", "juan@email.com"),
        Cliente("CLI002", "Maria Garcia", "987654322", "maria@email.com"),
        Cliente("CLI003", "Carlos Lopez", "987654323")
    ]
    
    for cliente in clientes:
        try:
            sistema.agregar_cliente(cliente)
        except Exception:
            pass  # Continuar con los demas
    
    bicicletas = [
        Bicicleta("B001", "Mountain Bike", 6000),
        Bicicleta("B002", "City Bike", 4000),
        Bicicleta("B003", "Electric Bike", 8000)
    ]
    
    for bici in bicicletas:
        try:
            sistema.agregar_bicicleta(bici)
        except Exception:
            pass  # Continuar con las demas
    
    return sistema

def mostrar_menu():
    """Mostrar opciones del menu principal"""
    print("\n" + "="*50)
    print("           SISTEMA BIKECITY - MENU PRINCIPAL")
    print("="*50)
    print("1. Ver estado del sistema")
    print("2. Agregar cliente")
    print("3. Agregar bicicleta")
    print("4. Reservar bicicleta")
    print("5. Procesar pago")
    print("6. Completar reserva")
    print("7. Verificar reservas vencidas")
    print("8. Salir")
    print("="*50)

def main():
    """Funcion principal con menu interactivo"""
    print("BIENVENIDO AL SISTEMA BIKECITY")
    print("="*40)
    
    sistema = inicializar_sistema()
    
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opcion (1-8): ").strip()
            
            if opcion == "1":
                sistema.mostrar_estado()
                
            elif opcion == "2":
                print("\n--- AGREGAR CLIENTE ---")
                id_cliente = input("ID del cliente: ").strip()
                nombre = input("Nombre completo: ").strip()
                telefono = input("Telefono: ").strip()
                email = input("Email (opcional): ").strip()
                try:
                    nuevo_cliente = Cliente(id_cliente, nombre, telefono, email)
                    sistema.agregar_cliente(nuevo_cliente)
                except Exception as e:
                    print(f"Error: {e}")
                    
            elif opcion == "3":
                print("\n--- AGREGAR BICICLETA ---")
                id_bici = input("ID de bicicleta: ").strip()
                modelo = input("Modelo: ").strip()
                try:
                    precio = float(input("Precio por hora (default 5000): ") or "5000")
                    nueva_bici = Bicicleta(id_bici, modelo, precio)
                    sistema.agregar_bicicleta(nueva_bici)
                except ValueError:
                    print("Error: Precio debe ser numerico")
                except Exception as e:
                    print(f"Error: {e}")
                    
            elif opcion == "4":
                print("\n--- CREAR RESERVA ---")
                cliente_id = input("ID del cliente: ").strip() # strip para evitar espacios
                bicicleta_id = input("ID de bicicleta: ").strip()
                try:
                    horas = float(input("Horas a reservar: "))
                    reserva_id = sistema.crear_reserva(cliente_id, bicicleta_id, horas)
                    print(f"Reserva creada con ID: {reserva_id}")
                except ValueError:
                    print("Error: Horas debe ser numerico")
                except Exception as e:
                    print(f"Error: {e}")
                    
            elif opcion == "5":
                print("\n--- PROCESAR PAGO ---")
                try:
                    reserva_id = int(input("ID de reserva: "))
                    monto = float(input("Monto a pagar: "))
                    sistema.procesar_pago(reserva_id, monto)
                except ValueError:
                    print("Error: ID y monto deben ser numericos")
                except Exception as e:
                    print(f"Error: {e}")
                    
            elif opcion == "6":
                print("\n--- COMPLETAR RESERVA ---")
                try:
                    reserva_id = int(input("ID de reserva: "))
                    sistema.completar_reserva(reserva_id)
                except ValueError:
                    print("Error: ID debe ser numerico")
                except Exception as e:
                    print(f"Error: {e}")
                    
            elif opcion == "7":
                print("\n--- VERIFICAR RESERVAS VENCIDAS ---")
                sistema.verificar_vencidas()
                
            elif opcion == "8":
                print("\nGracias por usar BIKECITY. ¡Hasta pronto!")
                break
                
            else:
                print("Opcion invalida. Seleccione del 1 al 8.")
                
            input("\nPresione ENTER para continuar...")
            
        except KeyboardInterrupt:
            print("\n\nSaliendo del sistema...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("Presione ENTER para continuar...")

if __name__ == "__main__":
    main()
