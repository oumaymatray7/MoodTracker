import os
from pathlib import Path

# BASE_DIR représente la racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Application installée (assure-toi que "activities" est bien dedans)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'activities',  # ← Nom de ton app
     'crispy_forms',
     'crispy_bootstrap4',
]

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'activities' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuration des fichiers statiques
STATIC_URL = '/static/'

SECRET_KEY = 'django-insecure-!$2!v3y#8t@g1q8d4s@&y4gm*z+u8h1wn4+!r^l2y8_=6p8a#t'

# Mode développement (True) ou production (False)
DEBUG = True  # ← Tu peux mettre False plus tard en production

# Liste des hôtes autorisés à accéder à ton app (obligatoire si DEBUG=False)
ALLOWED_HOSTS = []  # ← Vide = accepté en local si DEBUG=True

# Configuration de la base de données par défaut (SQLite pour commencer)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuration du middleware (nécessaire pour le fonctionnement de base de Django)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuration de l'URL racine
ROOT_URLCONF = 'MoodTracker.urls'

# Configuration du serveur WSGI
WSGI_APPLICATION = 'MoodTracker.wsgi.application'

# Configuration de la langue et du fuseau horaire
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Fichiers médias (si besoin plus tard)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'mes_activites'
LOGOUT_REDIRECT_URL = 'login'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
