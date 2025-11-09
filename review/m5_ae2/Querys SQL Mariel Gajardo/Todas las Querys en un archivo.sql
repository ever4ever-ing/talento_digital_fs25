SELECT clientes.nombre, clientes.email, clientes.telefono
FROM clientes JOIN Alquileres 
     ON clientes.id_cliente = alquileres.id_cliente
     WHERE '2025-03-15' BETWEEN fecha_inicio AND fecha_fin;
     
     SELECT vehiculos.modelo, vehiculos.marcar, vehiculos.precio_dia
FROM Vehiculos JOIN Alquileres
     ON vehiculos.id_vehiculo = alquileres.id_vehiculo
     WHERE (MONTH(alquileres.fecha_inicio) = 3 AND YEAR(alquileres.fecha_inicio) = 2025);
     
     SELECT 
    c.nombre,
    a.fecha_inicio,
    a.fecha_fin,
    v.precio_dia,
    datediff(a.fecha_fin,a.fecha_inicio) as dias,
    datediff(a.fecha_fin,a.fecha_inicio) * v.precio_dia AS total_pagar
    
FROM clientes c
JOIN alquileres a ON c.id_cliente = a.id_cliente
JOIN vehiculos v ON a.id_vehiculo = v.id_vehiculo;

SELECT clientes.nombre, clientes.email 
FROM Clientes 
LEFT JOIN Alquileres ON clientes.id_cliente = alquileres.id_cliente
LEFT JOIN Pagos ON alquileres.id_alquiler = pagos.id_alquiler
WHERE pagos.id_pago IS NULL;

SELECT clientes.id_cliente, clientes.nombre, AVG(pagos.monto) AS Promedio_pago
FROM Clientes
LEFT JOIN Alquileres ON alquileres.id_cliente = clientes.id_cliente 
LEFT JOIN Pagos ON alquileres.id_alquiler = pagos.id_alquiler
GROUP BY clientes.id_cliente, clientes.nombre;

SELECT vehiculos.modelo, vehiculos.marcar, vehiculos.precio_dia, alquileres.fecha_inicio, alquileres.fecha_fin
FROM Vehiculos
LEFT JOIN Alquileres on vehiculos.id_vehiculo = alquileres.id_vehiculo
WHERE (alquileres.fecha_inicio <= '2025-03-18' AND alquileres.fecha_fin <= '2025-03-18')
;

SELECT vehiculos.marcar, vehiculos.modelo
FROM Vehiculos
INNER JOIN Alquileres ON alquileres.id_vehiculo = vehiculos.id_vehiculo
WHERE MONTH(alquileres.fecha_inicio) = 3 
AND YEAR(alquileres.fecha_inicio) = 2025
GROUP BY vehiculos.id_vehiculo, vehiculos.marcar, vehiculos.modelo
HAVING COUNT(alquileres.id_alquiler) > 1;

SELECT clientes.nombre AS Nombre_Cliente, SUM(pagos.monto) AS Total_Pago
FROM Clientes
INNER JOIN Alquileres ON alquileres.id_cliente = clientes.id_cliente 
INNER JOIN Pagos ON alquileres.id_alquiler = pagos.id_alquiler
WHERE pagos.monto IS NOT NULL
GROUP BY clientes.id_cliente, clientes.nombre;

SELECT clientes.nombre, alquileres.fecha_inicio, alquileres.fecha_fin, vehiculos.modelo, vehiculos.marcar
From Clientes
JOIN alquileres on alquileres.id_cliente = clientes.id_cliente
JOIN vehiculos on vehiculos.id_vehiculo = alquileres.id_vehiculo
WHERE vehiculos.id_vehiculo = 3;

SELECT clientes.nombre AS Nombre_Cliente, 
SUM(DATEDIFF(alquileres.fecha_fin,alquileres.fecha_inicio)) AS Total_Dias_Alquilados
FROM Clientes
JOIN Alquileres ON clientes.id_cliente = alquileres.id_cliente
GROUP BY clientes.id_cliente, clientes.nombre
ORDER BY Total_Dias_Alquilados DESC;