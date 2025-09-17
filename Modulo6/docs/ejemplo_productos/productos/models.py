# productos/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) # blank=True permite que el campo esté vacío en formularios
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, default='General') # Campo adicional con valor por defecto
    
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Se añade la fecha automáticamente al crear
    

    def __str__(self):
        return self.nombre
