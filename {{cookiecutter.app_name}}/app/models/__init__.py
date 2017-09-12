from flask_sandboy import Sandboy

from .foo import Foo
from .basket import Basket


class APIScaffold(object):
    def init_app(self, app, db, decorators=[]):
        sandboy = Sandboy(app, db, [Foo, Basket], decorators=decorators)
        return sandboy
