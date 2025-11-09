-- =====================================================
-- ACTIVIDAD EVALUATIVA 4 - LIBRERÍA DB
-- Creación de base de datos y tablas con modificaciones
-- =====================================================

-- 1. CREAR LA BASE DE DATOS
DROP DATABASE IF EXISTS libreria_db;
CREATE DATABASE libreria_db;
USE libreria_db;

-- =====================================================
-- 2. CREAR LAS TABLAS INICIALES
-- =====================================================

-- Tabla Clientes
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_cliente VARCHAR(100) NOT NULL,
    correo_cliente VARCHAR(100) NOT NULL UNIQUE,
    telefono_cliente VARCHAR(15) NOT NULL,
    direccion_cliente VARCHAR(255) NOT NULL
);

-- Tabla Libros
CREATE TABLE Libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo_libro VARCHAR(255) NOT NULL,
    autor_libro VARCHAR(100) NOT NULL,
    precio_libro DECIMAL(10,2) NOT NULL,
    cantidad_disponible INT NOT NULL,
    categoria_libro VARCHAR(50) NOT NULL
);

-- Tabla Pedidos
CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    total_pedido DECIMAL(10,2) NOT NULL,
    estado_pedido VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

-- Tabla Detalles_Pedido
CREATE TABLE Detalles_Pedido (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_libro INT NOT NULL,
    cantidad_libro INT NOT NULL,
    precio_libro DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro)
);

-- Tabla Pagos
CREATE TABLE Pagos (
    id_pago INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    fecha_pago DATE NOT NULL,
    monto_pago DECIMAL(10,2) NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido)
);

-- =====================================================
-- 3. INSERTAR DATOS DE EJEMPLO PARA PRUEBAS
-- =====================================================

-- Insertar clientes de ejemplo
INSERT INTO Clientes (nombre_cliente, correo_cliente, telefono_cliente, direccion_cliente) VALUES
('Juan Pérez', 'juan.perez@email.com', '1234567890', 'Av. Principal 123'),
('María González', 'maria.gonzalez@email.com', '0987654321', 'Calle Secundaria 456'),
('Carlos López', 'carlos.lopez@email.com', '1122334455', 'Plaza Central 789');

-- Insertar libros de ejemplo
INSERT INTO Libros (titulo_libro, autor_libro, precio_libro, cantidad_disponible, categoria_libro) VALUES
('Don Quijote de la Mancha', 'Miguel de Cervantes', 25.99, 10, 'Clásicos'),
('Cien años de soledad', 'Gabriel García Márquez', 18.50, 15, 'Literatura'),
('El Principito', 'Antoine de Saint-Exupéry', 12.75, 20, 'Infantil'),
('1984', 'George Orwell', 22.00, 8, 'Ciencia Ficción'),
('Harry Potter y la Piedra Filosofal', 'J.K. Rowling', 28.99, 12, 'Fantasía');

-- Insertar pedidos de ejemplo
INSERT INTO Pedidos (id_cliente, fecha_pedido, total_pedido, estado_pedido) VALUES
(1, '2024-01-15', 44.49, 'Pendiente'),
(2, '2024-01-16', 31.25, 'Confirmado'),
(3, '2024-01-17', 22.00, 'Entregado');

-- Insertar detalles de pedido de ejemplo
INSERT INTO Detalles_Pedido (id_pedido, id_libro, cantidad_libro, precio_libro) VALUES
(1, 1, 1, 25.99),
(1, 3, 1, 12.75),
(2, 2, 1, 18.50),
(2, 3, 1, 12.75),
(3, 4, 1, 22.00);

-- Insertar pagos de ejemplo
INSERT INTO Pagos (id_pedido, fecha_pago, monto_pago, metodo_pago) VALUES
(1, '2024-01-15', 44.49, 'Tarjeta de Crédito'),
(2, '2024-01-16', 31.25, 'Transferencia Bancaria'),
(3, '2024-01-17', 22.00, 'Efectivo');

-- =====================================================
-- 4. MODIFICACIONES SOLICITADAS
-- =====================================================

-- 4.1 Cambiar telefono_cliente a VARCHAR(20)
ALTER TABLE Clientes 
DROP CHECK Clientes_chk_1;

ALTER TABLE Clientes 
MODIFY COLUMN telefono_cliente VARCHAR(20) NOT NULL;

-- 4.2 Modificar precio_libro para aceptar 3 decimales
ALTER TABLE Libros 
MODIFY COLUMN precio_libro DECIMAL(10,3) NOT NULL;

-- 4.3 Agregar campo fecha_confirmacion a tabla Pagos
ALTER TABLE Pagos 
ADD COLUMN fecha_confirmacion DATE;

-- Actualizar algunos pagos con fecha de confirmación
UPDATE Pagos 
SET fecha_confirmacion = DATE_ADD(fecha_pago, INTERVAL 1 DAY) 
WHERE id_pago IN (2, 3);

-- =====================================================
-- 5. ELIMINAR TABLA DETALLES_PEDIDO
-- =====================================================

-- Primero eliminamos las referencias de clave foránea si es necesario
DROP TABLE Detalles_Pedido;

-- =====================================================
-- 6. ELIMINAR TABLA PAGOS
-- =====================================================

DROP TABLE Pagos;

-- =====================================================
-- 7. TRUNCAR TABLA PEDIDOS
-- =====================================================

-- Desactivar temporalmente las verificaciones de claves foráneas
SET FOREIGN_KEY_CHECKS = 0;

-- Truncar la tabla Pedidos
TRUNCATE TABLE Pedidos;

-- Reactivar las verificaciones de claves foráneas
SET FOREIGN_KEY_CHECKS = 1;

-- =====================================================
-- 8. VERIFICAR ESTRUCTURA FINAL
-- =====================================================

-- Mostrar las tablas restantes
SHOW TABLES;

-- Mostrar estructura de las tablas restantes
DESCRIBE Clientes;
DESCRIBE Libros;
DESCRIBE Pedidos;
