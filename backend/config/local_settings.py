# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.
import os
from distutils.util import strtobool

DEBUG = bool(strtobool(os.environ.get('DJANGO_DEBUG', False)))

# Make these unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']
NEVERCACHE_KEY = os.environ['NEVERCACHE_KEY']

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": os.path.join('data', os.environ['DB_NAME']),
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# Allowed development hosts
ALLOWED_HOSTS = [os.environ['PROJECT_URL'], ]
