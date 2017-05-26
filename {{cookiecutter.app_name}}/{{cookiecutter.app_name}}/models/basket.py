from sqlalchemy.sql.expression import text

from {{cookiecutter.app_name}}.extensions import db


class Basket(db.Model):
    "A basket of foos."

    __tablename__ = 'basket'

    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column('name', db.Text(), nullable=False)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
    foos = db.relationship('Foo', backref='basket', lazy='dynamic')
