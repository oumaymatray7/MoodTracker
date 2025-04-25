from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from activities.models import ActiviteBienEtre

from .forms import ActiviteForm


def accueil_public(request):
    return render(request, 'public/index.html')
def profile(request):
    return render(request, 'dashboard/profile.html')
def themes(request):
    return render(request, 'dashboard/themes.html')



@login_required
def ajouter_activite(request):
    if request.method == 'POST':
        form = ActiviteForm(request.POST)
        if form.is_valid():
            activite = form.save(commit=False)
            activite.utilisateur = request.user
            activite.save()
            return redirect('mes_activites')
    else:
        form = ActiviteForm()
    return render(request, 'ajouter_activite_simple.html', {'form': form})


def statistiques(request):
    return render(request, 'dashboard/statistiques.html')
def mes_activites(request):
    activites = ActiviteBienEtre.objects.filter(utilisateur=request.user).order_by('-date')
    return render(request, 'dashboard/mes_activites.html', {'activites': activites})

@login_required
def dashboard(request):
    activites = ActiviteBienEtre.objects.filter(utilisateur=request.user)
    return render(request, 'dashboard/base_dashboard.html', {'activites': activites})
def contact(request):
    return render(request, 'public/contact.html')  # crée ce template dans ton dossier templates/public

@login_required
def liste_activites(request):
    activites = ActiviteBienEtre.objects.filter(utilisateur=request.user)
    return render(request, 'dashboard/liste.html', {'activites': activites})
@login_required
def edit_entry(request, id):
    activite = get_object_or_404(ActiviteBienEtre, id=id, utilisateur=request.user)
    # ...


@login_required
def create_activite(request):
    if request.method == 'POST':
        form = ActiviteForm(request.POST)
        if form.is_valid():
            activite = form.save(commit=False)
            activite.utilisateur = request.user
            activite.save()
            return redirect('mes_activites')
    else:
        form = ActiviteForm()
    return render(request, 'dashboard/create.html', {'form': form})


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
def register(request):
   
    # (optionnel) tu peux afficher un message si déjà connecté
    if request.user.is_authenticated:
        messages.info(request, "Vous êtes déjà connecté.")


    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # connexion automatique après inscription
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('mes_activites')
    else:
        form = UserCreationForm()

    return render(request, 'public/register.html', {'form': form})