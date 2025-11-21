from django.db import models

# Create your models here.

# Relación Muchos a Uno: Una categoría puede tener muchos productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre


# Relación Muchos a Muchos: Un producto puede tener muchas etiquetas
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#007bff', help_text='Color en formato hexadecimal')
    
    class Meta:
        db_table = 'etiquetas'
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Relación Muchos a Uno con Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    disponible = models.BooleanField(default=True)
    # Relación Muchos a Muchos con Etiqueta
    etiquetas = models.ManyToManyField(Etiqueta, related_name='productos', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.nombre


# Relación Uno a Uno: Cada producto tiene un único detalle
class DetalleProducto(models.Model):
    # Relación Uno a Uno con Producto
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='detalle')
    peso = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text='Peso en kilogramos')
    dimensiones_largo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text='Largo en centímetros')
    dimensiones_ancho = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text='Ancho en centímetros')
    dimensiones_alto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text='Alto en centímetros')
    material = models.CharField(max_length=100, blank=True, null=True)
    fabricante = models.CharField(max_length=100, blank=True, null=True)
    pais_origen = models.CharField(max_length=100, blank=True, null=True)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True, unique=True)
    
    class Meta:
        db_table = 'detalles_productos'
        verbose_name = 'Detalle de Producto'
        verbose_name_plural = 'Detalles de Productos'
    
    def __str__(self):
        return f"Detalle de {self.producto.nombre}"
    
    @property
    def dimensiones_completas(self):
        """Retorna las dimensiones en formato legible"""
        if self.dimensiones_largo and self.dimensiones_ancho and self.dimensiones_alto:
            return f"{self.dimensiones_largo} x {self.dimensiones_ancho} x {self.dimensiones_alto} cm"
        return "No especificado"
