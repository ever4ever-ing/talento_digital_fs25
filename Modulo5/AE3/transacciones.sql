-- Procedimiento para agendar una cita con verificación de disponibilidad
DELIMITER //
CREATE PROCEDURE AgendarCita(
    IN p_id_cliente INT,
    IN p_fecha_hora DATETIME
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Verificar si el cliente existe
    IF NOT EXISTS (SELECT 1 FROM Clientes WHERE id_cliente = p_id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El cliente no existe';
    END IF;
    
    -- Verificar si ya existe una cita en esa fecha y hora
    IF EXISTS (SELECT 1 FROM Citas WHERE fecha_hora = p_fecha_hora) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ya existe una cita programada para esa fecha y hora';
    END IF;
    
    -- Insertar la nueva cita
    INSERT INTO Citas (id_cliente, fecha_hora, estado)
    VALUES (p_id_cliente, p_fecha_hora, 'pendiente');
    
    COMMIT;
END //
DELIMITER ;

-- Procedimiento para procesar el reciclaje de un artículo con transacción
DELIMITER //
CREATE PROCEDURE ProcesarArticuloReciclado(
    IN p_id_articulo INT,
    IN p_nuevo_estado ENUM('en_proceso', 'reciclado', 'desechado')
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Verificar si el artículo existe
    IF NOT EXISTS (SELECT 1 FROM Artículos WHERE id_articulo = p_id_articulo) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El artículo no existe';
    END IF;
    
    -- Actualizar el estado del artículo
    UPDATE Artículos 
    SET estado = p_nuevo_estado
    WHERE id_articulo = p_id_articulo;
    
    -- Registrar en auditoría si es necesario
    IF p_nuevo_estado = 'reciclado' THEN
        INSERT INTO AuditoriaCitas (id_cita, accion, fecha_cambio)
        SELECT c.id_cita, 'completada', NOW()
        FROM Citas c
        INNER JOIN Artículos a ON c.id_cliente = a.id_cliente
        WHERE a.id_articulo = p_id_articulo
        AND c.estado = 'confirmada';
    END IF;
    
    COMMIT;
END //
DELIMITER ;

-- Procedimiento para cancelar una cita con rollback en caso de error
DELIMITER //
CREATE PROCEDURE CancelarCita(
    IN p_id_cita INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Verificar si la cita existe
    IF NOT EXISTS (SELECT 1 FROM Citas WHERE id_cita = p_id_cita) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La cita no existe';
    END IF;
    
    -- Registrar en auditoría antes de eliminar
    INSERT INTO AuditoriaCitas (id_cita, accion, fecha_hora_anterior, fecha_cambio)
    SELECT id_cita, 'cancelacion', fecha_hora, NOW()
    FROM Citas
    WHERE id_cita = p_id_cita;
    
    -- Eliminar la cita
    DELETE FROM Citas WHERE id_cita = p_id_cita;
    
    COMMIT;
END //
DELIMITER ;