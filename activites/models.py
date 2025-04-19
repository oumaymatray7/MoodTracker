from django.contrib.auth.models import User
from django.db import models


class ActiviteBienEtre(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    type_activite = models.CharField(max_length=100)
    humeur = models.CharField(max_length=50)
    duree_minutes = models.PositiveIntegerField()
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type_activite} ({self.date}) - {self.utilisateur.username}"
