-- =============================================================
-- SCRIPT COMPLETO: Estructura, datos de ejemplo y consultas SQL
-- =============================================================

/* =============================================================
   CREACIÓN DE TABLAS
   ============================================================= */
DROP TABLE IF EXISTS Pagos;
DROP TABLE IF EXISTS Alquileres;
DROP TABLE IF EXISTS Vehiculos;
DROP TABLE IF EXISTS Clientes;

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion VARCHAR(150)
);

CREATE TABLE Vehiculos (
    id_vehiculo INT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    año INT,
    precio_dia DECIMAL(10,2) NOT NULL
);

CREATE TABLE Alquileres (
    id_alquiler INT PRIMARY KEY,
    id_cliente INT,
    id_vehiculo INT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculos(id_vehiculo)
);

CREATE TABLE Pagos (
    id_pago INT PRIMARY KEY,
    id_alquiler INT,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATE NOT NULL,
    FOREIGN KEY (id_alquiler) REFERENCES Alquileres(id_alquiler)
);

/* =============================================================
   INSERCIÓN DE DATOS DE EJEMPLO
   ============================================================= */
INSERT INTO Clientes (id_cliente, nombre, telefono, email, direccion) VALUES
(1, 'Juan Pérez', '555-1234', 'juan@mail.com', 'Calle 123'),
(2, 'Laura Gómez', '555-5678', 'laura@mail.com', 'Calle 456'),
(3, 'Carlos Sánchez', '555-9101', 'carlos@mail.com', 'Calle 789');

INSERT INTO Vehiculos (id_vehiculo, marca, modelo, año, precio_dia) VALUES
(1, 'Toyota', 'Corolla', 2020, 30.00),
(2, 'Honda', 'Civic', 2019, 28.00),
(3, 'Ford', 'Focus', 2021, 35.00);

INSERT INTO Alquileres (id_alquiler, id_cliente, id_vehiculo, fecha_inicio, fecha_fin) VALUES
(1, 1, 2, '2025-03-10', '2025-03-15'),
(2, 2, 1, '2025-03-12', '2025-03-16'),
(3, 3, 3, '2025-03-20', '2025-03-22');

INSERT INTO Pagos (id_pago, id_alquiler, monto, fecha_pago) VALUES
(1, 1, 150.00, '2025-03-12'),
(2, 2, 112.00, '2025-03-13'),
(3, 3, 70.00, '2025-03-20');


-- Archivo: consultas_alquiler_autos.sql
-- Descripción: Consultas SQL para la plataforma de gestión de alquiler de automóviles.
-- Dialecto objetivo: MySQL 8+ (ANSI compatible en su mayoría).
-- Suposiciones:
--  - Las tablas se llaman exactamente: Clientes, Vehiculos, Alquileres, Pagos
--  - Claves:
--      Clientes.id_cliente (PK)
--      Vehiculos.id_vehiculo (PK)
--      Alquileres.id_alquiler (PK), id_cliente (FK -> Clientes), id_vehiculo (FK -> Vehiculos)
--      Pagos.id_pago (PK), id_alquiler (FK -> Alquileres)
--  - Las fechas incluyen ambos extremos del alquiler (día de inicio y fin). Por ello, los días
--    de arriendo se calculan como DATEDIFF(fecha_fin, fecha_inicio) + 1.

/* =============================================================
   Consulta 1
   Mostrar el nombre, telefono y email de todos los clientes que
   tienen un alquiler activo hoy (CURRENT_DATE).
   ============================================================= */
SELECT DISTINCT
    c.nombre,
    c.telefono,
    c.email
FROM Alquileres a
JOIN Clientes c     ON c.id_cliente = a.id_cliente
WHERE CURRENT_DATE BETWEEN a.fecha_inicio AND a.fecha_fin;


/* =============================================================
   Consulta 2
   Vehículos que se alquilaron en marzo de 2025.
   Se considera "alquilado en marzo" si el arriendo se solapa con
   el intervalo [2025-03-01, 2025-03-31].
   ============================================================= */
SELECT DISTINCT
    v.modelo,
    v.marca,
    v.precio_dia
FROM Alquileres a
JOIN Vehiculos v    ON v.id_vehiculo = a.id_vehiculo
WHERE a.fecha_inicio <= DATE('2025-03-31')
  AND a.fecha_fin    >= DATE('2025-03-01');


/* =============================================================
   Consulta 3
   Calcular el precio total del alquiler para cada cliente, considerando
   el número de días (incluyendo ambos extremos) * precio_dia, sumado
   sobre todos sus arriendos.
   ============================================================= */
SELECT
    c.nombre,
    SUM( (DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1) * v.precio_dia ) AS total_arriendos_usd
FROM Alquileres a
JOIN Clientes c  ON c.id_cliente   = a.id_cliente
JOIN Vehiculos v ON v.id_vehiculo  = a.id_vehiculo
GROUP BY c.id_cliente, c.nombre
ORDER BY total_arriendos_usd DESC;


/* =============================================================
   Consulta 4
   Clientes que no han realizado ningún pago (no hay registros en Pagos
   asociados a sus alquileres).
   ============================================================= */
SELECT
    c.nombre,
    c.email
FROM Clientes c
WHERE NOT EXISTS (
    SELECT 1
    FROM Alquileres a
    JOIN Pagos p ON p.id_alquiler = a.id_alquiler
    WHERE a.id_cliente = c.id_cliente
);


/* =============================================================
   Consulta 5
   Promedio de los pagos realizados por cada cliente.
   Incluye clientes sin pagos con promedio 0.
   ============================================================= */
SELECT
    c.nombre,
    COALESCE(AVG(p.monto), 0) AS promedio_pago
FROM Clientes c
LEFT JOIN Alquileres a ON a.id_cliente = c.id_cliente
LEFT JOIN Pagos p      ON p.id_alquiler = a.id_alquiler
GROUP BY c.id_cliente, c.nombre
ORDER BY promedio_pago DESC, c.nombre;


/* =============================================================
   Consulta 6
   Vehículos disponibles para alquilar en una fecha específica (ejemplo: 2025-03-18).
   Un vehículo está DISPONIBLE si no tiene arriendos que se solapen con esa fecha.
   ============================================================= */
SELECT
    v.modelo,
    v.marca,
    v.precio_dia
FROM Vehiculos v
LEFT JOIN Alquileres a
  ON a.id_vehiculo = v.id_vehiculo
 AND DATE('2025-03-18') BETWEEN a.fecha_inicio AND a.fecha_fin
WHERE a.id_alquiler IS NULL
ORDER BY v.marca, v.modelo;


/* =============================================================
   Consulta 7
   Marca y modelo de los vehículos que se alquilaron más de una vez
   en marzo de 2025 (considerando solape con el mes).
   ============================================================= */
SELECT
    v.marca,
    v.modelo,
    COUNT(*) AS veces_alquilado_marzo
FROM Alquileres a
JOIN Vehiculos v ON v.id_vehiculo = a.id_vehiculo
WHERE a.fecha_inicio <= DATE('2025-03-31')
  AND a.fecha_fin    >= DATE('2025-03-01')
GROUP BY v.id_vehiculo, v.marca, v.modelo
HAVING COUNT(*) > 1
ORDER BY veces_alquilado_marzo DESC, v.marca, v.modelo;


/* =============================================================
   Consulta 8
   Total de monto pagado por cada cliente (suma de pagos).
   Incluye clientes sin pagos con total 0.
   ============================================================= */
SELECT
    c.nombre,
    COALESCE(SUM(p.monto), 0) AS total_pagado
FROM Clientes c
LEFT JOIN Alquileres a ON a.id_cliente = c.id_cliente
LEFT JOIN Pagos p      ON p.id_alquiler = a.id_alquiler
GROUP BY c.id_cliente, c.nombre
ORDER BY total_pagado DESC, c.nombre;


/* =============================================================
   Consulta 9
   Clientes que alquilaron el vehículo Ford Focus (id_vehiculo = 3).
   Muestra nombre del cliente y el rango de fechas del alquiler.
   ============================================================= */
SELECT
    c.nombre,
    a.fecha_inicio,
    a.fecha_fin
FROM Alquileres a
JOIN Clientes c ON c.id_cliente = a.id_cliente
WHERE a.id_vehiculo = 3
ORDER BY a.fecha_inicio;


/* =============================================================
   Consulta 10
   Nombre del cliente y total de días alquilados por cliente, ordenado
   de mayor a menor. El total de días considera ambos extremos (inicio y fin).
   ============================================================= */
SELECT
    c.nombre,
    SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1) AS total_dias_alquilados
FROM Alquileres a
JOIN Clientes c ON c.id_cliente = a.id_cliente
GROUP BY c.id_cliente, c.nombre
ORDER BY total_dias_alquilados DESC, c.nombre;
