-- ===========================================
-- ACTIVIDAD EVALUATIVA 1 - CONSULTAS SQL
-- ===========================================
-- Crear la base de datos si no existe y usarla
CREATE DATABASE IF NOT EXISTS bd_empleados;
USE bd_empleados;

-- Crear la tabla empleados
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    departamento VARCHAR(50),
    salario DECIMAL(10,2)
);

-- Insertar los datos de empleados
INSERT INTO empleados (id, nombre, departamento, salario) VALUES
(1, 'Ana García', 'Recursos Humanos', 32000),
(2, 'Luis Pérez', 'Marketing', 35000),
(3, 'Carlos Díaz', 'Ventas', 27000),
(4, 'María López', 'Contabilidad', 40000),
(5, 'Pedro Martínez', 'Desarrollo', 45000),
(6, 'Julia Fernández', 'Recursos Humanos', 31000),
(7, 'Juan Rodríguez', 'Marketing', 38000),
(8, 'Elena Sánchez', 'Ventas', 26000),
(9, 'David González', 'Contabilidad', 42000),
(10, 'Raquel Pérez', 'Desarrollo', 46000),
(11, 'Fernando García', 'Recursos Humanos', 33000),
(12, 'Isabel Ruiz', 'Marketing', 36000),
(13, 'Sergio Gómez', 'Ventas', 28000),
(14, 'Carmen Romero', 'Contabilidad', 39000),
(15, 'José Torres', 'Desarrollo', 48000);

-- ===========================================
-- CONSULTA 1: Actualizar el salario del empleado con ID=3 a 30000
-- ===========================================
UPDATE empleados SET salario = 30000 WHERE id = 3;

-- Verificar el cambio
SELECT * FROM empleados WHERE id = 3;

-- ===========================================
-- CONSULTA 2: Proyectar todos los empleados que trabajen en el departamento de 'Ventas'
-- ===========================================
SELECT * FROM empleados WHERE departamento = 'Ventas';

-- ===========================================
-- CONSULTA 3: Calcular el salario promedio para cada departamento
-- ===========================================
SELECT departamento, AVG(salario) AS salario_promedio
FROM empleados
GROUP BY departamento;

-- ===========================================
-- CONSULTA 4: Proyectar solo los nombres de todos los departamentos
-- ===========================================
SELECT DISTINCT departamento FROM empleados;

-- ===========================================
-- CONSULTA 5: Proyectar los dos empleados con los salarios más bajos, ordenados de forma ascendente por salario
-- ===========================================
SELECT nombre, salario
FROM empleados
ORDER BY salario ASC
LIMIT 2;

-- ===========================================
-- CONSULTAS ADICIONALES PARA VERIFICACIÓN
-- ===========================================

-- Ver todos los empleados después de la actualización
SELECT * FROM empleados ORDER BY id;

-- Ver resumen por departamento con conteo de empleados
SELECT departamento, COUNT(*) AS num_empleados, AVG(salario) AS salario_promedio
FROM empleados
GROUP BY departamento
ORDER BY salario_promedio DESC;