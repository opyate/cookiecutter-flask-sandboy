from flask.ext.sandboy import Sandboy

from .foo import Foo


class APIScaffold(object):

    def init_app(self, app, db, auth=None):
        sandboy = Sandboy(app, db, 
            [Foo])
        return sandboy