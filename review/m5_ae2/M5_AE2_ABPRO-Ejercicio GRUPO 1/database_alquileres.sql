-- 1. CREACIÓN Y USO DE LA BASE DE DATOS
DROP DATABASE IF EXISTS alquiler_autos;
CREATE DATABASE alquiler_autos;
USE alquiler_autos;

-- 2. CREACIÓN DE LAS TABLAS

-- Tabla Clientes: Almacena la información de los clientes.
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion VARCHAR(255)
);

-- Tabla Vehiculos:
CREATE TABLE Vehiculos (
    id_vehiculo INT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    anio INT,
    precio_dia INT(10)
);

-- Tabla Alquileres:
CREATE TABLE Alquileres (
    id_alquiler INT PRIMARY KEY,
    id_cliente INT,
    id_vehiculo INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculos(id_vehiculo)
);

-- Tabla Pagos:
CREATE TABLE Pagos (
    id_pago INT PRIMARY KEY,
    id_alquiler INT,
    monto DECIMAL(10, 2),
    fecha_pago DATE,
    FOREIGN KEY (id_alquiler) REFERENCES Alquileres(id_alquiler)
);

-- 3. INSERCIÓN DE DATOS DE EJEMPLO

-- Insertar datos en la tabla Clientes
INSERT INTO Clientes (id_cliente, nombre, telefono, email, direccion) VALUES
(1, 'Juan Pérez', '555-1234', 'juan@mail.com', 'Calle 123'),
(2, 'Laura Gómez', '555-5678', 'laura@mail.com', 'Calle 456'),
(3, 'Carlos Sánchez', '555-9101', 'carlos@mail.com', 'Calle 789');

-- Insertar datos en la tabla Vehiculos
INSERT INTO Vehiculos (id_vehiculo, marca, modelo, anio, precio_dia) VALUES
(1, 'Toyota', 'Corolla', 2020, 30),
(2, 'Honda', 'Civic', 2019, 28),
(3, 'Ford', 'Focus', 2021, 35);

-- Insertar datos en la tabla Alquileres
INSERT INTO Alquileres (id_alquiler, id_cliente, id_vehiculo, fecha_inicio, fecha_fin) VALUES
(1, 1, 2, '2025-03-10', '2025-03-15'),
(2, 2, 1, '2025-03-12', '2025-03-16'),
(3, 3, 3, '2025-03-20', '2025-03-22');

-- Insertar datos en la tabla Pagos
INSERT INTO Pagos (id_pago, id_alquiler, monto, fecha_pago) VALUES
(1, 1, 150.00, '2025-03-12'),
(2, 2, 112.00, '2025-03-13'),
(3, 3, 70.00, '2025-03-20');
