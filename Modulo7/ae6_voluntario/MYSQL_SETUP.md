# 🔧 Configuración de MySQL para el Proyecto

## 📋 Requisitos Previos

1. **MySQL Server** instalado en tu sistema
2. **Python 3.x** instalado
3. **Visual Studio C++ Build Tools** (para Windows)

---

## 🚀 Instalación Paso a Paso

### 1. Instalar MySQL Server

#### Windows:
1. Descarga MySQL desde: https://dev.mysql.com/downloads/installer/
2. Ejecuta el instalador
3. Durante la instalación:
   - Selecciona "Developer Default"
   - Configura la contraseña de root
   - Mantén el puerto por defecto (3306)

#### Verificar instalación:
```powershell
mysql --version
```

### 2. Crear la Base de Datos

Abre MySQL desde la terminal o MySQL Workbench:

```powershell
# Conectar a MySQL
mysql -u root -p
```

Ejecuta los siguientes comandos SQL:

```sql
-- Crear la base de datos
CREATE DATABASE voluntarios_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Verificar que se creó
SHOW DATABASES;

-- Salir de MySQL
EXIT;
```

### 3. Instalar el Cliente MySQL para Python

**IMPORTANTE**: En Windows, necesitas instalar Visual Studio C++ Build Tools primero.

#### Opción A: Instalar Build Tools (Recomendado)
1. Descarga: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Instala "Desktop development with C++"
3. Reinicia tu sistema

Luego instala mysqlclient:
```powershell
pip install mysqlclient
```

#### Opción B: Usar PyMySQL (Alternativa más simple)
Si tienes problemas con mysqlclient, usa PyMySQL:

```powershell
pip install pymysql
```

Y agrega al inicio de `config/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### 4. Configurar las Credenciales

Edita el archivo `config/settings.py` y ajusta las credenciales de MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'voluntarios_db',
        'USER': 'root',  # Tu usuario de MySQL
        'PASSWORD': 'tu_password',  # Tu contraseña de MySQL
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

### 5. Ejecutar las Migraciones

```powershell
# Crear las migraciones
python manage.py makemigrations

# Aplicar las migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar el servidor
python manage.py runserver
```

---

## 🔍 Verificar la Conexión

Puedes verificar que Django se conectó correctamente a MySQL:

```powershell
python manage.py dbshell
```

Esto debería abrir una sesión de MySQL. Si funciona, ¡la configuración es correcta!

---

## ⚠️ Solución de Problemas

### Error: "No module named 'MySQLdb'"
**Solución**: Instala mysqlclient o usa PyMySQL como alternativa.

```powershell
pip install pymysql
```

### Error: "Can't connect to MySQL server"
**Solución**: 
1. Verifica que MySQL esté corriendo: `net start MySQL80`
2. Verifica el puerto: debe ser 3306
3. Verifica usuario y contraseña en settings.py

### Error: "Access denied for user"
**Solución**: 
- Verifica las credenciales en `settings.py`
- Asegúrate de que el usuario tiene permisos:

```sql
GRANT ALL PRIVILEGES ON voluntarios_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

### Error al instalar mysqlclient en Windows
**Solución**: 
1. Instala Visual Studio Build Tools
2. O usa PyMySQL como alternativa (más fácil)

---

## 📊 Comandos Útiles de MySQL

```sql
-- Ver todas las bases de datos
SHOW DATABASES;

-- Usar la base de datos
USE voluntarios_db;

-- Ver las tablas creadas por Django
SHOW TABLES;

-- Ver estructura de una tabla
DESCRIBE voluntarios_voluntario;

-- Ver datos de voluntarios
SELECT * FROM voluntarios_voluntario;

-- Ver datos de eventos
SELECT * FROM voluntarios_evento;

-- Borrar la base de datos (cuidado!)
DROP DATABASE voluntarios_db;
```

---

## 🔐 Seguridad (Producción)

Para producción, usa variables de entorno:

1. Instala python-decouple:
```powershell
pip install python-decouple
```

2. Crea un archivo `.env`:
```env
DB_NAME=voluntarios_db
DB_USER=root
DB_PASSWORD=tu_password_super_seguro
DB_HOST=localhost
DB_PORT=3306
```

3. Modifica `settings.py`:
```python
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```

---

## ✅ Checklist de Configuración

- [ ] MySQL Server instalado
- [ ] Base de datos `voluntarios_db` creada
- [ ] mysqlclient o PyMySQL instalado
- [ ] Credenciales configuradas en settings.py
- [ ] Migraciones ejecutadas exitosamente
- [ ] Superusuario creado
- [ ] Servidor Django funcionando
- [ ] Puedes acceder a la aplicación

---

## 📞 Soporte

Si tienes problemas:
1. Verifica que MySQL esté corriendo
2. Revisa los logs de Django
3. Verifica las credenciales
4. Consulta la documentación oficial de Django

**Enlaces útiles:**
- Django Databases: https://docs.djangoproject.com/en/4.2/ref/databases/
- MySQL Documentation: https://dev.mysql.com/doc/
- mysqlclient: https://github.com/PyMySQL/mysqlclient

---

¡Listo! Tu aplicación ahora usa MySQL como base de datos. 🎉
