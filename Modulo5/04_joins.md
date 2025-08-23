# JOINs y Subconsultas en MySQL - Módulo 5

## Preparación: Creación de Tablas Relacionadas

Primero creemos las tablas necesarias para practicar JOINs y subconsultas:

```sql
-- Tabla clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100),
    ciudad VARCHAR(50),
    telefono VARCHAR(15)
);

-- Tabla pedidos
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    fecha_pedido DATE,
    total DECIMAL(10,2),
    estado VARCHAR(20),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Tabla productos
CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    precio DECIMAL(8,2),
    categoria VARCHAR(30),
    stock INT
);

-- Tabla detalle_pedidos (relación muchos a muchos)
CREATE TABLE detalle_pedidos (
    id INT PRIMARY KEY,
    pedido_id INT,
    producto_id INT,
    cantidad INT,
    precio_unitario DECIMAL(8,2),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Tabla empleados (para ejemplos de subconsultas)
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    salario DECIMAL(10,2),
    departamento VARCHAR(30),
    jefe_id INT,
    FOREIGN KEY (jefe_id) REFERENCES empleados(id)
);
```

## Inserción de Datos de Prueba

```sql
-- Insertar clientes
INSERT INTO clientes VALUES
(1, 'Juan Pérez', 'juan@email.com', 'Madrid', '123-456-789'),
(2, 'María González', 'maria@email.com', 'Barcelona', '987-654-321'),
(3, 'Pedro Rodríguez', 'pedro@email.com', 'Valencia', '456-789-123'),
(4, 'Ana López', 'ana@email.com', 'Sevilla', '789-123-456'),
(5, 'Carlos Martín', 'carlos@email.com', 'Bilbao', '321-654-987');

-- Insertar productos
INSERT INTO productos VALUES
(1, 'Laptop Dell', 899.99, 'Tecnología', 25),
(2, 'Mouse Logitech', 29.99, 'Tecnología', 100),
(3, 'Teclado Mecánico', 79.99, 'Tecnología', 50),
(4, 'Monitor 24"', 199.99, 'Tecnología', 30),
(5, 'Silla Oficina', 149.99, 'Muebles', 15),
(6, 'Escritorio', 299.99, 'Muebles', 10);

-- Insertar pedidos (algunos clientes sin pedidos, algunos pedidos sin cliente válido)
INSERT INTO pedidos VALUES
(1, 1, '2024-01-15', 929.98, 'Completado'),
(2, 2, '2024-01-20', 109.98, 'Pendiente'),
(3, 1, '2024-02-10', 199.99, 'Enviado'),
(4, 3, '2024-02-15', 449.98, 'Completado'),
(5, NULL, '2024-03-01', 79.99, 'Cancelado'),  -- Pedido sin cliente
(6, 999, '2024-03-05', 299.99, 'Pendiente');  -- Cliente inexistente

-- Insertar detalle de pedidos
INSERT INTO detalle_pedidos VALUES
(1, 1, 1, 1, 899.99),  -- Juan: 1 Laptop
(2, 1, 2, 1, 29.99),   -- Juan: 1 Mouse
(3, 2, 3, 1, 79.99),   -- María: 1 Teclado
(4, 2, 2, 1, 29.99),   -- María: 1 Mouse
(5, 3, 4, 1, 199.99),  -- Juan: 1 Monitor
(6, 4, 5, 2, 149.99),  -- Pedro: 2 Sillas
(7, 4, 1, 1, 149.99);  -- Pedro: 1 Laptop (precio especial)

-- Insertar empleados (con jerarquía)
INSERT INTO empleados VALUES
(1, 'Ana', 'García', 5000.00, 'Administración', NULL),      -- Jefe general
(2, 'Luis', 'Martín', 4500.00, 'Ventas', 1),               -- Jefe de ventas
(3, 'Carmen', 'López', 4200.00, 'Marketing', 1),           -- Jefe de marketing
(4, 'David', 'Ruiz', 3200.00, 'Ventas', 2),                -- Vendedor
(5, 'Elena', 'Torres', 3400.00, 'Ventas', 2),              -- Vendedora
(6, 'Miguel', 'Sánchez', 3800.00, 'Marketing', 3),         -- Marketing
(7, 'Laura', 'Jiménez', 2800.00, 'Ventas', 2),             -- Vendedora junior
(8, 'Roberto', 'Morales', 3600.00, 'Desarrollo', 1),       -- Desarrollador
(9, 'Sofia', 'Herrera', 4000.00, 'Desarrollo', 1);         -- Desarrolladora senior
```

## 1. INNER JOIN (JOIN)

El INNER JOIN devuelve solo los registros que tienen coincidencias en ambas tablas.

### Ejemplo básico: Clientes con sus pedidos

```sql
-- Mostrar clientes que SÍ tienen pedidos
SELECT 
    clientes.id AS cliente_id,
    clientes.nombre AS cliente_nombre,
    pedidos.id AS pedido_id,
    pedidos.fecha_pedido,
    pedidos.total,
    pedidos.estado
FROM clientes 
JOIN pedidos ON clientes.id = pedidos.cliente_id
ORDER BY clientes.nombre, pedidos.fecha_pedido;
```

**Resultado esperado:** Solo Juan (2 pedidos), María (1 pedido) y Pedro (1 pedido). Ana y Carlos NO aparecen porque no tienen pedidos.

### Ejemplo con múltiples JOINs

```sql
-- Detalle completo: Cliente -> Pedido -> Productos
SELECT 
    c.nombre AS cliente,
    p.id AS pedido_id,
    p.fecha_pedido,
    pr.nombre AS producto,
    dp.cantidad,
    dp.precio_unitario,
    (dp.cantidad * dp.precio_unitario) AS subtotal
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
JOIN detalle_pedidos dp ON p.id = dp.pedido_id
JOIN productos pr ON dp.producto_id = pr.id
ORDER BY c.nombre, p.fecha_pedido, pr.nombre;
```

## 2. LEFT JOIN (LEFT OUTER JOIN)

El LEFT JOIN devuelve TODOS los registros de la tabla izquierda y las coincidencias de la derecha.

### Ejemplo básico: Todos los clientes (con o sin pedidos)

```sql
-- Mostrar TODOS los clientes, incluso los que no tienen pedidos
SELECT 
    clientes.id AS cliente_id,
    clientes.nombre AS cliente_nombre,
    clientes.ciudad,
    pedidos.id AS pedido_id,
    pedidos.fecha_pedido,
    pedidos.total,
    CASE 
        WHEN pedidos.id IS NULL THEN 'Sin pedidos'
        ELSE pedidos.estado
    END AS estado_pedido
FROM clientes 
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
ORDER BY clientes.nombre, pedidos.fecha_pedido;
```

**Resultado esperado:** Aparecen TODOS los clientes (Juan, María, Pedro, Ana, Carlos). Ana y Carlos tendrán NULL en los campos de pedidos.

### Ejemplo: Clientes sin pedidos

```sql
-- Encontrar clientes que NO han hecho pedidos
SELECT 
    clientes.id,
    clientes.nombre,
    clientes.email,
    clientes.ciudad
FROM clientes 
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
WHERE pedidos.id IS NULL;
```

### Ejemplo: Resumen de ventas por cliente

```sql
-- Resumen de todos los clientes con total de pedidos
SELECT 
    c.nombre AS cliente,
    c.ciudad,
    COUNT(p.id) AS total_pedidos,
    COALESCE(SUM(p.total), 0) AS total_gastado,
    CASE 
        WHEN COUNT(p.id) = 0 THEN 'Sin actividad'
        WHEN COUNT(p.id) = 1 THEN 'Cliente nuevo'
        ELSE 'Cliente frecuente'
    END AS tipo_cliente
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nombre, c.ciudad
ORDER BY total_gastado DESC;
```

## 3. RIGHT JOIN (RIGHT OUTER JOIN)

El RIGHT JOIN devuelve TODOS los registros de la tabla derecha y las coincidencias de la izquierda.

### Ejemplo básico: Todos los pedidos (con o sin cliente válido)

```sql
-- Mostrar TODOS los pedidos, incluso los que no tienen cliente válido
SELECT 
    pedidos.id AS pedido_id,
    pedidos.fecha_pedido,
    pedidos.total,
    pedidos.estado,
    clientes.id AS cliente_id,
    COALESCE(clientes.nombre, 'Cliente no encontrado') AS cliente_nombre,
    COALESCE(clientes.email, 'Email no disponible') AS cliente_email
FROM clientes 
RIGHT JOIN pedidos ON clientes.id = pedidos.cliente_id
ORDER BY pedidos.fecha_pedido;
```

**Resultado esperado:** Aparecen TODOS los pedidos, incluyendo el pedido 5 (cliente NULL) y pedido 6 (cliente 999 inexistente).

### Ejemplo: Pedidos huérfanos

```sql
-- Encontrar pedidos sin cliente válido (datos inconsistentes)
SELECT 
    pedidos.id AS pedido_huerfano,
    pedidos.cliente_id AS cliente_inexistente,
    pedidos.fecha_pedido,
    pedidos.total,
    pedidos.estado
FROM clientes 
RIGHT JOIN pedidos ON clientes.id = pedidos.cliente_id
WHERE clientes.id IS NULL;
```

## 4. FULL OUTER JOIN (Simulado en MySQL)

MySQL no soporta FULL OUTER JOIN directamente, pero se puede simular con UNION:

```sql
-- Simular FULL OUTER JOIN: Todos los clientes Y todos los pedidos
SELECT 
    c.id AS cliente_id,
    c.nombre AS cliente_nombre,
    p.id AS pedido_id,
    p.fecha_pedido,
    p.total,
    'Cliente con/sin pedidos' AS tipo
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id

UNION

SELECT 
    c.id AS cliente_id,
    c.nombre AS cliente_nombre,
    p.id AS pedido_id,
    p.fecha_pedido,
    p.total,
    'Pedido con/sin cliente' AS tipo
FROM clientes c
RIGHT JOIN pedidos p ON c.id = p.cliente_id
WHERE c.id IS NULL

ORDER BY cliente_id, pedido_id;
```

## 5. SELF JOIN

Unir una tabla consigo misma, útil para relaciones jerárquicas:

```sql
-- Empleados con sus jefes
SELECT 
    e.nombre AS empleado,
    e.apellido AS apellido_empleado,
    e.departamento,
    e.salario,
    CONCAT(j.nombre, ' ', j.apellido) AS jefe,
    j.salario AS salario_jefe
FROM empleados e
LEFT JOIN empleados j ON e.jefe_id = j.id
ORDER BY e.departamento, e.salario DESC;
```

### Ejemplo: Empleados que ganan más que su jefe

```sql
-- Encontrar empleados que ganan más que su jefe
SELECT 
    CONCAT(e.nombre, ' ', e.apellido) AS empleado,
    e.salario AS salario_empleado,
    CONCAT(j.nombre, ' ', j.apellido) AS jefe,
    j.salario AS salario_jefe,
    (e.salario - j.salario) AS diferencia
FROM empleados e
JOIN empleados j ON e.jefe_id = j.id
WHERE e.salario > j.salario
ORDER BY diferencia DESC;
```

## 6. SUBCONSULTAS (SUBQUERIES)

### Subconsulta simple: Empleados con salario superior al promedio

```sql
-- Empleados que ganan más que el promedio
SELECT 
    nombre,
    apellido,
    departamento,
    salario,
    (SELECT AVG(salario) FROM empleados) AS salario_promedio,
    ROUND(salario - (SELECT AVG(salario) FROM empleados), 2) AS diferencia_promedio
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados)
ORDER BY salario DESC;
```

### Subconsulta con IN: Clientes con pedidos en estado específico

```sql
-- Clientes que tienen al menos un pedido completado
SELECT 
    id,
    nombre,
    email,
    ciudad
FROM clientes
WHERE id IN (
    SELECT DISTINCT cliente_id 
    FROM pedidos 
    WHERE estado = 'Completado' AND cliente_id IS NOT NULL
);
```

### Subconsulta con EXISTS: Clientes con pedidos

```sql
-- Clientes que tienen al menos un pedido (usando EXISTS)
SELECT 
    c.id,
    c.nombre,
    c.ciudad
FROM clientes c
WHERE EXISTS (
    SELECT 1 
    FROM pedidos p 
    WHERE p.cliente_id = c.id
);
```

### Subconsulta correlacionada: Último pedido de cada cliente

```sql
-- Último pedido de cada cliente
SELECT 
    c.nombre AS cliente,
    p.id AS ultimo_pedido,
    p.fecha_pedido AS fecha_ultimo_pedido,
    p.total,
    p.estado
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
WHERE p.fecha_pedido = (
    SELECT MAX(p2.fecha_pedido)
    FROM pedidos p2
    WHERE p2.cliente_id = c.id
)
ORDER BY p.fecha_pedido DESC;
```

### Subconsulta con agregación: Departamentos con salario promedio alto

```sql
-- Departamentos con salario promedio superior al promedio general
SELECT 
    departamento,
    COUNT(*) AS num_empleados,
    ROUND(AVG(salario), 2) AS salario_promedio_dept,
    (SELECT ROUND(AVG(salario), 2) FROM empleados) AS salario_promedio_general
FROM empleados
GROUP BY departamento
HAVING AVG(salario) > (SELECT AVG(salario) FROM empleados)
ORDER BY salario_promedio_dept DESC;
```

## 7. Ejemplos Complejos Combinados

### Reporte completo de ventas

```sql
-- Reporte completo: Cliente, pedidos, productos y totales
SELECT 
    c.nombre AS cliente,
    c.ciudad,
    COUNT(DISTINCT p.id) AS total_pedidos,
    COUNT(dp.id) AS total_items,
    SUM(dp.cantidad * dp.precio_unitario) AS total_gastado,
    AVG(p.total) AS promedio_por_pedido,
    MAX(p.fecha_pedido) AS ultimo_pedido,
    GROUP_CONCAT(DISTINCT pr.categoria ORDER BY pr.categoria) AS categorias_compradas
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
LEFT JOIN detalle_pedidos dp ON p.id = dp.pedido_id
LEFT JOIN productos pr ON dp.producto_id = pr.id
GROUP BY c.id, c.nombre, c.ciudad
HAVING total_pedidos > 0  -- Solo clientes con pedidos
ORDER BY total_gastado DESC;
```

### Análisis de productos más vendidos

```sql
-- Productos más vendidos con información de clientes
SELECT 
    pr.nombre AS producto,
    pr.categoria,
    pr.precio AS precio_lista,
    COUNT(dp.id) AS veces_vendido,
    SUM(dp.cantidad) AS cantidad_total_vendida,
    AVG(dp.precio_unitario) AS precio_promedio_venta,
    SUM(dp.cantidad * dp.precio_unitario) AS ingresos_totales,
    COUNT(DISTINCT dp.pedido_id) AS pedidos_diferentes,
    GROUP_CONCAT(DISTINCT c.nombre ORDER BY c.nombre) AS clientes_compradores
FROM productos pr
JOIN detalle_pedidos dp ON pr.id = dp.producto_id
JOIN pedidos p ON dp.pedido_id = p.id
JOIN clientes c ON p.cliente_id = c.id
WHERE p.estado != 'Cancelado'
GROUP BY pr.id, pr.nombre, pr.categoria, pr.precio
ORDER BY cantidad_total_vendida DESC, ingresos_totales DESC;
```

### Empleados por encima del promedio de su departamento

```sql
-- Empleados que ganan más que el promedio de su departamento
SELECT 
    e.nombre,
    e.apellido,
    e.departamento,
    e.salario,
    dept_avg.salario_promedio_dept,
    ROUND(e.salario - dept_avg.salario_promedio_dept, 2) AS diferencia_promedio_dept
FROM empleados e
JOIN (
    SELECT 
        departamento,
        AVG(salario) AS salario_promedio_dept
    FROM empleados
    GROUP BY departamento
) dept_avg ON e.departamento = dept_avg.departamento
WHERE e.salario > dept_avg.salario_promedio_dept
ORDER BY e.departamento, diferencia_promedio_dept DESC;
```

## Ejercicios Prácticos

### 1. Ejercicio Básico
```sql
-- Encuentra todos los clientes de Madrid que han hecho pedidos
-- Muestra: nombre del cliente, email, total del pedido, fecha
```

### 2. Ejercicio Intermedio
```sql
-- Encuentra productos que nunca se han vendido
-- Usar LEFT JOIN y WHERE IS NULL
```

### 3. Ejercicio Avanzado
```sql
-- Crea un ranking de clientes por total gastado
-- Incluye clientes sin pedidos (total = 0)
-- Muestra posición en el ranking
```

### 4. Ejercicio con Subconsultas
```sql
-- Encuentra empleados que ganan más que TODOS los empleados de Ventas
-- Usar subconsulta con ALL o MAX
```

¡Estos ejemplos cubren todos los tipos de JOINs y subconsultas principales en MySQL!
