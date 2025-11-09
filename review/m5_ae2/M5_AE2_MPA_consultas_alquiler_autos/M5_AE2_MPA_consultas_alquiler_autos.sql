-- Usar la base de datos correcta
USE sistema_alquiler_autos;

-- -------------------------------------------------------
-- Consulta 1: Clientes con alquiler activo
-- -------------------------------------------------------
SELECT c.nombre, c.telefono, c.email
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
WHERE CURDATE() BETWEEN a.fecha_inicio AND a.fecha_fin;

-- -------------------------------------------------------
-- Consulta 2: Vehículos alquilados en marzo de 2025
-- -------------------------------------------------------
SELECT DISTINCT v.modelo, v.marca, v.precio_dia
FROM vehiculos v
JOIN alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE MONTH(a.fecha_inicio) = 3 AND YEAR(a.fecha_inicio) = 2025;

-- -------------------------------------------------------
-- Consulta 3: Precio total del alquiler para cada cliente
-- Calcula el total que pagó cada cliente sumando el precio por día
-- multiplicado por la cantidad de días que alquiló cada vehículo.
-- -------------------------------------------------------
SELECT 
    c.nombre,
    SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio) * v.precio_dia) AS precio_total
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
JOIN vehiculos v ON a.id_vehiculo = v.id_vehiculo
GROUP BY c.nombre;

-- -------------------------------------------------------
-- Consulta 4: Clientes que no han realizado ningún pago
-- Muestra el nombre y email de los clientes que tienen
-- al menos un alquiler pero no tienen pagos registrados.
-- -------------------------------------------------------
SELECT DISTINCT c.nombre, c.email
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
LEFT JOIN pagos p ON a.id_alquiler = p.id_alquiler
WHERE p.id_pago IS NULL;

-- -------------------------------------------------------
-- Consulta 5: Promedio de los pagos realizados por cliente
-- Muestra el nombre del cliente y el promedio de los montos pagados
-- -------------------------------------------------------
SELECT 
    c.nombre,
    ROUND(AVG(p.monto), 2) AS promedio_pago
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
JOIN pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.nombre;

-- -------------------------------------------------------
-- Consulta 6: Vehículos disponibles para alquilar en una fecha específica (ej. 2025-03-18)
-- Muestra modelo, marca y precio_dia de vehículos que NO están alquilados ese día.
-- -------------------------------------------------------
SELECT modelo, marca, precio_dia
FROM vehiculos v
WHERE v.id_vehiculo NOT IN (
    SELECT id_vehiculo
    FROM alquileres
    WHERE '2025-08-26' BETWEEN fecha_inicio AND fecha_fin
);

-- -------------------------------------------------------
-- Consulta 7: Vehículos alquilados más de una vez en marzo de 2025
-- Muestra marca y modelo de vehículos con más de un alquiler en ese mes.
-- -------------------------------------------------------
SELECT 
    v.marca,
    v.modelo,
    COUNT(*) AS cantidad_alquileres
FROM vehiculos v
JOIN alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE MONTH(a.fecha_inicio) = 3 AND YEAR(a.fecha_inicio) = 2025
GROUP BY v.id_vehiculo, v.marca, v.modelo
HAVING COUNT(*) > 1;

-- -------------------------------------------------------
-- Consulta 8: Total pagado por cada cliente
-- Muestra el nombre y la suma total de montos pagados por cliente
-- -------------------------------------------------------
SELECT 
    c.nombre,
    ROUND(SUM(p.monto), 2) AS total_pagado
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
JOIN pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.nombre;

-- -------------------------------------------------------
-- Consulta 9: Clientes que alquilaron el vehículo Ford Focus (id_vehiculo = 3)
-- Muestra nombre del cliente y fecha de inicio del alquiler
-- -------------------------------------------------------
SELECT 
    c.nombre,
    a.fecha_inicio
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
WHERE a.id_vehiculo = 3;

-- -------------------------------------------------------
-- Consulta 10: Total de días alquilados por cliente, ordenado de mayor a menor
-- -------------------------------------------------------
SELECT 
    c.nombre,
    SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio)) AS total_dias_alquilados
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
GROUP BY c.nombre
ORDER BY total_dias_alquilados DESC;

