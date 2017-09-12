# cookiecutter-flask-sandboy

A Flask-Sandboy template for [cookiecutter](https://github.com/audreyr/cookiecutter).

[![Build Status](https://travis-ci.org/opyate/cookiecutter-flask-sandboy.svg)](https://travis-ci.org/opyate/cookiecutter-flask-sandboy)

## Use it now

    pip install cookiecutter
    cookiecutter https://github.com/opyate/cookiecutter-flask-sandboy.git
    
You will be asked about your basic info (app name, etc.). This info will be used in your new project.

**Your newly-generated app is self-documenting, and its README will have more information on how to continue.**

## Features

- Flask-Sandboy for quick REST on your models
- Flask-SQLAlchemy with basic model
- Easy database migrations with Flask-Migrate
- Procfile for deploying to a PaaS (e.g. Heroku)
- One-click deploy for Heroku
- pytest and Factory-Boy for testing (example tests included)
- A simple ```manage.py``` script.
- Caching using Flask-Cache
- Utilizes best practices: [Blueprints](http://flask.pocoo.org/docs/blueprints/) and [Application Factory](http://flask.pocoo.org/docs/patterns/appfactories/) patterns

## Opinions

This template has the following opinions:

- the test database must be the same as the development database must be the same as the production database

# Inspiration

- [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)
- My [fork](https://github.com/opyate/flask_sandboy) of [sandboy](https://github.com/jeffknupp/flask_sandboy)


## License

MIT licensed.

## Changelog

### 0.1.1 (2015-07-02)

- Add extra model to show relations

### 0.1.0 (2015-06-16)

- First iteration
- Sandboy integration
- Working demo model


