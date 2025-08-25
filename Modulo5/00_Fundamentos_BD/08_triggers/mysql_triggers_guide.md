# Guía Completa de Triggers en MySQL

## ¿Qué son los Triggers?

Los **triggers** (disparadores) son procedimientos almacenados especiales que se ejecutan automáticamente en respuesta a eventos específicos en una tabla o vista de base de datos. Son como "funciones reactivas" que responden a cambios en los datos sin necesidad de ser llamados explícitamente.

### Características principales:
- Se ejecutan automáticamente cuando ocurre un evento específico
- No pueden ser invocados directamente
- Forman parte de la transacción que los activa
- Pueden prevenir operaciones mediante errores

## Tipos de Triggers

### Por momento de ejecución:
- **BEFORE**: Se ejecuta antes del evento
- **AFTER**: Se ejecuta después del evento

### Por evento:
- **INSERT**: Al insertar nuevos registros
- **UPDATE**: Al actualizar registros existentes
- **DELETE**: Al eliminar registros

## Sintaxis Básica

```sql
CREATE TRIGGER nombre_trigger
    {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
    ON nombre_tabla
    FOR EACH ROW
BEGIN
    -- Código del trigger
END;
```

## Ejemplos Prácticos con Nuestra Base de Datos

### 1. Trigger de Auditoría - Registro de Cambios en Usuarios

**PROPÓSITO**: Este trigger implementa un sistema de auditoría que registra automáticamente todos los cambios realizados en la tabla `usuarios`.

**FUNCIONALIDAD EXPLICADA**:

Primero creamos una tabla para auditoría:

```sql
CREATE TABLE auditoria_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- ID único del registro de auditoría
    usuario_id INT,                            -- ID del usuario que fue modificado
    accion VARCHAR(20),                        -- Tipo de operación (INSERT, UPDATE, DELETE)
    nombre_anterior VARCHAR(45),               -- Valor anterior del nombre
    apellido_anterior VARCHAR(45),             -- Valor anterior del apellido
    nombre_nuevo VARCHAR(45),                  -- Valor nuevo del nombre
    apellido_nuevo VARCHAR(45),                -- Valor nuevo del apellido
    fecha_cambio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Momento exacto del cambio
    usuario_sistema VARCHAR(50)               -- Usuario de MySQL que realizó el cambio
);
```

**TRIGGER EXPLICADO PASO A PASO**:

```sql
DELIMITER $$
CREATE TRIGGER tr_auditoria_usuarios_update
    AFTER UPDATE ON usuarios              -- Se activa DESPUÉS de una actualización
    FOR EACH ROW                          -- Se ejecuta para cada fila modificada
BEGIN
    INSERT INTO auditoria_usuarios (
        usuario_id, accion, nombre_anterior, apellido_anterior,
        nombre_nuevo, apellido_nuevo, usuario_sistema
    ) VALUES (
        NEW.id,        -- ID del usuario (después del cambio)
        'UPDATE',      -- Tipo de operación
        OLD.nombre,    -- Nombre ANTES del cambio
        OLD.apellido,  -- Apellido ANTES del cambio
        NEW.nombre,    -- Nombre DESPUÉS del cambio
        NEW.apellido,  -- Apellido DESPUÉS del cambio
        USER()         -- Usuario de MySQL que ejecutó la operación
    );
END$$
DELIMITER ;
```

Dato: DELIMITER es un comando específico de MySQL que cambia el delimitador de sentencias temporalmente. Por defecto, MySQL usa el punto y coma (;) para indicar el final de una sentencia SQL.

**¿CÓMO FUNCIONA?**:
- **`OLD`**: Contiene los valores de la fila antes de la modificación
- **`NEW`**: Contiene los valores de la fila después de la modificación
- **`USER()`**: Función que devuelve el nombre del usuario de MySQL actual
- **`AFTER UPDATE`**: Se ejecuta después de que el cambio ya se ha realizado

**CASOS DE USO**:
- Cumplimiento normativo (GDPR, SOX, etc.)
- Investigación de cambios no autorizados
- Recuperación de datos en caso de errores
- Análisis de patrones de uso

### 2. Trigger de Validación - Control de Totales en Pedidos

**PROPÓSITO**: Este trigger actúa como un "guardián" que valida los datos antes de que se inserten en la tabla `pedidos`, asegurando que cumplan con las reglas de negocio.

**FUNCIONALIDAD EXPLICADA PASO A PASO**:

```sql
DELIMITER $$
CREATE TRIGGER tr_validar_total_pedido
    BEFORE INSERT ON pedidos              -- Se activa ANTES de insertar
    FOR EACH ROW                          -- Para cada fila que se intenta insertar
BEGIN
    -- VALIDACIÓN 1: Total debe ser positivo
    IF NEW.total <= 0 THEN
        SIGNAL SQLSTATE '45000'           -- Lanza un error personalizado
        SET MESSAGE_TEXT = 'El total del pedido debe ser mayor a cero';
    END IF;
    
    -- VALIDACIÓN 2: Fecha no puede ser futura
    IF NEW.fecha > CURDATE() THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La fecha del pedido no puede ser futura';
    END IF;
END$$
DELIMITER ;
```

**¿CÓMO FUNCIONA?**:
- **`BEFORE INSERT`**: Se ejecuta antes de que los datos se guarden en la tabla
- **`NEW.campo`**: Accede a los valores que se van a insertar
- **`SIGNAL SQLSTATE '45000'`**: Es la forma de lanzar errores personalizados en MySQL
- **`CURDATE()`**: Función que devuelve la fecha actual

**¿QUÉ PASA SI FALLA?**:
- Si alguna validación falla, la operación INSERT se cancela completamente
- Se devuelve un mensaje de error claro al cliente
- No se inserta ningún dato en la tabla

**EJEMPLO DE USO**:
```sql
-- ESTO FUNCIONARÁ:
INSERT INTO pedidos (fecha, total, usuario_id) VALUES ('2024-08-24', 150.00, 1);

-- ESTO FALLARÁ (total negativo):
INSERT INTO pedidos (fecha, total, usuario_id) VALUES ('2024-08-24', -50.00, 1);

-- ESTO FALLARÁ (fecha futura):
INSERT INTO pedidos (fecha, total, usuario_id) VALUES ('2026-01-01', 100.00, 1);
```

**VENTAJAS**:
- Centraliza las reglas de negocio en la base de datos
- Garantiza integridad independientemente de la aplicación
- Previene datos inconsistentes desde el origen

### 3. Trigger Automático - Actualizar Códigos de Pedido

**PROPÓSITO**: Este trigger automatiza la generación de códigos únicos y legibles para cada pedido, eliminando la necesidad de que la aplicación genere estos códigos manualmente.

**PREPARACIÓN**: Primero agregamos una columna para almacenar el código:

```sql
-- Agregar columna para código automático
ALTER TABLE pedidos ADD COLUMN codigo_pedido VARCHAR(20);
```

**FUNCIONALIDAD EXPLICADA PASO A PASO**:

```sql
DELIMITER $$
CREATE TRIGGER tr_generar_codigo_pedido
    BEFORE INSERT ON pedidos              -- Se ejecuta ANTES de insertar
    FOR EACH ROW                          -- Para cada nuevo pedido
BEGIN
    -- Genera un código automático con el formato: PED-YYYY-NNNNNN
    SET NEW.codigo_pedido = CONCAT(
        'PED-',                           -- Prefijo identificatorio
        YEAR(NEW.fecha),                  -- Año del pedido
        '-',                              -- Separador
        LPAD(NEW.id, 6, '0')             -- ID del pedido con ceros a la izquierda
    );
END$$
DELIMITER ;
```

**¿CÓMO FUNCIONA?**:
- **`CONCAT()`**: Concatena múltiples cadenas de texto
- **`YEAR(NEW.fecha)`**: Extrae el año de la fecha del pedido
- **`LPAD(NEW.id, 6, '0')`**: Rellena el ID con ceros a la izquierda hasta 6 dígitos
- **`SET NEW.campo`**: Modifica el valor que se va a insertar

**EJEMPLOS DE CÓDIGOS GENERADOS**:
```sql
-- Si el pedido tiene ID 123 y fecha '2024-08-24'
-- Resultado: PED-2024-000123

-- Si el pedido tiene ID 45678 y fecha '2024-12-31'
-- Resultado: PED-2024-045678

-- Si el pedido tiene ID 1000000 y fecha '2025-01-15'
-- Resultado: PED-2025-1000000
```

**VENTAJAS**:
- Códigos únicos y legibles para humanos
- Incluye información temporal útil
- Generación automática sin intervención manual
- Formato consistente en toda la base de datos

**CASOS DE USO**:
- Referencias para clientes (más fácil que recordar un ID numérico)
- Reportes y facturas
- Seguimiento de pedidos
- Integración con sistemas externos

### 4. Trigger de Conteo - Mantener Estadísticas

**PROPÓSITO**: Este trigger mantiene automáticamente estadísticas de ventas por producto, actualizando contadores cada vez que un producto se agrega a un pedido.

**PREPARACIÓN**: Crear tabla de estadísticas:

```sql
CREATE TABLE estadisticas_productos (
    producto_id INT PRIMARY KEY,          -- ID del producto (clave primaria)
    veces_pedido INT DEFAULT 0,           -- Contador de veces que se ha pedido
    ultima_vez_pedido DATE,               -- Fecha de la última vez que se pidió
    FOREIGN KEY (producto_id) REFERENCES productos(id)  -- Relación con productos
);
```

**FUNCIONALIDAD EXPLICADA PASO A PASO**:

```sql
DELIMITER $$
CREATE TRIGGER tr_actualizar_estadisticas_producto
    AFTER INSERT ON pedidos_has_productos    -- Se activa cuando se agrega un producto a un pedido
    FOR EACH ROW                             -- Para cada producto agregado
BEGIN
    -- PASO 1: Obtener la fecha del pedido
    DECLARE fecha_pedido DATE;               -- Variable local para almacenar la fecha
    SELECT fecha INTO fecha_pedido           -- Consulta la fecha del pedido
    FROM pedidos 
    WHERE id = NEW.pedido_id;               -- Usando el ID del pedido recién insertado
    
    -- PASO 2: Actualizar o insertar estadísticas
    INSERT INTO estadisticas_productos (
        producto_id, 
        veces_pedido, 
        ultima_vez_pedido
    ) VALUES (
        NEW.producto_id,                     -- ID del producto
        1,                                   -- Primera vez (si no existe el registro)
        fecha_pedido                         -- Fecha del pedido
    )
    ON DUPLICATE KEY UPDATE                  -- Si ya existe un registro para este producto:
        veces_pedido = veces_pedido + 1,     -- Incrementa el contador en 1
        ultima_vez_pedido = fecha_pedido;    -- Actualiza la fecha más reciente
END$$
DELIMITER ;
```

**¿CÓMO FUNCIONA?**:
- **`DECLARE`**: Declara una variable local dentro del trigger
- **`SELECT ... INTO`**: Asigna el resultado de una consulta a una variable
- **`INSERT ... ON DUPLICATE KEY UPDATE`**: Intenta insertar, pero si ya existe (por la PRIMARY KEY), ejecuta el UPDATE
- **`NEW.campo`**: Accede a los datos que acabamos de insertar

**EJEMPLO PRÁCTICO**:
```sql
-- Estado inicial: tabla estadisticas_productos vacía

-- Se ejecuta: INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES (100, 222);
-- Resultado: Se crea registro (producto_id=222, veces_pedido=1, ultima_vez_pedido='2024-08-24')

-- Se ejecuta otra vez: INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES (101, 222);
-- Resultado: Se actualiza (producto_id=222, veces_pedido=2, ultima_vez_pedido='2024-08-24')
```

**VENTAJAS**:
- Estadísticas en tiempo real sin consultas complejas
- No requiere procesos batch nocturnos
- Datos siempre actualizados
- Base para reportes de productos más vendidos

**CASOS DE USO**:
- Dashboard de ventas en tiempo real
- Reportes de productos más populares
- Análisis de tendencias de consumo
- Gestión de inventario basada en demanda

### 5. Trigger de Eliminación en Cascada Personalizada

**PROPÓSITO**: Este trigger implementa una eliminación en cascada personalizada que registra la acción en auditoría antes de eliminar registros relacionados.

**⚠️ ADVERTENCIA**: Este tipo de trigger modifica múltiples tablas y debe usarse con extrema precaución.

**FUNCIONALIDAD EXPLICADA PASO A PASO**:

```sql
DELIMITER $$
CREATE TRIGGER tr_eliminar_usuario_cascada
    AFTER DELETE ON usuarios                -- Se activa DESPUÉS de eliminar un usuario
    FOR EACH ROW                             -- Para cada usuario eliminado
BEGIN
    -- PASO 1: Registrar la eliminación en auditoría
    INSERT INTO auditoria_usuarios (
        usuario_id, 
        accion, 
        nombre_anterior, 
        apellido_anterior
    ) VALUES (
        OLD.id,                              -- ID del usuario eliminado
        'DELETE',                            -- Tipo de operación
        OLD.nombre,                          -- Nombre del usuario eliminado
        OLD.apellido                         -- Apellido del usuario eliminado
    );
    
    -- PASO 2: Eliminar relaciones en tabla intermedia
    DELETE FROM pedidos_has_productos        -- Elimina productos de todos los pedidos del usuario
    WHERE pedido_id IN (                     -- Subconsulta para obtener IDs de pedidos
        SELECT id FROM pedidos 
        WHERE usuario_id = OLD.id
    );
    
    -- PASO 3: Eliminar pedidos del usuario
    DELETE FROM pedidos                      -- Elimina todos los pedidos del usuario
    WHERE usuario_id = OLD.id;
END$$
DELIMITER ;
```

**¿CÓMO FUNCIONA?**:
- **`AFTER DELETE`**: Se ejecuta después de que el usuario ya fue eliminado
- **`OLD.campo`**: Accede a los datos del registro eliminado
- **Subconsulta**: `WHERE pedido_id IN (SELECT ...)` elimina múltiples registros relacionados
- **Orden de eliminación**: Primero auditoría, luego relaciones, después pedidos

**SECUENCIA DE EVENTOS**:
```sql
-- 1. Se ejecuta: DELETE FROM usuarios WHERE id = 5;
-- 2. El usuario se elimina de la tabla usuarios
-- 3. El trigger se activa automáticamente y:
--    a) Registra la eliminación en auditoria_usuarios
--    b) Elimina todos los registros de pedidos_has_productos relacionados
--    c) Elimina todos los pedidos del usuario
```

**VENTAJAS**:
- Mantiene integridad referencial personalizada
- Registra eliminaciones para auditoría
- Limpia automáticamente registros huérfanos
- Control total sobre el proceso de eliminación

**DESVENTAJAS Y RIESGOS**:
- Puede eliminar grandes cantidades de datos sin advertencia
- Dificulta la recuperación de información
- Puede afectar el rendimiento en eliminaciones masivas
- Debugging complejo si algo sale mal

**ALTERNATIVAS MÁS SEGURAS**:
```sql
-- En lugar de eliminar, marcar como inactivo:
ALTER TABLE usuarios ADD COLUMN activo BOOLEAN DEFAULT TRUE;

-- Trigger más seguro que solo marca como inactivo:
DELIMITER $$
CREATE TRIGGER tr_desactivar_usuario
    BEFORE DELETE ON usuarios
    FOR EACH ROW
BEGIN
    -- Prevenir eliminación y marcar como inactivo
    INSERT INTO usuarios_inactivos (id, nombre, apellido, fecha_desactivacion)
    VALUES (OLD.id, OLD.nombre, OLD.apellido, NOW());
    
    SIGNAL SQLSTATE '45000' 
    SET MESSAGE_TEXT = 'Usuario marcado como inactivo en lugar de eliminado';
END$$
DELIMITER ;
```

## Casos de Uso Avanzados

### 1. Trigger para Normalización Automática de Datos

**PROPÓSITO**: Este trigger aplica automáticamente reglas de formato y normalización a los datos antes de que se guarden, asegurando consistencia en el formato de texto.

**FUNCIONALIDAD EXPLICADA PASO A PASO**:

```sql
DELIMITER $$
CREATE TRIGGER tr_normalizar_direcciones
    BEFORE INSERT ON direcciones            -- Se ejecuta ANTES de insertar
    FOR EACH ROW                             -- Para cada dirección nueva
BEGIN
    -- NORMALIZACIÓN 1: Capitalizar primera letra de calle
    SET NEW.calle = CONCAT(
        UPPER(SUBSTRING(NEW.calle, 1, 1)),   -- Primera letra en mayúscula
        LOWER(SUBSTRING(NEW.calle, 2))       -- Resto en minúscula
    );
    
    -- NORMALIZACIÓN 2: Capitalizar primera letra de colonia
    SET NEW.colonia = CONCAT(
        UPPER(SUBSTRING(NEW.colonia, 1, 1)), 
        LOWER(SUBSTRING(NEW.colonia, 2))
    );
    
    -- NORMALIZACIÓN 3: Capitalizar primera letra de ciudad
    SET NEW.ciudad = CONCAT(
        UPPER(SUBSTRING(NEW.ciudad, 1, 1)), 
        LOWER(SUBSTRING(NEW.ciudad, 2))
    );
    
    -- NORMALIZACIÓN 4: País siempre en mayúsculas
    SET NEW.pais = UPPER(NEW.pais);
END$$
DELIMITER ;
```

**¿CÓMO FUNCIONA?**:
- **`SUBSTRING(texto, posicion, longitud)`**: Extrae parte de una cadena
- **`UPPER()` y `LOWER()`**: Convierten texto a mayúsculas/minúsculas
- **`CONCAT()`**: Une múltiples cadenas de texto
- **`SET NEW.campo`**: Modifica el valor antes de guardarlo

**EJEMPLOS DE TRANSFORMACIÓN**:
```sql
-- ENTRADA: ('AV siempre viva 123', 'LAS FLORES', 'ciudad de méxico', 'mexico')
-- SALIDA:  ('Av siempre viva 123', 'Las flores', 'Ciudad de méxico', 'MEXICO')

-- ENTRADA: ('CALLE PRINCIPAL', 'centro', 'GUADALAJARA', 'mx')
-- SALIDA:  ('Calle principal', 'Centro', 'Guadalajara', 'MX')
```

**VENTAJAS**:
- Consistencia automática en formato de datos
- Reduce errores humanos de captura
- Facilita búsquedas y comparaciones
- Mejora la presentación de datos

**CASOS DE USO**:
- Sistemas de CRM y facturación
- Bases de datos de contactos
- Aplicaciones de delivery
- Sistemas gubernamentales

### 2. Trigger de Historial de Precios

**PROPÓSITO**: Este trigger mantiene automáticamente un historial completo de todos los cambios de precio de los productos, creando un registro auditorio valioso para análisis de negocio.

**PREPARACIÓN**: Agregar columna de precio y crear tabla de historial:

```sql
-- Tabla para historial de precios (agregar precio a productos)
ALTER TABLE productos ADD COLUMN precio DECIMAL(10,2) DEFAULT 0;

CREATE TABLE historial_precios (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- ID único del registro histórico
    producto_id INT,                        -- ID del producto que cambió de precio
    precio_anterior DECIMAL(10,2),          -- Precio antes del cambio
    precio_nuevo DECIMAL(10,2),             -- Precio después del cambio
    fecha_cambio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Momento exacto del cambio
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);
```

**FUNCIONALIDAD EXPLICADA PASO A PASO**:

```sql
DELIMITER $$
CREATE TRIGGER tr_historial_precios
    AFTER UPDATE ON productos               -- Se activa DESPUÉS de actualizar un producto
    FOR EACH ROW                             -- Para cada producto modificado
BEGIN
    -- Solo actuar si el precio realmente cambió
    IF OLD.precio != NEW.precio THEN        -- Compara precio anterior vs nuevo
        INSERT INTO historial_precios (
            producto_id, 
            precio_anterior, 
            precio_nuevo
        ) VALUES (
            NEW.id,                          -- ID del producto
            OLD.precio,                      -- Precio antes del cambio
            NEW.precio                       -- Precio después del cambio
        );
    END IF;
END$$
DELIMITER ;
```

**¿CÓMO FUNCIONA?**:
- **`AFTER UPDATE`**: Se ejecuta después de que el cambio ya se aplicó
- **`IF OLD.precio != NEW.precio`**: Solo actúa si hubo un cambio real en el precio
- **`OLD.precio`**: Valor del precio antes de la actualización
- **`NEW.precio`**: Valor del precio después de la actualización
- **Timestamp automático**: La fecha se registra automáticamente

**EJEMPLO PRÁCTICO**:
```sql
-- Situación inicial:
-- productos: (id=1, nombre='Laptop', precio=1000.00)
-- historial_precios: (vacío)

-- Se ejecuta: UPDATE productos SET precio = 1200.00 WHERE id = 1;
-- Resultado en historial_precios:
-- (producto_id=1, precio_anterior=1000.00, precio_nuevo=1200.00, fecha_cambio='2024-08-24 10:30:00')

-- Se ejecuta: UPDATE productos SET precio = 950.00 WHERE id = 1;
-- Nuevo registro en historial_precios:
-- (producto_id=1, precio_anterior=1200.00, precio_nuevo=950.00, fecha_cambio='2024-08-24 15:45:00')
```

**CONSULTAS ÚTILES PARA ANÁLISIS**:
```sql
-- Ver evolución de precios de un producto específico:
SELECT p.nombre, hp.precio_anterior, hp.precio_nuevo, hp.fecha_cambio
FROM historial_precios hp
JOIN productos p ON hp.producto_id = p.id
WHERE p.id = 1
ORDER BY hp.fecha_cambio;

-- Productos con más cambios de precio:
SELECT p.nombre, COUNT(*) as cambios_precio
FROM historial_precios hp
JOIN productos p ON hp.producto_id = p.id
GROUP BY p.id, p.nombre
ORDER BY cambios_precio DESC;

-- Incrementos/decrementos promedio por producto:
SELECT p.nombre, 
       AVG(hp.precio_nuevo - hp.precio_anterior) as cambio_promedio
FROM historial_precios hp
JOIN productos p ON hp.producto_id = p.id
GROUP BY p.id, p.nombre;
```

**VENTAJAS**:
- Trazabilidad completa de cambios de precio
- Base de datos para análisis de competitividad
- Evidencia para auditorías financieras
- Datos para algoritmos de pricing dinámico

**CASOS DE USO**:
- E-commerce con precios dinámicos
- Análisis de inflación por categoría
- Cumplimiento regulatorio de transparencia de precios
- Estudios de elasticidad de precio-demanda

## Variables Especiales en Triggers

### OLD y NEW - Los Pilares de los Triggers

**`OLD`** y **`NEW`** son variables especiales que MySQL proporciona automáticamente en los triggers para acceder a los datos antes y después de las operaciones.

**DISPONIBILIDAD POR TIPO DE OPERACIÓN**:

| Operación | OLD | NEW | Descripción |
|-----------|-----|-----|-------------|
| INSERT    | ❌   | ✅   | Solo hay datos nuevos |
| UPDATE    | ✅   | ✅   | Hay datos antes y después del cambio |
| DELETE    | ✅   | ❌   | Solo hay datos anteriores |

**FUNCIONALIDAD EXPLICADA**:

- **OLD**: Contiene los valores anteriores (disponible en UPDATE y DELETE)
- **NEW**: Contiene los valores nuevos (disponible en INSERT y UPDATE)

**EJEMPLO DETALLADO DE USO**:

```sql
-- Ejemplo de uso de OLD y NEW en un trigger de auditoría completa
DELIMITER $$
CREATE TRIGGER ejemplo_old_new
    AFTER UPDATE ON usuarios                 -- Se activa en actualizaciones
    FOR EACH ROW
BEGIN
    -- COMPARACIÓN DE CAMPOS INDIVIDUALES
    IF OLD.nombre != NEW.nombre THEN        -- Si cambió el nombre
        INSERT INTO auditoria (mensaje, fecha) 
        VALUES (
            CONCAT('Usuario ID ', OLD.id, ': nombre cambió de "', 
                   OLD.nombre, '" a "', NEW.nombre, '"'),
            NOW()
        );
    END IF;
    
    -- MÚLTIPLES COMPARACIONES EN UNA SOLA OPERACIÓN
    IF OLD.apellido != NEW.apellido OR OLD.direccion_id != NEW.direccion_id THEN
        INSERT INTO auditoria (mensaje, fecha)
        VALUES (
            CONCAT('Usuario ', NEW.nombre, ' (ID: ', NEW.id, 
                   ') actualizó información personal'),
            NOW()
        );
    END IF;
    
    -- CÁLCULOS CON VALORES OLD Y NEW
    IF OLD.saldo != NEW.saldo THEN
        INSERT INTO movimientos_cuenta (
            usuario_id,
            saldo_anterior,
            saldo_nuevo,
            diferencia,
            tipo_movimiento
        ) VALUES (
            NEW.id,
            OLD.saldo,
            NEW.saldo,
            NEW.saldo - OLD.saldo,              -- Cálculo de diferencia
            CASE 
                WHEN NEW.saldo > OLD.saldo THEN 'CREDITO'
                ELSE 'DEBITO'
            END
        );
    END IF;
END$$
DELIMITER ;
```

**CASOS PRÁCTICOS DE USO**:

**1. En TRIGGER INSERT (solo NEW disponible)**:
```sql
CREATE TRIGGER ejemplo_insert
    BEFORE INSERT ON productos
    FOR EACH ROW
BEGIN
    -- Validar datos nuevos
    IF NEW.precio <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Precio debe ser positivo';
    END IF;
    
    -- Modificar datos antes de insertar
    SET NEW.nombre = UPPER(NEW.nombre);      -- Convertir nombre a mayúsculas
    SET NEW.fecha_creacion = NOW();          -- Asignar fecha actual
END$$
```

**2. En TRIGGER DELETE (solo OLD disponible)**:
```sql
CREATE TRIGGER ejemplo_delete
    BEFORE DELETE ON usuarios
    FOR EACH ROW
BEGIN
    -- Validar antes de eliminar
    IF OLD.tipo_usuario = 'ADMINISTRADOR' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'No se puede eliminar un administrador';
    END IF;
    
    -- Registrar eliminación
    INSERT INTO usuarios_eliminados (
        id_original, nombre, apellido, fecha_eliminacion
    ) VALUES (
        OLD.id, OLD.nombre, OLD.apellido, NOW()
    );
END$$
```

**3. En TRIGGER UPDATE (OLD y NEW disponibles)**:
```sql
CREATE TRIGGER ejemplo_update_completo
    AFTER UPDATE ON pedidos
    FOR EACH ROW
BEGIN
    -- Registrar cambios significativos
    IF ABS(NEW.total - OLD.total) > 100 THEN    -- Si cambio > $100
        INSERT INTO alertas_pedidos (
            pedido_id,
            total_anterior,
            total_nuevo,
            diferencia,
            motivo
        ) VALUES (
            NEW.id,
            OLD.total,
            NEW.total,
            NEW.total - OLD.total,
            'CAMBIO_SIGNIFICATIVO_TOTAL'
        );
    END IF;
    
    -- Validar cambios de estado
    IF OLD.estado = 'COMPLETADO' AND NEW.estado != 'COMPLETADO' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'No se puede cambiar un pedido completado';
    END IF;
END$$
```

**LIMITACIONES Y CONSIDERACIONES**:

- **No se pueden modificar OLD**: `OLD` es de solo lectura
- **NEW solo se puede modificar en BEFORE**: En triggers `AFTER`, `NEW` es de solo lectura
- **Campos calculados**: Se pueden usar en expresiones matemáticas y lógicas
- **Comparación de NULL**: Tener cuidado con campos que pueden ser NULL

**EJEMPLO CON MANEJO DE NULL**:
```sql
IF IFNULL(OLD.email, '') != IFNULL(NEW.email, '') THEN
    -- Lógica cuando el email cambia (maneja NULL correctamente)
END IF;
```

## Gestión de Triggers

### Ver triggers existentes
```sql
SHOW TRIGGERS;
SHOW TRIGGERS FROM nombre_base_datos;
SHOW TRIGGERS LIKE 'usuarios%';
```

### Ver definición completa
```sql
SHOW CREATE TRIGGER nombre_trigger;
```

### Eliminar triggers
```sql
DROP TRIGGER IF EXISTS nombre_trigger;
```

### Deshabilitar/Habilitar triggers temporalmente
```sql
-- MySQL no tiene comando directo, pero se puede:
-- 1. Respaldar la definición
-- 2. Eliminar el trigger
-- 3. Recrearlo cuando sea necesario
```

## Mejores Prácticas

### 1. Nomenclatura Clara
```sql
-- Usar prefijo que indique tipo
tr_auditoria_tabla_evento
tr_validacion_tabla_campo
tr_calculo_tabla_operacion
```

### 2. Mantener Triggers Simples
```sql
-- MAL: Trigger muy complejo
DELIMITER $$
CREATE TRIGGER tr_complejo
    AFTER INSERT ON pedidos
    FOR EACH ROW
BEGIN
    -- 50 líneas de código complejo
END$$
DELIMITER ;

-- BIEN: Trigger simple que llama a procedimiento
DELIMITER $$
CREATE TRIGGER tr_simple
    AFTER INSERT ON pedidos
    FOR EACH ROW
BEGIN
    CALL sp_procesar_pedido(NEW.id);
END$$
DELIMITER ;
```

### 3. Manejo de Errores
```sql
DELIMITER $$
CREATE TRIGGER tr_con_manejo_errores
    BEFORE INSERT ON pedidos
    FOR EACH ROW
BEGIN
    DECLARE usuario_existe INT DEFAULT 0;
    
    SELECT COUNT(*) INTO usuario_existe 
    FROM usuarios 
    WHERE id = NEW.usuario_id;
    
    IF usuario_existe = 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El usuario especificado no existe';
    END IF;
END$$
DELIMITER ;
```

### 4. Evitar Bucles Infinitos

**⚠️ PELIGRO CRÍTICO**: Este es uno de los errores más comunes y peligrosos al crear triggers.

**¿QUÉ ES UN BUCLE INFINITO EN TRIGGERS?**
Un bucle infinito ocurre cuando un trigger modifica la misma tabla que lo activó, causando que el trigger se ejecute de nuevo, y así sucesivamente hasta que el sistema se bloquee.

**EJEMPLO PELIGROSO**:
```sql
-- ¡NUNCA HAGAS ESTO!
DELIMITER $$
CREATE TRIGGER tr_peligroso
    AFTER UPDATE ON productos
    FOR EACH ROW
BEGIN
    -- ¡PELIGRO! Esto puede crear un bucle infinito
    UPDATE productos SET descripcion = UPPER(descripcion) WHERE id = NEW.id;
    -- Este UPDATE vuelve a activar el trigger, que vuelve a hacer UPDATE, etc.
END$$
DELIMITER ;
```

**¿POR QUÉ ES PELIGROSO?**
1. **Consumo de CPU**: El servidor se bloquea procesando triggers infinitamente
2. **Bloqueo de tablas**: La tabla queda bloqueada impidiendo otras operaciones
3. **Crash del servidor**: Puede agotar recursos y causar caída del sistema
4. **Corrupción de datos**: En casos extremos puede dañar la integridad

**ESTRATEGIAS PARA EVITAR BUCLES**:

**1. USAR TRIGGERS `BEFORE` PARA MODIFICACIONES EN LA MISMA TABLA**:
```sql
-- CORRECTO: Usar BEFORE para modificar la misma fila
DELIMITER $$
CREATE TRIGGER tr_seguro_before
    BEFORE UPDATE ON productos
    FOR EACH ROW
BEGIN
    -- Esto es seguro porque modifica NEW antes de que se guarde
    SET NEW.descripcion = UPPER(NEW.descripcion);
    SET NEW.fecha_modificacion = NOW();
    -- No se ejecuta otro UPDATE, por lo tanto no hay bucle
END$$
DELIMITER ;
```

**2. USAR CONDICIONES PARA EVITAR RE-EJECUCIÓN**:
```sql
-- TÉCNICA: Verificar si ya se hizo el cambio
DELIMITER $$
CREATE TRIGGER tr_seguro_condicional
    AFTER UPDATE ON productos
    FOR EACH ROW
BEGIN
    -- Solo actualizar si la descripción no está ya en mayúsculas
    IF NEW.descripcion != UPPER(NEW.descripcion) THEN
        UPDATE productos 
        SET descripcion = UPPER(descripcion) 
        WHERE id = NEW.id;
    END IF;
END$$
DELIMITER ;
```

**3. USAR BANDERAS O CAMPOS DE CONTROL**:
```sql
-- Agregar campo de control
ALTER TABLE productos ADD COLUMN procesado_trigger BOOLEAN DEFAULT FALSE;

DELIMITER $$
CREATE TRIGGER tr_con_bandera
    AFTER UPDATE ON productos
    FOR EACH ROW
BEGIN
    -- Solo procesar si no ha sido procesado por el trigger
    IF NOT NEW.procesado_trigger THEN
        UPDATE productos 
        SET descripcion = UPPER(descripcion),
            procesado_trigger = TRUE
        WHERE id = NEW.id;
    END IF;
END$$
DELIMITER ;
```

**4. MODIFICAR OTRAS TABLAS EN LUGAR DE LA MISMA**:
```sql
-- RECOMENDADO: Usar tablas auxiliares
DELIMITER $$
CREATE TRIGGER tr_seguro_tabla_auxiliar
    AFTER UPDATE ON productos
    FOR EACH ROW
BEGIN
    -- Registrar en tabla de logs (NO modifica productos)
    INSERT INTO logs_productos (
        producto_id, 
        accion, 
        descripcion_anterior, 
        descripcion_nueva
    ) VALUES (
        NEW.id, 
        'UPDATE', 
        OLD.descripcion, 
        NEW.descripcion
    );
    
    -- Actualizar estadísticas en tabla separada
    UPDATE estadisticas_productos 
    SET ultima_modificacion = NOW() 
    WHERE producto_id = NEW.id;
END$$
DELIMITER ;
```

**DETECCIÓN DE BUCLES INFINITOS**:

**Síntomas de que tienes un bucle infinito**:
- El servidor MySQL se vuelve extremadamente lento
- Las consultas simples tardan mucho tiempo
- Alta utilización de CPU en el proceso MySQL
- Errores de "table is full" o "lock wait timeout"

**Cómo recuperarse de un bucle infinito**:
```sql
-- 1. Identificar y matar procesos problemáticos
SHOW PROCESSLIST;
KILL [process_id];

-- 2. Eliminar el trigger problemático inmediatamente
DROP TRIGGER IF EXISTS tr_peligroso;

-- 3. Verificar la integridad de los datos
SELECT COUNT(*) FROM productos WHERE descripcion IS NULL;
```

**MEJORES PRÁCTICAS PREVENTIVAS**:

1. **Siempre pregúntate**: "¿Este trigger puede modificar la tabla que lo activa?"
2. **Usa BEFORE cuando sea posible** para modificaciones en la misma tabla
3. **Testa los triggers** en un ambiente de desarrollo primero
4. **Documenta las dependencias** entre triggers
5. **Evita trigger complejos** que modifiquen múltiples tablas
6. **Usa transacciones** para poder hacer rollback en caso de problemas

**EJEMPLO DE TRIGGER BIEN DISEÑADO**:
```sql
DELIMITER $$
CREATE TRIGGER tr_producto_bien_disenado
    BEFORE UPDATE ON productos
    FOR EACH ROW
BEGIN
    -- Todas las modificaciones usan SET NEW (no hay bucle)
    SET NEW.descripcion = TRIM(UPPER(NEW.descripcion));
    SET NEW.fecha_modificacion = NOW();
    
    -- Validaciones que no modifican la tabla
    IF NEW.precio <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El precio debe ser positivo';
    END IF;
    
    -- Logs en tabla separada (sin riesgo de bucle)
    INSERT INTO logs_cambios (tabla, registro_id, accion)
    VALUES ('productos', NEW.id, 'UPDATE');
END$$
DELIMITER ;
```

## Limitaciones y Consideraciones

### Limitaciones:
- No se pueden crear triggers en tablas temporales
- Un trigger no puede llamar a procedimientos que retornen resultados
- Los triggers pueden afectar el rendimiento
- Debugging puede ser complejo

### Consideraciones de Rendimiento:
- Los triggers se ejecutan dentro de la transacción
- Pueden ralentizar operaciones INSERT, UPDATE, DELETE
- Mantener la lógica simple y eficiente

## Ejemplos de Prueba

### Probar los triggers creados:

**PROPÓSITO DE LAS PRUEBAS**: Verificar que cada trigger funciona correctamente y produce los resultados esperados.

**EJEMPLO 1: Probar trigger de auditoría**
```sql
-- Prueba del trigger tr_auditoria_usuarios_update
UPDATE usuarios SET nombre = 'Valeria Modificada' WHERE id = 1;

-- Verificar que se registró en auditoría:
SELECT * FROM auditoria_usuarios;
-- Resultado esperado: Un nuevo registro con:
-- - usuario_id = 1
-- - accion = 'UPDATE'  
-- - nombre_anterior = 'Valeria' (valor original)
-- - nombre_nuevo = 'Valeria Modificada'
-- - fecha_cambio = timestamp actual
-- - usuario_sistema = tu usuario MySQL actual
```

**EJEMPLO 2: Probar trigger de validación (debería fallar)**
```sql
-- Prueba del trigger tr_validar_total_pedido
INSERT INTO pedidos (id, fecha, total, usuario_id) VALUES (555, '2025-01-01', -100, 1);

-- Resultado esperado: ERROR
-- Error Code: 1644
-- Error Message: "El total del pedido debe ser mayor a cero"
-- Explicación: El trigger detectó un total negativo y evitó la inserción

-- Prueba con fecha futura (también debería fallar):
INSERT INTO pedidos (id, fecha, total, usuario_id) VALUES (556, '2026-12-31', 100, 1);
-- Error esperado: "La fecha del pedido no puede ser futura"
```

**EJEMPLO 3: Probar trigger de estadísticas**
```sql
-- Preparación: Verificar estado inicial
SELECT * FROM estadisticas_productos WHERE producto_id = 222;
-- Resultado inicial: Puede estar vacío o tener datos previos

-- Ejecutar la prueba:
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES (554, 222);

-- Verificar resultado:
SELECT * FROM estadisticas_productos WHERE producto_id = 222;
-- Resultado esperado:
-- - Si es la primera vez: veces_pedido = 1
-- - Si ya existía: veces_pedido incrementado en 1
-- - ultima_vez_pedido = fecha del pedido 554
```

**EJEMPLO 4: Probar trigger de código automático**
```sql
-- Insertar un pedido nuevo
INSERT INTO pedidos (id, fecha, total, usuario_id) VALUES (999, '2024-08-24', 150.00, 1);

-- Verificar que se generó el código automático:
SELECT id, codigo_pedido, fecha, total FROM pedidos WHERE id = 999;
-- Resultado esperado: codigo_pedido = 'PED-2024-000999'
```

**EJEMPLO 5: Probar trigger de normalización**
```sql
-- Insertar dirección con formato inconsistente:
INSERT INTO direcciones (calle, colonia, ciudad, pais) 
VALUES ('AV INSURGENTES 123', 'las flores', 'CIUDAD DE MÉXICO', 'mexico');

-- Verificar normalización:
SELECT * FROM direcciones WHERE calle LIKE '%INSURGENTES%';
-- Resultado esperado:
-- calle = 'Av insurgentes 123'
-- colonia = 'Las flores'  
-- ciudad = 'Ciudad de méxico'
-- pais = 'MEXICO'
```

**EJEMPLO 6: Probar trigger de historial de precios**
```sql
-- Cambiar precio de un producto:
UPDATE productos SET precio = 1250.00 WHERE id = 1;

-- Verificar que se registró el cambio:
SELECT * FROM historial_precios WHERE producto_id = 1 ORDER BY fecha_cambio DESC LIMIT 1;
-- Resultado esperado: Un registro con precio_anterior y precio_nuevo diferentes
```

**TESTS DE VALIDACIÓN COMPLETOS**:

```sql
-- Test Suite completo para verificar todos los triggers
-- Ejecuta este bloque completo para probar todos los triggers

START TRANSACTION;  -- Usar transacción para poder hacer rollback si algo falla

-- 1. Test de auditoría
UPDATE usuarios SET apellido = 'Test Apellido' WHERE id = 1;
SELECT 'PASS: Auditoría' AS test_result WHERE EXISTS (
    SELECT 1 FROM auditoria_usuarios 
    WHERE usuario_id = 1 AND accion = 'UPDATE' AND apellido_nuevo = 'Test Apellido'
);

-- 2. Test de validación (capturar error)
-- Nota: Este test causará un error, pero es el comportamiento esperado
-- INSERT INTO pedidos (fecha, total, usuario_id) VALUES ('2024-08-24', -50, 1);

-- 3. Test de estadísticas
INSERT INTO pedidos (id, fecha, total, usuario_id) VALUES (9999, '2024-08-24', 100, 1);
INSERT INTO pedidos_has_productos (pedido_id, producto_id) VALUES (9999, 222);
SELECT 'PASS: Estadísticas' AS test_result WHERE EXISTS (
    SELECT 1 FROM estadisticas_productos WHERE producto_id = 222
);

-- 4. Test de código automático
SELECT 'PASS: Código automático' AS test_result WHERE EXISTS (
    SELECT 1 FROM pedidos WHERE id = 9999 AND codigo_pedido LIKE 'PED-2024-009999'
);

-- Hacer rollback para no afectar datos reales
ROLLBACK;
```

**HERRAMIENTAS DE DEBUGGING**:

```sql
-- Ver qué triggers están activos:
SELECT TRIGGER_NAME, EVENT_MANIPULATION, EVENT_OBJECT_TABLE, ACTION_TIMING
FROM INFORMATION_SCHEMA.TRIGGERS 
WHERE TRIGGER_SCHEMA = DATABASE();

-- Ver errores recientes de triggers:
SHOW WARNINGS;
SHOW ERRORS;

-- Verificar logs de MySQL (en caso de errores graves):
-- Buscar en: /var/log/mysql/error.log (Linux) o MySQL error log (Windows)
```

**RESULTADOS ESPERADOS RESUMIDOS**:
- ✅ **Auditoría**: Nuevos registros en `auditoria_usuarios`
- ❌ **Validación**: Errores controlados con mensajes claros  
- ✅ **Estadísticas**: Contadores actualizados en `estadisticas_productos`
- ✅ **Códigos automáticos**: Formato `PED-YYYY-NNNNNN` en `pedidos.codigo_pedido`
- ✅ **Normalización**: Texto con formato consistente
- ✅ **Historial**: Registros de cambios en `historial_precios`

## Conclusión

Los triggers son herramientas poderosas para automatizar procesos, mantener integridad de datos y crear funcionalidades reactivas en MySQL. Cuando se usan correctamente, pueden simplificar significativamente la lógica de aplicación y garantizar consistencia en los datos.

**Recuerda**: Úsalos con moderación y siempre documenta su funcionamiento para facilitar el mantenimiento futuro.