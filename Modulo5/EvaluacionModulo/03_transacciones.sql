DELIMITER //

CREATE PROCEDURE registrar_compra(
    IN p_id_transaction INT,
    IN p_cantidad INT,
    IN p_id_producto INT,
    IN p_id_proveedor INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error: Transacción cancelada' AS Resultado;
    END;
    
    START TRANSACTION;
    
    -- Insertar la transacción de compra
    INSERT INTO transacciones (id_transaction, tipo, fecha, cantidad, estado, id_producto, id_proveedor)
    VALUES (p_id_transaction, 'Compra', NOW(), p_cantidad, 'En proceso', p_id_producto, p_id_proveedor);

    -- Actualizar el inventario del producto
    UPDATE productos 
    SET cantidad = cantidad + p_cantidad 
    WHERE id_producto = p_id_producto;

    -- Actualizar el estado de la transacción a completada
    UPDATE transacciones 
    SET estado = 'Completada' 
    WHERE id_transaction = p_id_transaction;
    
    COMMIT;
    
    SELECT 'Transacción completada exitosamente' AS Resultado;
END //

DELIMITER ;

-- Llamar al procedimiento
CALL registrar_compra(1004, 10, 2, 101);