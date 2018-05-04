from flask import Blueprint

app_route1 = Blueprint("route1", __name__, url_prefix="/route1")


@app_route1.route("/test")
def test():
    return "/route1/test"
