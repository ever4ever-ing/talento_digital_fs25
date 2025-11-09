SELECT clientes.id_cliente, clientes.nombre, AVG(pagos.monto) AS Promedio_pago
FROM Clientes
LEFT JOIN Alquileres ON alquileres.id_cliente = clientes.id_cliente 
LEFT JOIN Pagos ON alquileres.id_alquiler = pagos.id_alquiler
GROUP BY clientes.id_cliente, clientes.nombre;
