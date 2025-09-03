import os
import time
import datetime
import subprocess
import sys
import schedule
import threading

def check_mysql_tools():
    """Verificar que las herramientas de MySQL estén disponibles"""
    try:
        subprocess.run(["mysqldump", "--version"], capture_output=True, check=True)
        subprocess.run(["mysql", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Las herramientas de MySQL (mysqldump/mysql) no están instaladas o no están en el PATH")
        return False

def create_backup():
    """Crear un backup de la base de datos"""
    # Configuración - MODIFICA ESTOS VALORES
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "password"  # Considera usar variables de entorno para seguridad
    DB_NAME = "catalogo_productos"
    BACKUP_DIR = "backups"
    
    # Crear directorio de backups si no existe
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    # Generar nombre de archivo con timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"backup_{DB_NAME}_{timestamp}.sql")
    
    # Comando para hacer el backup
    cmd = [
        "mysqldump",
        f"--host={DB_HOST}",
        f"--user={DB_USER}",
        f"--password={DB_PASSWORD}",
        "--single-transaction",
        "--routines",
        "--events",
        DB_NAME
    ]
    
    try:
        print(f"[{timestamp}] Creando backup: {backup_file}")
        
        # Ejecutar el comando y guardar la salida en un archivo
        with open(backup_file, "w") as output_file:
            result = subprocess.run(cmd, stdout=output_file, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print(f"[{timestamp}] Backup completado exitosamente: {backup_file}")
            
            # Limpiar backups antiguos (más de 7 días)
            clean_old_backups(BACKUP_DIR)
            
            return True
        else:
            print(f"[{timestamp}] Error en backup: {result.stderr}")
            # Eliminar archivo de backup fallido
            if os.path.exists(backup_file):
                os.remove(backup_file)
            return False
            
    except Exception as e:
        print(f"[{timestamp}] Excepción durante backup: {str(e)}")
        return False

def clean_old_backups(backup_dir, days_to_keep=7):
    """Eliminar backups más antiguos que days_to_keep"""
    now = time.time()
    for filename in os.listdir(backup_dir):
        filepath = os.path.join(backup_dir, filename)
        if os.path.isfile(filepath) and filename.startswith("backup_") and filename.endswith(".sql"):
            # Verificar si el archivo es más antiguo que days_to_keep
            if os.stat(filepath).st_mtime < now - (days_to_keep * 86400):
                try:
                    os.remove(filepath)
                    print(f"Eliminado backup antiguo: {filename}")
                except Exception as e:
                    print(f"Error eliminando {filename}: {str(e)}")

def run_scheduler():
    """Ejecutar el planificador en un hilo separado"""
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    print("Iniciando script de backup de MySQL")
    print("Presiona Ctrl+C para detener\n")
    
    # Verificar que las herramientas de MySQL estén disponibles
    if not check_mysql_tools():
        sys.exit(1)
    
    # Programar backup cada minuto
    schedule.every(1).minutes.do(create_backup)
    
    # Ejecutar un backup inmediatamente al inicio
    create_backup()
    
    # Ejecutar el planificador en un hilo separado
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    
    try:
        # Mantener el script principal ejecutándose
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo script de backup...")
        sys.exit(0)

if __name__ == "__main__":
    main()