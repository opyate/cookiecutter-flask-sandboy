from sqlalchemy.sql.expression import text

from application.extensions import db


class Foo(db.Model):
    "A foo."

    __tablename__ = 'foo'

    id = db.Column('id', db.Integer(), primary_key=True)
    bar = db.Column('bar', db.Integer(), nullable=False)
    baz = db.Column('baz', db.Text(), nullable=False)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'))
