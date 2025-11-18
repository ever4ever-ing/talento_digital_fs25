# 🔄 Guía de Migraciones en Django

## ¿Qué son las Migraciones?

Las migraciones son la forma en que Django propaga cambios en tus modelos (agregar un campo, eliminar un modelo, etc.) a tu esquema de base de datos. Son archivos Python que contienen las instrucciones para modificar la estructura de la base de datos.

---

## 📋 Comandos Principales

### 1. `makemigrations` - Crear Migraciones

```powershell
# Crear migraciones para todas las apps
python manage.py makemigrations

# Crear migraciones para una app específica (RECOMENDADO)
python manage.py makemigrations voluntarios
```

**¿Qué hace?**
- Lee los modelos en `models.py`
- Compara con las migraciones anteriores
- Genera un archivo de migración (ej: `0001_initial.py`) en la carpeta `migrations/`

### 2. `migrate` - Aplicar Migraciones

```powershell
# Aplicar todas las migraciones pendientes
python manage.py migrate

# Aplicar migraciones de una app específica (RECOMENDADO)
python manage.py migrate voluntarios
```

**¿Qué hace?**
- Lee los archivos de migración
- Ejecuta las instrucciones SQL en la base de datos
- Crea/modifica tablas, campos, índices, etc.

---

## 🔍 El Problema que Tuvimos

### Situación Inicial:

1. **Creamos los modelos** en `voluntarios/models.py`:
   ```python
   class Voluntario(models.Model):
       nombre = models.CharField(max_length=255)
       email = models.EmailField(unique=True)
       # ...
   
   class Evento(models.Model):
       titulo = models.CharField(max_length=255)
       # ...
   ```

2. **Ejecutamos** (sin especificar la app):
   ```powershell
   python manage.py makemigrations  # ❌ No detectó cambios en voluntarios
   python manage.py migrate          # ✅ Migró apps del sistema (auth, admin, etc.)
   ```

3. **Resultado**:
   - ✅ Tablas del sistema Django creadas (auth_user, django_session, etc.)
   - ❌ Tablas de voluntarios **NO creadas**
   - ❌ Error: `Table 'voluntarios_db.voluntarios_voluntario' doesn't exist`

### ¿Por qué pasó?

Cuando ejecutamos `makemigrations` sin especificar la app:
- Django no detectó cambios en `voluntarios` 
- Puede ser por timing, configuración o porque Django pensó que no había cambios
- **No se creó** el archivo `voluntarios/migrations/0001_initial.py`

---

## ✅ La Solución

### Paso 1: Crear migraciones específicas
```powershell
python manage.py makemigrations voluntarios
```

**Salida:**
```
Migrations for 'voluntarios':
  voluntarios\migrations\0001_initial.py
    + Create model Voluntario
    + Create model Evento
```

Esto creó el archivo `voluntarios/migrations/0001_initial.py` con:
```python
operations = [
    migrations.CreateModel(
        name='Voluntario',
        fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('nombre', models.CharField(max_length=255)),
            ('email', models.EmailField(unique=True)),
            # ...
        ],
    ),
    migrations.CreateModel(
        name='Evento',
        fields=[
            # ...
        ],
    ),
]
```

### Paso 2: Aplicar las migraciones
```powershell
python manage.py migrate voluntarios
```

**Salida:**
```
Operations to perform:
  Apply all migrations: voluntarios
Running migrations:
  Applying voluntarios.0001_initial... OK
```

Esto ejecutó SQL en MySQL para crear:
- Tabla `voluntarios_voluntario`
- Tabla `voluntarios_evento`
- Tabla `voluntarios_evento_voluntarios` (para la relación ManyToMany)

---

## 📚 Buenas Prácticas

### ✅ HACER:

1. **Ser específico con las apps:**
   ```powershell
   python manage.py makemigrations voluntarios
   python manage.py migrate voluntarios
   ```

2. **Verificar antes de migrar:**
   ```powershell
   python manage.py makemigrations --dry-run  # Ver qué se creará
   python manage.py showmigrations            # Ver estado de migraciones
   ```

3. **Revisar el archivo de migración:**
   - Abre `voluntarios/migrations/0001_initial.py`
   - Verifica que tenga sentido antes de aplicar

4. **Hacer migraciones pequeñas:**
   - Haz `makemigrations` después de cada cambio importante
   - No acumules muchos cambios

### ❌ EVITAR:

1. **Ejecutar solo comandos genéricos:**
   ```powershell
   python manage.py makemigrations  # Puede no detectar tu app
   ```

2. **Editar archivos de migración manualmente** (a menos que sepas lo que haces)

3. **Borrar migraciones ya aplicadas** (causa problemas)

4. **Hacer `migrate` sin antes hacer `makemigrations`**

---

## 🔧 Comandos Útiles

### Ver el estado de las migraciones:
```powershell
python manage.py showmigrations
```

**Salida:**
```
voluntarios
 [X] 0001_initial
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
...
```
- `[X]` = Aplicada
- `[ ]` = Pendiente

### Ver el SQL que ejecutará una migración:
```powershell
python manage.py sqlmigrate voluntarios 0001
```

### Revertir una migración:
```powershell
python manage.py migrate voluntarios 0000  # Volver al inicio
python manage.py migrate voluntarios 0001  # Ir a una migración específica
```

### Verificar problemas:
```powershell
python manage.py check
```

---

## 🎯 Flujo de Trabajo Recomendado

```
1. Modificar models.py
   ↓
2. python manage.py makemigrations nombre_app
   ↓
3. Revisar el archivo de migración creado
   ↓
4. python manage.py migrate nombre_app
   ↓
5. Verificar que funcionó: python manage.py runserver
```

---

## 🐛 Solución de Problemas Comunes

### "No changes detected"
**Problema:** Django no detecta cambios en los modelos.

**Soluciones:**
- Verifica que la app esté en `INSTALLED_APPS` en `settings.py`
- Usa el comando específico: `makemigrations nombre_app`
- Asegúrate de haber guardado `models.py`

### "Table already exists"
**Problema:** Intentas crear una tabla que ya existe.

**Soluciones:**
- Usa `python manage.py migrate --fake` (cuidado!)
- O borra la base de datos y vuelve a migrar desde cero

### "Table doesn't exist"
**Problema:** Django busca una tabla que no existe.

**Soluciones:**
- Ejecuta: `python manage.py makemigrations nombre_app`
- Luego: `python manage.py migrate nombre_app`

---

## 📊 Estructura de Archivos de Migración

```
voluntarios/
├── migrations/
│   ├── __init__.py
│   ├── 0001_initial.py      # Primera migración (crea tablas)
│   ├── 0002_auto_...py      # Segunda migración (modificaciones)
│   └── 0003_...py           # Tercera migración
├── models.py
└── ...
```

Cada archivo de migración tiene:
- **dependencies**: Migraciones que deben ejecutarse antes
- **operations**: Lista de operaciones (CreateModel, AddField, etc.)

---

## 💡 Resumen

| Comando | ¿Cuándo usar? | ¿Qué hace? |
|---------|---------------|------------|
| `makemigrations` | Después de cambiar `models.py` | Crea archivo de migración |
| `migrate` | Después de `makemigrations` | Aplica cambios a la BD |
| `showmigrations` | Para verificar estado | Muestra migraciones aplicadas |
| `sqlmigrate` | Para ver SQL generado | Muestra el SQL sin ejecutar |

---

## ✅ Checklist Final

- [ ] Modifiqué `models.py`
- [ ] Ejecuté `makemigrations nombre_app`
- [ ] Revisé el archivo de migración creado
- [ ] Ejecuté `migrate nombre_app`
- [ ] Verifiqué que el servidor funciona sin errores
- [ ] Probé la funcionalidad en el navegador

---

¡Ahora entiendes cómo funcionan las migraciones en Django! 🎉
