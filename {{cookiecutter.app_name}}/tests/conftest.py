# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import pytest

from {{ cookiecutter.app_name }}.settings import TestConfig
from {{ cookiecutter.app_name }}.app import create_app
from {{ cookiecutter.app_name }}.extensions import db as _db


@pytest.yield_fixture(scope='session')
def app():
    _app = create_app(TestConfig)
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    with app.test_client() as client:
        _db.app = app
        _db.create_all()
        yield client
        _db.session.rollback()
        _db.drop_all()
