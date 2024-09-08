FROM node:14-alpine AS build-stage

WORKDIR /opt/app-name

ARG COMMIT_SHA
ENV REACT_APP_COMMIT=$COMMIT_SHA
ENV REACT_APP_API_URL=https://ci_site_url/ci_branch
ENV PUBLIC_URL=/ci_branch

# Install dependencies
COPY package.json /opt/app-name/package.json
RUN cd /opt/app-name; npm install

# Build application
COPY . /opt/app-name
RUN cd /opt/app-name; npm run build

FROM nginx:alpine

COPY ./nginx_docker /etc/nginx/conf.d/default.conf
EXPOSE 3000
COPY --from=build-stage --chown=nginx:nginx /opt/app-name/build /www/build

