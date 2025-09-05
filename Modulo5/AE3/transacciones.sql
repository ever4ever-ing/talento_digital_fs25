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
    IF NOT EXISTS (SELECT 1 FROM clientes WHERE id_clientes = p_id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El cliente no existe';
    END IF;
    
    -- Verificar si ya existe una cita en esa fecha y hora
    IF EXISTS (SELECT 1 FROM citas WHERE fecha_hora = p_fecha_hora) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ya existe una cita programada para esa fecha y hora';
    END IF;
    
    -- Insertar la nueva cita
    INSERT INTO citas (id_cliente, fecha_hora)
    VALUES (p_id_cliente, p_fecha_hora);
    
    COMMIT;
END //
DELIMITER ;