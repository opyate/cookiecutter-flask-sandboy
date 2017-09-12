# -*- coding: utf-8 -*-
from factory import Sequence, PostGenerationMethodCall
from factory.alchemy import SQLAlchemyModelFactory

from app.models.foo import Foo
from app.extensions import db


class BaseFactory(SQLAlchemyModelFactory):

    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class FooFactory(BaseFactory):
    bar = Sequence(lambda n: n)
    baz = Sequence(lambda n: 'baz-%s' % n)

    class Meta:
        model = Foo
