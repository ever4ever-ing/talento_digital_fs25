-- =====================================================
-- SISTEMA DE GESTIÓN DE INVENTARIOS - MySQL
-- =====================================================

-- 1. CREACIÓN DE LA BASE DE DATOS Y TABLAS
-- =====================================================

CREATE DATABASE IF NOT EXISTS sistema_inventario;
USE sistema_inventario;

-- Tabla Proveedores
CREATE TABLE IF NOT EXISTS proveedores (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

-- Tabla Productos
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    cantidad_inventario INT NOT NULL DEFAULT 0,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    CHECK (precio >= 0),
    CHECK (cantidad_inventario >= 0)
);

-- Tabla Transacciones
CREATE TABLE IF NOT EXISTS transacciones (
    id_transaccion INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('compra', 'venta') NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    total DECIMAL(12,2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    id_producto INT NOT NULL,
    id_proveedor INT,
    observaciones TEXT,
    CHECK (cantidad > 0),
    CHECK (precio_unitario >= 0),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) 
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor) 
        ON UPDATE CASCADE ON DELETE SET NULL
);

-- Índices para optimización
CREATE INDEX idx_producto_nombre ON productos(nombre);
CREATE INDEX idx_transacciones_fecha ON transacciones(fecha);
CREATE INDEX idx_transacciones_tipo ON transacciones(tipo);
CREATE INDEX idx_transacciones_producto ON transacciones(id_producto);

-- =====================================================
-- 2. INSERCIÓN DE DATOS DE EJEMPLO
-- =====================================================

-- Insertar Proveedores
INSERT INTO proveedores (nombre, direccion, telefono, email) VALUES
('Distribuidora Central S.A.', 'Av. Principal 123, Santiago', '+56912345678', 'ventas@distcentral.cl'),
('Proveedora del Norte Ltda.', 'Calle Norte 456, Antofagasta', '+56987654321', 'contacto@pronorte.cl'),
('Suministros del Sur', 'Pasaje Sur 789, Temuco', '+56923456789', 'pedidos@sumsur.cl'),
('TecnoPartes Chile', 'Industrial 321, Valparaíso', '+56934567890', 'info@tecnopartes.cl');

-- Insertar Productos
INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES
('Laptop HP Pavilion', 'Laptop HP Pavilion 15.6" Intel i5 8GB RAM 256GB SSD', 599990.00, 25),
('Mouse Inalámbrico Logitech', 'Mouse inalámbrico óptico con receptor USB', 15990.00, 150),
('Teclado Mecánico RGB', 'Teclado mecánico retroiluminado switches azules', 89990.00, 45),
('Monitor Samsung 24"', 'Monitor LED Full HD 1920x1080 24 pulgadas', 179990.00, 30),
('Disco SSD 500GB', 'Unidad SSD SATA 2.5" 500GB alta velocidad', 79990.00, 80),
('Memoria RAM 8GB DDR4', 'Módulo memoria RAM 8GB DDR4 2400MHz', 39990.00, 120),
('Webcam HD', 'Cámara web HD 1080p con micrófono integrado', 29990.00, 75),
('Parlantes 2.1', 'Sistema de parlantes 2.1 con subwoofer 40W', 49990.00, 35);


-- Insertar transacciones (respetando claves foráneas)
INSERT INTO transacciones (tipo, fecha, cantidad, estado, id_producto, id_proveedor) VALUES
('COMPRA', '2024-01-15', 20, 'COMPLETADO', 1, 1),
('COMPRA', '2024-01-16', 100, 'COMPLETADO', 2, 2),
('VENTA', '2024-01-17', 5, 'COMPLETADO', 1, 3),
('COMPRA', '2024-01-18', 50, 'COMPLETADO', 3, 3),
('VENTA', '2024-01-19', 10, 'COMPLETADO', 2, 2),
('COMPRA', '2024-01-20', 30, 'COMPLETADO', 4, 1),
('VENTA', '2024-01-21', 2, 'COMPLETADO', 4, 2),
('COMPRA', '2024-01-22', 70, 'COMPLETADO', 5, 4),
('VENTA', '2024-01-23', 15, 'COMPLETADO', 5, 1),
('COMPRA', '2024-01-24', 100, 'PENDIENTE', 6, 2);

