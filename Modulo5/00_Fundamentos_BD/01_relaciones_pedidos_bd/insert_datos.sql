-- Limpiar datos existentes (en orden inverso a las dependencias)
SET FOREIGN_KEY_CHECKS = 0;

DELETE FROM pedidos_has_productos;
DELETE FROM pedidos;
DELETE FROM productos;
DELETE FROM usuarios;
DELETE FROM direcciones;

-- Reiniciar los contadores AUTO_INCREMENT
ALTER TABLE direcciones AUTO_INCREMENT = 1;
ALTER TABLE usuarios AUTO_INCREMENT = 1;
ALTER TABLE productos AUTO_INCREMENT = 1;
ALTER TABLE pedidos AUTO_INCREMENT = 1;

SET FOREIGN_KEY_CHECKS = 1;

-- Insertar direcciones primero
INSERT INTO direcciones (calle, colonia, ciudad, pais) VALUES
('Calle 114', 'San José', 'Rancho de Luna','Costa Rica'),
('5 Av. Monsefior Miguel 545', 'Atacama', 'Tierra Amarilla', 'Chile'),
('Dover 2903', 'Narvarte', 'Monterrey', 'México'),
('Avenida 77', 'Araucania', 'Temuco', 'Chile');

-- Insertar usuarios usando los IDs de direcciones generados automáticamente
INSERT INTO usuarios (nombre, apellido, direccion_id) VALUES
('Valeria', 'Romero', 1),
('Kevin', 'Duque', 2),
('Alfredo', 'Salazar', 3),
('Everardo', 'Alvarado', 4);

-- Insertar productos
INSERT INTO productos (nombre, descripcion) VALUES
('lapiz', 'lapiz que te ayudará a escribir ERDs'),
('libreta', 'para escribir todas tus notas de MySQL'),
('clip', 'sostiene tus hojas'),
('boligrafo', 'tus notas no se borraran con nada'),
('marcatextos', 'para subrayar lo más importante'),
('tijeras', 'recorta todo lo que necesites');

-- Insertar pedidos usando los IDs de usuarios generados automáticamente
INSERT INTO pedidos (fecha, total, usuario_id) VALUES
('2022-07-15', 500.10, 3),
('2023-08-10', 250.50, 2),
('2023-12-18', 303.13, 1),
('2023-12-23', 407.00, 3);

-- Insertar relaciones pedidos-productos
-- Nota: Los IDs se generarán automáticamente, por lo que necesitamos ajustar estas referencias
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES
(1, 1),  -- pedido 1, producto lapiz
(1, 3),  -- pedido 1, producto clip
(1, 6),  -- pedido 1, producto tijeras
(2, 2),  -- pedido 2, producto libreta
(2, 4),  -- pedido 2, producto boligrafo
(3, 3),  -- pedido 3, producto clip
(4, 3),  -- pedido 4, producto clip
(4, 4),  -- pedido 4, producto boligrafo
(4, 5),  -- pedido 4, producto marcatextos
(4, 6);  -- pedido 4, producto tijeras