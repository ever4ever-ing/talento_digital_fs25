SELECT clientes.nombre, clientes.email 
FROM Clientes 
LEFT JOIN Alquileres ON clientes.id_cliente = alquileres.id_cliente
LEFT JOIN Pagos ON alquileres.id_alquiler = pagos.id_alquiler
WHERE pagos.id_pago IS NULL;