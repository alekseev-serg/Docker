#!/bin/sh

python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn -c "/app/gunicorn_config.py" ABCofDevops.wsgi