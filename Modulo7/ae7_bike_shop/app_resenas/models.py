from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from app_bicicletas.models import Bicicleta


class Resena(models.Model):
    """
    Modelo para reseñas de bicicletas
    Cada cliente puede dejar una reseña por bicicleta con puntuación de 1-5 estrellas
    """
    bicicleta = models.ForeignKey(
        Bicicleta,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    puntuacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Puntuación de 1 a 5 estrellas'
    )
    comentario = models.TextField(
        max_length=1000,
        help_text='Comparte tu experiencia con esta bicicleta'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
        ordering = ['-fecha_creacion']
        # Un usuario solo puede hacer una reseña por bicicleta
        unique_together = ['bicicleta', 'usuario']

    def __str__(self):
        return f'{self.usuario.first_name} - {self.bicicleta.marca} {self.bicicleta.modelo} ({self.puntuacion}⭐)'

    @property
    def estrellas_llenas(self):
        """Devuelve el número de estrellas llenas"""
        return range(self.puntuacion)

    @property
    def estrellas_vacias(self):
        """Devuelve el número de estrellas vacías"""
        return range(5 - self.puntuacion)
