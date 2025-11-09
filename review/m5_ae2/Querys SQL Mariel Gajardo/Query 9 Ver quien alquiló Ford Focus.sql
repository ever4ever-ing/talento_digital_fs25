SELECT clientes.nombre, alquileres.fecha_inicio, alquileres.fecha_fin, vehiculos.modelo, vehiculos.marcar
From Clientes
JOIN alquileres on alquileres.id_cliente = clientes.id_cliente
JOIN vehiculos on vehiculos.id_vehiculo = alquileres.id_vehiculo
WHERE vehiculos.id_vehiculo = 3;