from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    is_private = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')

    class Meta:
        permissions = [
            ("can_manage_event", "Can create and manage events"),# sin este permiso, no se podran crear eventos
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Redirige a la lista de eventos tras crear/editar
        return reverse('events:list')
