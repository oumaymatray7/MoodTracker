from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from activities import views as activities_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajouter-activite/', activities_views.ajouter_activite, name='ajouter_activite'),
    path('', include('activities.urls')),
     path('login/', auth_views.LoginView.as_view(template_name='public/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
