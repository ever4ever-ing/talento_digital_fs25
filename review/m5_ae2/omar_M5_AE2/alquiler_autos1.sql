
-- Creación de tablas
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion VARCHAR(150)
);

CREATE TABLE Vehiculos (
    id_vehiculo INT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    año INT,
    precio_dia DECIMAL(10,2)
);

CREATE TABLE Alquileres (
    id_alquiler INT PRIMARY KEY,
    id_cliente INT,
    id_vehiculo INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculos(id_vehiculo)
);

CREATE TABLE Pagos (
    id_pago INT PRIMARY KEY,
    id_alquiler INT,
    monto DECIMAL(10,2),
    fecha_pago DATE,
    FOREIGN KEY (id_alquiler) REFERENCES Alquileres(id_alquiler)
);

-- Inserción de datos
INSERT INTO Clientes VALUES
(1, 'Juan Pérez', '555-1234', 'juan@mail.com', 'Calle 123'),
(2, 'Laura Gómez', '555-5678', 'laura@mail.com', 'Calle 456'),
(3, 'Carlos Sánchez', '555-9101', 'carlos@mail.com', 'Calle 789');

INSERT INTO Vehiculos VALUES
(1, 'Toyota', 'Corolla', 2020, 30.00),
(2, 'Honda', 'Civic', 2019, 28.00),
(3, 'Ford', 'Focus', 2021, 35.00);

INSERT INTO Alquileres VALUES
(1, 1, 2, '2025-03-10', '2025-03-15'),
(2, 2, 1, '2025-03-12', '2025-03-16'),
(3, 3, 3, '2025-03-20', '2025-03-22');

INSERT INTO Pagos VALUES
(1, 1, 150.00, '2025-03-12'),
(2, 2, 112.00, '2025-03-13'),
(3, 3, 70.00, '2025-03-20');

-- Consultas 


-- 1. Clientes con alquiler activo
SELECT c.nombre, c.telefono, c.email
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE CURDATE() BETWEEN a.fecha_inicio AND a.fecha_fin;

-- 2. Vehículos alquilados en marzo 2025
SELECT v.marca, v.modelo, v.precio_dia
FROM Vehiculos v
JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE MONTH(a.fecha_inicio) = 3 AND YEAR(a.fecha_inicio) = 2025;

-- 3. Precio total del alquiler por cliente
SELECT c.nombre,
       SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio) * v.precio_dia) AS total_alquiler
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Vehiculos v ON a.id_vehiculo = v.id_vehiculo
GROUP BY c.nombre;

-- 4. Clientes sin pagos
SELECT c.nombre, c.email
FROM Clientes c
LEFT JOIN Alquileres a ON c.id_cliente = a.id_cliente
LEFT JOIN Pagos p ON a.id_alquiler = p.id_alquiler
WHERE p.id_pago IS NULL;

-- 5. Promedio de pagos por cliente
SELECT c.nombre, AVG(p.monto) AS promedio_pagos
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.nombre;

-- 6. Vehículos disponibles en fecha específica
SELECT v.marca, v.modelo, v.precio_dia
FROM Vehiculos v
WHERE v.id_vehiculo NOT IN (
    SELECT a.id_vehiculo
    FROM Alquileres a
    WHERE '2025-03-18' BETWEEN a.fecha_inicio AND a.fecha_fin
);

-- 7. Vehículos alquilados más de una vez en marzo 2025
SELECT v.marca, v.modelo, COUNT(*) AS veces_alquilado
FROM Vehiculos v
JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE MONTH(a.fecha_inicio) = 3 AND YEAR(a.fecha_inicio) = 2025
GROUP BY v.marca, v.modelo
HAVING COUNT(*) > 1;

-- 8. Total de pagos por cliente
SELECT c.nombre, SUM(p.monto) AS total_pagado
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.nombre;

-- 9. Clientes que alquilaron el Ford Focus
SELECT c.nombre, a.fecha_inicio, a.fecha_fin
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE a.id_vehiculo = 3;

-- 10. Total de días alquilados por cliente
SELECT c.nombre,
       SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio)) AS total_dias
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
GROUP BY c.nombre
ORDER BY total_dias DESC;
