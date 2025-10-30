from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")
    porciones = models.IntegerField()
    calorias = models.IntegerField(help_text="Cantidad de calorías por porción")

    def __str__(self):
        return self.nombre