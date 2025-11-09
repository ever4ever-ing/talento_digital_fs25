# MySQL y Django: Guía Completa de Integración

## ¿Qué es Django?

Django es un framework web de alto nivel escrito en Python que fomenta el desarrollo rápido y el diseño limpio y pragmático. Django incluye un **ORM (Object-Relational Mapping)** potente que permite interactuar con bases de datos relacionales como MySQL de manera intuitiva usando código Python.

## ¿Por qué usar MySQL con Django?

### Ventajas de la combinación MySQL + Django:

- **Escalabilidad**: MySQL maneja grandes volúmenes de datos eficientemente
- **Rendimiento**: Optimizado para aplicaciones web de alto tráfico
- **Compatibilidad**: Django tiene soporte nativo completo para MySQL
- **Confiabilidad**: MySQL es una base de datos madura y estable
- **Ecosistema**: Gran comunidad y herramientas disponibles

## Configuración Inicial

### 1. Instalación de Dependencias

```bash
# Instalar Django
pip install Django

# Instalar cliente MySQL para Python
pip install mysqlclient

# Alternativas si mysqlclient da problemas:
pip install PyMySQL
# o
pip install mysql-connector-python
```

### 2. Configuración en settings.py

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mi_base_datos',
        'USER': 'usuario_mysql',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# Configuración adicional para MySQL
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### 3. Configuración con Variables de Entorno (Recomendado)

```python
import os
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}
```

## Modelos Django para Nuestra Base de Datos

Vamos a recrear la estructura de tu base de datos usando modelos Django:

### models.py

```python
from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
    calle = models.CharField(max_length=45)
    colonia = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'direcciones'
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
    
    def __str__(self):
        return f"{self.calle}, {self.colonia}, {self.ciudad}, {self.pais}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    fecha = models.DateField()
    total = models.FloatField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='PedidoProducto')
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.nombre_completo}"

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    class Meta:
        db_table = 'pedidos_has_productos'
        unique_together = ('pedido', 'producto')
        verbose_name = 'Producto del Pedido'
        verbose_name_plural = 'Productos del Pedido'
    
    def __str__(self):
        return f"{self.producto.nombre} - Pedido {self.pedido.id}"
```

## Migraciones Django

### 1. Crear Migraciones

```bash
# Crear migraciones basadas en los modelos
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate
```

### 2. Migración desde Base de Datos Existente

```bash
# Generar modelos desde una BD existente
python manage.py inspectdb > models.py

# Crear migraciones iniciales sin aplicar
python manage.py makemigrations --empty nombre_app

# Marcar migraciones como aplicadas (si ya tienes datos)
python manage.py migrate --fake-initial
```

## Django ORM: Operaciones con MySQL

### 1. Operaciones CRUD Básicas

```python
from miapp.models import Usuario, Direccion, Producto, Pedido

# CREATE - Crear registros
direccion = Direccion.objects.create(
    calle="Av. Principal 123",
    colonia="Centro",
    ciudad="Ciudad de México",
    pais="México"
)

usuario = Usuario.objects.create(
    nombre="Juan",
    apellido="Pérez",
    direccion=direccion
)

# READ - Leer registros
# Obtener todos los usuarios
usuarios = Usuario.objects.all()

# Filtrar usuarios
usuarios_mexico = Usuario.objects.filter(direccion__pais="México")

# Obtener un usuario específico
usuario = Usuario.objects.get(id=1)

# UPDATE - Actualizar registros
usuario.nombre = "Juan Carlos"
usuario.save()

# O usando update
Usuario.objects.filter(id=1).update(nombre="Juan Carlos")

# DELETE - Eliminar registros
usuario.delete()
# O
Usuario.objects.filter(id=1).delete()
```

### 2. Consultas Avanzadas

```python
from django.db.models import Count, Sum, Avg, Q
from datetime import date, timedelta

# Joins automáticos
pedidos_con_usuario = Pedido.objects.select_related('usuario', 'usuario__direccion')

# Agregaciones
stats = Pedido.objects.aggregate(
    total_pedidos=Count('id'),
    total_ventas=Sum('total'),
    ticket_promedio=Avg('total')
)

# Filtros complejos con Q objects
filtro_complejo = Usuario.objects.filter(
    Q(nombre__icontains="juan") | Q(apellido__icontains="pérez")
)

# Consultas con fechas
pedidos_recientes = Pedido.objects.filter(
    fecha__gte=date.today() - timedelta(days=30)
)

# Anotaciones
usuarios_con_pedidos = Usuario.objects.annotate(
    total_pedidos=Count('pedido'),
    total_gastado=Sum('pedido__total')
).filter(total_pedidos__gt=0)

# Subconsultas
productos_mas_vendidos = Producto.objects.annotate(
    veces_pedido=Count('pedidoproducto')
).order_by('-veces_pedido')[:5]
```

### 3. Raw SQL cuando sea necesario

```python
# Ejecutar SQL directo
usuarios = Usuario.objects.raw("""
    SELECT u.*, d.ciudad, d.pais 
    FROM usuarios u 
    JOIN direcciones d ON u.direccion_id = d.id 
    WHERE d.pais = %s
""", ['México'])

# Para consultas que no retornan modelos
from django.db import connection

def reporte_ventas_por_mes():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                DATE_FORMAT(fecha, '%%Y-%%m') as mes,
                COUNT(*) as total_pedidos,
                SUM(total) as ventas_totales
            FROM pedidos 
            GROUP BY DATE_FORMAT(fecha, '%%Y-%%m')
            ORDER BY mes
        """)
        return cursor.fetchall()
```

## Vistas Django para Reportes

### views.py

```python
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum, Avg
from .models import Usuario, Pedido, Producto

def dashboard(request):
    # Estadísticas generales
    stats = {
        'total_usuarios': Usuario.objects.count(),
        'total_pedidos': Pedido.objects.count(),
        'total_productos': Producto.objects.count(),
        'ventas_totales': Pedido.objects.aggregate(Sum('total'))['total__sum'] or 0
    }
    
    # Ventas por país
    ventas_por_pais = Usuario.objects.values('direccion__pais').annotate(
        total_ventas=Sum('pedido__total'),
        total_pedidos=Count('pedido')
    ).order_by('-total_ventas')
    
    context = {
        'stats': stats,
        'ventas_por_pais': ventas_por_pais
    }
    
    return render(request, 'dashboard.html', context)

def api_productos_populares(request):
    productos = Producto.objects.annotate(
        veces_pedido=Count('pedidoproducto')
    ).order_by('-veces_pedido')[:10]
    
    data = [
        {
            'nombre': p.nombre,
            'veces_pedido': p.veces_pedido,
            'descripcion': p.descripcion
        }
        for p in productos
    ]
    
    return JsonResponse({'productos': data})
```

## Templates para Mostrar Datos

### dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Dashboard de Ventas</h1>
    
    <div class="stats-grid">
        <div class="stat-card">
            <h3>Total Usuarios</h3>
            <p>{{ stats.total_usuarios }}</p>
        </div>
        <div class="stat-card">
            <h3>Total Pedidos</h3>
            <p>{{ stats.total_pedidos }}</p>
        </div>
        <div class="stat-card">
            <h3>Ventas Totales</h3>
            <p>${{ stats.ventas_totales|floatformat:2 }}</p>
        </div>
    </div>
    
    <h2>Ventas por País</h2>
    <table>
        <thead>
            <tr>
                <th>País</th>
                <th>Total Pedidos</th>
                <th>Ventas Totales</th>
            </tr>
        </thead>
        <tbody>
            {% for venta in ventas_por_pais %}
            <tr>
                <td>{{ venta.direccion__pais }}</td>
                <td>{{ venta.total_pedidos }}</td>
                <td>${{ venta.total_ventas|floatformat:2 }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

## Django Admin para Gestión

### admin.py

```python
from django.contrib import admin
from .models import Direccion, Usuario, Producto, Pedido, PedidoProducto

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'colonia', 'ciudad', 'pais')
    list_filter = ('pais', 'ciudad')
    search_fields = ('calle', 'colonia', 'ciudad')

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha', 'total')
    list_filter = ('fecha', 'usuario__direccion__pais')
    search_fields = ('usuario__nombre', 'usuario__apellido')
    inlines = [PedidoProductoInline]
    date_hierarchy = 'fecha'

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'direccion')
    list_filter = ('direccion__pais',)
    search_fields = ('nombre', 'apellido')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion')
    search_fields = ('nombre', 'descripcion')
```

## Optimización y Mejores Prácticas

### 1. Optimización de Consultas

```python
# Usar select_related para ForeignKey
pedidos = Pedido.objects.select_related('usuario', 'usuario__direccion')

# Usar prefetch_related para ManyToMany
pedidos = Pedido.objects.prefetch_related('productos')

# Combinar ambos
pedidos = Pedido.objects.select_related('usuario').prefetch_related('productos')

# Usar only() para campos específicos
usuarios = Usuario.objects.only('nombre', 'apellido')

# Usar defer() para excluir campos pesados
productos = Producto.objects.defer('descripcion')
```

### 2. Índices de Base de Datos

```python
class Usuario(models.Model):
    nombre = models.CharField(max_length=45, db_index=True)
    apellido = models.CharField(max_length=45)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    
    class Meta:
        indexes = [
            models.Index(fields=['nombre', 'apellido']),
            models.Index(fields=['direccion'], name='idx_usuario_direccion'),
        ]
```

### 3. Conexiones de Base de Datos

```python
# settings.py - Configuración de conexiones múltiples
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'produccion_db',
        # ... otras configuraciones
    },
    'reportes': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reportes_db',
        # ... configuración para base de reportes
    }
}

# Usar diferentes bases de datos
# Escribir en producción
usuario = Usuario.objects.using('default').get(id=1)

# Leer de reportes
stats = Pedido.objects.using('reportes').aggregate(Sum('total'))
```

## Comandos de Gestión Personalizados

### management/commands/importar_datos.py

```python
from django.core.management.base import BaseCommand
from miapp.models import Usuario, Direccion, Producto

class Command(BaseCommand):
    help = 'Importa datos desde archivos CSV'

    def add_arguments(self, parser):
        parser.add_argument('--archivo', type=str, help='Archivo CSV a importar')

    def handle(self, *args, **options):
        import csv
        
        with open(options['archivo'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Lógica de importación
                pass
        
        self.stdout.write(
            self.style.SUCCESS('Datos importados exitosamente')
        )
```

## Testing con MySQL

### tests.py

```python
from django.test import TestCase
from django.db import transaction
from .models import Usuario, Direccion, Pedido

class PedidoTestCase(TestCase):
    def setUp(self):
        self.direccion = Direccion.objects.create(
            calle="Test St",
            colonia="Test",
            ciudad="Test City",
            pais="Test Country"
        )
        
        self.usuario = Usuario.objects.create(
            nombre="Test",
            apellido="User",
            direccion=self.direccion
        )

    def test_crear_pedido(self):
        pedido = Pedido.objects.create(
            fecha='2023-01-01',
            total=100.00,
            usuario=self.usuario
        )
        
        self.assertEqual(pedido.usuario.nombre, "Test")
        self.assertTrue(pedido.id is not None)

    def test_transaccion_atomica(self):
        with transaction.atomic():
            # Operaciones que deben ser atómicas
            pass
```

## Conclusión

La integración entre MySQL y Django ofrece una solución robusta para el desarrollo de aplicaciones web. Django proporciona:

- **ORM intuitivo** que simplifica las operaciones de base de datos
- **Migraciones automáticas** para evolución del esquema
- **Interfaz de administración** lista para usar
- **Herramientas de testing** integradas
- **Optimizaciones** para consultas complejas

Esta combinación es ideal para proyectos que requieren escalabilidad, rendimiento y facilidad de desarrollo.