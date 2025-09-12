
-- 2. Actualizar cantidad después de una venta (id_producto = 1, cantidad vendida = 3)
UPDATE productos 
SET cantidad = cantidad - 3 
WHERE id_producto = 1;

-- 3. Eliminar un producto si ya no está disponible (ejemplo: eliminar producto con ID 3)
-- Primero eliminamos las transacciones relacionadas para mantener la integridad referencial
DELETE FROM transacciones 
WHERE id_producto = 3;

-- Luego eliminamos el producto
DELETE FROM productos 
WHERE id_producto = 3;

