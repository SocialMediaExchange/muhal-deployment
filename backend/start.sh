#!/bin/bash

python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py migrate

gunicorn -b 0.0.0.0:8000 --log-file=/var/log/gunicorn.log muhal.wsgi