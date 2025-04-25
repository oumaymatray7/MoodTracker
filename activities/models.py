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
