import os
import sys

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Also add ../../apps to python path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# =============================================================================
# # Django
# =============================================================================
ALLOWED_HOSTS = ['*']
USE_X_FORWARDED_HOST = True

SITE_ID = 1

SITE_DOMAIN = os.environ.get('SITE_DOMAIN', 'http://localhost')

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'whitenoise',
    'rest_framework',
    'monster',
    'attacks',
    'bindings',
    'players',

    ## Sorl Thumbnail'
    'sorl.thumbnail',
    'django_extensions',

)
# OUR_APPS = (
#     'monster',
#     'attacks',
#     'bindings',
#     'players',
# )
# INSTALLED_APPS = THIRD_PARTY_APPS + OUR_APPS

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'src/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SECRET_KEY = os.environ.get("SECRET_KEY", '{{ secret_key }}')

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

DEFAULT_FROM_EMAIL = 'Do Not Reply <donotreply@blank.com>'
SERVER_EMAIL = 'Do Not Reply <donotreply@blank.com>'

# =============================================================================
# # Wagtail
# =============================================================================
WAGTAIL_SITE_NAME = 'Monsta Dex'

# =============================================================================
# Debugging
# =============================================================================
DEBUG = os.environ.get('DEBUG', True)

# =============================================================================
# Database
# =============================================================================

DATABASES = {'default': {}}


db_from_env = dj_database_url.config()
if db_from_env:
    DATABASES['default'].update(db_from_env)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'monstadex.db',
        }
    }

# DATABASES['default'] = d/j_database_url.config()

# # =============================================================================
# # SSL
# # =============================================================================
# if os.environ.get('USE_SSL'):
#     SECURE_SSL_REDIRECT = True
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# else:
#     # Allows us to use with django-oauth-toolkit on localhost sans https
#     SESSION_COOKIE_SECURE = False


# =============================================================================
# DRF
# =============================================================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DATETIME_INPUT_FORMATS': (
        'iso-8601',
        '%B %d, %Y',
    )
}

# =============================================================================
# OAuth
# =============================================================================
CORS_ORIGIN_ALLOW_ALL = True

if not DEBUG:
    assert not CORS_ORIGIN_ALLOW_ALL, "Disable CORS_ORIGIN_ALLOW_ALL if we're not in DEBUG mode"

# =============================================================================
# Storage
# =============================================================================
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'src/static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
MEDIA_URL = '/media/'

# =============================================================================
# Debug
# =============================================================================
if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE = (
                     'debug_toolbar.middleware.DebugToolbarMiddleware',
                     'querycount.middleware.QueryCountMiddleware',
                 ) + MIDDLEWARE  # we want Debug Middleware at the top

    INTERNAL_IPS = ['127.0.0.1']

    import socket

    try:
        INTERNAL_IPS.append(socket.gethostbyname(socket.gethostname())[:-1])
    except socket.gaierror:
        pass

    QUERYCOUNT = {
        'IGNORE_REQUEST_PATTERNS': [
            r'^/admin/',
            r'^/static/',
        ]
    }

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True
    }

LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'
