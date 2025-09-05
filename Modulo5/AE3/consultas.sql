-- Consultar clientes con sus artículos y estado
SELECT c.nombre, c.telefono, a.tipo_articulo, a.estado
FROM Clientes c
INNER JOIN Artículos a ON c.id_cliente = a.id_cliente
ORDER BY c.nombre;

-- Consultar citas pendientes
SELECT c.nombre, ci.fecha_hora, ci.estado
FROM Citas ci
INNER JOIN Clientes c ON ci.id_cliente = c.id_cliente
WHERE ci.estado = 'pendiente'
ORDER BY ci.fecha_hora;

-- Consultar pagos realizados por cada cliente
SELECT c.nombre, SUM(p.monto) as total_pagado, COUNT(p.id_pago) as cantidad_pagos
FROM Pagos p
INNER JOIN Clientes c ON p.id_cliente = c.id_cliente
GROUP BY p.id_cliente;