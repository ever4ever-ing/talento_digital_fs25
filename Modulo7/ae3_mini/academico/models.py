
from django.db import models

class Profesor(models.Model):
	nombre = models.CharField(max_length=100)
	especialidad = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Curso(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')

	def __str__(self):
		return self.nombre

class Estudiante(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.nombre

class Perfil(models.Model):
	estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name='perfil')
	biografia = models.TextField()
	foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
	redes_sociales = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return f"Perfil de {self.estudiante.nombre}"

class Inscripcion(models.Model):
	ESTADO_CHOICES = (
		('A', 'Activo'),
		('F', 'Finalizado'),
	)
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	fecha_inscripcion = models.DateField(auto_now_add=True)
	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')
	nota_final = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

	class Meta:
		unique_together = ('estudiante', 'curso')

	def __str__(self):
		return f"{self.estudiante.nombre} en {self.curso.nombre}"
