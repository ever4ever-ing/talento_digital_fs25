# Ejemplos de Transacciones en MySQL

**Base de Datos:** Sistema de Pedidos  
**Propiedades ACID:** Atomicidad, Consistencia, Aislamiento, Durabilidad

## 1. Conceptos Básicos de Transacciones

### Verificar configuración inicial
```sql
-- Verificar el estado actual del autocommit
SELECT @@autocommit;

-- Ver todas las transacciones activas
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;
```

## 2. Ejemplo Básico - Crear un Pedido Completo

**Demostración de ATOMICIDAD:** Todo o nada

### Escenario: Crear un pedido nuevo con sus productos
```sql
START TRANSACTION;

-- Insertar un nuevo pedido
INSERT INTO pedidos (id, fecha, total, usuario_id) 
VALUES (555, '2024-01-15', 450.75, 1);

-- Agregar productos al pedido
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES 
(555, 222),  -- lápiz
(555, 223),  -- libreta
(555, 225);  -- bolígrafo

-- Si todo está correcto, confirmar la transacción
COMMIT;
```

### Verificar que el pedido se creó correctamente
```sql
SELECT p.*, php.producto_id, pr.nombre 
FROM pedidos p 
LEFT JOIN pedidos_has_productos php ON p.id = php.pedido_id
LEFT JOIN productos pr ON php.producto_id = pr.id
WHERE p.id = 555;
```

## 3. Ejemplo de Rollback - Operación Fallida

**Demostración de cómo deshacer cambios cuando algo falla**

```sql

START TRANSACTION;

-- Intentar insertar un pedido con datos incorrectos
INSERT INTO pedidos (id, fecha, total, usuario_id) 
VALUES (556, '2024-01-16', 299.99, 1);

-- Intentar agregar productos
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES 
(556, 222),
(556, 999);  -- Este producto NO existe - causará problemas

-- Simular que detectamos un error (producto inexistente)
-- En una aplicación real, esto sería manejado por la lógica de negocio

-- Deshacer todos los cambios
ROLLBACK;
```

### Verificar que NO se creó el pedido
```sql
-- Debe retornar 0 filas
SELECT COUNT(*) as pedidos_556 FROM pedidos WHERE id = 556;
```

## 4. Transacción Compleja - Actualización de Datos

**Demostración de CONSISTENCIA:** Los datos mantienen su integridad

```sql

START TRANSACTION;

-- Actualizar información de usuario y su dirección
UPDATE usuarios 
SET nombre = 'Valeria Andrea', apellido = 'Romero Silva' 
WHERE id = 1;

-- Actualizar la dirección correspondiente
UPDATE direcciones 
SET calle = 'Calle 114 Norte', colonia = 'San José Centro'
WHERE id = 4;  -- Dirección de Valeria

-- Agregar un nuevo pedido para este usuario actualizado
INSERT INTO pedidos (id, fecha, total, usuario_id) 
VALUES (557, '2024-01-17', 175.25, 1);

-- Agregar productos al nuevo pedido
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES 
(557, 224),  -- clip
(557, 226);  -- marcatextos

-- Confirmar todos los cambios
COMMIT;
```

### Verificar la consistencia de los datos
```sql
SELECT 
    u.id,
    u.nombre,
    u.apellido,
    d.calle,
    d.colonia,
    COUNT(p.id) as total_pedidos
FROM usuarios u 
JOIN direcciones d ON u.direccion_id = d.id 
LEFT JOIN pedidos p ON u.id = p.usuario_id 
WHERE u.id = 1
GROUP BY u.id, u.nombre, u.apellido, d.calle, d.colonia;
```

## 5. Transacciones con Savepoints

**Permite hacer rollback parcial dentro de una transacción**

```sql

START TRANSACTION;

-- Insertar un pedido base
INSERT INTO pedidos (id, fecha, total, usuario_id) 
VALUES (558, '2024-01-18', 0, 2);  -- Total inicial en 0

-- Crear un savepoint
SAVEPOINT sp_pedido_creado;

-- Agregar primer grupo de productos
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES 
(558, 222),
(558, 223);

-- Actualizar total del pedido
UPDATE pedidos SET total = 150.00 WHERE id = 558;

-- Crear otro savepoint
SAVEPOINT sp_primeros_productos;

-- Intentar agregar más productos
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES 
(558, 225),
(558, 226);

-- Actualizar total nuevamente
UPDATE pedidos SET total = 250.00 WHERE id = 558;

-- Simular que hay un problema con los últimos productos
-- Rollback solo hasta el savepoint anterior
ROLLBACK TO SAVEPOINT sp_primeros_productos;

-- Confirmar la transacción con solo los primeros productos
COMMIT;
```

### Verificar el resultado
```sql
SELECT p.*, php.producto_id, pr.nombre 
FROM pedidos p 
LEFT JOIN pedidos_has_productos php ON p.id = php.pedido_id
LEFT JOIN productos pr ON php.producto_id = pr.id
WHERE p.id = 558;
```

## 6. Demostración de Aislamiento

**Diferentes niveles de aislamiento de transacciones**

```sql

-- Verificar el nivel actual de aislamiento
SELECT @@transaction_isolation;

-- Ejemplo de transacción con nivel de aislamiento específico
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;

START TRANSACTION;

-- Esta consulta verá solo datos confirmados por otras transacciones
SELECT u.nombre, u.apellido, COUNT(p.id) as pedidos
FROM usuarios u 
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido;

-- Simular trabajo adicional...
SELECT SLEEP(2);

-- Segunda consulta en la misma transacción
SELECT COUNT(*) as total_pedidos FROM pedidos;

COMMIT;

-- Restaurar nivel de aislamiento por defecto
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

## 7. Ejemplo Práctico - Transferencia de Pedidos

**Escenario:** Transferir un pedido de un usuario a otro

```sql

START TRANSACTION;

-- Variables para el ejemplo
SET @pedido_a_transferir = 552;
SET @usuario_origen = 2;  -- Kevin
SET @usuario_destino = 4; -- Everardo

-- Verificar que el pedido pertenece al usuario origen
SELECT COUNT(*) INTO @verificacion
FROM pedidos 
WHERE id = @pedido_a_transferir AND usuario_id = @usuario_origen;

-- Solo proceder si la verificación es correcta
-- En una aplicación real, esto sería una condición IF
-- SELECT @verificacion as 'Pedido encontrado (debe ser 1)';

-- Transferir el pedido
UPDATE pedidos 
SET usuario_id = @usuario_destino 
WHERE id = @pedido_a_transferir AND usuario_id = @usuario_origen;

-- Verificar que se afectó exactamente 1 fila
SELECT ROW_COUNT() as 'Filas actualizadas';

-- Confirmar la transacción
COMMIT;
```

### Verificar el resultado de la transferencia
```sql
SELECT 
    p.id as pedido_id,
    CONCAT(u.nombre, ' ', u.apellido) as nuevo_propietario,
    p.fecha,
    p.total
FROM pedidos p
JOIN usuarios u ON p.usuario_id = u.id
WHERE p.id = @pedido_a_transferir;
```

## 8. Transacción con Manejo de Errores

**Ejemplo de cómo manejar errores en transacciones**

```sql

DELIMITER //

CREATE PROCEDURE CrearPedidoSeguro(
    IN p_pedido_id INT,
    IN p_fecha DATE,
    IN p_total DECIMAL(10,2),
    IN p_usuario_id INT,
    IN p_productos TEXT  -- Lista de IDs separados por comas
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Verificar que el usuario existe
    IF NOT EXISTS (SELECT 1 FROM usuarios WHERE id = p_usuario_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Usuario no existe';
    END IF;
    
    -- Crear el pedido
    INSERT INTO pedidos (id, fecha, total, usuario_id) 
    VALUES (p_pedido_id, p_fecha, p_total, p_usuario_id);
    
    -- Aquí normalmente procesaríamos la lista de productos
    -- Por simplicidad, agregamos productos fijos
    INSERT INTO pedidos_has_productos (pedido_id, producto_id) 
    VALUES 
        (p_pedido_id, 222),
        (p_pedido_id, 223);
    
    COMMIT;
    
    SELECT 'Pedido creado exitosamente' as resultado;
    
END //

DELIMITER ;
```

### Probar el procedimiento
```sql
-- Crear pedido usando el procedimiento seguro
CALL CrearPedidoSeguro(559, '2024-01-19', 125.50, 3, '222,223');

-- Verificar el pedido creado
SELECT * FROM pedidos WHERE id = 559;
```

## 9. Transacciones Deadlock - Demostración

**Ejemplo de cómo pueden ocurrir deadlocks**

### Transacción 1 (ejecutar en una sesión)
```sql
/*
START TRANSACTION;
UPDATE usuarios SET nombre = 'Usuario1_Modificado' WHERE id = 1;
-- Esperar un momento antes de la siguiente línea
SELECT SLEEP(5);
UPDATE usuarios SET nombre = 'Usuario2_Modificado' WHERE id = 2;
COMMIT;
*/
```

### Transacción 2 (ejecutar simultáneamente en otra sesión)
```sql
/*
START TRANSACTION;
UPDATE usuarios SET nombre = 'Usuario2_Modificado_2' WHERE id = 2;
-- Esperar un momento antes de la siguiente línea
SELECT SLEEP(5);
UPDATE usuarios SET nombre = 'Usuario1_Modificado_2' WHERE id = 1;
COMMIT;
*/
```

## 10. Monitoreo de Transacciones

### Ver transacciones activas
```sql
SELECT 
    trx_id,
    trx_state,
    trx_started,
    trx_requested_lock_id,
    trx_wait_started,
    trx_weight,
    trx_mysql_thread_id,
    trx_query
FROM INFORMATION_SCHEMA.INNODB_TRX;
```

### Ver bloqueos activos
```sql
SELECT 
    lock_id,
    lock_trx_id,
    lock_mode,
    lock_type,
    lock_table,
    lock_index,
    lock_rec
FROM INFORMATION_SCHEMA.INNODB_LOCKS;
```

### Ver esperas de bloqueos
```sql
SELECT 
    requesting_trx_id,
    requested_lock_id,
    blocking_trx_id,
    blocking_lock_id
FROM INFORMATION_SCHEMA.INNODB_LOCK_WAITS;
```

## 11. Ejemplos de Diferentes Modos Autocommit

```sql

-- Verificar estado actual
SELECT @@autocommit as 'Autocommit actual';

-- Desactivar autocommit para control manual
SET autocommit = 0;

-- Ahora todas las operaciones requieren COMMIT explícito
INSERT INTO pedidos (id, fecha, total, usuario_id) 
VALUES (560, '2024-01-20', 89.99, 4);

-- Los cambios no son permanentes hasta hacer COMMIT
SELECT * FROM pedidos WHERE id = 560;

-- Confirmar manualmente
COMMIT;

-- Reactivar autocommit
SET autocommit = 1;
```

## 12. Limpieza - Eliminar Datos de Prueba

**Eliminar los pedidos de ejemplo creados**

```sql

START TRANSACTION;

-- Eliminar relaciones primero
DELETE FROM pedidos_has_productos WHERE pedido_id IN (555, 557, 558, 559, 560);

-- Eliminar pedidos
DELETE FROM pedidos WHERE id IN (555, 557, 558, 559, 560);

-- Restaurar datos originales del usuario 1
UPDATE usuarios 
SET nombre = 'Valeria', apellido = 'Romero' 
WHERE id = 1;

UPDATE direcciones 
SET calle = 'Calle 114', colonia = 'San José'
WHERE id = 4;

-- Restaurar pedido transferido
UPDATE pedidos 
SET usuario_id = 2 
WHERE id = 552;

COMMIT;

-- Eliminar el procedimiento de prueba
DROP PROCEDURE IF EXISTS CrearPedidoSeguro;
```

## 13. Verificación Final

```sql
-- Verificar que los datos están como al inicio
SELECT 'Usuarios' as tabla, COUNT(*) as registros FROM usuarios
UNION ALL
SELECT 'Pedidos' as tabla, COUNT(*) as registros FROM pedidos
UNION ALL
SELECT 'Productos' as tabla, COUNT(*) as registros FROM productos
UNION ALL
SELECT 'Direcciones' as tabla, COUNT(*) as registros FROM direcciones
UNION ALL
SELECT 'Pedidos_Productos' as tabla, COUNT(*) as registros FROM pedidos_has_productos;
```