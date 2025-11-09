CREATE DATABASE rentacar;
USE rentacar;

-- Tabla Clientes
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion VARCHAR(150)
) ENGINE=InnoDB;

-- Tabla Vehiculos
CREATE TABLE Vehiculos (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio YEAR NOT NULL,
    precio_dia DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB;

-- Tabla Alquileres
CREATE TABLE Alquileres (
    id_alquiler INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_vehiculo INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculos(id_vehiculo)
) ENGINE=InnoDB;

-- Tabla Pagos
CREATE TABLE Pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_alquiler INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATE NOT NULL,
    FOREIGN KEY (id_alquiler) REFERENCES Alquileres(id_alquiler)
) ENGINE=InnoDB;

-- Insertar datos en Clientes
INSERT INTO Clientes (nombre, telefono, email, direccion) VALUES
('Juan Pérez', '555-1234', 'juan@mail.com', 'Calle 123'),
('Laura Gómez', '555-5678', 'laura@mail.com', 'Calle 456'),
('Carlos Sánchez', '555-9101', 'carlos@mail.com', 'Calle 789');

-- Insertar datos en Vehiculos
INSERT INTO Vehiculos (marca, modelo, anio, precio_dia) VALUES
('Toyota', 'Corolla', 2020, 30.00),
('Honda', 'Civic', 2019, 28.00),
('Ford', 'Focus', 2021, 35.00);

-- Insertar datos en Alquileres
INSERT INTO Alquileres (id_cliente, id_vehiculo, fecha_inicio, fecha_fin) VALUES
(1, 2, '2025-03-10', '2025-03-15'),
(2, 1, '2025-03-12', '2025-03-16'),
(3, 3, '2025-03-20', '2025-03-22');

-- Insertar datos en Pagos
INSERT INTO Pagos (id_alquiler, monto, fecha_pago) VALUES
(1, 150.00, '2025-03-12'),
(2, 112.00, '2025-03-13'),
(3, 70.00, '2025-03-20');

-- Consultas

-- Consulta 1: Clientes con alquiler activo hoy
SELECT c.nombre, c.telefono, c.email
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE CURDATE() BETWEEN a.fecha_inicio AND a.fecha_fin;

-- Consulta 2: Vehículos alquilados en marzo 2025
SELECT v.modelo, v.marca, v.precio_dia
FROM Vehiculos v
JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE MONTH(a.fecha_inicio) = 3 AND YEAR(a.fecha_inicio) = 2025;

-- Consulta 3: Precio total de alquiler por cliente
SELECT c.nombre, SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio) * v.precio_dia) AS total_alquiler
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Vehiculos v ON a.id_vehiculo = v.id_vehiculo
GROUP BY c.id_cliente;

-- Consulta 4: Clientes sin pagos
SELECT c.nombre, c.email
FROM Clientes c
LEFT JOIN Alquileres a ON c.id_cliente = a.id_cliente
LEFT JOIN Pagos p ON a.id_alquiler = p.id_alquiler
WHERE p.id_pago IS NULL;

-- Consulta 5: Promedio de pagos por cliente
SELECT c.nombre, AVG(p.monto) AS promedio_pago
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.id_cliente;

-- Consulta 6: Vehículos disponibles en fecha específica (ejemplo 2025-03-18)
SELECT v.modelo, v.marca, v.precio_dia
FROM Vehiculos v
WHERE v.id_vehiculo NOT IN (
    SELECT a.id_vehiculo
    FROM Alquileres a
    WHERE '2025-03-18' BETWEEN a.fecha_inicio AND a.fecha_fin
);

-- Consulta 7: Vehículos alquilados más de una vez en marzo 2025
SELECT v.marca, v.modelo, COUNT(*) AS veces_alquilado
FROM Vehiculos v
JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE MONTH(a.fecha_inicio) = 3 AND YEAR(a.fecha_inicio) = 2025
GROUP BY v.id_vehiculo
HAVING COUNT(*) > 1;

-- Consulta 8: Total pagado por cada cliente
SELECT c.nombre, SUM(p.monto) AS total_pagado
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.id_cliente;

-- Consulta 9: Clientes que alquilaron Ford Focus
SELECT c.nombre, a.fecha_inicio, a.fecha_fin
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE a.id_vehiculo = 3;

-- Consulta 10: Total de días alquilados por cliente
SELECT c.nombre, SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio)) AS total_dias
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
GROUP BY c.id_cliente
ORDER BY total_dias DESC;
