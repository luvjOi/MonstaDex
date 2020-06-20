import os

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(application)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "settings.base")
