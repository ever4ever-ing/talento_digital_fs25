from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    ubicacion = models.CharField(max_length=300)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='eventos_creados')
    participantes = models.ManyToManyField(User, related_name='eventos_participando', blank=True)

    def __str__(self):
        return self.titulo
    
    def total_participantes(self):
        """Retorna el número total de participantes"""
        return self.participantes.count()
    
    def esta_participando(self, user):
        """Verifica si un usuario está participando en el evento"""
        return self.participantes.filter(id=user.id).exists()