import mysql.connector


def consultar_tickets_mysql(nombre, apellido, config_db):
    """
    Versión para MySQL
    config_db debe ser un diccionario con: host, user, password, database
    """
    try:
        conexion = mysql.connector.connect(**config_db)
        cursor = conexion.cursor()

        consulta = """
        SELECT t.destino, t.fecha, t.precio
        FROM tickets t
        JOIN viajeros v ON v.id = t.id_viajero
        WHERE v.nombre = %s AND v.apellido = %s
        """

        cursor.execute(consulta, (nombre, apellido))
        resultados = cursor.fetchall()

        return resultados

    except mysql.connector.Error as error:
        print(f"Error MySQL: {error}")
        return []

    finally:
        if conexion:
            conexion.close()


if __name__ == "__main__":

    config_db = {
        'host': 'localhost',          # Cambia por tu host
        'database': 'agencia_viajes',  # Cambia por el nombre de tu base de datos
        'user': 'root',         # Cambia por tu usuario
        'password': 'password',  # Cambia por tu contraseña
        'port': 3306                  # Puerto por defecto de MySQL
    }
    # Parámetros variables
    nombre_viajero = "Ana"
    apellido_viajero = "Pérez"
    
    # Ejecutar la consulta
    resultados = consultar_tickets_mysql(nombre_viajero, apellido_viajero, config_db)
    
    # Mostrar resultados
    if resultados:
        print(f"Tickets encontrados para {nombre_viajero} {apellido_viajero}:")
        print("-" * 50)
        for ticket in resultados:
            destino, fecha, precio = ticket
            print(f"Destino: {destino}, Fecha: {fecha}, Precio: ${precio}")
    else:
        print(f"No se encontraron tickets para {nombre_viajero} {apellido_viajero}")