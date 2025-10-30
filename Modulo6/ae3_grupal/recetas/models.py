from django.db import models

# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/imagenes/')

    def __str__(self):
        return self.nombre