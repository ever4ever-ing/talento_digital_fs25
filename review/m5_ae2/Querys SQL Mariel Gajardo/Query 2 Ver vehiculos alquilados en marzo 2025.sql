SELECT vehiculos.modelo, vehiculos.marcar, vehiculos.precio_dia
FROM Vehiculos JOIN Alquileres
     ON vehiculos.id_vehiculo = alquileres.id_vehiculo
     WHERE (MONTH(alquileres.fecha_inicio) = 3 AND YEAR(alquileres.fecha_inicio) = 2025);