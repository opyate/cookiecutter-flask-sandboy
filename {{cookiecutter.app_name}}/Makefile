.PHONY: test run

test:
	python manage.py test

run:
	python manage.py server

db_init:
	python manage.py db migrate
	python manage.py db upgrade

db_run_once:
	python manage.py db init


