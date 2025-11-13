from django.db import models

class Bicicleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)  # mtb, ruta, enduro, trail, bmx
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    disponible = models.BooleanField(default=True)
    anio = models.IntegerField()
    imagen = models.ImageField(upload_to='bicicletas/', blank=True, null=True)
    def precio_formateado(self):
        return f"{self.precio:,.0f}".replace(",", ".")
    def __str__(self):
        return f"{self.marca} {self.modelo}"