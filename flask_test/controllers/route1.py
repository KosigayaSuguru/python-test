from flask import Blueprint
from flask_test.models.TestJsonSerialize import TestJsonSerialize
import pyckson
from flask import json
from flask import current_app
from threading import local
from flask_test.controllers.thread_local1 import ThreadLocalTest1
from flask_test.controllers.thread_local2 import ThreadLocalTest2
from time import sleep
import random

app_route1 = Blueprint("route1", __name__, url_prefix="/route1")


@app_route1.route("/test")
def test():
    return "/route1/test"


@app_route1.route("/test_thread_local")
def test_thread_local():
    """
    スレッドローカルで設定した値がスレッド毎（リクエスト毎）に別々で設定、取得できることの確認
    ※
    /test_thread_local に対してリクエストを連打し、スレッドローカルに対してスレッド毎に設定した値が
    別スレッドからの処理で上書きされないことを確認する
    """

    # staticなメソッドを使って、スレッドローカルに値を設定する
    ThreadLocalTest1.set()
    # 設定した値の表示が入れ子になるようにwaitをかける
    sleep(random.randint(2, 6))
    # スレッドローカルで設定した値をnewしたインスタンスを経由して表示
    ThreadLocalTest2().call()

    return "/route1/test"


@app_route1.route("/test_json_serialize")
def test_json_serialize():
    """オブジェクトのJson変換（jackson的な）のテスト
    """

    # dictionary型に変換される
    a = TestJsonSerialize("p1", "p2")
    # ログ出し
    current_app.logger.info(vars(a))
    # dictionaryをjson文字列に変換する
    return json.jsonify(pyckson.serialize(a))
