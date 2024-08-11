FROM python:3.11.6-alpine3.18 as dependencies

WORKDIR /app

RUN pip install --upgrade --no-cache pip
RUN apk update --no-cache \
    && apk add gcc git g++ musl-dev make python3-dev libc-dev libffi-dev openssl-dev postgresql-dev postgresql-client
RUN pip install --upgrade pip

FROM dependencies as BASE
ADD . /app
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]