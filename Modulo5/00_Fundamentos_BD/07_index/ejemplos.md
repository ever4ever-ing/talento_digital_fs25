# Ejemplos de Índices en MySQL

**Base de Datos:** Sistema de Pedidos  
**Objetivo:** Optimización de Rendimiento de Consultas

## 1. Análisis Inicial - Ver Índices Existentes

### Ver todos los índices de las tablas
```sql
SHOW INDEX FROM usuarios;
SHOW INDEX FROM pedidos;
SHOW INDEX FROM productos;
SHOW INDEX FROM direcciones;
SHOW INDEX FROM pedidos_has_productos;
```

### Ver información detallada de índices
```sql
SELECT 
    TABLE_NAME,
    INDEX_NAME,
    COLUMN_NAME,
    NON_UNIQUE,
    INDEX_TYPE,
    CARDINALITY
FROM INFORMATION_SCHEMA.STATISTICS 
WHERE TABLE_SCHEMA = DATABASE()
ORDER BY TABLE_NAME, INDEX_NAME, SEQ_IN_INDEX;
```

## 2. Consultas Sin Índices - Análisis de Rendimiento

### Activar el profiling para medir rendimiento
```sql
SET profiling = 1;

-- Consulta que puede beneficiarse de índices
SELECT * FROM usuarios WHERE apellido = 'Romero';

-- Consulta de rango de fechas
SELECT * FROM pedidos WHERE fecha BETWEEN '2023-01-01' AND '2023-12-31';

-- Consulta con JOIN sin optimizar
SELECT u.nombre, u.apellido, p.fecha, p.total
FROM usuarios u
JOIN pedidos p ON u.id = p.usuario_id
WHERE u.apellido LIKE 'S%';
```

### Ver el rendimiento de las consultas
```sql
-- Ver el rendimiento de las consultas
SHOW PROFILES;

-- Analizar plan de ejecución (EXPLAIN)
EXPLAIN SELECT * FROM usuarios WHERE apellido = 'Romero';
EXPLAIN SELECT * FROM pedidos WHERE fecha BETWEEN '2023-01-01' AND '2023-12-31';
```

## 3. Índices Simples - Una Columna

### Crear índices en columnas frecuentemente consultadas
```sql
CREATE INDEX idx_usuarios_apellido ON usuarios(apellido);

-- Crear índice en fecha de pedidos
CREATE INDEX idx_pedidos_fecha ON pedidos(fecha);

-- Crear índice en nombre de productos
CREATE INDEX idx_productos_nombre ON productos(nombre);

-- Crear índice en país de direcciones
CREATE INDEX idx_direcciones_pais ON direcciones(pais);
```

### Verificar que los índices se crearon
```sql
SHOW INDEX FROM usuarios WHERE Key_name = 'idx_usuarios_apellido';
SHOW INDEX FROM pedidos WHERE Key_name = 'idx_pedidos_fecha';
```

## 4. Pruebas de Rendimiento con Índices

### Consultas optimizadas con índices
```sql
-- Mismas consultas que antes, ahora optimizadas
EXPLAIN SELECT * FROM usuarios WHERE apellido = 'Romero';
EXPLAIN SELECT * FROM pedidos WHERE fecha BETWEEN '2023-01-01' AND '2023-12-31';

-- Consulta optimizada con índice
SELECT * FROM usuarios WHERE apellido = 'Romero';
SELECT * FROM pedidos WHERE fecha BETWEEN '2023-01-01' AND '2023-12-31';

-- Comparar rendimiento
SHOW PROFILES;
```

## 5. Índices Compuestos - Múltiples Columnas

### Crear índices compuestos para consultas específicas
```sql

-- Comparar rendimiento
SHOW PROFILES;

-- ============================================
-- 5. ÍNDICES COMPUESTOS - MÚLTIPLES COLUMNAS
-- ============================================

-- Índice compuesto para consultas que filtran por usuario y fecha
CREATE INDEX idx_pedidos_usuario_fecha ON pedidos(usuario_id, fecha);

-- Índice compuesto para direcciones por país y ciudad
CREATE INDEX idx_direcciones_pais_ciudad ON direcciones(pais, ciudad);

-- Índice para la tabla de relación muchos a muchos
CREATE INDEX idx_pedidos_productos ON pedidos_has_productos(pedido_id, producto_id);
```

### Verificar los índices compuestos
```sql
SHOW INDEX FROM pedidos WHERE Key_name = 'idx_pedidos_usuario_fecha';
SHOW INDEX FROM direcciones WHERE Key_name = 'idx_direcciones_pais_ciudad';
```

## 6. Pruebas con Índices Compuestos

### Consultas que aprovechan los índices compuestos
```sql
EXPLAIN SELECT * FROM pedidos WHERE usuario_id = 3 AND fecha >= '2023-01-01';

EXPLAIN SELECT * FROM direcciones WHERE pais = 'Chile' AND ciudad = 'Temuco';

-- Consulta que usa JOIN optimizado
EXPLAIN SELECT 
    u.nombre, 
    u.apellido, 
    p.fecha, 
    p.total
FROM usuarios u
JOIN pedidos p ON u.id = p.usuario_id
WHERE u.id = 3 AND p.fecha >= '2023-01-01';
```

## 7. Índices Únicos - Garantizar Unicidad

### Ejemplos de índices únicos
```sql

-- Consulta que usa JOIN optimizado
EXPLAIN SELECT 
    u.nombre, 
    u.apellido, 
    p.fecha, 
    p.total
FROM usuarios u
JOIN pedidos p ON u.id = p.usuario_id
WHERE u.id = 3 AND p.fecha >= '2023-01-01';

-- ============================================
-- 7. ÍNDICES ÚNICOS - GARANTIZAR UNICIDAD
-- ============================================

-- Agregar una columna de email a usuarios (simulado con ALTER TABLE)
-- ALTER TABLE usuarios ADD COLUMN email VARCHAR(100);

-- Crear índice único para email (evitar duplicados)
-- CREATE UNIQUE INDEX idx_usuarios_email_unique ON usuarios(email);

-- Ejemplo de índice único en combinación de columnas
-- Asegurar que un producto solo aparezca una vez por pedido
-- (Este ya debería existir como PRIMARY KEY o UNIQUE constraint)

-- Verificar constraint único existente en pedidos_has_productos
SHOW CREATE TABLE pedidos_has_productos;
```

## 8. Índices Funcionales - Expresiones

### Crear índices en expresiones y funciones
```sql

-- ============================================
-- 8. ÍNDICES FUNCIONALES - EXPRESIONES
-- ============================================

-- Índice en función UPPER para búsquedas sin importar mayúsculas/minúsculas
CREATE INDEX idx_usuarios_apellido_upper ON usuarios((UPPER(apellido)));

-- Índice en función YEAR para consultas por año
CREATE INDEX idx_pedidos_year ON pedidos((YEAR(fecha)));

-- Índice en función LENGTH para búsquedas por longitud de nombre
CREATE INDEX idx_productos_nombre_length ON productos((LENGTH(nombre)));
```

## 9. Pruebas con Índices Funcionales

### Consultas que aprovechan índices funcionales
```sql

-- ============================================
-- 9. PRUEBAS CON ÍNDICES FUNCIONALES
-- ============================================

-- Consultas que aprovechan índices funcionales
EXPLAIN SELECT * FROM usuarios WHERE UPPER(apellido) = 'ROMERO';

EXPLAIN SELECT * FROM pedidos WHERE YEAR(fecha) = 2023;

EXPLAIN SELECT * FROM productos WHERE LENGTH(nombre) > 5;

-- Ejecutar las consultas
SELECT * FROM usuarios WHERE UPPER(apellido) = 'ROMERO';
SELECT * FROM pedidos WHERE YEAR(fecha) = 2023;
SELECT * FROM productos WHERE LENGTH(nombre) > 5;
```

## 10. Análisis de Cardinalidad y Selectividad

### Analizar la distribución de datos para decidir índices
```sql
SELECT * FROM productos WHERE LENGTH(nombre) > 5;

-- ============================================
-- 10. ANÁLISIS DE CARDINALIDAD Y SELECTIVIDAD
-- ============================================

SELECT 
    'apellidos_usuarios' as analisis,
    COUNT(DISTINCT apellido) as valores_unicos,
    COUNT(*) as total_registros,
    ROUND(COUNT(DISTINCT apellido) / COUNT(*) * 100, 2) as selectividad_pct
FROM usuarios

UNION ALL

SELECT 
    'paises',
    COUNT(DISTINCT pais),
    COUNT(*),
    ROUND(COUNT(DISTINCT pais) / COUNT(*) * 100, 2)
FROM direcciones

UNION ALL

SELECT 
    'años_pedidos',
    COUNT(DISTINCT YEAR(fecha)),
    COUNT(*),
    ROUND(COUNT(DISTINCT YEAR(fecha)) / COUNT(*) * 100, 2)
FROM pedidos;
```

### Ver estadísticas de índices
```sql
SELECT 
    TABLE_NAME,
    INDEX_NAME,
    CARDINALITY,
    CASE 
        WHEN CARDINALITY > 100 THEN 'Alta selectividad'
        WHEN CARDINALITY BETWEEN 10 AND 100 THEN 'Media selectividad'
        ELSE 'Baja selectividad'
    END as selectividad
FROM INFORMATION_SCHEMA.STATISTICS 
WHERE TABLE_SCHEMA = DATABASE()
    AND INDEX_NAME != 'PRIMARY'
ORDER BY CARDINALITY DESC;
```

## 11. Índices Parciales - Filtros Condicionales

### Alternativas para índices condicionales
```sql
-- MySQL no soporta índices parciales directamente como PostgreSQL
-- Pero podemos simular con índices en columnas calculadas

-- Crear una columna calculada para pedidos del 2023
-- ALTER TABLE pedidos ADD COLUMN es_2023 BOOLEAN GENERATED ALWAYS AS (YEAR(fecha) = 2023);
-- CREATE INDEX idx_pedidos_2023 ON pedidos(es_2023);

-- Alternativa: Índice en expresión condicional
-- Para pedidos con montos altos
CREATE INDEX idx_pedidos_montos_altos ON pedidos(total) WHERE total > 400;
```

## 12. Monitoreo de Uso de Índices

### Verificar que los índices se están usando
```sql
SELECT 
    OBJECT_SCHEMA,
    OBJECT_NAME,
    INDEX_NAME,
    COUNT_FETCH,
    COUNT_INSERT,
    COUNT_UPDATE,
    COUNT_DELETE
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE OBJECT_SCHEMA = DATABASE()
ORDER BY COUNT_FETCH DESC;
```

### Ver estadísticas de rendimiento de tablas
```sql
SELECT 
    OBJECT_SCHEMA,
    OBJECT_NAME,
    COUNT_READ,
    COUNT_WRITE,
    COUNT_FETCH,
    SUM_TIMER_WAIT/1000000000 as total_latency_ms
FROM performance_schema.table_io_waits_summary_by_table
WHERE OBJECT_SCHEMA = DATABASE()
ORDER BY SUM_TIMER_WAIT DESC;
```

## 13. Consultas Optimizadas Complejas

### Query compleja optimizada con múltiples índices
```sql
EXPLAIN SELECT 
    u.nombre,
    u.apellido,
    d.pais,
    d.ciudad,
    COUNT(p.id) as total_pedidos,
    SUM(p.total) as total_gastado,
    AVG(p.total) as promedio_pedido
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id
LEFT JOIN pedidos p ON u.id = p.usuario_id
WHERE d.pais IN ('Chile', 'México')
    AND (p.fecha >= '2023-01-01' OR p.fecha IS NULL)
GROUP BY u.id, u.nombre, u.apellido, d.pais, d.ciudad
HAVING total_gastado > 200
ORDER BY total_gastado DESC;
```

### Consulta con subconsulta optimizada
```sql
EXPLAIN SELECT 
    pr.nombre,
    pr.descripcion,
    (SELECT COUNT(*) 
     FROM pedidos_has_productos php 
     WHERE php.producto_id = pr.id) as veces_vendido
FROM productos pr
WHERE pr.id IN (
    SELECT DISTINCT php.producto_id
    FROM pedidos_has_productos php
    JOIN pedidos p ON php.pedido_id = p.id
    WHERE p.fecha >= '2023-01-01'
)
ORDER BY veces_vendido DESC;
```

## 14. Índices para Optimizar JOINs

### Crear índices específicos para mejorar JOINs
```sql
CREATE INDEX idx_usuarios_direccion_id ON usuarios(direccion_id);
CREATE INDEX idx_pedidos_usuario_id ON pedidos(usuario_id);
```

### Verificar mejora en consultas con JOIN
```sql
EXPLAIN SELECT 
    u.nombre,
    u.apellido,
    d.ciudad,
    p.fecha,
    p.total
FROM usuarios u
JOIN direcciones d ON u.direccion_id = d.id
JOIN pedidos p ON u.id = p.usuario_id
WHERE d.pais = 'Chile'
ORDER BY p.fecha DESC;
```

## 15. Casos Donde los Índices No Ayudan

### Consultas que no se benefician de índices
```sql
-- 1. Funciones que modifican la columna indexada
EXPLAIN SELECT * FROM usuarios WHERE CONCAT(nombre, ' ', apellido) = 'Valeria Romero';

-- 2. Consultas con LIKE que empiezan con wildcard
EXPLAIN SELECT * FROM usuarios WHERE apellido LIKE '%mero';

-- 3. Consultas que devuelven muchos registros
EXPLAIN SELECT * FROM usuarios WHERE apellido IS NOT NULL;

-- 4. Expresiones complejas en WHERE
EXPLAIN SELECT * FROM pedidos WHERE total + 100 > 500;
```

## 16. Mantenimiento de Índices

### Operaciones de mantenimiento
```sql
-- Analizar fragmentación de índices
ANALYZE TABLE usuarios, pedidos, productos, direcciones, pedidos_has_productos;

-- Optimizar tablas y reorganizar índices
OPTIMIZE TABLE usuarios, pedidos, productos, direcciones, pedidos_has_productos;

-- Verificar integridad de índices
CHECK TABLE usuarios, pedidos, productos, direcciones, pedidos_has_productos;
```

## 17. Eliminar Índices No Utilizados

### Identificar índices poco utilizados
```sql
-- Identificar índices poco utilizados
SELECT 
    OBJECT_SCHEMA,
    OBJECT_NAME,
    INDEX_NAME,
    COUNT_FETCH,
    COUNT_INSERT + COUNT_UPDATE + COUNT_DELETE as modificaciones,
    CASE 
        WHEN COUNT_FETCH = 0 AND COUNT_INSERT + COUNT_UPDATE + COUNT_DELETE > 0 
        THEN 'Candidato a eliminar'
        WHEN COUNT_FETCH < (COUNT_INSERT + COUNT_UPDATE + COUNT_DELETE) * 0.1 
        THEN 'Poco eficiente'
        ELSE 'En uso'
    END as estado
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE OBJECT_SCHEMA = DATABASE()
    AND INDEX_NAME IS NOT NULL
    AND INDEX_NAME != 'PRIMARY'
ORDER BY COUNT_FETCH ASC;

-- Ejemplo de eliminación de índice (comentado para seguridad)
-- DROP INDEX idx_productos_nombre_length ON productos;
```

## 18. Resumen de Mejores Prácticas

### Ver resumen final de índices creados
```sql
SELECT 
    TABLE_NAME,
    INDEX_NAME,
    GROUP_CONCAT(COLUMN_NAME ORDER BY SEQ_IN_INDEX) as columnas,
    CASE NON_UNIQUE 
        WHEN 0 THEN 'ÚNICO' 
        ELSE 'NO ÚNICO' 
    END as tipo,
    INDEX_TYPE
FROM INFORMATION_SCHEMA.STATISTICS 
WHERE TABLE_SCHEMA = DATABASE()
    AND INDEX_NAME != 'PRIMARY'
GROUP BY TABLE_NAME, INDEX_NAME, NON_UNIQUE, INDEX_TYPE
ORDER BY TABLE_NAME, INDEX_NAME;
```

### Consulta de resumen de rendimiento
```sql
SELECT 
    'Consulta optimizada con índices' as tipo,
    'apellido = Romero' as ejemplo,
    'Usa idx_usuarios_apellido' as indice_usado
UNION ALL
SELECT 
    'Consulta optimizada con índices',
    'fecha BETWEEN 2023-01-01 AND 2023-12-31',
    'Usa idx_pedidos_fecha'
UNION ALL
SELECT 
    'Consulta optimizada con índices',
    'usuario_id = 3 AND fecha >= 2023-01-01',
    'Usa idx_pedidos_usuario_fecha'
UNION ALL
SELECT 
    'Consulta optimizada con índices',
    'pais = Chile AND ciudad = Temuco',
    'Usa idx_direcciones_pais_ciudad';
```

## 19. Limpieza (Opcional)

### Para limpiar los índices de prueba (CUIDADO en producción)
```sql
/*
DROP INDEX idx_usuarios_apellido ON usuarios;
DROP INDEX idx_pedidos_fecha ON pedidos;
DROP INDEX idx_productos_nombre ON productos;
DROP INDEX idx_direcciones_pais ON direcciones;
DROP INDEX idx_pedidos_usuario_fecha ON pedidos;
DROP INDEX idx_direcciones_pais_ciudad ON direcciones;
DROP INDEX idx_pedidos_productos ON pedidos_has_productos;
DROP INDEX idx_usuarios_apellido_upper ON usuarios;
DROP INDEX idx_pedidos_year ON pedidos;
DROP INDEX idx_productos_nombre_length ON productos;
DROP INDEX idx_usuarios_direccion_id ON usuarios;
DROP INDEX idx_pedidos_usuario_id ON pedidos;
*/
```
DROP INDEX idx_usuarios_apellido_upper ON usuarios;
DROP INDEX idx_pedidos_year ON pedidos;
DROP INDEX idx_productos_nombre_length ON productos;
DROP INDEX idx_usuarios_direccion_id ON usuarios;
DROP INDEX idx_pedidos_usuario_id ON pedidos;
*/