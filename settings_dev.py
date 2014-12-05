"""
These settings are used by the ``manage.py`` command.

"""
DEBUG = True

SITE_ID = 1

USE_TZ = True
TIME_ZONE = 'UTC'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

EXTERNAL_APPS = [
    'bootstrap_admin',
    # Django core apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    # Required apps
    'international',
    'django_fsm',
    'rest_framework',
    'django_extensions',
    'django_filters'
]

INTERNAL_APPS = [
    'silver',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

ROOT_URLCONF = 'silver.urls'
STATIC_URL = '/static/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = 'secret'

REST_FRAMEWORK = {
    'PAGINATE_BY': 30,
    'PAGINATE_BY_PARAM': 'per_page',
    'MAX_PAGINATE_BY': 100,
}

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True
