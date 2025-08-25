# EJEMPLOS DE TRIGGERS EN MYSQL
## Base de Datos: Sistema de Pedidos
### Automatización y Integridad de Datos

---

## 1. PREPARACIÓN - CREAR TABLAS AUXILIARES

### Tabla para auditoría de usuarios
```sql
CREATE TABLE auditoria_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    accion VARCHAR(10), -- INSERT, UPDATE, DELETE
    campo_modificado VARCHAR(50),
    valor_anterior TEXT,
    valor_nuevo TEXT,
    fecha_modificacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario_sistema VARCHAR(100) DEFAULT USER()
);
```

### Tabla para logs de pedidos
```sql
CREATE TABLE logs_pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    accion VARCHAR(20),
    total_anterior DECIMAL(10,2),
    total_nuevo DECIMAL(10,2),
    descripcion TEXT,
    fecha_log DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla para estadísticas automáticas
```sql
CREATE TABLE estadisticas_productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    total_vendido INT DEFAULT 0,
    ultima_venta DATETIME,
    UNIQUE KEY unique_producto (producto_id)
);
```

### Tabla para control de stock (simulado)
```sql
CREATE TABLE inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    stock_actual INT DEFAULT 100,
    stock_minimo INT DEFAULT 10,
    ultima_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_producto_inventario (producto_id)
);
```

### Inicializar inventario para productos existentes
```sql
INSERT INTO inventario (producto_id, stock_actual, stock_minimo) VALUES
(222, 50, 5),   -- lápiz
(223, 30, 3),   -- libreta
(224, 100, 10), -- clip
(225, 45, 5),   -- bolígrafo
(226, 25, 2),   -- marcatextos
(227, 15, 1);   -- tijeras
```

---

## 2. TRIGGERS `AFTER INSERT` - DESPUÉS DE INSERTAR

### Trigger: Auditar creación de nuevos usuarios
```sql
DELIMITER //
CREATE TRIGGER tr_usuarios_after_insert
    AFTER INSERT ON usuarios
    FOR EACH ROW
BEGIN
    INSERT INTO auditoria_usuarios (
        usuario_id, 
        accion, 
        campo_modificado, 
        valor_nuevo, 
        descripcion
    ) VALUES (
        NEW.id, 
        'INSERT', 
        'usuario_completo',
        CONCAT('Nombre: ', NEW.nombre, ', Apellido: ', NEW.apellido, ', Dirección: ', NEW.direccion_id),
        'Nuevo usuario creado'
    );
END//
DELIMITER ;
```

### Trigger: Log automático de nuevos pedidos
```sql
DELIMITER //
CREATE TRIGGER tr_pedidos_after_insert
    AFTER INSERT ON pedidos
    FOR EACH ROW
BEGIN
    INSERT INTO logs_pedidos (
        pedido_id,
        accion,
        total_nuevo,
        descripcion
    ) VALUES (
        NEW.id,
        'CREADO',
        NEW.total,
        CONCAT('Nuevo pedido creado por usuario ', NEW.usuario_id, ' por $', NEW.total)
    );
END//
DELIMITER ;
```

---

## 3. TRIGGERS `AFTER UPDATE` - DESPUÉS DE ACTUALIZAR

### Trigger: Auditar cambios en usuarios
```sql
DELIMITER //
CREATE TRIGGER tr_usuarios_after_update
    AFTER UPDATE ON usuarios
    FOR EACH ROW
BEGIN
    -- Auditar cambio de nombre
    IF OLD.nombre != NEW.nombre THEN
        INSERT INTO auditoria_usuarios (
            usuario_id, accion, campo_modificado, 
            valor_anterior, valor_nuevo
        ) VALUES (
            NEW.id, 'UPDATE', 'nombre', 
            OLD.nombre, NEW.nombre
        );
    END IF;
    
    -- Auditar cambio de apellido
    IF OLD.apellido != NEW.apellido THEN
        INSERT INTO auditoria_usuarios (
            usuario_id, accion, campo_modificado, 
            valor_anterior, valor_nuevo
        ) VALUES (
            NEW.id, 'UPDATE', 'apellido', 
            OLD.apellido, NEW.apellido
        );
    END IF;
    
    -- Auditar cambio de dirección
    IF OLD.direccion_id != NEW.direccion_id THEN
        INSERT INTO auditoria_usuarios (
            usuario_id, accion, campo_modificado, 
            valor_anterior, valor_nuevo
        ) VALUES (
            NEW.id, 'UPDATE', 'direccion_id', 
            OLD.direccion_id, NEW.direccion_id
        );
    END IF;
END//
DELIMITER ;
```

### Trigger: Log de cambios en pedidos
```sql
DELIMITER //
CREATE TRIGGER tr_pedidos_after_update
    AFTER UPDATE ON pedidos
    FOR EACH ROW
BEGIN
    -- Solo registrar si cambió el total
    IF OLD.total != NEW.total THEN
        INSERT INTO logs_pedidos (
            pedido_id,
            accion,
            total_anterior,
            total_nuevo,
            descripcion
        ) VALUES (
            NEW.id,
            'MODIFICADO',
            OLD.total,
            NEW.total,
            CONCAT('Total cambiado de $', OLD.total, ' a $', NEW.total)
        );
    END IF;
END//
DELIMITER ;
```

---

## 4. TRIGGERS `AFTER DELETE` - DESPUÉS DE ELIMINAR

### Trigger: Auditar eliminación de usuarios
```sql
DELIMITER //
CREATE TRIGGER tr_usuarios_after_delete
    AFTER DELETE ON usuarios
    FOR EACH ROW
BEGIN
    INSERT INTO auditoria_usuarios (
        usuario_id, 
        accion, 
        campo_modificado, 
        valor_anterior
    ) VALUES (
        OLD.id, 
        'DELETE', 
        'usuario_eliminado',
        CONCAT('Usuario: ', OLD.nombre, ' ', OLD.apellido, ' eliminado')
    );
END//
DELIMITER ;
```

---

## 5. TRIGGERS `BEFORE INSERT` - ANTES DE INSERTAR

### Trigger: Validar datos antes de insertar usuario
```sql
DELIMITER //
CREATE TRIGGER tr_usuarios_before_insert
    BEFORE INSERT ON usuarios
    FOR EACH ROW
BEGIN
    -- Validar que el nombre no esté vacío
    IF NEW.nombre = '' OR NEW.nombre IS NULL THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El nombre del usuario no puede estar vacío';
    END IF;
    
    -- Validar que el apellido no esté vacío
    IF NEW.apellido = '' OR NEW.apellido IS NULL THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El apellido del usuario no puede estar vacío';
    END IF;
    
    -- Capitalizar primera letra automáticamente
    SET NEW.nombre = CONCAT(UPPER(SUBSTRING(NEW.nombre, 1, 1)), 
                           LOWER(SUBSTRING(NEW.nombre, 2)));
    SET NEW.apellido = CONCAT(UPPER(SUBSTRING(NEW.apellido, 1, 1)), 
                             LOWER(SUBSTRING(NEW.apellido, 2)));
END//
DELIMITER ;
```

### Trigger: Validar pedidos antes de insertar
```sql
DELIMITER //
CREATE TRIGGER tr_pedidos_before_insert
    BEFORE INSERT ON pedidos
    FOR EACH ROW
BEGIN
    -- Validar que el total sea positivo
    IF NEW.total <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El total del pedido debe ser mayor a 0';
    END IF;
    
    -- Validar que el usuario exista
    IF NOT EXISTS (SELECT 1 FROM usuarios WHERE id = NEW.usuario_id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El usuario especificado no existe';
    END IF;
    
    -- Establecer fecha actual si no se proporciona
    IF NEW.fecha IS NULL THEN
        SET NEW.fecha = CURDATE();
    END IF;
END//
DELIMITER ;
```

---

## 6. TRIGGERS `BEFORE UPDATE` - ANTES DE ACTUALIZAR

### Trigger: Validar actualizaciones de pedidos
```sql
DELIMITER //
CREATE TRIGGER tr_pedidos_before_update
    BEFORE UPDATE ON pedidos
    FOR EACH ROW
BEGIN
    -- No permitir cambios en pedidos muy antiguos
    IF OLD.fecha < DATE_SUB(CURDATE(), INTERVAL 1 YEAR) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'No se pueden modificar pedidos de hace más de un año';
    END IF;
    
    -- Validar que el nuevo total sea positivo
    IF NEW.total <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El total del pedido debe ser mayor a 0';
    END IF;
    
    -- Evitar cambios drásticos en el total (más del 500%)
    IF NEW.total > OLD.total * 5 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El aumento del total es demasiado grande, verifique los datos';
    END IF;
END//
DELIMITER ;
```

---

## 7. TRIGGERS `BEFORE DELETE` - ANTES DE ELIMINAR

### Trigger: Validar eliminación de usuarios
```sql
DELIMITER //
CREATE TRIGGER tr_usuarios_before_delete
    BEFORE DELETE ON usuarios
    FOR EACH ROW
BEGIN
    -- No permitir eliminar usuarios con pedidos
    IF EXISTS (SELECT 1 FROM pedidos WHERE usuario_id = OLD.id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'No se puede eliminar un usuario que tiene pedidos asociados';
    END IF;
END//
DELIMITER ;
```

---

## 8. TRIGGERS PARA MANTENIMIENTO DE INVENTARIO

### Trigger: Actualizar estadísticas al agregar productos a pedidos
```sql
DELIMITER //
CREATE TRIGGER tr_pedidos_productos_after_insert
    AFTER INSERT ON pedidos_has_productos
    FOR EACH ROW
BEGIN
    -- Actualizar estadísticas del producto
    INSERT INTO estadisticas_productos (producto_id, total_vendido, ultima_venta)
    VALUES (NEW.producto_id, 1, NOW())
    ON DUPLICATE KEY UPDATE 
        total_vendido = total_vendido + 1,
        ultima_venta = NOW();
    
    -- Reducir stock (simulado)
    UPDATE inventario 
    SET stock_actual = stock_actual - 1,
        ultima_actualizacion = NOW()
    WHERE producto_id = NEW.producto_id;
END//
DELIMITER ;
```

### Trigger: Verificar stock antes de agregar producto a pedido
```sql
DELIMITER //
CREATE TRIGGER tr_pedidos_productos_before_insert
    BEFORE INSERT ON pedidos_has_productos
    FOR EACH ROW
BEGIN
    DECLARE stock_disponible INT DEFAULT 0;
    
    -- Obtener stock actual
    SELECT stock_actual INTO stock_disponible
    FROM inventario 
    WHERE producto_id = NEW.producto_id;
    
    -- Verificar si hay stock
    IF stock_disponible <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Producto sin stock disponible';
    END IF;
    
    -- Advertir si stock está bajo
    IF stock_disponible <= (SELECT stock_minimo FROM inventario WHERE producto_id = NEW.producto_id) THEN
        -- En MySQL no podemos mostrar warnings fácilmente desde triggers, 
        -- pero podemos loggearlo
        INSERT INTO logs_pedidos (pedido_id, accion, descripcion)
        VALUES (NEW.pedido_id, 'STOCK_BAJO', 
                CONCAT('Stock bajo para producto ', NEW.producto_id, ': ', stock_disponible, ' unidades'));
    END IF;
END//
DELIMITER ;
```

---

## 9. TRIGGER COMPLEJO - CÁLCULO AUTOMÁTICO

### Trigger: Actualizar total del pedido automáticamente
Este trigger simula que cada producto tiene un precio fijo.
```sql
DELIMITER //
CREATE TRIGGER tr_actualizar_total_pedido
    AFTER INSERT ON pedidos_has_productos
    FOR EACH ROW
BEGIN
    DECLARE precio_producto DECIMAL(10,2) DEFAULT 0;
    DECLARE nuevo_total DECIMAL(10,2) DEFAULT 0;
    
    -- Precios simulados por producto
    CASE NEW.producto_id
        WHEN 222 THEN SET precio_producto = 15.50;  -- lápiz
        WHEN 223 THEN SET precio_producto = 45.00;  -- libreta
        WHEN 224 THEN SET precio_producto = 5.25;   -- clip
        WHEN 225 THEN SET precio_producto = 12.75;  -- bolígrafo
        WHEN 226 THEN SET precio_producto = 25.30;  -- marcatextos
        WHEN 227 THEN SET precio_producto = 18.90;  -- tijeras
        ELSE SET precio_producto = 10.00;           -- precio por defecto
    END CASE;
    
    -- Calcular nuevo total del pedido
    SELECT 
        COALESCE(SUM(
            CASE php.producto_id
                WHEN 222 THEN 15.50
                WHEN 223 THEN 45.00
                WHEN 224 THEN 5.25
                WHEN 225 THEN 12.75
                WHEN 226 THEN 25.30
                WHEN 227 THEN 18.90
                ELSE 10.00
            END
        ), 0) INTO nuevo_total
    FROM pedidos_has_productos php
    WHERE php.pedido_id = NEW.pedido_id;
    
    -- Actualizar el total del pedido
    UPDATE pedidos 
    SET total = nuevo_total 
    WHERE id = NEW.pedido_id;
END//
DELIMITER ;
```

---

## 10. PRUEBAS DE LOS TRIGGERS

### Probar trigger de inserción de usuarios
```sql
INSERT INTO usuarios (id, nombre, apellido, direccion_id) 
VALUES (5, 'maría', 'gonzález', 4);
```
**Verificar auditoría:**
```sql
SELECT * FROM auditoria_usuarios WHERE usuario_id = 5;
```

### Probar trigger de pedidos
```sql
INSERT INTO pedidos (id, fecha, total, usuario_id) 
VALUES (561, '2024-01-25', 100.00, 5);
```
**Verificar logs:**
```sql
SELECT * FROM logs_pedidos WHERE pedido_id = 561;
```

### Probar actualización de usuario
```sql
UPDATE usuarios SET nombre = 'María Elena' WHERE id = 5;
```
**Verificar auditoría de cambio:**
```sql
SELECT * FROM auditoria_usuarios WHERE usuario_id = 5 ORDER BY fecha_modificacion;
```

### Probar trigger de productos
```sql
INSERT INTO pedidos_has_productos (pedido_id, producto_id) 
VALUES (561, 222);
```
**Verificar estadísticas y inventario:**
```sql
SELECT * FROM estadisticas_productos WHERE producto_id = 222;
SELECT * FROM inventario WHERE producto_id = 222;
```
**Verificar cálculo automático de total:**
```sql
SELECT * FROM pedidos WHERE id = 561;
```

---

## 11. TRIGGERS CON MANEJO DE ERRORES

Estas pruebas deberían fallar:
```sql
-- INSERT INTO usuarios (id, nombre, apellido, direccion_id) VALUES (6, '', 'Test', 4);
-- INSERT INTO pedidos (id, fecha, total, usuario_id) VALUES (562, '2024-01-25', -100, 5);
```

Prueba de eliminación protegida (debería fallar porque el usuario tiene pedidos):
```sql
-- DELETE FROM usuarios WHERE id = 1;
```

---

## 12. CONSULTAS DE MONITOREO

### Ver todos los triggers creados
```sql
SELECT 
    TRIGGER_NAME,
    EVENT_MANIPULATION,
    EVENT_OBJECT_TABLE,
    ACTION_TIMING
FROM INFORMATION_SCHEMA.TRIGGERS 
WHERE TRIGGER_SCHEMA = DATABASE()
ORDER BY EVENT_OBJECT_TABLE, ACTION_TIMING, EVENT_MANIPULATION;
```

### Resumen de auditoría
```sql
SELECT 
    accion,
    COUNT(*) as total_acciones,
    MIN(fecha_modificacion) as primera_accion,
    MAX(fecha_modificacion) as ultima_accion
FROM auditoria_usuarios
GROUP BY accion;
```

### Estadísticas de productos
```sql
SELECT 
    p.nombre,
    ep.total_vendido,
    ep.ultima_venta,
    i.stock_actual
FROM productos p
LEFT JOIN estadisticas_productos ep ON p.id = ep.producto_id
LEFT JOIN inventario i ON p.id = i.producto_id
ORDER BY ep.total_vendido DESC;
```

### Logs de pedidos más recientes
```sql
SELECT 
    lp.*,
    p.fecha as fecha_pedido,
    u.nombre as usuario_nombre
FROM logs_pedidos lp
JOIN pedidos p ON lp.pedido_id = p.id
JOIN usuarios u ON p.usuario_id = u.id
ORDER BY lp.fecha_log DESC
LIMIT 10;
```

---

## 13. GESTIÓN DE TRIGGERS

### Ver definición de un trigger específico
```sql
-- SHOW CREATE TRIGGER tr_usuarios_after_insert;
```

### Listar todos los triggers
```sql
SHOW TRIGGERS;
```

### Eliminar un trigger
```sql
-- DROP TRIGGER IF EXISTS tr_usuarios_after_insert;
```

---

## 14. TRIGGERS PARA CASOS ESPECÍFICOS

### Trigger para mantener histórico de precios
```sql
CREATE TABLE historico_precios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    precio_anterior DECIMAL(10,2),
    precio_nuevo DECIMAL(10,2),
    fecha_cambio DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Trigger que simula cambios de precio (para demostración)
```sql
DELIMITER //
CREATE TRIGGER tr_historico_precios
    BEFORE UPDATE ON productos
    FOR EACH ROW
BEGIN
    -- Solo para demostración, simular que la descripción tiene el precio
    IF OLD.descripcion != NEW.descripcion THEN
        INSERT INTO historico_precios (producto_id, precio_anterior, precio_nuevo)
        VALUES (OLD.id, 0.00, 0.00);  -- Precios simulados
    END IF;
END//
DELIMITER ;
```

---

## 15. LIMPIEZA (COMENTADO PARA SEGURIDAD)
Para eliminar las tablas y triggers de prueba:
```sql
/*
-- Eliminar triggers
DROP TRIGGER IF EXISTS tr_usuarios_after_insert;
DROP TRIGGER IF EXISTS tr_usuarios_after_update;
DROP TRIGGER IF EXISTS tr_usuarios_after_delete;
DROP TRIGGER IF EXISTS tr_usuarios_before_insert;
DROP TRIGGER IF EXISTS tr_usuarios_before_delete;
DROP TRIGGER IF EXISTS tr_pedidos_after_insert;
DROP TRIGGER IF EXISTS tr_pedidos_after_update;
DROP TRIGGER IF EXISTS tr_pedidos_before_insert;
DROP TRIGGER IF EXISTS tr_pedidos_before_update;
DROP TRIGGER IF EXISTS tr_pedidos_productos_after_insert;
DROP TRIGGER IF EXISTS tr_pedidos_productos_before_insert;
DROP TRIGGER IF EXISTS tr_actualizar_total_pedido;
DROP TRIGGER IF EXISTS tr_historico_precios;

-- Eliminar datos de prueba
DELETE FROM usuarios WHERE id = 5;
DELETE FROM pedidos WHERE id = 561;

-- Eliminar tablas auxiliares
DROP TABLE IF EXISTS auditoria_usuarios;
DROP TABLE IF EXISTS logs_pedidos;
DROP TABLE IF EXISTS estadisticas_productos;
DROP TABLE IF EXISTS inventario;
DROP TABLE IF EXISTS historico_precios;
*/
```