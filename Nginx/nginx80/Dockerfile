FROM nginx:latest
LABEL authors="sergey.alekseev"

RUN cd /etc/nginx/conf.d && rm default.conf

COPY nginx80.conf /etc/nginx/conf.d/nginx.conf
COPY index.html /usr/share/nginx/html/index.html