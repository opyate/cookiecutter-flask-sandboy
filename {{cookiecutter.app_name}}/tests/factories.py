# -*- coding: utf-8 -*-
from factory import Sequence, PostGenerationMethodCall
from factory.alchemy import SQLAlchemyModelFactory

from {{cookiecutter.app_name}}.models.foo import Foo
from {{cookiecutter.app_name}}.extensions import db


class BaseFactory(SQLAlchemyModelFactory):

    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class FooFactory(BaseFactory):
    bar = Sequence(lambda n: n)
    baz = Sequence(lambda n: 'baz-%s' % n)

    class Meta:
        model = Foo
