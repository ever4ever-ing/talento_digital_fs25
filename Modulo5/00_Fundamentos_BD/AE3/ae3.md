# AE3 - Base de Datos de Clientes y Pedidos

## Descripción
Sistema de base de datos para gestionar clientes y sus pedidos, implementando relaciones entre tablas y operaciones CRUD básicas.

## 1. Creación de la Base de Datos

```sql
-- Crear la base de datos
CREATE DATABASE clientes_pedidos_db;
USE clientes_pedidos_db;
```

## 2. Estructura de Tablas

### Tabla Clientes
```sql
-- Crear tabla clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(20)
);
```

### Tabla Pedidos
```sql
-- Crear tabla pedidos
CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);
```

## 3. Inserción de Datos

### Insertar Clientes
```sql
-- Insertar 5 clientes
INSERT INTO clientes (nombre, direccion, telefono) VALUES
('Juan Pérez', 'Calle Falsa 123', '+123456789'),
('María García', 'Avenida Siempre Viva 742', '+987654321'),
('Carlos López', 'Boulevard de los Sueños 12', '+192837465'),
('Ana Martínez', 'Plaza Central 7', '+564738291'),
('Luisa Rodríguez', 'Camino Real 45', '+657483920');
```

### Insertar Pedidos
```sql
-- Insertar 10 pedidos
INSERT INTO pedidos (cliente_id, fecha, total) VALUES
(1, '2024-01-15', 150.75),
(1, '2024-02-20', 200.00),
(2, '2024-01-17', 89.50),
(2, '2024-02-18', 120.00),
(3, '2024-01-20', 350.25),
(3, '2024-02-21', 400.00),
(4, '2024-01-22', 75.30),
(4, '2024-02-23', 220.40),
(5, '2024-01-25', 95.99),
(5, '2024-02-25', 110.50);
```

## 4. Consultas y Operaciones

### Consultar todos los clientes y sus pedidos
```sql
-- Proyectar clientes y sus pedidos
SELECT c.id, c.nombre, p.id AS pedido_id, p.fecha, p.total
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;
```

### Consultar pedidos de un cliente específico
```sql
-- Proyectar pedidos de un cliente específico (ID = 2)
SELECT * FROM pedidos WHERE cliente_id = 2;
```

### Calcular total de pedidos por cliente
```sql
-- Calcular total de pedidos por cliente
SELECT c.id, c.nombre, SUM(p.total) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nombre;
```

## 5. Operaciones de Actualización y Eliminación

### Actualizar información de cliente
```sql
-- Actualizar dirección de un cliente (ID = 3)
UPDATE clientes SET direccion = 'Nueva Dirección 999' WHERE id = 3;
```

### Eliminar cliente y sus pedidos
```sql
-- Eliminar un cliente y sus pedidos (ID = 4)
DELETE FROM clientes WHERE id = 4;
```