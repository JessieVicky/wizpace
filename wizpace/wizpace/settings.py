"""
Django settings for wizpace project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# PATHs
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

STATIC_PATH = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Absolute path to the media directory
MEDIA_URL = '/media/'

# DIRs
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

STATICFILES_DIRS = (
    STATIC_PATH,
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd2=v$rg1x55vxn7-!h51(pr5&^5p(y^xyvns#@m0vtbp7fig8&'

# SECURITY WARNING: don't run with debug turned on in production!
import socket
if 'Wizpace' in socket.gethostname():
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.wizpace.se', '.wizpace.com']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'bootstrap3',
    'account',
    'pinax_theme_bootstrap',
    'bootstrapform',
    'shortuuidfield',
    'cities_light',
    'django_extensions',
    # 'django_countries',
    # Wizpace apps
    'custom_reg',
    'custom_settings',
    'user_profiles',
    'custom_projects',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default, requires by django
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',

    # django-auser-accounts
    'account.context_processors.account',
    'django.core.context_processors.request',
    'pinax_theme_bootstrap.context_processors.theme',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',

    # django-auser-accounts
    'account.auth_backends.EmailAuthenticationBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # django-auser-accounts
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'wizpace.urls'

WSGI_APPLICATION = 'wizpace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'NAME': 'wizpace_db',
	'USER': 'wizpace',
	'PASSWORD': 'FAB07DC896801366CBC79F9AF4B939EB5E4628E49983A56A7E2097BDDE07EDF6',
	'HOST': 'localhost',
	'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LOGIN_URL = '/account/login/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if DEBUG:
    ACCOUNT_OPEN_SIGNUP = True
else:
    ACCOUNT_OPEN_SIGNUP = False

SITE_ID = 1

# Email Settings
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST_USER = 'register@wizpace.com'
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = 'Dragonball0759'
    EMAIL_HOST = 'mail.gandi.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

# Force english
from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
)

# django-user-accounts settings
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_USER_DISPLAY = lambda user: user.email

# COUNTRIES_OVERRIDE = {
#     'AX': '---------------'
# }

# COUNTRIES_FIRST = ['AX']
