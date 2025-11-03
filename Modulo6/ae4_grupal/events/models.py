from django.db import models


class Event(models.Model):
    # Campo de texto para el nombre del evento (máximo 100 caracteres)
    name = models.CharField(max_length=100)
    # Campo de fecha para la fecha del evento
    date = models.DateField()
    # Campo de texto para la ubicación (opcional: blank=True)
    location = models.CharField(max_length=200, blank=True)
    def __str__(self):
        """Texto que se muestra cuando imprimimos el objeto"""
        return f"{self.name} ({self.date})"


class Participant(models.Model):
    # Relación con Event: un participante pertenece a un evento
    # on_delete=CASCADE: si se elimina el evento, se eliminan sus participantes
    # related_name='participants': permite acceder a los participantes desde el evento
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)
    # Campo de texto para el nombre del participante
    name = models.CharField(max_length=100)
    # Campo especial para email (valida formato de correo)
    email = models.EmailField()
    def __str__(self):
        """Texto que se muestra cuando imprimimos el objeto"""
        return f"{self.name} <{self.email}>"
