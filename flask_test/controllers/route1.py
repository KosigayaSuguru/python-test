from flask import Blueprint
from flask_test.models.TestJsonSerialize import TestJsonSerialize
import pyckson
from flask import json

app_route1 = Blueprint("route1", __name__, url_prefix="/route1")


@app_route1.route("/test")
def test():
    return "/route1/test"


@app_route1.route("/test_json_serialize")
def test_json_serialize():
    """オブジェクトのJson変換（jackson的な）のテスト
    """
    # dictionary型に変換される
    a = TestJsonSerialize("p1", "p2")
    # dictionaryをjson文字列に変換する
    return json.jsonify(pyckson.serialize(a))
