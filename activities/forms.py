from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from .models import ActiviteBienEtre


class ActiviteForm(forms.ModelForm):
    class Meta:
        model = ActiviteBienEtre
        fields = ['mood', 'activity', 'comment']
        widgets = {
            'mood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment est votre humeur ?'}),
            'activity': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Décrivez votre activité'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Un commentaire ? (facultatif)'}),
        }
class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']  # Seul le username modifiable
        labels = {
            'username': 'Nom d\'utilisateur'
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']