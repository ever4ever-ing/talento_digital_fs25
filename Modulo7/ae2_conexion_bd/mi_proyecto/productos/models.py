from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)