FROM python:3.9-slim

RUN mkdir -p /opt/app_name

COPY . /opt/app_name

RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen ru_RU.UTF-8 && \
    apt-get install -y python3-dev && \
    apt-get install -y gcc libsasl2-dev python3-dev libldap2-dev libssl-dev && \
    pip3 install -r /opt/app_name/requirements.txt

WORKDIR /opt/app_name



CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
