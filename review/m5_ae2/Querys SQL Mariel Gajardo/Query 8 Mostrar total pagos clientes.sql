SELECT clientes.nombre AS Nombre_Cliente, SUM(pagos.monto) AS Total_Pago
FROM Clientes
LEFT JOIN Alquileres ON alquileres.id_cliente = clientes.id_cliente 
LEFT JOIN Pagos ON alquileres.id_alquiler = pagos.id_alquiler
WHERE pagos.monto IS NOT NULL
GROUP BY clientes.id_cliente, clientes.nombre;
