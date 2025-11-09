-- Conectar a la base de datos
USE alquiler_autos_db;


-- Consulta 1: Mostrar el nombre, teléfono y email de todos los clientes que tienen un
-- alquiler activo (es decir, cuya fecha actual esté dentro del rango entre fecha_inicio y fecha_fin).
SELECT
    c.nombre,
    c.telefono,
    c.email
FROM
    Clientes c
JOIN
    Alquileres a ON c.id_cliente = a.id_cliente
WHERE
    '2025-03-14' BETWEEN a.fecha_inicio AND a.fecha_fin;


-- Consulta 2: Mostrar los vehículos que se alquilaron en el mes de marzo de 2025. Debe
-- mostrar el modelo, marca, y precio_dia de esos vehículos.
SELECT DISTINCT
    v.modelo,
    v.marca,
    v.precio_dia
FROM
    Vehiculos v
JOIN
    Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE
    MONTH(a.fecha_inicio) = 3 AND YEAR(a.fecha_inicio) = 2025;


-- Consulta 3: Calcular el precio total del alquiler para cada cliente, considerando el
-- número de días que alquiló el vehículo (el precio por día de cada vehículo multiplicado
-- por la cantidad de días de alquiler).
SELECT
    c.nombre,
    v.modelo,
    DATEDIFF(a.fecha_fin, a.fecha_inicio) AS dias_alquiler,
    v.precio_dia,
    DATEDIFF(a.fecha_fin, a.fecha_inicio) * v.precio_dia AS total_a_pagar
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Vehiculos v ON a.id_vehiculo = v.id_vehiculo;


-- Consulta 4: Encontrar los clientes que no han realizado ningún pago (no tienen
-- registros en la tabla Pagos). Muestra su nombre y email.
SELECT c.nombre, c.email
FROM Clientes c
WHERE c.id_cliente NOT IN (
    SELECT a.id_cliente
    FROM Alquileres a
    INNER JOIN Pagos p ON a.id_alquiler = p.id_alquiler
);


-- Consulta 5: Calcular el promedio de los pagos realizados por cada cliente. Muestra el
-- nombre del cliente y el promedio de pago.
SELECT c.nombre, AVG(p.monto) AS promedio_pago
FROM Clientes c
JOIN Alquileres a ON c.id_cliente = a.id_cliente
JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.nombre;


-- Consulta 6: Mostrar los vehículos que están disponibles para alquilar en una fecha
-- específica (por ejemplo, 2025-03-18). Debe mostrar el modelo, marca y precio_dia.
-- Si el vehículo está ocupado, no se debe incluir.
SELECT v.marca, v.modelo, v.precio_dia
FROM Vehiculos v
WHERE v.id_vehiculo NOT IN (
    SELECT a.id_vehiculo
    FROM Alquileres a
    WHERE '2025-03-18' BETWEEN a.fecha_inicio AND a.fecha_fin
);


-- Consulta 7: Encontrar la marca y el modelo de los vehículos que se alquilaron más de
-- una vez en el mes de marzo de 2025.
SELECT v.marca, v.modelo
FROM Vehiculos v
INNER JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE YEAR(a.fecha_inicio) = 2025 AND MONTH(a.fecha_inicio) = 3
GROUP BY v.id_vehiculo, v.marca, v.modelo
HAVING COUNT(a.id_alquiler) > 1;


-- Consulta 8: Mostrar el total de monto pagado por cada cliente. Debe mostrar el
-- nombre del cliente y la cantidad total de pagos realizados (suma del monto de los pagos).
SELECT c.nombre, SUM(p.monto) AS total_pagado
FROM Clientes c
INNER JOIN alquileres a ON c.id_cliente = a.id_cliente
INNER JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.id_cliente, c.nombre;


-- Consulta 9: Mostrar los clientes que alquilaron el vehículo Ford Focus (con id_vehiculo = 3).
-- Debe mostrar el nombre del cliente y la fecha del alquiler.
SELECT c.nombre, a.fecha_inicio, a.fecha_fin
FROM Alquileres a
JOIN Clientes c ON a.id_cliente = c.id_cliente
WHERE a.id_vehiculo = 3;


-- Consulta 10: Realizar una consulta que muestre el nombre del cliente y el total de días
-- alquilados de cada cliente, ordenado de mayor a menor total de días. El total de días
-- es calculado como la diferencia entre fecha_inicio y fecha_fin.
SELECT c.nombre, SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio)) AS total_dias
FROM Alquileres a
JOIN Clientes c ON a.id_cliente = c.id_cliente
GROUP BY c.id_cliente
ORDER BY total_dias DESC;