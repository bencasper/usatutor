# pull official base image
FROM python:3.7.7-alpine
# set work directory
WORKDIR /Users/ben/usatutor/usatutor_admin

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install mysql dependencies
RUN apk update \
    && apk add mariadb-dev gcc python3-dev musl-dev
# https://github.com/python-pillow/Pillow/issues/1763
RUN apk add --no-cache freetype-dev jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers
RUN apk add --no-cache tzdata

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install https://github.com/darklow/django-suit/tarball/v2

# copy project
COPY . .