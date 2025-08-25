# Sistema de Alquiler de Vehículos

Este documento contiene la estructura de base de datos y consultas SQL para un sistema de alquiler de vehículos desarrollado en MySQL.

---

## 1. Definición de Tablas

```sql
-- Tabla Clientes
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion VARCHAR(200)
);
```

```sql
-- Tabla Vehículos
CREATE TABLE Vehiculos (
    id_vehiculo INT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    año INT,
    precio_dia DECIMAL(10,2) NOT NULL
);
```

```sql
-- Tabla Alquileres
CREATE TABLE Alquileres (
    id_alquiler INT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_vehiculo INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculos(id_vehiculo)
);
```

```sql
-- Tabla Pagos
CREATE TABLE Pagos (
    id_pago INT PRIMARY KEY,
    id_alquiler INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATE NOT NULL,
    FOREIGN KEY (id_alquiler) REFERENCES Alquileres(id_alquiler)
);
```

---

## 2. Inserción de Datos

```sql
-- Insertar datos de ejemplo en Clientes
INSERT INTO Clientes (id_cliente, nombre, telefono, email, direccion) VALUES
(1, 'Juan Pérez', '555-1234', 'juan@mail.com', 'Calle 123'),
(2, 'Laura Gómez', '555-5678', 'laura@mail.com', 'Calle 456'),
(3, 'Carlos Sánchez', '555-9101', 'carlos@mail.com', 'Calle 789');
```

```sql
-- Insertar datos de ejemplo en Vehículos
INSERT INTO Vehiculos (id_vehiculo, marca, modelo, año, precio_dia) VALUES
(1, 'Toyota', 'Corolla', 2020, 30.00),
(2, 'Honda', 'Civic', 2019, 28.00),
(3, 'Ford', 'Focus', 2021, 35.00);
```

```sql
-- Insertar datos de ejemplo en Alquileres
INSERT INTO Alquileres (id_alquiler, id_cliente, id_vehiculo, fecha_inicio, fecha_fin) VALUES
(1, 2, 2, '2025-03-10', '2025-03-15'),
(2, 2, 1, '2025-03-12', '2025-03-16'),
(3, 3, 3, '2025-03-20', '2025-03-22');
```

```sql
-- Insertar datos de ejemplo en Pagos
INSERT INTO Pagos (id_pago, id_alquiler, monto, fecha_pago) VALUES
(1, 1, 150.00, '2025-03-12'),
(2, 2, 112.00, '2025-03-13'),
(3, 3, 70.00, '2025-03-20');
```

---

## 3. Consultas SQL

### Consulta 1: Clientes con alquiler activo

**Propósito:** Encontrar clientes que tienen un alquiler activo en la fecha actual.

**Explicación técnica:**
- `CURDATE()`: Función de MySQL que devuelve la fecha actual
- `BETWEEN`: Verifica si la fecha actual está dentro del rango de fechas del alquiler
- `INNER JOIN`: Solo muestra clientes que SÍ tienen alquileres

**Resultado esperado:** Clientes cuyo período de alquiler incluye la fecha de hoy.

```sql
-- Mostrar nombre, telefono y email de clientes con alquiler activo (MySQL)
SELECT c.nombre, c.telefono, c.email
FROM Clientes c
INNER JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE CURDATE() BETWEEN a.fecha_inicio AND a.fecha_fin;

-- Alternativa con fecha específica para pruebas:
-- WHERE '2025-03-14' BETWEEN a.fecha_inicio AND a.fecha_fin;
```

### Consulta 2: Vehículos alquilados en marzo 2025

**Propósito:** Mostrar información de vehículos que fueron alquilados específicamente en marzo de 2025.

**Explicación técnica:**
- `SELECT DISTINCT`: Elimina duplicados, cada vehículo aparece solo una vez aunque haya sido alquilado múltiples veces
- `YEAR()` y `MONTH()`: Funciones de MySQL para extraer año y mes de una fecha
- `INNER JOIN`: Solo incluye vehículos que SÍ tienen alquileres

**Resultado esperado:** Lista única de vehículos con sus detalles que tuvieron alquileres iniciados en marzo 2025.

```sql
-- Mostrar modelo, marca y precio_dia de vehículos alquilados en marzo 2025 (MySQL)
SELECT DISTINCT v.modelo, v.marca, v.precio_dia
FROM Vehiculos v
INNER JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE YEAR(a.fecha_inicio) = 2025 AND MONTH(a.fecha_inicio) = 3;

-- Alternativa usando DATE_FORMAT (más eficiente en MySQL):
-- WHERE DATE_FORMAT(a.fecha_inicio, '%Y-%m') = '2025-03';
```

### Consulta 3: Precio total del alquiler por cliente

**Propósito:** Calcular el costo total que cada cliente debe pagar por todos sus alquileres.

**Explicación técnica:**
- `DATEDIFF()`: Calcula días entre fecha_fin y fecha_inicio
- `+ 1`: Se suma 1 porque ambas fechas (inicio y fin) se incluyen en el alquiler
- `SUM()`: Suma todos los costos de alquileres por cliente
- `GROUP BY`: Agrupa resultados por cliente para obtener totales individuales

**Fórmula:** `precio_dia × (días_alquiler) = costo_por_alquiler`

**Resultado esperado:** Cada cliente con su costo total acumulado de todos sus alquileres.

```sql
-- Calcular precio total considerando días de alquiler y precio por día (MySQL)
SELECT c.nombre, 
       SUM(v.precio_dia * (DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1)) AS precio_total
FROM Clientes c
INNER JOIN Alquileres a ON c.id_cliente = a.id_cliente
INNER JOIN Vehiculos v ON a.id_vehiculo = v.id_vehiculo
GROUP BY c.id_cliente, c.nombre;

-- Nota: En MySQL, DATEDIFF() calcula la diferencia en días
-- Se suma 1 para incluir ambas fechas (inicio y fin)
```

### Consulta 4: Clientes sin pagos

**Propósito:** Identificar clientes que tienen alquileres pero no han realizado ningún pago.

**Explicación técnica:**
- `LEFT JOIN`: Incluye todos los clientes, aunque no tengan alquileres o pagos
- `IS NULL`: Filtra registros donde no existe pago asociado
- Útil para identificar deudores o pagos pendientes

**Resultado esperado:** Clientes con alquileres registrados pero sin pagos en el sistema.

```sql
-- Encontrar clientes que no han realizado ningún pago
SELECT c.nombre, c.email
FROM Clientes c
LEFT JOIN Alquileres a ON c.id_cliente = a.id_cliente
LEFT JOIN Pagos p ON a.id_alquiler = p.id_alquiler
WHERE p.id_pago IS NULL;
```

### Consulta 5: Promedio de pagos por cliente

**Propósito:** Calcular el promedio de los montos pagados por cada cliente.

**Explicación técnica:**
- `AVG()`: Función agregada que calcula el promedio de valores numéricos
- `INNER JOIN`: Solo incluye clientes que tienen alquileres Y pagos
- `GROUP BY`: Agrupa por cliente para calcular promedio individual

**Resultado esperado:** Cada cliente con el promedio de sus pagos realizados.

```sql
-- Calcular promedio de pagos realizados por cada cliente
SELECT c.nombre, AVG(p.monto) AS promedio_pago
FROM Clientes c
INNER JOIN Alquileres a ON c.id_cliente = a.id_cliente
INNER JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.id_cliente, c.nombre;
```

### Consulta 6: Vehículos disponibles en fecha específica (2025-03-18)

**Propósito:** Encontrar vehículos que están disponibles (no alquilados) en una fecha específica.

**Explicación técnica:**
- `NOT IN`: Excluye vehículos que aparecen en la subconsulta
- `BETWEEN`: Verifica si la fecha específica está dentro del rango de alquiler
- Subconsulta: Obtiene los ID de vehículos ocupados en esa fecha

**Resultado esperado:** Vehículos libres para alquilar en la fecha consultada.

```sql
-- Mostrar vehículos que NO están ocupados en la fecha específica
SELECT v.modelo, v.marca, v.precio_dia
FROM Vehiculos v
WHERE v.id_vehiculo NOT IN (
    SELECT a.id_vehiculo
    FROM Alquileres a
    WHERE '2025-03-18' BETWEEN a.fecha_inicio AND a.fecha_fin
);
```

### Consulta 7: Vehículos alquilados más de una vez en marzo 2025

**Propósito:** Identificar vehículos populares que fueron alquilados múltiples veces en marzo 2025.

**Explicación técnica:**
- `GROUP BY`: Agrupa por vehículo para contar alquileres individuales
- `HAVING`: Filtra grupos que cumplen condiciones (después del GROUP BY)
- `COUNT()`: Cuenta el número de alquileres por vehículo
- `> 1`: Solo muestra vehículos con más de un alquiler

**Resultado esperado:** Marca y modelo de vehículos con alta demanda en marzo 2025.

```sql
-- Encontrar marca y modelo de vehículos con más de un alquiler en marzo 2025
SELECT v.marca, v.modelo
FROM Vehiculos v
INNER JOIN Alquileres a ON v.id_vehiculo = a.id_vehiculo
WHERE YEAR(a.fecha_inicio) = 2025 AND MONTH(a.fecha_inicio) = 3
GROUP BY v.id_vehiculo, v.marca, v.modelo
HAVING COUNT(a.id_alquiler) > 1;
```

### Consulta 8: Total de monto pagado por cliente

**Propósito:** Calcular la suma total de dinero que cada cliente ha pagado efectivamente.

**Explicación técnica:**
- `SUM()`: Suma todos los montos de pagos realizados por cada cliente
- `INNER JOIN`: Solo incluye clientes que tienen alquileres Y pagos registrados
- `GROUP BY`: Agrupa por cliente para obtener el total individual

**Resultado esperado:** Cada cliente con el total real pagado (no el costo teórico).

```sql
-- Mostrar nombre del cliente y suma total de sus pagos
SELECT c.nombre, SUM(p.monto) AS total_pagado
FROM Clientes c
INNER JOIN Alquileres a ON c.id_cliente = a.id_cliente
INNER JOIN Pagos p ON a.id_alquiler = p.id_alquiler
GROUP BY c.id_cliente, c.nombre;
```

### Consulta 9: Clientes que alquilaron Ford Focus (id_vehiculo = 3)

**Propósito:** Encontrar qué clientes alquilaron un vehículo específico (Ford Focus).

**Explicación técnica:**
- `WHERE a.id_vehiculo = 3`: Filtra solo alquileres del vehículo con ID 3 (Ford Focus)
- `INNER JOIN`: Relaciona clientes con sus alquileres
- `AS fecha_alquiler`: Alias para hacer más clara la columna de fecha

**Resultado esperado:** Nombres de clientes y fechas cuando alquilaron el Ford Focus.

```sql
-- Mostrar nombre del cliente y fecha del alquiler para Ford Focus
SELECT c.nombre, a.fecha_inicio AS fecha_alquiler
FROM Clientes c
INNER JOIN Alquileres a ON c.id_cliente = a.id_cliente
WHERE a.id_vehiculo = 3;
```

### Consulta 10: Total de días alquilados por cliente (ordenado)

**Propósito:** Calcular cuántos días en total cada cliente ha alquilado vehículos, ordenado de mayor a menor.

**Explicación técnica:**
- `DATEDIFF() + 1`: Calcula días de alquiler incluyendo fecha de inicio y fin
- `SUM()`: Suma todos los días de alquileres múltiples por cliente
- `GROUP BY`: Agrupa por cliente para obtener totales individuales
- `ORDER BY... DESC`: Ordena de mayor a menor número de días

**Resultado esperado:** Ranking de clientes por días totales alquilados, mostrando los más frecuentes primero.

```sql
-- Mostrar nombre del cliente y total de días alquilados, ordenado desc
SELECT c.nombre, 
       SUM(DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1) AS total_dias_alquilados
FROM Clientes c
INNER JOIN Alquileres a ON c.id_cliente = a.id_cliente
GROUP BY c.id_cliente, c.nombre
ORDER BY total_dias_alquilados DESC;
```

---

## 4. Consultas Adicionales para Verificación

### Verificar datos actuales en las tablas

**Propósito:** Crear un resumen rápido que muestra cuántos registros hay en cada tabla del sistema.

**Explicación técnica:**
- `UNION ALL`: Combina los resultados de múltiples consultas SELECT
- `ALL`: Mantiene todos los registros, incluso duplicados (más eficiente que UNION simple)
- Cada SELECT debe tener el mismo número de columnas y tipos compatibles
- `COUNT(*)`: Cuenta todos los registros en cada tabla
- `AS tabla`: Crea una columna literal identificando el nombre de cada tabla

**Resultado esperado:** Una tabla que muestra el nombre de cada tabla y su total de registros.

```sql
-- Verificar datos actuales en las tablas
SELECT 'CLIENTES' AS tabla, COUNT(*) AS total_registros FROM Clientes
UNION ALL
SELECT 'VEHICULOS' AS tabla, COUNT(*) AS total_registros FROM Vehiculos
UNION ALL
SELECT 'ALQUILERES' AS tabla, COUNT(*) AS total_registros FROM Alquileres
UNION ALL
SELECT 'PAGOS' AS tabla, COUNT(*) AS total_registros FROM Pagos;
```

### Ver todos los datos

**Propósito:** Consultas básicas para mostrar todos los registros de cada tabla.

**Explicación técnica:**
- `SELECT *`: Selecciona todas las columnas de la tabla
- Útil para verificar el contenido completo de cada tabla
- Recomendado para tablas pequeñas durante desarrollo y testing

```sql
SELECT * FROM Clientes;
SELECT * FROM Vehiculos;
SELECT * FROM Alquileres;
SELECT * FROM Pagos;
```

### Consulta útil: Ver relaciones completas

**Propósito:** Crear un reporte completo que muestra toda la información relevante de cada alquiler.

**Explicación técnica:**
- `DATEDIFF()`: Calcula la diferencia en días entre fecha_fin y fecha_inicio
- `+ 1`: Se suma 1 porque si alquilas del 10 al 12, son 3 días (10, 11, 12), no 2
- `LEFT JOIN Pagos`: Incluye alquileres aunque no tengan pagos asociados
- `ORDER BY`: Ordena por cliente y luego por fecha de inicio
- Cálculo de costo total: `precio_dia × días_alquiler`

**Ejemplo:** Del 2025-03-10 al 2025-03-15 = 5 días + 1 = 6 días

**Resultado esperado:** Reporte detallado mostrando cliente, vehículo, fechas, cálculos de costo y pagos realizados.

```sql
SELECT 
    c.nombre AS cliente,
    v.marca,
    v.modelo,
    a.fecha_inicio,
    a.fecha_fin,
    DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1 AS dias_alquiler,
    v.precio_dia,
    (v.precio_dia * (DATEDIFF(a.fecha_fin, a.fecha_inicio) + 1)) AS costo_total,
    p.monto AS monto_pagado,
    p.fecha_pago
FROM Clientes c
INNER JOIN Alquileres a ON c.id_cliente = a.id_cliente
INNER JOIN Vehiculos v ON a.id_vehiculo = v.id_vehiculo
LEFT JOIN Pagos p ON a.id_alquiler = p.id_alquiler
ORDER BY c.nombre, a.fecha_inicio;
```