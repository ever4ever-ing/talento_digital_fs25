"""
PLANTILLA DE APRENDIZAJE - Sistema de Reservas BIKECITY
Actividad práctica para implementar manejo de excepciones

INSTRUCCIONES:
1. Complete los métodos marcados con TODO
2. Implemente el manejo de excepciones según se indica
3. Pruebe cada funcionalidad antes de continuar
4. Use los comentarios como guía para la implementación
"""

from datetime import datetime, timedelta

# ============== EXCEPCION PERSONALIZADA ==============

class ReservaError(Exception):
    """
    TODO: Implementar excepción personalizada
    - Debe recibir mensaje y código de error opcional
    - Heredar de Exception
    """
    def __init__(self, mensaje, codigo_error=None):
        # TODO: Implementar constructor
        pass

# ============== CLASES DEL SISTEMA ==============

class Bicicleta:
    """
    Clase que representa una bicicleta en el sistema
    """
    def __init__(self, id_bici, modelo, precio_hora=5000):
        """
        TODO: Implementar constructor de Bicicleta
        Atributos necesarios:
        - id: identificador único
        - modelo: tipo de bicicleta
        - precio_hora: costo por hora
        - disponible: boolean (True por defecto)
        - estado: string ("Bueno" por defecto)
        """
        pass
        
    def __str__(self):
        """
        TODO: Implementar representación en string
        Formato sugerido: "Bicicleta {id} - {modelo} - {disponible} ({estado})"
        """
        pass

class Cliente:
    """
    Clase que representa un cliente del sistema
    """
    def __init__(self, id_cliente, nombre, telefono, email=""):
        """
        TODO: Implementar constructor de Cliente
        Atributos necesarios:
        - id: identificador único
        - nombre: nombre completo
        - telefono: número de contacto
        - email: correo electrónico (opcional)
        - fecha_registro: datetime.now()
        - reservas_historicas: lista vacía
        """
        pass
        
    def __str__(self):
        """
        TODO: Implementar representación en string
        Formato sugerido: "Cliente {id} - {nombre} - Tel: {telefono}"
        """
        pass

class Reserva:
    """
    Clase que representa una reserva en el sistema
    """
    def __init__(self, id_reserva, cliente_id, bicicleta_id, horas):
        """
        TODO: Implementar constructor de Reserva
        Atributos necesarios:
        - id: identificador único
        - cliente_id: ID del cliente
        - bicicleta_id: ID de la bicicleta
        - horas: duración de la reserva
        - fecha_reserva: datetime.now()
        - fecha_limite: fecha_reserva + timedelta(hours=1)
        - estado: "Pendiente"
        - monto: 0 (se calcula después)
        """
        pass
        
    def __str__(self):
        """
        TODO: Implementar representación en string
        Formato: "Reserva {id} - Cliente: {cliente_id} - Estado: {estado} - Monto: ${monto}"
        """
        pass

class SistemaBikeCity:
    """
    Clase principal que maneja todo el sistema de reservas
    """
    def __init__(self):
        """
        TODO: Implementar constructor del sistema
        Inicializar diccionarios vacíos para:
        - bicicletas: {id_bici: objeto_bicicleta}
        - clientes: {id_cliente: objeto_cliente}
        - reservas: {id_reserva: objeto_reserva}
        - reservas_activas: {cliente_id: reserva_id}
        - contador_reservas: 1
        """
        pass
        
    def agregar_cliente(self, cliente):
        """
        TODO: Implementar agregar cliente con manejo de excepciones
        
        Validaciones necesarias:
        1. Verificar que sea instancia de Cliente (TypeError)
        2. Verificar que no exista el ID (ReservaError con código "DUPLICADO")
        
        Usar try/except/finally:
        - try: validaciones y agregar cliente
        - except: capturar TypeError y ReservaError, imprimir error y re-lanzar
        - finally: imprimir "Operacion de agregar cliente finalizada"
        """
        pass
        
    def agregar_bicicleta(self, bicicleta):
        """
        TODO: Implementar agregar bicicleta con manejo de excepciones
        
        Similar a agregar_cliente pero para bicicletas
        Código de error para duplicado: "DUPLICADA"
        """
        pass
    
    def crear_reserva(self, cliente_id, bicicleta_id, horas):
        """
        TODO: Implementar crear reserva con manejo múltiple de excepciones
        
        Este es el método más complejo. Debe manejar:
        
        1. ValueError: para validaciones básicas
           - cliente_id debe ser string no vacío
           - horas debe ser número positivo
           
        2. KeyError: para existencia de datos
           - cliente_id debe existir en self.clientes
           - bicicleta_id debe existir en self.bicicletas
           
        3. ReservaError: para reglas de negocio
           - Cliente no debe tener reserva activa ("RESERVA_DUPLICADA")
           - Bicicleta debe estar disponible ("NO_DISPONIBLE")
           
        Flujo sugerido:
        1. Validar parámetros
        2. Verificar existencia de cliente y bicicleta
        3. Verificar reglas de negocio
        4. Crear reserva y calcular monto
        5. Registrar en sistema
        6. Actualizar estado de bicicleta
        
        Usar finally para limpiezas y logging
        """
        conexion_activa = True
        try:
            # TODO: Implementar validaciones y lógica
            pass
            
        except ValueError as e:
            # TODO: Manejar errores de validación
            pass
        except KeyError as e:
            # TODO: Manejar errores de datos no encontrados
            pass
        except ReservaError as e:
            # TODO: Manejar errores de reglas de negocio
            pass
        except Exception as e:
            # TODO: Manejar errores inesperados
            pass
        finally:
            # TODO: Limpiezas y logging
            pass
    
    def procesar_pago(self, reserva_id, monto_pagado):
        """
        TODO: Implementar procesamiento de pago
        
        Validaciones:
        1. Reserva debe existir (KeyError)
        2. Reserva debe estar en estado "Pendiente" (ReservaError)
        3. Monto debe ser exacto (ReservaError con código "MONTO_INCORRECTO")
        
        Si todo ok: cambiar estado a "Activa"
        """
        try:
            # TODO: Implementar lógica
            pass
        except (KeyError, ReservaError) as e:
            # TODO: Manejar errores
            pass
        finally:
            # TODO: Logging de transacción
            pass
    
    def completar_reserva(self, reserva_id):
        """
        TODO: Implementar completar reserva
        
        Validaciones:
        1. Reserva debe existir
        2. Reserva debe estar "Activa"
        
        Acciones:
        1. Liberar bicicleta (disponible = True)
        2. Cambiar estado a "Completada"
        3. Remover de reservas_activas
        """
        try:
            # TODO: Implementar lógica
            pass
        except KeyError:
            # TODO: Convertir a ReservaError
            pass
        except ReservaError as e:
            # TODO: Manejar error y re-lanzar
            pass
        finally:
            # TODO: Logging
            pass
    
    def verificar_vencidas(self):
        """
        TODO: Implementar verificación de reservas vencidas
        
        Lógica:
        1. Obtener fecha/hora actual
        2. Buscar reservas "Pendiente" con fecha_limite vencida
        3. Para cada vencida: liberar bicicleta, cambiar estado, limpiar activas
        4. Manejar errores individuales sin afectar el proceso completo
        """
        ahora = datetime.now()
        vencidas = []
        
        try:
            # TODO: Implementar búsqueda y cancelación
            pass
        except Exception as e:
            # TODO: Manejar errores generales
            pass
        finally:
            # TODO: Reporte de procesamiento
            pass
    
    def mostrar_estado(self):
        """
        TODO: Implementar mostrar estado del sistema
        
        Mostrar:
        1. Clientes registrados
        2. Bicicletas disponibles/no disponibles
        3. Reservas activas con nombre del cliente
        """
        pass


def inicializar_sistema():
    """
    TODO: Implementar inicialización con datos por defecto
    
    Crear:
    1. Instancia de SistemaBikeCity
    2. 3 clientes de ejemplo
    3. 3 bicicletas de ejemplo
    4. Agregar al sistema usando try/except para continuar si hay errores
    """
    pass

def mostrar_menu():
    """
    TODO: Implementar menú de opciones
    
    Opciones sugeridas:
    1. Ver estado del sistema
    2. Agregar cliente
    3. Agregar bicicleta
    4. Crear reserva
    5. Procesar pago
    6. Completar reserva
    7. Verificar reservas vencidas
    8. Salir
    """
    pass

def main():
    """
    TODO: Implementar función principal con menú interactivo
    
    Estructura:
    1. Inicializar sistema
    2. Bucle principal con try/except
    3. Manejar cada opción del menú
    4. Validar entrada del usuario
    5. Manejar KeyboardInterrupt para salida elegante
    """
    pass

if __name__ == "__main__":
    print(" BIKECITY - Completa las funciones marcadas con TODO")
    print("Ejecuta main() cuando termines la implementación")
    # main()  # Descomenta cuando implementes el sistema completo
    #Función de prueba básica - descomenta cuando implementes las clases


if __name__ == "__main__":
    # TODO: Cuando termines la implementación, cambiar a main()
    main() 