import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-only'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rental',  # <-- our app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cps510_gui.urls'
TEMPLATES = [{
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS':[BASE_DIR/'templates'], 'APP_DIRS':True,
    'OPTIONS':{'context_processors':[
        'django.template.context_processors.debug','django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages',
    ]},
}]
WSGI_APPLICATION = 'cps510_gui.wsgi.application'

DATABASES = {
    "default": {  # site/admin -> always runs
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "oracle": {   # used only by our /db-setup/ buttons
        "ENGINE": "django.db.backends.oracle",
        "NAME": os.getenv("ORACLE_DSN", "oracle.scs.ryerson.ca:1521/orcl"),
        "USER": os.getenv("ORACLE_USER", ""),
        "PASSWORD": os.getenv("ORACLE_PASSWORD", ""),
    },
}


LANGUAGE_CODE='en-us'
TIME_ZONE='America/Toronto'
USE_I18N=True
USE_TZ=True
STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

