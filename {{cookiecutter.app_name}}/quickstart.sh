#!/usr/bin/env bash

export SECRET_KEY=$(head /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 42 | head -n 1 | tr -d '\n')
export DATABASE_URL=postgres://postgres@localhost:5432/{{cookiecutter.app_name}}
export HTTP_BASICAUTH_USERNAME=AzureDiamond
export HTTP_BASICAUTH_PASSWORD=hunter2

# see https://flask-migrate.readthedocs.io/en/latest/ for the meanings of
# init, migrate, and upgrade.
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py server

