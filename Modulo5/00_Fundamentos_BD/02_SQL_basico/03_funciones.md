# Funciones MySQL - Módulo 5

## Preparación: Tablas de Ejemplo

Antes de ejecutar los ejemplos, creemos algunas tablas con datos de prueba:

```sql
-- Tabla empleados para ejemplos
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    salario DECIMAL(10,2),
    fecha_contrato DATE,
    departamento VARCHAR(30),
    email VARCHAR(100)
);

INSERT INTO empleados VALUES
(1, 'Juan', 'Pérez', 3500.50, '2022-01-15', 'Ventas', 'juan.perez@empresa.com'),
(2, 'María', 'González', 4200.75, '2021-06-10', 'Marketing', 'maria.gonzalez@empresa.com'),
(3, 'Pedro', 'Rodríguez', 3800.00, '2023-03-22', 'Desarrollo', 'pedro.rodriguez@empresa.com'),
(4, 'Ana', 'López', 3200.25, '2022-11-05', 'Ventas', 'ana.lopez@empresa.com'),
(5, 'Carlos', 'Martín', 4500.00, '2020-09-18', 'Administración', 'carlos.martin@empresa.com');

-- Tabla productos para ejemplos adicionales
CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    precio DECIMAL(8,2),
    stock INT,
    categoria VARCHAR(30)
);

INSERT INTO productos VALUES
(1, 'Laptop HP', 899.99, 15, 'Tecnología'),
(2, 'Mouse Inalámbrico', 25.50, 50, 'Tecnología'),
(3, 'Escritorio Oficina', 250.00, 8, 'Muebles'),
(4, 'Silla Ergonómica', 180.75, 12, 'Muebles'),
(5, 'Monitor 24"', 320.00, 20, 'Tecnología');
```

## 1. Funciones de Manipulación de Cadenas

### CONCAT - Concatenar cadenas

```sql
-- Concatenar nombre y apellido
SELECT 
    id,
    CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM empleados;

-- Concatenar múltiples campos
SELECT 
    id,
    CONCAT(nombre, ' (', departamento, ')') AS empleado_departamento
FROM empleados;
```

### LENGTH - Longitud de cadena

```sql
-- Obtener la longitud del nombre
SELECT 
    nombre,
    LENGTH(nombre) AS longitud_nombre
FROM empleados;

-- Filtrar por longitud de email
SELECT 
    nombre,
    email,
    LENGTH(email) AS longitud_email
FROM empleados
WHERE LENGTH(email) > 25;
```

### SUBSTRING - Extraer subcadena

```sql
-- Extraer las primeras 3 letras del nombre
SELECT 
    nombre,
    SUBSTRING(nombre, 1, 3) AS iniciales_nombre
FROM empleados;

-- Extraer el dominio del email (después del @)
SELECT 
    email,
    SUBSTRING(email, LOCATE('@', email) + 1) AS dominio
FROM empleados;
```

### UPPER - Convertir a mayúsculas

```sql
-- Convertir nombres a mayúsculas
SELECT 
    nombre,
    UPPER(nombre) AS nombre_mayusculas,
    UPPER(departamento) AS departamento_mayusculas
FROM empleados;
```

### LOWER - Convertir a minúsculas

```sql
-- Convertir emails a minúsculas
SELECT 
    nombre,
    email,
    LOWER(email) AS email_minusculas
FROM empleados;
```

## 2. Funciones Numéricas

### SUM - Suma de valores

```sql
-- Suma total de salarios
SELECT SUM(salario) AS total_salarios
FROM empleados;

-- Suma de salarios por departamento
SELECT 
    departamento,
    SUM(salario) AS total_salarios_dept
FROM empleados
GROUP BY departamento;
```

### AVG - Promedio de valores

```sql
-- Promedio de salarios
SELECT AVG(salario) AS promedio_salarios
FROM empleados;

-- Promedio de precios por categoría
SELECT 
    categoria,
    AVG(precio) AS precio_promedio
FROM productos
GROUP BY categoria;
```

### MAX - Valor máximo

```sql
-- Salario máximo
SELECT MAX(salario) AS salario_maximo
FROM empleados;

-- Precio máximo por categoría
SELECT 
    categoria,
    MAX(precio) AS precio_maximo
FROM productos
GROUP BY categoria;
```

### MIN - Valor mínimo

```sql
-- Salario mínimo
SELECT MIN(salario) AS salario_minimo
FROM empleados;

-- Stock mínimo por categoría
SELECT 
    categoria,
    MIN(stock) AS stock_minimo
FROM productos
GROUP BY categoria;
```

### ROUND - Redondear números

```sql
-- Redondear salarios a enteros
SELECT 
    nombre,
    salario,
    ROUND(salario) AS salario_redondeado,
    ROUND(salario, 1) AS salario_un_decimal
FROM empleados;

-- Calcular aumento del 10% redondeado
SELECT 
    nombre,
    salario,
    ROUND(salario * 1.10, 2) AS salario_con_aumento
FROM empleados;
```

## 3. Funciones de Fecha y Hora

### NOW - Fecha y hora actuales

```sql
-- Obtener fecha y hora actual
SELECT NOW() AS fecha_hora_actual;

-- Calcular años trabajados
SELECT 
    nombre,
    fecha_contrato,
    NOW() AS fecha_actual,
    ROUND(DATEDIFF(NOW(), fecha_contrato) / 365, 1) AS años_trabajados
FROM empleados;
```

### CURDATE - Fecha actual

```sql
-- Obtener solo la fecha actual
SELECT CURDATE() AS fecha_actual;

-- Empleados contratados este año
SELECT 
    nombre,
    fecha_contrato
FROM empleados
WHERE YEAR(fecha_contrato) = YEAR(CURDATE());
```

### CURTIME - Hora actual

```sql
-- Obtener solo la hora actual
SELECT CURTIME() AS hora_actual;

-- Crear un registro con timestamp
SELECT 
    'Consulta ejecutada a las:' AS mensaje,
    CURTIME() AS hora_consulta;
```

### DATE_FORMAT - Formatear fechas

```sql
-- Formatear fechas en diferentes formatos
SELECT 
    nombre,
    fecha_contrato,
    DATE_FORMAT(fecha_contrato, '%d/%m/%Y') AS fecha_dd_mm_yyyy,
    DATE_FORMAT(fecha_contrato, '%W, %M %d, %Y') AS fecha_texto_completo,
    DATE_FORMAT(fecha_contrato, '%Y-%m') AS año_mes
FROM empleados;
```

### DAY, MONTH, YEAR - Extraer componentes de fecha

```sql
-- Extraer día, mes y año
SELECT 
    nombre,
    fecha_contrato,
    DAY(fecha_contrato) AS dia,
    MONTH(fecha_contrato) AS mes,
    YEAR(fecha_contrato) AS año
FROM empleados;

-- Empleados contratados en marzo
SELECT 
    nombre,
    fecha_contrato
FROM empleados
WHERE MONTH(fecha_contrato) = 3;
```

## 4. Funciones de Agregación

### COUNT - Contar registros

```sql
-- Contar total de empleados
SELECT COUNT(*) AS total_empleados
FROM empleados;

-- Contar empleados por departamento
SELECT 
    departamento,
    COUNT(*) AS cantidad_empleados
FROM empleados
GROUP BY departamento;

-- Contar empleados con salario mayor a 4000
SELECT COUNT(*) AS empleados_salario_alto
FROM empleados
WHERE salario > 4000;
```

### GROUP_CONCAT - Concatenar valores agrupados

```sql
-- Listar todos los empleados por departamento
SELECT 
    departamento,
    GROUP_CONCAT(nombre ORDER BY nombre SEPARATOR ', ') AS lista_empleados
FROM empleados
GROUP BY departamento;

-- Listar productos por categoría con precios
SELECT 
    categoria,
    GROUP_CONCAT(CONCAT(nombre, ' ($', precio, ')') ORDER BY precio DESC SEPARATOR ' | ') AS productos_precios
FROM productos
GROUP BY categoria;
```

## 5. Funciones de Control de Flujo

### IF - Evaluación condicional

```sql
-- Clasificar salarios como altos o bajos
SELECT 
    nombre,
    salario,
    IF(salario > 4000, 'Alto', 'Bajo') AS clasificacion_salario
FROM empleados;

-- Determinar si hay stock suficiente
SELECT 
    nombre,
    stock,
    IF(stock > 15, 'Stock suficiente', 'Stock bajo') AS estado_stock
FROM productos;
```

### CASE - Evaluaciones múltiples

```sql
-- Clasificar empleados por rango salarial
SELECT 
    nombre,
    salario,
    CASE 
        WHEN salario < 3500 THEN 'Básico'
        WHEN salario BETWEEN 3500 AND 4000 THEN 'Intermedio'
        WHEN salario > 4000 THEN 'Alto'
        ELSE 'No clasificado'
    END AS rango_salarial
FROM empleados;

-- Clasificar productos por precio
SELECT 
    nombre,
    precio,
    CASE 
        WHEN precio < 100 THEN 'Económico'
        WHEN precio BETWEEN 100 AND 300 THEN 'Medio'
        WHEN precio > 300 THEN 'Premium'
    END AS categoria_precio
FROM productos;
```

## 6. Funciones de Conversión de Datos

### CAST - Conversión de tipos

```sql
-- Convertir salario a entero
SELECT 
    nombre,
    salario,
    CAST(salario AS SIGNED) AS salario_entero
FROM empleados;

-- Convertir fecha a cadena
SELECT 
    nombre,
    fecha_contrato,
    CAST(fecha_contrato AS CHAR) AS fecha_texto
FROM empleados;
```

### CONVERT - Conversión con formato

```sql
-- Convertir precio a entero
SELECT 
    nombre,
    precio,
    CONVERT(precio, SIGNED) AS precio_entero
FROM productos;

-- Convertir número a cadena con formato específico
SELECT 
    nombre,
    salario,
    CONVERT(salario, CHAR) AS salario_texto
FROM empleados;
```

## Ejemplos Combinados

### Consulta compleja usando múltiples funciones

```sql
-- Reporte completo de empleados
SELECT 
    CONCAT(UPPER(LEFT(nombre, 1)), LOWER(SUBSTRING(nombre, 2))) AS nombre_formateado,
    CONCAT(apellido, ', ', nombre) AS apellido_nombre,
    CONCAT('$', FORMAT(salario, 2)) AS salario_formateado,
    departamento,
    DATE_FORMAT(fecha_contrato, '%d de %M de %Y') AS fecha_contrato_formateada,
    CASE 
        WHEN DATEDIFF(CURDATE(), fecha_contrato) > 730 THEN 'Veterano'
        WHEN DATEDIFF(CURDATE(), fecha_contrato) > 365 THEN 'Experimentado'
        ELSE 'Nuevo'
    END AS antiguedad,
    IF(salario > AVG(salario) OVER(), 'Arriba del promedio', 'Abajo del promedio') AS comparacion_promedio
FROM empleados
ORDER BY salario DESC;
```

### Resumen estadístico por departamento

```sql
-- Estadísticas completas por departamento
SELECT 
    departamento,
    COUNT(*) AS total_empleados,
    CONCAT('$', FORMAT(MIN(salario), 2)) AS salario_minimo,
    CONCAT('$', FORMAT(MAX(salario), 2)) AS salario_maximo,
    CONCAT('$', FORMAT(AVG(salario), 2)) AS salario_promedio,
    CONCAT('$', FORMAT(SUM(salario), 2)) AS total_nomina,
    GROUP_CONCAT(nombre ORDER BY salario DESC SEPARATOR ', ') AS empleados_ordenados_por_salario
FROM empleados
GROUP BY departamento
ORDER BY AVG(salario) DESC;
```
