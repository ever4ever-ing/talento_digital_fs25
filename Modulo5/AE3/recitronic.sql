-- Insertar clientes
INSERT INTO Clientes (nombre, telefono, direccion) VALUES
('María González', '555-1234', 'Av. Principal #123, Ciudad'),
('Carlos López', '555-5678', 'Calle Secundaria #456, Ciudad'),
('Ana Martínez', '555-9012', 'Boulevard Central #789, Ciudad');

-- Insertar artículos
INSERT INTO Artículos (id_cliente, tipo_articulo, estado, descripcion) VALUES
(1, 'Smartphone', 'pendiente', 'iPhone 7 con pantalla rota'),
(1, 'Tablet', 'pendiente', 'Samsung Galaxy Tab A'),
(2, 'Laptop', 'pendiente', 'Dell Inspiron con batería defectuosa'),
(3, 'Monitor', 'pendiente', 'LG 24" con puerto HDMI dañado');

-- Insertar citas
INSERT INTO Citas (id_cliente, fecha_hora, estado) VALUES
(1, '2024-01-15 10:00:00', 'pendiente'),
(2, '2024-01-16 14:30:00', 'pendiente'),
(3, '2024-01-17 11:15:00', 'pendiente');

-- Insertar pagos
INSERT INTO Pagos (id_cliente, monto, fecha_pago, metodo_pago) VALUES
(1, 25.00, '2024-01-10 09:45:00', 'efectivo'),
(2, 35.50, '2024-01-11 13:20:00', 'tarjeta'),
(3, 42.75, '2024-01-12 16:30:00', 'transferencia');