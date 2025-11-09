# Ejemplos de Normalización de Base de Datos MySQL

## Tabla Inicial (Sin Normalizar)

### Estructura de la tabla:
```sql
CREATE TABLE pedidos_sin_normalizar (
    pedido_id INT,
    fecha_pedido DATE,
    cliente_nombre VARCHAR(100),
    cliente_email VARCHAR(100),
    cliente_telefono VARCHAR(20),
    cliente_direccion VARCHAR(200),
    producto1_nombre VARCHAR(100),
    producto1_precio DECIMAL(10,2),
    producto1_categoria VARCHAR(50),
    producto2_nombre VARCHAR(100),
    producto2_precio DECIMAL(10,2),
    producto2_categoria VARCHAR(50),
    vendedor_nombre VARCHAR(100),
    vendedor_email VARCHAR(100),
    total_pedido DECIMAL(10,2)
);
```

### Datos de ejemplo:

| pedido_id | fecha_pedido | cliente_nombre | cliente_email | cliente_telefono | cliente_direccion | producto1_nombre | producto1_precio | producto1_categoria | producto2_nombre | producto2_precio | producto2_categoria | vendedor_nombre | vendedor_email | total_pedido |
|-----------|--------------|----------------|---------------|------------------|-------------------|------------------|------------------|-------------------|------------------|------------------|-------------------|----------------|----------------|--------------|
| 1 | 2024-01-15 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Laptop Dell | 899.99 | Electrónicos | Mouse Logitech | 25.99 | Accesorios | María García | maria.garcia@empresa.com | 925.98 |
| 2 | 2024-01-16 | Ana López | ana@email.com | 555-0102 | Av. Principal 456, Santiago | iPhone 14 | 1199.99 | Electrónicos | NULL | NULL | NULL | Carlos Ruiz | carlos.ruiz@empresa.com | 1199.99 |
| 3 | 2024-01-17 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Tablet Samsung | 299.99 | Electrónicos | NULL | NULL | NULL | María García | maria.garcia@empresa.com | 299.99 |

### Problemas identificados:
- ❌ **Redundancia**: Información de clientes y vendedores se repite
- ❌ **Valores NULL**: Cuando no hay segundo producto
- ❌ **Grupos repetitivos**: producto1, producto2, etc.
- ❌ **Anomalías**: Difícil actualizar, insertar o eliminar datos

---

## Primera Forma Normal (1NF)

**Regla:** Eliminar grupos repetitivos y asegurar valores atómicos.

### Estructura:
```sql
CREATE TABLE pedidos_1nf (
    pedido_id INT,
    fecha_pedido DATE,
    cliente_nombre VARCHAR(100),
    cliente_email VARCHAR(100),
    cliente_telefono VARCHAR(20),
    cliente_direccion VARCHAR(200),
    producto_nombre VARCHAR(100),
    producto_precio DECIMAL(10,2),
    producto_categoria VARCHAR(50),
    vendedor_nombre VARCHAR(100),
    vendedor_email VARCHAR(100)
);
```

### Datos en 1NF:

| pedido_id | fecha_pedido | cliente_nombre | cliente_email | cliente_telefono | cliente_direccion | producto_nombre | producto_precio | producto_categoria | vendedor_nombre | vendedor_email |
|-----------|--------------|----------------|---------------|------------------|-------------------|-----------------|------------------|-------------------|----------------|----------------|
| 1 | 2024-01-15 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Laptop Dell | 899.99 | Electrónicos | María García | maria.garcia@empresa.com |
| 1 | 2024-01-15 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Mouse Logitech | 25.99 | Accesorios | María García | maria.garcia@empresa.com |
| 2 | 2024-01-16 | Ana López | ana@email.com | 555-0102 | Av. Principal 456, Santiago | iPhone 14 | 1199.99 | Electrónicos | Carlos Ruiz | carlos.ruiz@empresa.com |
| 3 | 2024-01-17 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Tablet Samsung | 299.99 | Electrónicos | María García | maria.garcia@empresa.com |

### ✅ Mejoras logradas:
- Eliminados los grupos repetitivos (producto1, producto2)
- Cada celda contiene un valor atómico
- No hay valores NULL innecesarios

### ❌ Problemas que persisten:
- Aún hay mucha redundancia
- Dependencias funcionales parciales

---

## Segunda Forma Normal (2NF)

**Regla:** Estar en 1NF + eliminar dependencias funcionales parciales.

**Clave compuesta identificada:** (pedido_id, producto_nombre)

### Dependencias parciales encontradas:
- `fecha_pedido`, `cliente_*`, `vendedor_*` → dependen solo de `pedido_id`
- `producto_precio`, `producto_categoria` → dependen solo de `producto_nombre`

### Estructuras en 2NF:

#### Tabla: pedidos
```sql
CREATE TABLE pedidos (
    pedido_id INT PRIMARY KEY,
    fecha_pedido DATE,
    cliente_nombre VARCHAR(100),
    cliente_email VARCHAR(100),
    cliente_telefono VARCHAR(20),
    cliente_direccion VARCHAR(200),
    vendedor_nombre VARCHAR(100),
    vendedor_email VARCHAR(100)
);
```

| pedido_id | fecha_pedido | cliente_nombre | cliente_email | cliente_telefono | cliente_direccion | vendedor_nombre | vendedor_email |
|-----------|--------------|----------------|---------------|------------------|-------------------|----------------|----------------|
| 1 | 2024-01-15 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | María García | maria.garcia@empresa.com |
| 2 | 2024-01-16 | Ana López | ana@email.com | 555-0102 | Av. Principal 456, Santiago | Carlos Ruiz | carlos.ruiz@empresa.com |
| 3 | 2024-01-17 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | María García | maria.garcia@empresa.com |

#### Tabla: productos
```sql
CREATE TABLE productos (
    producto_nombre VARCHAR(100) PRIMARY KEY,
    producto_precio DECIMAL(10,2),
    producto_categoria VARCHAR(50)
);
```

| producto_nombre | producto_precio | producto_categoria |
|-----------------|------------------|-------------------|
| Laptop Dell | 899.99 | Electrónicos |
| Mouse Logitech | 25.99 | Accesorios |
| iPhone 14 | 1199.99 | Electrónicos |
| Tablet Samsung | 299.99 | Electrónicos |

#### Tabla: pedido_detalle
```sql
CREATE TABLE pedido_detalle (
    pedido_id INT,
    producto_nombre VARCHAR(100),
    PRIMARY KEY (pedido_id, producto_nombre),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (producto_nombre) REFERENCES productos(producto_nombre)
);
```

| pedido_id | producto_nombre |
|-----------|-----------------|
| 1 | Laptop Dell |
| 1 | Mouse Logitech |
| 2 | iPhone 14 |
| 3 | Tablet Samsung |

### ✅ Mejoras logradas:
- Eliminadas las dependencias parciales
- Información de productos centralizada
- Menor redundancia

### ❌ Problemas que persisten:
- Dependencias transitivas aún presentes

---

## Tercera Forma Normal (3NF)

**Regla:** Estar en 2NF + eliminar dependencias transitivas.

### Dependencias transitivas identificadas:
- `cliente_email`, `cliente_telefono`, `cliente_direccion` → dependen de `cliente_nombre`
- `vendedor_email` → depende de `vendedor_nombre`
- `producto_categoria` → podríamos crear tabla separada de categorías

### Estructuras finales en 3NF:

#### Tabla: clientes
```sql
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(200)
);
```

| cliente_id | nombre | email | telefono | direccion |
|------------|--------|-------|----------|-----------|
| 1 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago |
| 2 | Ana López | ana@email.com | 555-0102 | Av. Principal 456, Santiago |

#### Tabla: vendedores
```sql
CREATE TABLE vendedores (
    vendedor_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE,
    email VARCHAR(100)
);
```

| vendedor_id | nombre | email |
|-------------|--------|-------|
| 1 | María García | maria.garcia@empresa.com |
| 2 | Carlos Ruiz | carlos.ruiz@empresa.com |

#### Tabla: categorias
```sql
CREATE TABLE categorias (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) UNIQUE
);
```

| categoria_id | nombre |
|--------------|--------|
| 1 | Electrónicos |
| 2 | Accesorios |

#### Tabla: productos_3nf
```sql
CREATE TABLE productos_3nf (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE,
    precio DECIMAL(10,2),
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);
```

| producto_id | nombre | precio | categoria_id |
|-------------|--------|--------|--------------|
| 1 | Laptop Dell | 899.99 | 1 |
| 2 | Mouse Logitech | 25.99 | 2 |
| 3 | iPhone 14 | 1199.99 | 1 |
| 4 | Tablet Samsung | 299.99 | 1 |

#### Tabla: pedidos_3nf
```sql
CREATE TABLE pedidos_3nf (
    pedido_id INT PRIMARY KEY,
    fecha_pedido DATE,
    cliente_id INT,
    vendedor_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(vendedor_id)
);
```

| pedido_id | fecha_pedido | cliente_id | vendedor_id |
|-----------|--------------|------------|-------------|
| 1 | 2024-01-15 | 1 | 1 |
| 2 | 2024-01-16 | 2 | 2 |
| 3 | 2024-01-17 | 1 | 1 |

#### Tabla: pedido_detalle_3nf
```sql
CREATE TABLE pedido_detalle_3nf (
    pedido_id INT,
    producto_id INT,
    cantidad INT DEFAULT 1,
    precio_unitario DECIMAL(10,2),
    PRIMARY KEY (pedido_id, producto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos_3nf(pedido_id),
    FOREIGN KEY (producto_id) REFERENCES productos_3nf(producto_id)
);
```

| pedido_id | producto_id | cantidad | precio_unitario |
|-----------|-------------|----------|-----------------|
| 1 | 1 | 1 | 899.99 |
| 1 | 2 | 1 | 25.99 |
| 2 | 3 | 1 | 1199.99 |
| 3 | 4 | 1 | 299.99 |

---

## Vista Completa - Recreando los Datos Originales

```sql
CREATE VIEW vista_pedidos_completa AS
SELECT 
    p.pedido_id,
    p.fecha_pedido,
    c.nombre as cliente_nombre,
    c.email as cliente_email,
    c.telefono as cliente_telefono,
    c.direccion as cliente_direccion,
    prod.nombre as producto_nombre,
    pd.precio_unitario as producto_precio,
    cat.nombre as producto_categoria,
    v.nombre as vendedor_nombre,
    v.email as vendedor_email,
    (pd.cantidad * pd.precio_unitario) as subtotal
FROM pedidos_3nf p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN vendedores v ON p.vendedor_id = v.vendedor_id
JOIN pedido_detalle_3nf pd ON p.pedido_id = pd.pedido_id
JOIN productos_3nf prod ON pd.producto_id = prod.producto_id
JOIN categorias cat ON prod.categoria_id = cat.categoria_id;
```

### Resultado de la vista:

| pedido_id | fecha_pedido | cliente_nombre | cliente_email | cliente_telefono | cliente_direccion | producto_nombre | producto_precio | producto_categoria | vendedor_nombre | vendedor_email | subtotal |
|-----------|--------------|----------------|---------------|------------------|-------------------|-----------------|------------------|-------------------|----------------|----------------|----------|
| 1 | 2024-01-15 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Laptop Dell | 899.99 | Electrónicos | María García | maria.garcia@empresa.com | 899.99 |
| 1 | 2024-01-15 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Mouse Logitech | 25.99 | Accesorios | María García | maria.garcia@empresa.com | 25.99 |
| 2 | 2024-01-16 | Ana López | ana@email.com | 555-0102 | Av. Principal 456, Santiago | iPhone 14 | 1199.99 | Electrónicos | Carlos Ruiz | carlos.ruiz@empresa.com | 1199.99 |
| 3 | 2024-01-17 | Juan Pérez | juan@email.com | 555-0101 | Calle 123, Santiago | Tablet Samsung | 299.99 | Electrónicos | María García | maria.garcia@empresa.com | 299.99 |

---

## Comparación: Antes vs. Después

### Tabla de Mejoras

| Aspecto | Tabla Original | Tablas Normalizadas (3NF) |
|---------|----------------|---------------------------|
| **Número de tablas** | 1 tabla | 6 tablas relacionadas |
| **Redundancia** | ❌ Alta redundancia | ✅ Mínima redundancia |
| **Integridad** | ❌ Datos inconsistentes | ✅ Integridad referencial |
| **Flexibilidad** | ❌ Difícil de modificar | ✅ Fácil de mantener |
| **Espacio** | ❌ Desperdicio de espacio | ✅ Uso eficiente |
| **Escalabilidad** | ❌ Limitada | ✅ Altamente escalable |

### Ejemplos Prácticos de Beneficios

#### 1. Actualizar información de cliente:
```sql
-- ❌ Antes: Múltiples actualizaciones
UPDATE pedidos_sin_normalizar 
SET cliente_email = 'juan.nuevo@email.com' 
WHERE cliente_nombre = 'Juan Pérez';

-- ✅ Después: Una sola actualización
UPDATE clientes 
SET email = 'juan.nuevo@email.com' 
WHERE nombre = 'Juan Pérez';
```

#### 2. Agregar nuevo producto:
```sql
-- ✅ Ahora es simple y claro
INSERT INTO productos_3nf (nombre, precio, categoria_id) 
VALUES ('Audífonos Sony', 199.99, 2);
```

#### 3. Reportes complejos son más fáciles:
```sql
-- Total de ventas por categoría
SELECT 
    cat.nombre as categoria,
    SUM(pd.cantidad * pd.precio_unitario) as total_ventas,
    COUNT(DISTINCT p.pedido_id) as numero_pedidos
FROM categorias cat
JOIN productos_3nf prod ON cat.categoria_id = prod.categoria_id
JOIN pedido_detalle_3nf pd ON prod.producto_id = pd.producto_id
JOIN pedidos_3nf p ON pd.pedido_id = p.pedido_id
GROUP BY cat.nombre;
```

| categoria | total_ventas | numero_pedidos |
|-----------|-------------|----------------|
| Electrónicos | 2399.97 | 3 |
| Accesorios | 25.99 | 1 |

---

## ✅ Ventajas Finales de la Normalización

1. **📊 Eliminación de redundancia**: Cada dato se almacena una sola vez
2. **🔒 Integridad de datos**: Las actualizaciones son automáticamente consistentes  
3. **🚀 Flexibilidad**: Fácil agregar nuevos clientes, productos, categorías
4. **💾 Eficiencia de espacio**: Menor uso de almacenamiento
5. **🛠️ Mantenimiento**: Los cambios están aislados y controlados
6. **🔍 Consultas complejas**: Más fáciles de escribir y optimizar