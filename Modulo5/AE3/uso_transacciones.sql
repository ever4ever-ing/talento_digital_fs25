-- Ejemplo 1: Agendar una nueva cita
CALL AgendarCita(2, '2024-01-18 15:00:00');

-- Ejemplo 2: Procesar un artículo como reciclado
CALL ProcesarArticuloReciclado(1, 'reciclado');

-- Ejemplo 3: Cancelar una cita
CALL CancelarCita(2);

-- Ejemplo 4: Transacción con rollback (simulando un error)
START TRANSACTION;

INSERT INTO Pagos (id_cliente, monto, fecha_pago, metodo_pago)
VALUES (1, 50.00, NOW(), 'efectivo');

-- Esto provocará un error deliberadamente (cliente inexistente)
INSERT INTO Pagos (id_cliente, monto, fecha_pago, metodo_pago)
VALUES (999, 30.00, NOW(), 'tarjeta');

-- Si llegamos aquí, confirmamos la transacción
COMMIT;

-- Como hay un error, se ejecutará el rollback automáticamente