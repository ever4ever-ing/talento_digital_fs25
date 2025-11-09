SELECT vehiculos.modelo, vehiculos.marcar, vehiculos.precio_dia, alquileres.fecha_inicio, alquileres.fecha_fin
FROM Vehiculos
LEFT JOIN Alquileres on vehiculos.id_vehiculo = alquileres.id_vehiculo
WHERE (alquileres.fecha_inicio <= '2025-03-18' AND alquileres.fecha_fin <= '2025-03-18');
