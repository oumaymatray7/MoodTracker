from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil_public, name='accueil_public'),   # page d'accueil publique
    path('dashboard/', views.dashboard, name='dashboard'),   # tableau de bord
    path('dashboard/liste/', views.liste_activites, name='liste'),  # liste des activités
    path('send-feedback/', views.send_feedback, name='send_feedback'),  # Formulaire de contact
]
