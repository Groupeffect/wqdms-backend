FROM docker.io/python:3.12-slim-bookworm:latest as pyimage
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN apt update && apt -y dist-upgrade
RUN apt install -y nginx \
    gdal-bin geos-bin \
    libsqlite3-mod-spatialite \
    supervisor \
    git
RUN pip install --upgrade pip

FROM pyimage
WORKDIR /app
COPY ./app /app
RUN pip install -r /app/requirements.txt
COPY ./supervisor/. /etc/supervisor/conf.d/.
COPY ./nginx/. /etc/nginx/conf.d/.
EXPOSE 80 8081