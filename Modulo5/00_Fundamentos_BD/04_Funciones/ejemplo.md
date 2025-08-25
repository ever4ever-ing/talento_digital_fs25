# Funciones MySQL - Guía Completa con Ejemplos

Este documento contiene ejemplos prácticos de las principales funciones de MySQL aplicadas a un sistema de pedidos.

---

## 1. Funciones de Manipulación de Cadenas

### CONCAT - Crear dirección completa
```sql
SELECT 
    u.nombre,
    u.apellido,
    CONCAT(d.calle, ', ', d.colonia, ', ', d.ciudad, ', ', d.pais) AS direccion_completa
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id;
```

### LENGTH - Verificar longitud de nombres de productos
```sql
SELECT 
    nombre,
    LENGTH(nombre) AS longitud_nombre,
    CASE 
        WHEN LENGTH(nombre) > 8 THEN 'Nombre largo'
        ELSE 'Nombre corto'
    END AS categoria_longitud
FROM productos;
```

### SUBSTRING - Extraer código de área de dirección
```sql
SELECT 
    calle,
    SUBSTRING(calle, 1, 5) AS codigo_calle,
    ciudad
FROM direcciones;
```

### UPPER y LOWER - Normalizar datos
```sql
SELECT 
    UPPER(nombre) AS nombre_mayuscula,
    LOWER(descripcion) AS descripcion_minuscula,
    CONCAT(UPPER(SUBSTRING(nombre, 1, 1)), LOWER(SUBSTRING(nombre, 2))) AS nombre_capitalizado
FROM productos;
```

---

## 2. Funciones Numéricas

### SUM - Total de ventas por usuario
```sql
SELECT 
    u.nombre,
    u.apellido,
    SUM(p.total) AS total_gastado
FROM usuarios u
JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido;
```

### AVG - Promedio de pedidos
```sql
SELECT 
    AVG(total) AS promedio_pedidos,
    ROUND(AVG(total), 2) AS promedio_redondeado
FROM pedidos;
```

### MAX y MIN - Valores extremos de pedidos
```sql
SELECT 
    MAX(total) AS pedido_mayor,
    MIN(total) AS pedido_menor,
    MAX(total) - MIN(total) AS diferencia
FROM pedidos;
```

### ROUND - Redondear totales con descuentos simulados
```sql
SELECT 
    id,
    total,
    ROUND(total * 0.85, 2) AS total_con_descuento,
    ROUND(total * 0.15, 2) AS descuento_aplicado
FROM pedidos;
```

---

## 3. Funciones de Fecha y Hora

### NOW, CURDATE, CURTIME - Información temporal actual
```sql
SELECT 
    NOW() AS fecha_hora_actual,
    CURDATE() AS fecha_actual,
    CURTIME() AS hora_actual;
```

### DATE_FORMAT - Formatear fechas de pedidos
```sql
SELECT 
    id,
    fecha,
    DATE_FORMAT(fecha, '%d/%m/%Y') AS fecha_formato_latino,
    DATE_FORMAT(fecha, '%W, %M %d, %Y') AS fecha_formato_completo
FROM pedidos;
```

### DAY, MONTH, YEAR - Análisis temporal de pedidos
```sql
SELECT 
    YEAR(fecha) AS año,
    MONTH(fecha) AS mes,
    DAY(fecha) AS dia,
    COUNT(*) AS cantidad_pedidos,
    SUM(total) AS total_mes
FROM pedidos
GROUP BY YEAR(fecha), MONTH(fecha), DAY(fecha)
ORDER BY YEAR(fecha), MONTH(fecha), DAY(fecha);
```


---

## 4. Funciones de Agregación

### COUNT - Conteo de pedidos por usuario
```sql
SELECT 
    u.nombre,
    u.apellido,
    COUNT(p.id) AS total_pedidos,
    COALESCE(SUM(p.total), 0) AS total_gastado
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido;
```

### GROUP_CONCAT - Productos por pedido
```sql
SELECT 
    p.id AS pedido_id,
    p.fecha,
    p.total,
    GROUP_CONCAT(pr.nombre ORDER BY pr.nombre SEPARATOR ', ') AS productos_pedido
FROM pedidos p
JOIN pedidos_has_productos php ON p.id = php.pedido_id
JOIN productos pr ON php.producto_id = pr.id
GROUP BY p.id, p.fecha, p.total;
```

### Usuarios por ciudad
```sql
SELECT 
    d.ciudad,
    d.pais,
    GROUP_CONCAT(CONCAT(u.nombre, ' ', u.apellido) ORDER BY u.apellido SEPARATOR '; ') AS usuarios_ciudad
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id
GROUP BY d.ciudad, d.pais;
```

---

## 5. Funciones de Control de Flujo

### IF - Clasificar pedidos por monto
```sql
SELECT 
    id,
    fecha,
    total,
    IF(total > 400, 'Alto valor', 'Valor normal') AS categoria_pedido
FROM pedidos;
```

### CASE - Clasificación detallada de usuarios por gasto
```sql
SELECT 
    u.nombre,
    u.apellido,
    COALESCE(SUM(p.total), 0) AS total_gastado,
    CASE 
        WHEN COALESCE(SUM(p.total), 0) = 0 THEN 'Sin pedidos'
        WHEN SUM(p.total) < 300 THEN 'Cliente básico'
        WHEN SUM(p.total) BETWEEN 300 AND 500 THEN 'Cliente regular'
        ELSE 'Cliente premium'
    END AS categoria_cliente
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido;
```

### CASE con análisis geográfico
```sql
SELECT 
    d.pais,
    COUNT(u.id) AS usuarios_pais,
    CASE d.pais
        WHEN 'Chile' THEN 'Mercado principal'
        WHEN 'México' THEN 'Mercado secundario'
        WHEN 'Costa Rica' THEN 'Mercado emergente'
        ELSE 'Otros mercados'
    END AS categoria_mercado
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id
GROUP BY d.pais;
```

---

## 6. Funciones de Conversión de Datos

### CAST - Convertir fechas y números
```sql
SELECT 
    id,
    CAST(fecha AS CHAR) AS fecha_texto,
    CAST(total AS SIGNED) AS total_entero,
    CAST(total AS DECIMAL(10,1)) AS total_un_decimal
FROM pedidos;
```

### CONVERT - Conversión con más opciones
```sql
SELECT 
    nombre,
    CONVERT(nombre USING utf8) AS nombre_utf8,
    descripcion,
    LENGTH(descripcion) AS longitud_original
FROM productos;
```

---

## 7. Consultas Combinadas Avanzadas

### Reporte completo de ventas por país
```sql
SELECT 
    d.pais,
    COUNT(DISTINCT u.id) AS total_usuarios,
    COUNT(p.id) AS total_pedidos,
    COALESCE(SUM(p.total), 0) AS ventas_totales,
    ROUND(AVG(p.total), 2) AS promedio_pedido,
    GROUP_CONCAT(DISTINCT 
        CONCAT(u.nombre, ' ', u.apellido) 
        ORDER BY u.apellido 
        SEPARATOR '; '
    ) AS clientes,
    CASE 
        WHEN COUNT(p.id) = 0 THEN 'Sin actividad'
        WHEN COUNT(p.id) = 1 THEN 'Actividad baja'
        WHEN COUNT(p.id) BETWEEN 2 AND 3 THEN 'Actividad media'
        ELSE 'Actividad alta'
    END AS nivel_actividad
FROM direcciones d
JOIN usuarios u ON d.id = u.direccion_id
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY d.pais
ORDER BY COALESCE(SUM(p.total), 0) DESC;
```

### Análisis de productos más vendidos
```sql
SELECT 
    pr.nombre AS producto,
    UPPER(pr.descripcion) AS descripcion,
    COUNT(php.producto_id) AS veces_vendido,
    ROUND(
        (COUNT(php.producto_id) * 100.0 / (SELECT COUNT(*) FROM pedidos_has_productos)), 
        2
    ) AS porcentaje_ventas,
    IF(COUNT(php.producto_id) > 2, 'Popular', 'Poco popular') AS popularidad
FROM productos pr
LEFT JOIN pedidos_has_productos php ON pr.id = php.producto_id
GROUP BY pr.id, pr.nombre, pr.descripcion
ORDER BY COUNT(php.producto_id) DESC;
```

