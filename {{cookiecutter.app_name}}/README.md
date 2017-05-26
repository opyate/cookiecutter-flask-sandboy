# {{ cookiecutter.project_name }}

[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{ cookiecutter.app_name }}/.svg)](https://travis-ci.org/{{cookiecutter.github_username}}/{{ cookiecutter.app_name }})

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


{{ cookiecutter.project_short_description}}


## Quickstart

Run the following commands to bootstrap your environment.


    pip install -r requirements/dev.txt
    # Assuming Postgresql
    createdb  -h localhost -p 5432 -U postgres {{cookiecutter.app_name}}

    export {{cookiecutter.app_name | upper}}_SECRET=$(head /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 42 | head -n 1)
    export DATABASE_URL=postgres://postgres@localhost:5432/{{cookiecutter.app_name}}
    export HTTP_BASICAUTH_USERNAME=admin
    export HTTP_BASICAUTH_PASSWORD=password

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server

And finally, here's the backend developer's version of a pretty welcome screen:

    # create a foo
    curl -X POST \
      -H 'Content-Type: application/json' \
      http://localhost:5000/basket \
      -d '{"name":"Hello Basket"}'

    curl -X POST \
      -H 'Content-Type: application/json' \
      http://localhost:5000/foo \
      -d '{"bar":42,"baz":"quux","basket_id":1}'

    # read it back
    curl -X GET \
      -H 'Accept: application/json' \
      http://localhost:5000/foo/1


## Deployment

In your production environment, make sure the ``{{cookiecutter.app_name|upper}}_ENV`` environment variable is set to ``"prod"``.

## Shell

To open the interactive shell, run

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the [models]({{cookiecutter.app_name}}/models).

## Running Tests

To run all tests, run

    python manage.py test


## Migrations

Whenever a database migration needs to be made. Run the following commmands:

    python manage.py db migrate

This will generate a new migration script. Then run:

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
