from django.db import models
from django.conf import settings


class Tarea(models.Model):
	"""Modelo para representar una tarea del usuario."""
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(blank=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tareas')
	creada_en = models.DateTimeField(auto_now_add=True)
	completada = models.BooleanField(default=False)

	class Meta:
		ordering = ['-creada_en']

	def __str__(self):
		return f"{self.titulo} ({'✓' if self.completada else ' '})"

