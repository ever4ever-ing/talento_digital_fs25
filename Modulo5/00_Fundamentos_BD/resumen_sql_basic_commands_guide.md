# Guía de Comandos Básicos de SQL
## Base de Datos: Sistema de Pedidos

Esta guía te enseñará los comandos más fundamentales de SQL usando una base de datos real de un sistema de pedidos con usuarios, productos, direcciones y pedidos.

---

## 📊 Estructura de la Base de Datos

Nuestra base de datos tiene las siguientes tablas:
- **usuarios**: Información de clientes
- **direcciones**: Ubicaciones de los usuarios  
- **productos**: Catálogo de productos
- **pedidos**: Órdenes realizadas
- **pedidos_has_productos**: Relación productos-pedidos

---

## 1. 📖 SELECT - Consultar Datos

### Consulta Básica - Todos los registros
```sql
-- Ver todos los usuarios
SELECT * FROM usuarios;

-- Ver todos los productos
SELECT * FROM productos;

-- Ver todos los pedidos
SELECT * FROM pedidos;
```

### Consulta Específica - Columnas seleccionadas
```sql
-- Solo nombres y apellidos
SELECT nombre, apellido FROM usuarios;

-- Solo nombre y descripción de productos
SELECT nombre, descripcion FROM productos;

-- Solo fecha y total de pedidos
SELECT fecha, total FROM pedidos;
```

### Consultas con Alias (nombres más legibles)
```sql
-- Usar alias para columnas
SELECT 
    nombre AS primer_nombre,
    apellido AS apellido_usuario,
    direccion_id AS ubicacion
FROM usuarios;

-- Concatenar campos
SELECT 
    CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM usuarios;
```

---

## 2. 🔍 WHERE - Filtrar Datos

### Filtros Básicos
```sql
-- Usuario específico por ID
SELECT * FROM usuarios WHERE id = 1;

-- Productos específicos
SELECT * FROM productos WHERE nombre = 'lapiz';

-- Pedidos por usuario
SELECT * FROM pedidos WHERE usuario_id = 3;
```

### Operadores de Comparación
```sql
-- Pedidos mayores a 300
SELECT * FROM pedidos WHERE total > 300;

-- Pedidos entre rangos
SELECT * FROM pedidos WHERE total BETWEEN 200 AND 400;

-- Usuarios con nombres específicos
SELECT * FROM usuarios WHERE nombre IN ('Valeria', 'Kevin');
```

### Búsquedas con Patrones (LIKE)
```sql
-- Apellidos que empiecen con 'R'
SELECT * FROM usuarios WHERE apellido LIKE 'R%';

-- Productos que contengan 'clip'
SELECT * FROM productos WHERE nombre LIKE '%clip%';

-- Direcciones que terminen con 'Chile'
SELECT * FROM direcciones WHERE pais LIKE '%Chile';
```

### Filtros con Fechas
```sql
-- Pedidos del 2023
SELECT * FROM pedidos WHERE YEAR(fecha) = 2023;

-- Pedidos después de cierta fecha
SELECT * FROM pedidos WHERE fecha > '2023-01-01';

-- Pedidos de diciembre
SELECT * FROM pedidos WHERE MONTH(fecha) = 12;
```

---

## 3. 📊 Ordenar Datos - ORDER BY

### Orden Ascendente (menor a mayor)
```sql
-- Usuarios ordenados por apellido
SELECT * FROM usuarios ORDER BY apellido;

-- Pedidos ordenados por fecha
SELECT * FROM pedidos ORDER BY fecha;

-- Productos ordenados por nombre
SELECT * FROM productos ORDER BY nombre;
```

### Orden Descendente (mayor a menor)
```sql
-- Pedidos del más caro al más barato
SELECT * FROM pedidos ORDER BY total DESC;

-- Pedidos más recientes primero
SELECT * FROM pedidos ORDER BY fecha DESC;

-- Usuarios por apellido Z-A
SELECT * FROM usuarios ORDER BY apellido DESC;
```

### Orden por Múltiples Campos
```sql
-- Ordenar por apellido y luego por nombre
SELECT * FROM usuarios ORDER BY apellido, nombre;

-- Pedidos por usuario y luego por fecha
SELECT * FROM pedidos ORDER BY usuario_id, fecha DESC;
```

---

## 4. 🔢 Limitar Resultados - LIMIT

### Primeros Registros
```sql
-- Los primeros 3 usuarios
SELECT * FROM usuarios LIMIT 3;

-- Los 2 pedidos más caros
SELECT * FROM pedidos ORDER BY total DESC LIMIT 2;

-- Los primeros 5 productos
SELECT * FROM productos LIMIT 5;
```

### Paginación (OFFSET)
```sql
-- Saltar los primeros 2 usuarios y mostrar los siguientes 2
SELECT * FROM usuarios LIMIT 2 OFFSET 2;

-- Segunda "página" de productos (productos 3-4)
SELECT * FROM productos LIMIT 2 OFFSET 2;
```

---

## 5. 🔗 JOIN - Combinar Tablas

### INNER JOIN - Solo registros que coinciden
```sql
-- Usuarios con sus direcciones
SELECT 
    u.nombre,
    u.apellido,
    d.calle,
    d.ciudad,
    d.pais
FROM usuarios u
INNER JOIN direcciones d ON u.direccion_id = d.id;

-- Pedidos con información del usuario
SELECT 
    p.id AS pedido_id,
    p.fecha,
    p.total,
    u.nombre,
    u.apellido
FROM pedidos p
INNER JOIN usuarios u ON p.usuario_id = u.id;
```

### LEFT JOIN - Todos los registros de la tabla izquierda
```sql
-- Todos los usuarios, con o sin pedidos
SELECT 
    u.nombre,
    u.apellido,
    p.fecha,
    p.total
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id;

-- Todos los productos, vendidos o no
SELECT 
    pr.nombre,
    pr.descripcion,
    php.pedido_id
FROM productos pr
LEFT JOIN pedidos_has_productos php ON pr.id = php.producto_id;
```

### JOIN con Múltiples Tablas
```sql
-- Información completa de pedidos
SELECT 
    p.id AS pedido_id,
    p.fecha,
    p.total,
    u.nombre,
    u.apellido,
    d.ciudad,
    d.pais
FROM pedidos p
INNER JOIN usuarios u ON p.usuario_id = u.id
INNER JOIN direcciones d ON u.direccion_id = d.id;
```

---

## 6. 📈 Funciones de Agregación

### COUNT - Contar Registros
```sql
-- Total de usuarios
SELECT COUNT(*) AS total_usuarios FROM usuarios;

-- Total de pedidos por usuario
SELECT 
    usuario_id,
    COUNT(*) AS total_pedidos
FROM pedidos
GROUP BY usuario_id;

-- Pedidos por país
SELECT 
    d.pais,
    COUNT(p.id) AS pedidos_pais
FROM direcciones d
INNER JOIN usuarios u ON d.id = u.direccion_id
INNER JOIN pedidos p ON u.id = p.usuario_id
GROUP BY d.pais;
```

### SUM - Sumar Valores
```sql
-- Total de ventas
SELECT SUM(total) AS ventas_totales FROM pedidos;

-- Ventas por usuario
SELECT 
    usuario_id,
    SUM(total) AS total_gastado
FROM pedidos
GROUP BY usuario_id;
```

### AVG - Promedio
```sql
-- Promedio de pedidos
SELECT AVG(total) AS promedio_pedido FROM pedidos;

-- Promedio por usuario
SELECT 
    usuario_id,
    AVG(total) AS promedio_usuario
FROM pedidos
GROUP BY usuario_id;
```

### MAX y MIN - Valores Máximos y Mínimos
```sql
-- Pedido más caro y más barato
SELECT 
    MAX(total) AS pedido_mayor,
    MIN(total) AS pedido_menor
FROM pedidos;

-- Por usuario
SELECT 
    usuario_id,
    MAX(total) AS pedido_mayor,
    MIN(total) AS pedido_menor
FROM pedidos
GROUP BY usuario_id;
```

---

## 7. 👥 GROUP BY - Agrupar Datos

### Agrupación Básica
```sql
-- Pedidos por usuario
SELECT 
    usuario_id,
    COUNT(*) AS cantidad_pedidos,
    SUM(total) AS total_gastado
FROM pedidos
GROUP BY usuario_id;

-- Usuarios por país
SELECT 
    d.pais,
    COUNT(u.id) AS usuarios_pais
FROM direcciones d
INNER JOIN usuarios u ON d.id = u.direccion_id
GROUP BY d.pais;
```

### HAVING - Filtrar Grupos
```sql
-- Usuarios que han gastado más de 300
SELECT 
    usuario_id,
    SUM(total) AS total_gastado
FROM pedidos
GROUP BY usuario_id
HAVING SUM(total) > 300;

-- Países con más de 1 usuario
SELECT 
    d.pais,
    COUNT(u.id) AS usuarios_pais
FROM direcciones d
INNER JOIN usuarios u ON d.id = u.direccion_id
GROUP BY d.pais
HAVING COUNT(u.id) > 1;
```

---

## 8. ➕ INSERT - Agregar Datos

### Insertar un Registro
```sql
-- Nuevo producto
INSERT INTO productos (id, nombre, descripcion) 
VALUES (228, 'calculadora', 'para hacer cálculos matemáticos');

-- Nueva dirección
INSERT INTO direcciones (id, calle, colonia, ciudad, pais) 
VALUES (8, 'Av. Principal 123', 'Centro', 'Santiago', 'Chile');
```

### Insertar Múltiples Registros
```sql
-- Varios productos a la vez
INSERT INTO productos (id, nombre, descripcion) VALUES
(229, 'regla', 'para medir distancias'),
(230, 'goma', 'para borrar errores'),
(231, 'sacapuntas', 'para afilar lápices');
```

### Insertar con Datos de Otra Tabla
```sql
-- Crear tabla de respaldo de productos
CREATE TABLE productos_backup AS SELECT * FROM productos WHERE 1=0;

-- Copiar productos específicos
INSERT INTO productos_backup 
SELECT * FROM productos WHERE nombre LIKE '%clip%';
```

---

## 9. ✏️ UPDATE - Modificar Datos

### Actualización Básica
```sql
-- Actualizar descripción de un producto
UPDATE productos 
SET descripcion = 'lápiz de grafito para escribir y dibujar'
WHERE id = 222;

-- Actualizar total de un pedido
UPDATE pedidos 
SET total = 525.00 
WHERE id = 551;
```

### Actualización con Cálculos
```sql
-- Aplicar descuento del 10% a todos los pedidos
UPDATE pedidos 
SET total = total * 0.9 
WHERE fecha < '2023-01-01';

-- Actualizar basado en otra tabla
UPDATE usuarios u
INNER JOIN direcciones d ON u.direccion_id = d.id
SET u.nombre = CONCAT(u.nombre, ' (', d.pais, ')')
WHERE d.pais = 'Chile';
```

---

## 10. 🗑️ DELETE - Eliminar Datos

### Eliminar Registros Específicos
```sql
-- Eliminar un producto específico
DELETE FROM productos WHERE id = 228;

-- Eliminar pedidos antiguos
DELETE FROM pedidos WHERE fecha < '2022-01-01';
```

### Eliminar con JOIN
```sql
-- Eliminar productos que nunca se han vendido
DELETE p FROM productos p
LEFT JOIN pedidos_has_productos php ON p.id = php.producto_id
WHERE php.producto_id IS NULL;
```

---

## 11. 🏗️ CREATE TABLE - Crear Tablas

### Crear Tabla Básica
```sql
-- Tabla de categorías de productos
CREATE TABLE categorias (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);
```

### Crear Tabla con Claves Foráneas
```sql
-- Tabla de comentarios de productos
CREATE TABLE comentarios_productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    usuario_id INT,
    comentario TEXT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
```

---

## 12. 🔧 ALTER TABLE - Modificar Tablas

### Agregar Columnas
```sql
-- Agregar columna de teléfono a usuarios
ALTER TABLE usuarios ADD COLUMN telefono VARCHAR(15);

-- Agregar columna de stock a productos
ALTER TABLE productos ADD COLUMN stock INT DEFAULT 0;
```

### Modificar Columnas
```sql
-- Cambiar tamaño de columna
ALTER TABLE usuarios MODIFY COLUMN telefono VARCHAR(20);

-- Renombrar columna
ALTER TABLE usuarios RENAME COLUMN telefono TO celular;
```

---

## 13. 🗂️ Subconsultas

### Subconsultas en WHERE
```sql
-- Usuarios que han hecho pedidos
SELECT * FROM usuarios 
WHERE id IN (SELECT DISTINCT usuario_id FROM pedidos);

-- Productos más caros que el promedio
SELECT * FROM pedidos 
WHERE total > (SELECT AVG(total) FROM pedidos);
```

### Subconsultas en SELECT
```sql
-- Usuarios con su cantidad de pedidos
SELECT 
    nombre,
    apellido,
    (SELECT COUNT(*) FROM pedidos p WHERE p.usuario_id = u.id) AS total_pedidos
FROM usuarios u;
```

---

## 14. 💡 Casos Prácticos Comunes

### Reporte de Ventas
```sql
-- Reporte mensual de ventas
SELECT 
    YEAR(fecha) AS año,
    MONTH(fecha) AS mes,
    COUNT(*) AS total_pedidos,
    SUM(total) AS ventas_mes,
    AVG(total) AS promedio_pedido
FROM pedidos
GROUP BY YEAR(fecha), MONTH(fecha)
ORDER BY año, mes;
```

### Top Clientes
```sql
-- Los 3 mejores clientes
SELECT 
    u.nombre,
    u.apellido,
    COUNT(p.id) AS total_pedidos,
    SUM(p.total) AS total_gastado
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido
ORDER BY total_gastado DESC
LIMIT 3;
```

### Productos Populares
```sql
-- Productos más vendidos
SELECT 
    pr.nombre,
    pr.descripcion,
    COUNT(php.producto_id) AS veces_vendido
FROM productos pr
INNER JOIN pedidos_has_productos php ON pr.id = php.producto_id
GROUP BY pr.id, pr.nombre, pr.descripcion
ORDER BY veces_vendido DESC;
```

### Análisis Geográfico
```sql
-- Ventas por país
SELECT 
    d.pais,
    COUNT(DISTINCT u.id) AS total_clientes,
    COUNT(p.id) AS total_pedidos,
    SUM(p.total) AS ventas_pais
FROM direcciones d
INNER JOIN usuarios u ON d.id = u.direccion_id
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY d.pais
ORDER BY ventas_pais DESC;
```

---

## 📋 Resumen de Comandos Esenciales

| Comando | Propósito | Ejemplo |
|---------|-----------|---------|
| `SELECT` | Consultar datos | `SELECT * FROM usuarios` |
| `WHERE` | Filtrar datos | `WHERE id = 1` |
| `ORDER BY` | Ordenar resultados | `ORDER BY apellido` |
| `LIMIT` | Limitar resultados | `LIMIT 5` |
| `JOIN` | Combinar tablas | `INNER JOIN direcciones ON...` |
| `GROUP BY` | Agrupar datos | `GROUP BY usuario_id` |
| `HAVING` | Filtrar grupos | `HAVING SUM(total) > 300` |
| `INSERT` | Agregar datos | `INSERT INTO tabla VALUES...` |
| `UPDATE` | Modificar datos | `UPDATE tabla SET campo = valor` |
| `DELETE` | Eliminar datos | `DELETE FROM tabla WHERE...` |

---

## 🎯 Consejos


1. **Siempre usa WHERE en UPDATE y DELETE** para evitar modificar todos los registros
2. **Practica con SELECT** antes de hacer cambios con UPDATE/DELETE
3. **Usa alias** para hacer consultas más legibles
4. **Combina múltiples condiciones** con AND/OR
5. **Ordena resultados** para encontrar patrones más fácilmente
6. **Usa LIMIT** cuando explores datos grandes
7. **Practica JOINs** gradualmente: primero INNER, luego LEFT
8. **Guarda consultas útiles** para reutilizarlas

---

## 🚀 Próximos Pasos

Una vez domines estos comandos básicos, puedes avanzar a:
- Funciones avanzadas (CASE, IF, DATE_FORMAT)
- Vistas (VIEW)
- Procedimientos almacenados
- Triggers
- Índices para optimización
- Transacciones

¡Practica estos ejemplos y estarás listo para trabajar con cualquier base de datos SQL!