# Ejemplos Simples de COMMIT y ROLLBACK en MySQL

## ¿Qué son COMMIT y ROLLBACK?

- **COMMIT**: Confirma y guarda permanentemente todos los cambios de la transacción
- **ROLLBACK**: Cancela y deshace todos los cambios de la transacción

```sql
ALTER TABLE pedidos
DROP FOREIGN KEY fk_pedidos_usuarios1;

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_usuarios1
FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
ON DELETE CASCADE;
```

## Ejemplo 1: COMMIT - Guardando Cambios

```sql
-- Ver datos iniciales
SELECT * FROM usuarios;

-- Iniciar transacción
START TRANSACTION;

    -- Agregar un nuevo usuario
    INSERT INTO usuarios (id, nombre, apellido, direccion_id) 
    VALUES (5, 'Carlos', 'López', 8);
    
    -- Actualizar un usuario existente
    UPDATE usuarios SET nombre = 'Valeria Actualizada' WHERE id = 1;
    
    -- Ver los cambios (solo visibles en esta sesión)
    SELECT * FROM usuarios;

-- Confirmar todos los cambios
COMMIT;

-- Ahora los cambios son permanentes y visibles para todos
SELECT * FROM usuarios;
```

**Resultado**: Los cambios se guardan permanentemente en la base de datos.

## Ejemplo 2: ROLLBACK - Cancelando Cambios

```sql
-- Ver datos iniciales
SELECT * FROM usuarios;

-- Iniciar transacción
START TRANSACTION;

    -- Hacer cambios
    DELETE FROM usuarios WHERE id = 2;  -- Eliminar Kevin Duque
    UPDATE usuarios SET apellido = 'Apellido Cambiado' WHERE id = 1;
    
    -- Ver los cambios temporales
    SELECT * FROM usuarios;
    -- Kevin ya no aparece, Valeria tiene apellido cambiado

-- ¡Ups! Nos arrepentimos, cancelamos todo
ROLLBACK;

-- Ver que todo volvió a como estaba antes
SELECT * FROM usuarios;
-- Kevin sigue ahí, Valeria tiene su apellido original
```

**Resultado**: Todos los cambios se cancelan, la base de datos queda como antes.

## Ejemplo 3: Comparación Práctica

### Sin transacción (cambios inmediatos):
```sql
-- Estos cambios se guardan inmediatamente
INSERT INTO productos (id, nombre, descripcion) 
VALUES (228, 'borrador', 'borra tus errores');

UPDATE productos SET nombre = 'lápiz especial' WHERE id = 222;

-- No hay vuelta atrás, los cambios ya están guardados
SELECT * FROM productos WHERE id IN (222, 228);
```

### Con transacción COMMIT:
```sql
START TRANSACTION;
    
    INSERT INTO productos (id, nombre, descripcion) 
    VALUES (229, 'regla', 'para medir');
    
    UPDATE productos SET descripcion = 'descripción actualizada' WHERE id = 223;
    
-- Decidimos que queremos estos cambios
COMMIT;

-- Los cambios están guardados
SELECT * FROM productos WHERE id IN (223, 229);
```

### Con transacción ROLLBACK:
```sql
START TRANSACTION;
    
    DELETE FROM productos WHERE id = 224;  -- Eliminar el clip
    INSERT INTO productos (id, nombre, descripcion) 
    VALUES (230, 'calculadora', 'para cálculos');
    
-- Decidimos que NO queremos estos cambios
ROLLBACK;

-- El clip sigue ahí, la calculadora no se creó
SELECT * FROM productos WHERE id IN (224, 230);
```

## Ejemplo 4: Caso Real - Procesando un Pedido

```sql
-- Situación: Crear un pedido nuevo con productos

START TRANSACTION;

    -- Crear el pedido
    INSERT INTO pedidos (id, fecha, total, usuario_id) 
    VALUES (555, '2025-01-15', 200.50, 1);
    
    -- Agregar productos al pedido
    INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES 
    (555, 222),  -- lápiz
    (555, 225);  -- bolígrafo
    
    -- Ver cómo quedaría
    SELECT p.*, u.nombre, u.apellido 
    FROM pedidos p 
    JOIN usuarios u ON p.usuario_id = u.id 
    WHERE p.id = 555;
    
    SELECT pr.nombre 
    FROM productos pr 
    JOIN pedidos_has_productos php ON pr.id = php.producto_id 
    WHERE php.pedido_id = 555;

-- Si todo se ve bien, confirmamos
COMMIT;

-- Verificar que el pedido se guardó
SELECT * FROM pedidos WHERE id = 555;
SELECT * FROM pedidos_has_productos WHERE pedido_id = 555;
```


## Ejemplo 5: Autocommit ON/OFF

```sql
-- Ver configuración actual
SELECT @@autocommit;  -- Normalmente es 1 (activado)

-- Con autocommit activado (default):
UPDATE usuarios SET nombre = 'Cambio Inmediato' WHERE id = 2;
-- Este cambio se guarda automáticamente, no necesita COMMIT

-- Desactivar autocommit
SET autocommit = 0;

-- Ahora los cambios necesitan COMMIT manual
UPDATE usuarios SET nombre = 'Cambio Manual' WHERE id = 3;
-- Este cambio NO se guarda hasta hacer COMMIT

COMMIT;  -- Ahora sí se guarda

-- Reactivar autocommit
SET autocommit = 1;
```

## Reglas Simples a Recordar

### ✅ Usar COMMIT cuando:
- Todos los cambios son correctos
- Quieres que los cambios sean permanentes
- Otros usuarios deben ver los cambios

### ❌ Usar ROLLBACK cuando:
- Algo salió mal
- Los datos no son correctos
- Quieres cancelar todos los cambios de la transacción

### 🔄 Patrón básico:
```sql
START TRANSACTION;
    -- hacer cambios
    -- verificar que todo esté bien
    IF todo_correcto THEN
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
```

## Ejemplo de Práctica

```sql
-- Ejercicio: Transferir un producto de un pedido a otro

-- Ver estado inicial
SELECT * FROM pedidos_has_productos WHERE pedido_id IN (551, 552);

START TRANSACTION;

    -- Remover producto 222 del pedido 551
    DELETE FROM pedidos_has_productos 
    WHERE pedido_id = 551 AND producto_id = 222;
    
    -- Agregarlo al pedido 552
    INSERT INTO pedidos_has_productos (pedido_id, producto_id) 
    VALUES (552, 222);
    
    -- Ver cómo quedaría
    SELECT * FROM pedidos_has_productos WHERE pedido_id IN (551, 552);
    
    -- ¿Te gusta el resultado? 
    -- COMMIT para confirmar
    -- ROLLBACK para cancelar

COMMIT;  -- o ROLLBACK;

-- Ver resultado final
SELECT * FROM pedidos_has_productos WHERE pedido_id IN (551, 552);
```

La clave es: **START TRANSACTION** + cambios + **COMMIT** (para confirmar) o **ROLLBACK** (para cancelar).