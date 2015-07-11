import json

from django.core.exceptions import ImproperlyConfigured

from .base import *

with open("secrets.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

DEBUG = False

ALLOWED_HOSTS = ['gardenharmony.com']

TIME_ZONE = 'America/New_York'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': 'gardenharmony',
        'PASSWORD': get_secret("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}
