"""
Django settings for pagelabproject.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_UPLOAD_MAX_MEMORY_SIZE = 36214400
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qhk(v0g!4#(+_$$36hyks$nx!wkq$g&8qfgb92)92e)jkm1g%a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG_FLAG', False)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

if os.getenv('DJANGO_ALLOWED_HOST'): 
    ALLOWED_HOSTS.append(os.getenv('DJANGO_ALLOWED_HOST'))
    
INTERNAL_IPS = ['127.0.0.1',]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/var/webplatform/backups/pagelab'}
DBBACKUP_DATE_FORMAT = 'date-%d-%H'
DBBACKUP_FILENAME_TEMPLATE = 'pagelab-{datetime}.{extension}'


FORCE_SCRIPT_NAME = os.getenv('DJANGO_FORCE_SCRIPT_NAME', '/pagelab')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'report',
    'django_extensions',
    'dbbackup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')

ROOT_URLCONF = 'pageaudit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SETTINGS_PATH, '../templates'),
            'templates',
            'report/templates',
        ],
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

WSGI_APPLICATION = 'pageaudit.wsgi.application'


## Admins get 500 errors
## Managers get 404 errors
ADMINS = []
MANAGERS = []
ADMINS_EMAIL_TO_SMS = []


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': os.getenv('DJANGO_DB_NAME', 'perf_lab'),
        'USER': os.getenv('DJANGO_DB_USER', 'perf_lab'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD', ''),
        'HOST': os.getenv('DJANGO_DB_HOST', 'localhost'),
        'PORT': os.getenv('DJANGO_DB_PORT', 5432),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', '/var/webplatform/static/pagelab')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

STATIC_URL = os.getenv('DJANGO_STATIC_URL', '/static-pagelab/')
MEDIA_URL = os.getenv('DJANGO_MEDIA_URL', '/media/')

## Custom signin, signout, and post-signout page.
LOGIN_URL = '%s/report/signin/' % FORCE_SCRIPT_NAME
LOGOUT_URL = '%s/report/signout/' % FORCE_SCRIPT_NAME
LOGOUT_REDIRECT_URL = '%s/report/signedout/' % FORCE_SCRIPT_NAME


## Django first allows easy dev access via Django and wont error on LDAP for a local user.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

##LDAP_URL = ''

