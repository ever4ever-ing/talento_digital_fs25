# VetCare v3.0 - Sistema de Gestión de Citas con Persistencia

## Nuevas Características

### 🗄️ Persistencia de Datos
- **Guardado automático**: Los datos se guardan automáticamente al registrar o cancelar citas
- **Carga automática**: Al iniciar el programa, se cargan automáticamente los datos previos
- **Archivos JSON**: Los datos se almacenan en archivos JSON legibles:
  - `citas.json`: Lista de todas las citas activas
  - `historial.json`: Historial completo por mascota

### 🔧 Funcionalidades Mejoradas

#### Sistema de Validación
- **Validación de fecha**: Formato dd/mm/yy obligatorio
- **Validación de horarios**: Solo horarios predefinidos
- **Validación de motivos**: Lista predefinida de motivos válidos
- **Validación de campos**: No se permiten campos vacíos

#### Nuevas Opciones del Menú
1. **Ver horarios disponibles** - Consulta horarios libres por fecha
2. **Registrar nueva cita** - Registro con validaciones mejoradas
3. **Mostrar historial de mascota** - Historial completo con timestamps
4. **Ver citas del día** - Lista ordenada de citas por fecha
5. **Cancelar cita** - Cancelación con actualización automática
6. **Ver estadísticas del sistema** - ⭐ NUEVO: Estadísticas generales
7. **Crear backup de datos** - ⭐ NUEVO: Respaldo con timestamp
8. **Guardar datos manualmente** - ⭐ NUEVO: Guardado manual
9. **Salir** - Salida con guardado automático

### 📊 Estadísticas del Sistema
- Total de citas activas
- Total de mascotas registradas
- Distribución de citas por motivo
- Información de próximas citas

### 🔒 Sistema de Backup
- Creación de copias de respaldo con timestamp
- Formato: `backup_citas_YYYYMMDD_HHMMSS.json`
- Preserva datos en caso de corrupción

### 🛡️ Manejo de Errores
- Manejo de interrupciones (Ctrl+C)
- Guardado automático antes de salir
- Recuperación ante errores de archivo
- Validación robusta de entrada

## Archivos del Sistema

### Archivos de Datos
- `citas.json` - Citas activas (se crea automáticamente)
- `historial.json` - Historial de mascotas (se crea automáticamente)
- `backup_*.json` - Archivos de respaldo

### Archivos de Código
- `main_persistencia.py` - Programa principal con menú mejorado
- `funciones_persistencia.py` - Funciones con persistencia de datos

## Horarios Disponibles
- 09:00, 10:00, 11:00, 12:00
- 14:00, 15:00, 16:00, 17:00

## Motivos de Cita Válidos
- urgencia
- consulta 
- control
- vacunacion
- cirugia

## Uso del Sistema

### Ejecución
```bash
python v3/main_persistencia.py
```

### Primera Ejecución
- El sistema creará automáticamente los archivos de datos
- Se mostrará un mensaje de inicialización

### Ejecuciones Posteriores
- Los datos se cargarán automáticamente
- Se mostrará cuántas citas e historiales se encontraron

## Beneficios de la Versión 3

1. **Persistencia**: Los datos no se pierden al cerrar el programa
2. **Backup**: Sistema de respaldo para proteger los datos
3. **Validación**: Entrada de datos más robusta y confiable
4. **Estadísticas**: Información útil sobre el uso del sistema
5. **Manejo de errores**: Mayor estabilidad y confiabilidad
6. **Experiencia mejorada**: Interfaz más intuitiva y completa

## Migración desde Versiones Anteriores

Para migrar datos de versiones anteriores, simplemente:
1. Ejecute la versión 3
2. Registre manualmente las citas existentes
3. El sistema las guardará automáticamente

## Estructura de Datos

### Formato de Cita
```json
{
  "id": "001",
  "nombre_mascota": "Firulais",
  "fecha": "25/07/25",
  "horario": "10:00",
  "motivo": "consulta",
  "tutor": "Juan Pérez",
  "fecha_registro": "18/07/25 14:30:15"
}
```

### Formato de Historial
```json
{
  "001": [
    {
      "id": "001",
      "nombre_mascota": "Firulais",
      "fecha": "25/07/25",
      "horario": "10:00",
      "motivo": "consulta",
      "tutor": "Juan Pérez",
      "fecha_registro": "18/07/25 14:30:15"
    }
  ]
}
```
