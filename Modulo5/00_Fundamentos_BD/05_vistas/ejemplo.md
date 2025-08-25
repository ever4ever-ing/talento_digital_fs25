# Vistas en MySQL - Guía Completa con Ejemplos

Las vistas son "tablas virtuales" que simplifican consultas complejas y proporcionan una capa de abstracción sobre los datos. Este documento contiene ejemplos prácticos aplicados a un sistema de pedidos.

---

## 1. Vistas Básicas - Simplificación de Consultas

### Vista básica: Información completa de usuarios
```sql
CREATE VIEW vista_usuarios_completa AS
SELECT 
    u.id,
    u.nombre,
    u.apellido,
    CONCAT(u.nombre, ' ', u.apellido) AS nombre_completo,
    d.calle,
    d.colonia,
    d.ciudad,
    d.pais,
    CONCAT(d.calle, ', ', d.colonia, ', ', d.ciudad, ', ', d.pais) AS direccion_completa
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id;
```

### Consultar la vista
```sql
SELECT * FROM vista_usuarios_completa;
SELECT nombre_completo, ciudad, pais FROM vista_usuarios_completa WHERE pais = 'Chile';
```

---

## 2. Vistas con Agregaciones - Reportes

### Vista: Resumen de ventas por usuario
```sql
CREATE VIEW vista_resumen_usuarios AS
SELECT 
    u.id,
    u.nombre,
    u.apellido,
    CONCAT(u.nombre, ' ', u.apellido) AS cliente,
    d.ciudad,
    d.pais,
    COUNT(p.id) AS total_pedidos,
    COALESCE(SUM(p.total), 0) AS total_gastado,
    COALESCE(AVG(p.total), 0) AS promedio_pedido,
    COALESCE(MAX(p.total), 0) AS pedido_mayor,
    COALESCE(MIN(p.total), 0) AS pedido_menor,
    CASE 
        WHEN COALESCE(SUM(p.total), 0) = 0 THEN 'Sin pedidos'
        WHEN SUM(p.total) < 300 THEN 'Cliente básico'
        WHEN SUM(p.total) BETWEEN 300 AND 500 THEN 'Cliente regular'
        ELSE 'Cliente premium'
    END AS categoria_cliente
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido, d.ciudad, d.pais;
```

### Usar la vista para diferentes consultas
```sql
-- Clientes ordenados por total gastado
SELECT * FROM vista_resumen_usuarios
ORDER BY total_gastado DESC;

-- Clientes por categoría
SELECT categoria_cliente, COUNT(*) as cantidad
FROM vista_resumen_usuarios
GROUP BY categoria_cliente;

-- Clientes premium de una ciudad específica
SELECT * FROM vista_resumen_usuarios
WHERE categoria_cliente = 'Cliente premium' AND ciudad = 'Madrid';
```

## 3. Vistas con Joins Múltiples - Análisis de Productos

### Vista: Análisis de productos más vendidos
```sql
CREATE VIEW vista_productos_popularidad AS
SELECT 
    p.id,
    p.nombre,
    p.descripcion,
    COUNT(php.producto_id) AS veces_vendido,
    ROUND(
        (COUNT(php.producto_id) * 100.0 / 
         (SELECT COUNT(*) FROM pedidos_has_productos)), 
        2
    ) AS porcentaje_ventas,
    CASE 
        WHEN COUNT(php.producto_id) = 0 THEN 'Sin ventas'
        WHEN COUNT(php.producto_id) = 1 THEN 'Venta baja'
        WHEN COUNT(php.producto_id) BETWEEN 2 AND 3 THEN 'Venta media'
        ELSE 'Venta alta'
    END AS categoria_popularidad,
    -- Calcular un precio promedio estimado basado en los totales de pedidos
    CASE 
        WHEN COUNT(php.producto_id) > 0 THEN 'Disponible'
        ELSE 'Sin historial'
    END AS estado
FROM productos p
LEFT JOIN pedidos_has_productos php ON p.id = php.producto_id
GROUP BY p.id, p.nombre, p.descripcion;
```

### Consultas usando la vista
```sql
-- Productos ordenados por popularidad
SELECT * FROM vista_productos_popularidad 
ORDER BY veces_vendido DESC;

-- Productos de alta venta
SELECT * FROM vista_productos_popularidad 
WHERE categoria_popularidad = 'Venta alta';
```

## 4. Vista Detallada de Pedidos

### Vista: Pedidos con detalles completos
```sql
CREATE VIEW vista_pedidos_detallados AS
SELECT 
    ped.id AS pedido_id,
    ped.fecha,
    ped.total,
    CONCAT(u.nombre, ' ', u.apellido) AS cliente,
    u.id AS usuario_id,
    d.ciudad,
    d.pais,
    COUNT(php.producto_id) AS cantidad_productos,
    GROUP_CONCAT(
        pr.nombre 
        ORDER BY pr.nombre 
        SEPARATOR ', '
    ) AS productos,
    YEAR(ped.fecha) AS año,
    MONTH(ped.fecha) AS mes,
    DATE_FORMAT(ped.fecha, '%d/%m/%Y') AS fecha_formateada,
    CASE 
        WHEN ped.total < 300 THEN 'Pedido pequeño'
        WHEN ped.total BETWEEN 300 AND 400 THEN 'Pedido medio'
        ELSE 'Pedido grande'
    END AS categoria_pedido
FROM pedidos ped
JOIN usuarios u ON ped.usuario_id = u.id
JOIN direcciones d ON u.direccion_id = d.id
JOIN pedidos_has_productos php ON ped.id = php.pedido_id
JOIN productos pr ON php.producto_id = pr.id
GROUP BY ped.id, ped.fecha, ped.total, u.nombre, u.apellido, u.id, d.ciudad, d.pais;
```

### Consultas con la vista
```sql
-- Todos los pedidos detallados
SELECT * FROM vista_pedidos_detallados;

-- Pedidos de un año específico
SELECT * FROM vista_pedidos_detallados WHERE año = 2023;

-- Análisis por categoría de pedido
SELECT categoria_pedido, COUNT(*) 
FROM vista_pedidos_detallados 
GROUP BY categoria_pedido;
```

## 5. Vista de Análisis Geográfico

### Vista: Análisis por país/región
```sql
CREATE VIEW vista_analisis_geografico AS
SELECT 
    d.pais,
    d.ciudad,
    COUNT(DISTINCT u.id) AS total_usuarios,
    COUNT(p.id) AS total_pedidos,
    COALESCE(SUM(p.total), 0) AS ventas_totales,
    COALESCE(ROUND(AVG(p.total), 2), 0) AS promedio_pedido,
    CASE 
        WHEN COUNT(p.id) = 0 THEN 'Sin actividad'
        WHEN COUNT(p.id) = 1 THEN 'Actividad baja'
        WHEN COUNT(p.id) BETWEEN 2 AND 3 THEN 'Actividad media'
        ELSE 'Actividad alta'
    END AS nivel_actividad,
    GROUP_CONCAT(
        DISTINCT CONCAT(u.nombre, ' ', u.apellido)
        ORDER BY u.apellido 
        SEPARATOR '; '
    ) AS clientes
FROM direcciones d
JOIN usuarios u ON d.id = u.direccion_id
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY d.pais, d.ciudad;
```

### Consultas geográficas
```sql
-- Análisis por ubicación
SELECT * FROM vista_analisis_geografico;

-- Ventas totales por país
SELECT pais, SUM(ventas_totales) as total_pais 
FROM vista_analisis_geografico 
GROUP BY pais;
```

## 6. Vistas Temporales - Análisis de Fechas

### Vista: Análisis temporal de pedidos
```sql
CREATE VIEW vista_analisis_temporal AS
SELECT 
    p.id,
    p.fecha,
    p.total,
    YEAR(p.fecha) AS año,
    MONTH(p.fecha) AS mes,
    DAY(p.fecha) AS dia,
    DATE_FORMAT(p.fecha, '%Y-%m') AS año_mes,
    DATE_FORMAT(p.fecha, '%W') AS dia_semana,
    DATE_FORMAT(p.fecha, '%M') AS mes_nombre,
    QUARTER(p.fecha) AS trimestre,
    CONCAT('Q', QUARTER(p.fecha), '-', YEAR(p.fecha)) AS trimestre_año,
    DATEDIFF(CURDATE(), p.fecha) AS dias_desde_pedido,
    CASE 
        WHEN MONTH(p.fecha) IN (12, 1, 2) THEN 'Temporada Alta'
        WHEN MONTH(p.fecha) IN (6, 7, 8) THEN 'Temporada Media'
        ELSE 'Temporada Baja'
    END AS temporada
FROM pedidos p;
```

### Consultas temporales
```sql
-- Análisis temporal general
SELECT * FROM vista_analisis_temporal;

-- Ventas por año
SELECT año, COUNT(*) as pedidos_año, SUM(total) as ventas_año 
FROM vista_analisis_temporal 
GROUP BY año;

-- Análisis por temporada
SELECT temporada, COUNT(*), AVG(total) 
FROM vista_analisis_temporal 
GROUP BY temporada;
```

## 7. Vista Compleja - Dashboard Ejecutivo

### Vista: Dashboard ejecutivo completo
```sql
CREATE VIEW vista_dashboard_ejecutivo AS
SELECT 
    'Resumen General' AS categoria,
    NULL AS subcategoria,
    COUNT(DISTINCT u.id) AS total_usuarios,
    COUNT(DISTINCT p.id) AS total_pedidos,
    COUNT(DISTINCT pr.id) AS total_productos,
    ROUND(SUM(p.total), 2) AS ingresos_totales,
    ROUND(AVG(p.total), 2) AS ticket_promedio,
    COUNT(DISTINCT d.pais) AS paises_activos
FROM usuarios u
CROSS JOIN pedidos p
CROSS JOIN productos pr
CROSS JOIN direcciones d
WHERE u.direccion_id = d.id

UNION ALL

SELECT 
    'Por País' AS categoria,
    d.pais AS subcategoria,
    COUNT(DISTINCT u.id) AS usuarios,
    COUNT(p.id) AS pedidos,
    0 AS productos, -- No aplica para este grupo
    COALESCE(SUM(p.total), 0) AS ingresos,
    COALESCE(AVG(p.total), 0) AS promedio,
    1 AS activo
FROM direcciones d
JOIN usuarios u ON d.id = u.direccion_id
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY d.pais

UNION ALL

SELECT 
    'Productos Top' AS categoria,
    pr.nombre AS subcategoria,
    0 AS usuarios, -- No aplica
    COUNT(php.producto_id) AS pedidos,
    1 AS productos,
    0 AS ingresos, -- No tenemos precio unitario
    0 AS promedio,
    COUNT(php.producto_id) AS popularidad
FROM productos pr
LEFT JOIN pedidos_has_productos php ON pr.id = php.producto_id
GROUP BY pr.id, pr.nombre
ORDER BY COUNT(php.producto_id) DESC;
```

## 8. Operaciones con Vistas

### Modificar una vista existente
```sql 
-- Ejemplo de CREATE OR REPLACE VIEW
CREATE OR REPLACE VIEW vista_usuarios_completa AS
SELECT 
    u.id,
    UPPER(u.nombre) AS nombre,
    UPPER(u.apellido) AS apellido,
    UPPER(CONCAT(u.nombre, ' ', u.apellido)) AS nombre_completo,
    d.calle,
    d.colonia,
    d.ciudad,
    d.pais,
    UPPER(CONCAT(d.calle, ', ', d.colonia, ', ', d.ciudad, ', ', d.pais)) AS direccion_completa
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id;
```

### Ver información de las vistas
```sql
-- Listar todas las vistas
SHOW FULL TABLES WHERE Table_type = 'VIEW';

-- Ver la definición de una vista
SHOW CREATE VIEW vista_usuarios_completa;
```

## 9. Ejemplos de Uso Práctico de las Vistas

### Consulta 1: Top clientes por país
```sql
SELECT 
    pais,
    cliente,
    total_gastado
FROM vista_resumen_usuarios 
WHERE categoria_cliente IN ('Cliente regular', 'Cliente premium')
ORDER BY pais, total_gastado DESC;
```

### Consulta 2: Productos que necesitan promoción
```sql
SELECT 
    nombre,
    descripcion,
    veces_vendido,
    categoria_popularidad
FROM vista_productos_popularidad 
WHERE categoria_popularidad IN ('Sin ventas', 'Venta baja')
ORDER BY veces_vendido ASC;
```

### Consulta 3: Análisis de ventas por trimestre
```sql
SELECT 
    trimestre_año,
    COUNT(*) AS pedidos,
    SUM(total) AS ventas,
    AVG(total) AS promedio
FROM vista_analisis_temporal
GROUP BY trimestre_año, trimestre, año
ORDER BY año, trimestre;
```

### Consulta 4: Combinar vistas para análisis complejo
```sql
SELECT 
    vuc.pais,
    vuc.ciudad,
    vuc.nombre_completo,
    vru.total_pedidos,
    vru.categoria_cliente,
    COUNT(vpd.pedido_id) AS pedidos_detallados
FROM vista_usuarios_completa vuc
LEFT JOIN vista_resumen_usuarios vru ON vuc.id = vru.id
LEFT JOIN vista_pedidos_detallados vpd ON vuc.id = vpd.usuario_id
GROUP BY vuc.id, vuc.pais, vuc.ciudad, vuc.nombre_completo, vru.total_pedidos, vru.categoria_cliente
ORDER BY vru.total_gastado DESC;
```

## 10. Eliminar Vistas

### Comandos para eliminar vistas (comentado para seguridad)
```sql
-- Para eliminar las vistas cuando ya no las necesites:
-- DROP VIEW IF EXISTS vista_usuarios_completa;
-- DROP VIEW IF EXISTS vista_resumen_usuarios;
-- DROP VIEW IF EXISTS vista_productos_popularidad;
-- DROP VIEW IF EXISTS vista_pedidos_detallados;
-- DROP VIEW IF EXISTS vista_analisis_geografico;
-- DROP VIEW IF EXISTS vista_analisis_temporal;
-- DROP VIEW IF EXISTS vista_dashboard_ejecutivo;
```