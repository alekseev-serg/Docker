import os.path

path = os.path.abspath(os.curdir)

command = path + '/env/bin/gunicorn'
pythonpath = path + '/ABCofDevops'
bind = '0.0.0.0:8000'
workers = 5
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=ABCofDevops.settings'
