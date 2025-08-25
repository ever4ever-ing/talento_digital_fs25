

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
