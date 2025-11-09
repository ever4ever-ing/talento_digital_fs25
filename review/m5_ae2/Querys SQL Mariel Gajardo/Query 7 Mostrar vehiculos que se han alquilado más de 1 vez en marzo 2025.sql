SELECT vehiculos.marcar, vehiculos.modelo
FROM Vehiculos
INNER JOIN Alquileres ON alquileres.id_vehiculo = vehiculos.id_vehiculo
WHERE MONTH(alquileres.fecha_inicio) = 3 
AND YEAR(alquileres.fecha_inicio) = 2025
GROUP BY vehiculos.id_vehiculo, vehiculos.marcar, vehiculos.modelo
HAVING COUNT(alquileres.id_alquiler) > 1;
