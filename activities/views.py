import json

from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from activities.models import ActiviteBienEtre

from .forms import ActiviteForm, CustomPasswordChangeForm, UpdateAccountForm
from .models import ActiviteBienEtre, Feedback


@csrf_exempt


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

from activities.models import ActiviteBienEtre


@login_required
def liste_activites(request):
    activites = ActiviteBienEtre.objects.filter(utilisateur=request.user)
    return render(request, 'dashboard/liste.html', {'activites': activites})

@login_required
def edit_entry(request, id):
    activite = get_object_or_404(ActiviteBienEtre, id=id, utilisateur=request.user)
    # ...



def custom_logout(request):
    logout(request)
    return redirect('login')  # ou retour accueil_public

@login_required
def edit_activite(request, id):
    activite = get_object_or_404(ActiviteBienEtre, id=id, utilisateur=request.user)
    
    if request.method == 'POST':
        form = ActiviteForm(request.POST, instance=activite)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activité modifiée avec succès.')
            return redirect('mes_activites')  # <<< corrigé ici
    else:
        form = ActiviteForm(instance=activite)
    
    return render(request, 'dashboard/edit_activite.html', {'form': form})


@login_required
def delete_activite(request, id):
    activite = get_object_or_404(ActiviteBienEtre, id=id, utilisateur=request.user)
    
    if request.method == 'POST':
        activite.delete()
        messages.success(request, 'Activité supprimée avec succès.')
        return redirect('mes_activites')  # <<<< bien corrigé ici
    return render(request, 'dashboard/delete_activite.html', {'activite': activite})

@login_required
def profile(request):
    if request.method == 'POST':
        account_form = UpdateAccountForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if account_form.is_valid() and password_form.is_valid():
            account_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Important : éviter la déconnexion
            messages.success(request, 'Votre compte a été mis à jour avec succès.')
            return redirect('profile')
    else:
        account_form = UpdateAccountForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'dashboard/profile.html', {
        'account_form': account_form,
        'password_form': password_form
    })
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
def contact_page(request):
    return render(request, 'public/contact.html')


def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'dashboard/feedback_list.html', {'feedbacks': feedbacks})

@login_required  # optionnel
def send_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg_type = request.POST.get('type')
        message = request.POST.get('message')

        # ➡️ Enregistrer dans la base de données
        Feedback.objects.create(
            name=name,
            email=email,
            msg_type=msg_type,
            message=message
        )

        messages.success(request, "Merci ! Votre message a été envoyé.")
        return HttpResponseRedirect(reverse('contact'))  # ou accueil_public
    return HttpResponseRedirect(reverse('contact'))  # Si ce n'est pas un POST, retourner vers la page contact aussi

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

@login_required
def statistiques(request):
    categories_data = ActiviteBienEtre.objects.filter(utilisateur=request.user) \
        .values('activity') \
        .annotate(total=Count('id')) \
        .order_by('activity')

    monthly_data = ActiviteBienEtre.objects.filter(utilisateur=request.user) \
        .annotate(month=TruncMonth('date')) \
        .values('month') \
        .annotate(total=Count('id')) \
        .order_by('month')

    context = {
    'categories_data': json.dumps(list(categories_data), cls=DjangoJSONEncoder),
    'monthly_data': json.dumps(list(monthly_data), cls=DjangoJSONEncoder),
}

    return render(request, 'dashboard/statistique.html', context)