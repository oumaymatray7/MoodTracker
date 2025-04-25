from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil_public, name='accueil_public'),
    path('mes-activites/', views.liste_activites, name='mes_activites'),
    path('register/', views.register, name='register'),
    path('send-feedback/', views.send_feedback, name='send_feedback'),
     path('login/', auth_views.LoginView.as_view(template_name='public/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
