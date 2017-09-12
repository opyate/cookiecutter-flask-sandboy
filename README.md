# cookiecutter-flask-sandboy

A Flask-Sandboy template for [cookiecutter](https://github.com/audreyr/cookiecutter).

[![Build Status](https://travis-ci.org/opyate/cookiecutter-flask-sandboy.svg)](https://travis-ci.org/opyate/cookiecutter-flask-sandboy)

## Use it now

    pip install cookiecutter
    cookiecutter https://github.com/opyate/cookiecutter-flask-sandboy.git
    
You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

### Use it now, on Heroku

Run

    heroku create
    
The previous command will output your Heroku app name, e.g.

> Creating app... done, ⬢ serene-badger-31337
> https://serene-badger-31337.herokuapp.com/ | https://git.heroku.com/serene-badger-31337.git

Continue with these commands, substituting `https://git.heroku.com/serene-badger-31337.git` with your Git remote:

    git init ; git add . ; git commit -m init
    git remote add heroku https://git.heroku.com/serene-badger-31337.git
    git push heroku master
    
Now visit your app and continue the setup:

    heroku open

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


