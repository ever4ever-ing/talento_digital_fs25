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
