# {{ cookiecutter.app_name }}

[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{ cookiecutter.app_name }}/.svg)](https://travis-ci.org/{{cookiecutter.github_username}}/{{ cookiecutter.app_name }})

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


{{ cookiecutter.app_description}}


## Quickstart

Follow these 3 steps to bootstrap your environment and run the app.


### Step 1 - Install dependencies


    pip install -r requirements/dev.txt
    
### Step 2 - Create the database

E.g. if using Postgresql


    createdb  -h localhost -p 5432 -U postgres {{cookiecutter.app_name}}
    
### Step 3 - Quickstart


    ./quickstart.sh
    

### Step 4 - Load


Open [{{cookiecutter.app_name}}](http://127.0.0.1:5000) in a browser.

## Deployment

In your production environment, make sure the ``ENV`` environment variable is set to ``"prod"``.

### Heroku

Initialise {{cookiecutter.app_name}} as a Git repo with

    git init
    git add .
    git commit -m init
    
Create a new Heroku app

    heroku create
    heroku config:set HTTP_BASICAUTH_USERNAME=AzureDiamond
    heroku config:set HTTP_BASICAUTH_PASSWORD=hunter2
    heroku config:set ENV=prod
    heroku run python manage.py db upgrade
    
The last `upgrade` command will utilise the existing migration scripts we created in the [quickstart.sh](quickstart.sh).

Test the API on Heroku:

    curl -X POST \
      -u AzureDiamond:hunter2 \
      -H 'Content-Type: application/json' \
      https://fast-woodland-10679.herokuapp.com/basket \
      -d '{"name":"Hello Basket"}'
    

## Shell

To open the interactive shell, run

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the [models](app/models).

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
