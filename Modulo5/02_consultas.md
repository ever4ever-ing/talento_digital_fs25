# Consultas SQL - Módulo 5

## 1. Creación de Tablas y Datos de Ejemplo

### Tabla Personas

```sql
-- Crear tabla personas
CREATE TABLE personas (
    id INT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

-- Insertar datos de ejemplo
INSERT INTO personas (id, nombre, edad, ciudad) VALUES
(2, 'Juana', 23, 'Paris'),
(3, 'Pedro', 32, 'Chicago'),
(4, 'Pablo', 21, 'Nueva York'),
(5, 'Patricia', 19, 'Nueva York');
```

### Tabla Empleados

```sql
-- Crear tabla empleados
CREATE TABLE empleados (
    id_empleado INT,
    nombre VARCHAR(50),
    edad INT,
    departamento VARCHAR(50),
    salario DECIMAL(10,2)
);

-- Insertar datos de ejemplo
INSERT INTO empleados (id_empleado, nombre, edad, departamento, salario) VALUES
(100, 'María', 29, 'Desarrollo', 1000.00),
(101, 'Francisco', 31, 'Recursos Humanos', 2500.00),
(102, 'Matías', 25, 'Finanzas', 1500.00),
(103, 'Miyagi', 36, 'Marketing', 2600.00),
(104, 'Andrea', 42, 'Administración', 2000.00);
```

## 2. Consultas SELECT Básicas

### Consulta simple con WHERE

```sql
-- Seleccionar personas mayores de 20 años
SELECT *
FROM personas
WHERE edad > 20;
```

## 3. Consultas con Condiciones Múltiples

### Operador AND

```sql
-- Personas mayores de 18 años que viven en Nueva York
SELECT * 
FROM personas
WHERE edad > 18 AND ciudad = 'Nueva York';
```

### Operador NOT

```sql
-- Personas que NO tienen más de 28 años y viven en Nueva York
SELECT * 
FROM personas
WHERE NOT edad > 28 AND ciudad = 'Nueva York';
```

## 4. Consultas en Tabla Empleados

### Consultas por ID

```sql
-- Buscar empleado específico por ID
SELECT * 
FROM empleados 
WHERE id_empleado = 102;

-- Empleados con ID mayor a 102
SELECT * 
FROM empleados 
WHERE id_empleado > 102;
```

### Consultas por Departamento

```sql
-- Empleados que NO trabajan en Finanzas
SELECT * 
FROM empleados
WHERE NOT departamento = 'Finanzas';
```

### Consultas con LIKE (Patrones de Texto)

```sql
-- Empleados cuyo nombre empieza con 'A'
SELECT * 
FROM empleados 
WHERE nombre LIKE 'A%';

-- Empleados cuyo nombre empieza con 'AN'
SELECT * 
FROM empleados 
WHERE nombre LIKE 'AN%';
```