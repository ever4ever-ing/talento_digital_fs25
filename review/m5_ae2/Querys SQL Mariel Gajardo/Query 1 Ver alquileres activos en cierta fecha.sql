SELECT clientes.nombre, clientes.email, clientes.telefono
FROM clientes JOIN Alquileres 
     ON clientes.id_cliente = alquileres.id_cliente
     WHERE '2025-03-15' BETWEEN fecha_inicio AND fecha_fin;