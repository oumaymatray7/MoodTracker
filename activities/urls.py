from django.contrib.auth import views as auth_views
from django.urls import path

from activities import views as activities_views

from . import views

urlpatterns = [


    path('', views.accueil_public, name='accueil_public'),  
    # <<< AJOUTE BIEN name='accueil_public'
    path('profile/', views.profile, name='profile'),
path('logout/', views.custom_logout, name='logout'),

    path('send-feedback/', views.send_feedback, name='send_feedback'),
       path('contact/', views.contact_page, name='contact'),  
   path('ajouter-activite/', views.ajouter_activite, name='ajouter_activite'),

 path('feedbacks/', views.feedback_list, name='feedback_list'),

  path('modifier-activite/<int:id>/', activities_views.edit_activite, name='edit_entry'),
    path('supprimer-activite/<int:id>/', activities_views.delete_activite, name='delete_entry'),

    path('', activities_views.accueil_public, name='home'),
    path('mes-activites/', views.liste_activites, name='mes_activites'),
    path('register/', views.register, name='register'),
    path('send-feedback/', views.send_feedback, name='send_feedback'),
    path('login/', auth_views.LoginView.as_view(template_name='public/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('statistiques/', views.statistiques, name='statistiques'),
    path('themes/', views.themes, name='themes'),




]
