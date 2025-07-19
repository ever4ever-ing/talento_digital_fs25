# Lista de productos disponibles
inventario = [
    {"id": 1, "nombre": "Fertilizante Orgánico", "categoria": "Fertilizantes"},
    {"id": 2, "nombre": "Semillas de Tomate Orgánico", "categoria": "Semillas"},
    {"id": 3, "nombre": "Compost Natural", "categoria": "Fertilizantes"},
    {"id": 4, "nombre": "Semillas de Lechuga Orgánica", "categoria": "Semillas"}
]
# Set para categorías únicas
categorias = set([producto["categoria"] for producto in inventario])
# Tupla para datos inmutables de clientes agricultores
clientes = (("Carlos Mendoza", "carlos.mendoza@agroverde.com"),
            ("María González", "maria.gonzalez@agroverde.com"),
            ("Luis Ramírez", "luis.ramirez@agroverde.com"),)
# Diccionario para pedidos: clave = cliente, valor = lista de pedidos y estado
pedidos = {
    "Carlos Mendoza": [{"producto": "Fertilizante Orgánico", "estado": "Pendiente"}],
    "María González": [{"producto": "Semillas de Tomate Orgánico", "estado": "Entregado"}],
    "Luis Ramírez": [{"producto": "Compost Natural", "estado": "En Proceso"}]
}



# Menú interactivo
while True:
    print("\n--- Sistema de Gestión de Productos Agrícolas Orgánicos ---")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Registrar pedido")
    print("5. Mostrar pedidos")
    print("6. Mostrar categorías")
    print("7. Contar productos y pedidos")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")