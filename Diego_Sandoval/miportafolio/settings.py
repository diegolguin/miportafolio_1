from pathlib import Path
import os
import dj_database_url  # Para conectar la DB de Railway

# ---------------------------------------------
# BASE GENERAL
# ---------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'ierCHCHTOB10xNkXoZpVdkOXOAVhiU9Hz0gFBHjy521yW9qoNS'
DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "miportafolio1-production-26c5.up.railway.app",
    "127.0.0.1",
    "localhost"
]

# ---------------------------------------------
# APLICACIONES
# ---------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectos',
]

# ---------------------------------------------
# MIDDLEWARE
# ---------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Requerido para Railway
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------------------------
# URLS / WSGI
# ---------------------------------------------
ROOT_URLCONF = 'miportafolio.urls'
WSGI_APPLICATION = 'miportafolio.wsgi.application'

# ---------------------------------------------
# TEMPLATES
# ---------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# ---------------------------------------------
# BASE DE DATOS
# ---------------------------------------------
if os.environ.get("DATABASE_URL"):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ["DATABASE_URL"],
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ---------------------------------------------
# INTERNACIONALIZACIÓN
# ---------------------------------------------
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------
# ARCHIVOS ESTÁTICOS (WhiteNoise)
# ---------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---------------------------------------------
# LOGIN / LOGOUT
# ---------------------------------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/lista/'
LOGOUT_REDIRECT_URL = '/login/'

# ---------------------------------------------
# CONFIG FINAL
# ---------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
