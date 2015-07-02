from flask.ext.sandboy import Sandboy

from .foo import Foo
from .basket import Basket


class APIScaffold(object):
    def init_app(self, app, db, auth=None):
        sandboy = Sandboy(app, db, [Foo, Basket])
        return sandboy
