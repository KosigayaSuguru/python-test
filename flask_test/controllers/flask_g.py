from flask import g
import random


class FlaskG:

    def getData(self):
        if not hasattr(g, "hoge"):
            g.hoge = "flask.gだよ" + str(random.randint(1, 100))
        return g.hoge
