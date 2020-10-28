# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.
import os
from distutils.util import strtobool

DEBUG = bool(strtobool(os.environ.get('DJANGO_DEBUG', "False")))

# Make these unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']
NEVERCACHE_KEY = os.environ['NEVERCACHE_KEY']

# Allowed development hosts
ALLOWED_HOSTS = [os.environ['PROJECT_URL'], 'backend']


ADMINS = [(email.split('@')[0], email) for email in os.environ['ADMINS'].split(',')]
MANAGERS = [(email.split('@')[0], email) for email in os.environ['MANAGERS'].split(',')]

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
SERVER_EMAIL = os.environ['SERVER_EMAIL']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_SSL = True