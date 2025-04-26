from django.contrib.auth.models import User
from django.db import models


class ActiviteBienEtre(models.Model):
    mood = models.CharField(max_length=100)
    activity = models.TextField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.date}"
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    msg_type = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.msg_type})"