# Diagrama de Flujo del Sistema VetCare

Este diagrama representa el flujo de ejecución del sistema de gestión de citas veterinarias.

## Diagrama de Flujo Principal

```mermaid
flowchart TD
    A[Inicio] --> B[Inicializar listas y diccionarios]
    B --> C[Mostrar Menu]
    C --> D{Seleccionar Opcion}
    
    D -->|1| E[Registrar cita]
    D -->|2| F[Ver horarios]
    D -->|3| G[Ver historial]
    D -->|4| H[Salir]
    D -->|Otra| J[Opcion invalida]
    
    E --> E1[Ingresar datos mascota]
    E1 --> E2[Mostrar horarios disponibles]
    E2 --> E3[Registrar cita]
    E3 --> C
    
    F --> F1[Mostrar horarios disponibles]
    F1 --> C
    
    G --> G1[Ingresar nombre mascota]
    G1 --> G2[Mostrar historial]
    G2 --> C
    
    H --> I[Fin]
    
    J --> C
```

## Diagrama de la función `registrar_cita`

```mermaid
graph TD
    A[registrar_cita<br>citas, historial, nombre_mascota,<br>fecha, tratamiento] --> B[Crear diccionario 'cita'<br>con mascota, fecha y tratamiento]
    B --> C[Añadir 'cita' a la lista 'citas']
    C --> D{¿nombre_mascota<br>existe en historial?}
    D -- No --> E[Crear lista vacía para<br>nombre_mascota en historial]
    D -- Sí --> F[Añadir registro al historial<br>existente de la mascota]
    E --> F
    F --> G[Retornar citas y<br>historial actualizados]
```

## Diagrama de la función `horarios_disponibles`

```mermaid
graph TD
    A[horarios_disponibles<br>citas, horarios_posibles] --> B[Inicializar lista vacía 'ocupados']
    B --> C[Recorrer cada cita en 'citas']
    C --> D[Añadir fecha de la cita<br>a la lista 'ocupados']
    D --> E[Inicializar lista vacía 'disponibles']
    E --> F[Recorrer cada horario<br>en 'horarios_posibles']
    F --> G{¿Horario está en<br>lista 'ocupados'?}
    G -- No --> H[Añadir horario a<br>lista 'disponibles']
    G -- Sí --> I[Ignorar horario<br>ya ocupado]
    H --> J[Continuar con<br>siguiente horario]
    I --> J
    J --> K[Retornar lista 'disponibles']
```

## Diagrama de la función `mostrar_historial`

```mermaid
graph TD
    A[mostrar_historial<br>historial, nombre_mascota] --> B[Retornar historial.get<br>con nombre_mascota]
    B --> C[Si la mascota existe, devuelve<br>su lista de historiales;<br>si no, devuelve lista vacía]
```
