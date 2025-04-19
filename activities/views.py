from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from activities.models import ActiviteBienEtre


def accueil_public(request):
    return render(request, 'public/index.html')

def dashboard(request):
    activites = ActiviteBienEtre.objects.filter(utilisateur=request.user)
    return render(request, 'dashboard/base_dashboard.html', {'activites': activites})

@login_required
def liste_activites(request):
    return render(request, 'dashboard/liste.html')



@login_required  # facultatif pour ce type de formulaire
def send_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg_type = request.POST.get('type')
        message = request.POST.get('message')

        print("Feedback reçu :", name, email, msg_type, message)

        messages.success(request, "Merci ! Votre message a été envoyé.")
        return HttpResponseRedirect(reverse('accueil_public'))

    return HttpResponseRedirect(reverse('accueil_public'))