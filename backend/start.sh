#!/bin/bash

pipenv run python manage.py compilemessages
pipenv run python manage.py collectstatic --noinput
pipenv run python manage.py migrate

pipenv run gunicorn -b 0.0.0.0:8000 --log-file=/var/log/gunicorn.log muhal.wsgi