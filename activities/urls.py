from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil_public, name='accueil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/liste/', views.liste_activites, name='liste'),
]
