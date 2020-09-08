# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.
import os
from distutils.util import strtobool

DEBUG = bool(strtobool(os.environ.get('DJANGO_DEBUG', "False")))

# Make these unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']
NEVERCACHE_KEY = os.environ['NEVERCACHE_KEY']

# Allowed development hosts
ALLOWED_HOSTS = [os.environ['PROJECT_URL'], ]
