from django.db import models


class Voluntario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre completo")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    class Meta:
        verbose_name = "Voluntario" # nombre singular
        verbose_name_plural = "Voluntarios" # nombre plural
        ordering = ['-fecha_registro'] # ordena por fecha de registro descendente

    def __str__(self): # método para representar el objeto como cadena
        return self.nombre # retorna el nombre del voluntario

    def eventos_asignados(self):
        """Retorna la cantidad de eventos asignados al voluntario"""
        return self.eventos.count()


class Evento(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título del evento")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha = models.DateField(verbose_name="Fecha del evento")
    voluntarios = models.ManyToManyField(
        Voluntario, 
        related_name="eventos",  # permite acceder a los eventos desde el voluntario
        blank=True, # permite que un evento no tenga voluntarios asignados inicialmente
        verbose_name="Voluntarios asignados" # nombre para el campo de voluntarios asignados
    )

    class Meta:
        verbose_name = "Evento" # nombre singular
        verbose_name_plural = "Eventos"  # nombre plural
        ordering = ['fecha'] # ordena por fecha ascendente

    def __str__(self):# método para representar el objeto como cadena
        return self.titulo # retorna el título del evento

    def cantidad_voluntarios(self): # metodo de instancia
        """Retorna la cantidad de voluntarios asignados al evento"""
        return self.voluntarios.count()
