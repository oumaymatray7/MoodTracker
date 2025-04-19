from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from activities.models import ActiviteBienEtre


def accueil_public(request):
    return render(request, 'public/index.html')

def dashboard(request):
    activites = ActiviteBienEtre.objects.filter(utilisateur=request.user)
    return render(request, 'dashboard/base_dashboard.html', {'activites': activites})

@login_required
def liste_activites(request):
    return render(request, 'dashboard/liste.html')
