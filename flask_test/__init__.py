from flask import Flask
from flask_test.controllers import route1

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello, world"


app.register_blueprint(route1.app_route1)
