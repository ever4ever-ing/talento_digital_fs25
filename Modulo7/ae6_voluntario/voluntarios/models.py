from django.db import models


class Voluntario(models.Model):
    """
    Modelo que representa a un voluntario registrado en el sistema.
    """
    nombre = models.CharField(max_length=255, verbose_name="Nombre completo")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    class Meta:
        verbose_name = "Voluntario"
        verbose_name_plural = "Voluntarios"
        ordering = ['-fecha_registro']

    def __str__(self):
        return self.nombre

    def eventos_asignados(self):
        """Retorna la cantidad de eventos asignados al voluntario"""
        return self.eventos.count()


class Evento(models.Model):
    """
    Modelo que representa un evento comunitario organizado por la ONG.
    """
    titulo = models.CharField(max_length=255, verbose_name="Título del evento")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha = models.DateField(verbose_name="Fecha del evento")
    voluntarios = models.ManyToManyField(
        Voluntario, 
        related_name="eventos",
        blank=True,
        verbose_name="Voluntarios asignados"
    )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha']

    def __str__(self):
        return self.titulo

    def cantidad_voluntarios(self):
        """Retorna la cantidad de voluntarios asignados al evento"""
        return self.voluntarios.count()
