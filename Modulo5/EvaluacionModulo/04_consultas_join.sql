-- Total de ventas de un producto durante el mes anterior
SELECT 
    p.id_producto,
    p.nombre,
    SUM(t.cantidad) as total_vendido,
    SUM(t.cantidad * p.precio) as ingresos_totales
FROM transacciones t
INNER JOIN productos p ON t.id_producto = p.id_producto
WHERE t.tipo = 'Venta'
    AND t.estado = 'Completada'
    AND YEAR(t.fecha) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
    AND MONTH(t.fecha) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)
    AND p.id_producto = 1  -- Cambiar por el ID del producto deseado
GROUP BY p.id_producto, p.nombre;

--2. Consultas con JOINs para obtener información relacionada
--INNER JOIN entre productos, proveedores y transacciones
SELECT 
    t.id_transaction,
    t.tipo,
    t.fecha,
    t.cantidad,
    t.estado,
    p.nombre as producto,
    p.precio,
    prov.nombre as proveedor,
    prov.telefono as contacto_proveedor
FROM transacciones t
INNER JOIN productos p ON t.id_producto = p.id_producto
INNER JOIN proveedores prov ON t.id_proveedor = prov.id_proveedor
WHERE t.tipo = 'Compra'
ORDER BY t.fecha DESC;


--LEFT JOIN para incluir transacciones sin proveedor

SELECT 
    t.id_transaction,
    t.tipo,
    t.fecha,
    t.cantidad,
    t.estado,
    p.nombre as producto,
    p.precio,
    COALESCE(prov.nombre, 'Sin proveedor') as proveedor
FROM transacciones t
INNER JOIN productos p ON t.id_producto = p.id_producto
LEFT JOIN proveedores prov ON t.id_proveedor = prov.id_proveedor
ORDER BY t.fecha DESC;

--3. Consulta con subconsultas para productos no vendidos
--Productos que no se han vendido en el último mes

SELECT 
    p.id_producto,
    p.nombre,
    p.cantidad as stock_actual,
    p.precio
FROM productos p
WHERE p.id_producto NOT IN (
    SELECT DISTINCT t.id_producto
    FROM transacciones t
    WHERE t.tipo = 'Venta'
        AND t.estado = 'Completada'
        AND t.fecha >= DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)
)
ORDER BY p.nombre;

--Productos que nunca han sido vendidos
SELECT 
    p.id_producto,
    p.nombre,
    p.cantidad as stock_actual,
    p.precio
FROM productos p
WHERE p.id_producto NOT IN (
    SELECT DISTINCT t.id_producto
    FROM transacciones t
    WHERE t.tipo = 'Venta'
        AND t.estado = 'Completada'
)
ORDER BY p.nombre;


--Productos sin movimiento en los últimos 3 meses
SELECT 
    p.id_producto,
    p.nombre,
    p.cantidad as stock_actual,
    p.precio,
    (SELECT MAX(t.fecha) 
     FROM transacciones t 
     WHERE t.id_producto = p.id_producto) as ultima_transaccion
FROM productos p
WHERE p.id_producto NOT IN (
    SELECT DISTINCT t.id_producto
    FROM transacciones t
    WHERE t.fecha >= DATE_SUB(CURRENT_DATE, INTERVAL 3 MONTH)
)
ORDER BY p.nombre;
--Consulta adicional: Resumen de transacciones por proveedor

SELECT 
    prov.id_proveedor,
    prov.nombre as proveedor,
    COUNT(t.id_transaction) as total_transacciones,
    SUM(CASE WHEN t.tipo = 'Compra' THEN t.cantidad ELSE 0 END) as total_compras,
    SUM(CASE WHEN t.tipo = 'Venta' THEN t.cantidad ELSE 0 END) as total_ventas,
    MIN(t.fecha) as primera_transaccion,
    MAX(t.fecha) as ultima_transaccion
FROM proveedores prov
LEFT JOIN transacciones t ON prov.id_proveedor = t.id_proveedor
GROUP BY prov.id_proveedor, prov.nombre
ORDER BY total_transacciones DESC;