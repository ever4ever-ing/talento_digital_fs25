INSERT INTO direcciones (id, calle, colonia, ciudad, pais) VALUES
(4, 'Calle 114', 'San José', 'Rancho de Luna','Costa Rica'),
(5, '5 Av. Monsefior Miguel 545', 'Atacama', 'Tierra Amarilla', 'Chile'),
(6, 'Dover 2903', 'Narvarte', 'Monterrey', 'México'),
(7, 'Avenida 77', 'Araucania', 'Temuco', 'Chile');

INSERT INTO usuarios (id, nombre, apellido, direccion_id) VALUES
(1, 'Valeria', 'Romero', 4),
(2, 'Kevin', 'Duque', 5),
(3, 'Alfredo', 'Salazar', 6),
(4, 'Everardo', 'Alvarado', 7);

INSERT INTO productos (id, nombre, descripcion) VALUES
(222, 'lapiz', 'lapiz que te ayudará a escribir ERDs'),
(223, 'libreta', 'para escribir todas tus notas de MySQL'),
(224, 'clip', 'sostiene tus hojas'),
(225, 'boligrafo', 'tus notas no se borraran con nada'),
(226, 'marcatextos', 'para subrayar lo más importante'),
(227, 'tijeras', 'recorta todo lo que necesites');

INSERT INTO pedidos (id, fecha, total, usuario_id) VALUES
(551, '2022-07-15', 500.10, 3),
(552, '2023-08-10', 250.50, 2),
(553, '2023-12-18', 303.13, 1),
(554, '2023-12-23', 407.00, 3);

INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES
(551, 222),
(551, 224),
(551, 227),
(552, 223),
(552, 225),
(553, 224),
(554, 224),
(554, 225),
(554, 226),
(554, 227);