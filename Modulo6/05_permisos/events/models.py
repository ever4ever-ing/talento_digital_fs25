from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    is_private = models.BooleanField(default=False)
    allowed_users = models.ManyToManyField(User, blank=True, related_name='allowed_events')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')

    def __str__(self):
        return self.title

    def can_access(self, user):
        if not self.is_private:
            return True
        return user in self.allowed_users.all() or user == self.creator
