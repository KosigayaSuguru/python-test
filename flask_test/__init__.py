from flask import Flask
from flask_test.controllers import route1
from flask_test.controllers import error_handler
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config.from_pyfile(".\\config\\application.cfg")
print("---- show config ----")
# app.configに設定されている値を全部出す
for k, v in app.config.items():
    print(f"key: {k}, value: {v}")

# app.configの個別に確認したい値表示
print(f"app.env: {app.env}, app.debug: {app.debug}")
print(f"app.root_path: {app.root_path}")
print(f"app.instance_path: {app.instance_path}")
print("---------------------")


@app.route('/hello')
def hello_world():
    return "Hello, world"


@app.route('/favicon.ico')
def favicon():
    return "", 404


@app.route('/error_handle_test_badrequest')
def error_handle_test_badrequest():
    """エラーハンドリング確認用\n
    ※register_error_handler(BadRequest)でBadRequest例外を処理する確認\n
    """
    raise BadRequest("my BadRequest message")


@app.route('/error_handle_test')
def error_handle_test():
    """エラーハンドリング確認用\n
    ※register_error_handler(Exception)で例外を全部処理する確認\n
    ※BadRequest例外は、専用の例外ハンドラに行くのも確認\n
    """

    raise Exception("error_handle_test")


# コントローラをルーティングに追加
app.register_blueprint(route1.app_route1)

# エラーハンドラ追加（とりこぼした例外を全て処理する）
app.register_error_handler(Exception, error_handler.error)

# エラーハンドラ追加（BadRequest例外を処理する）
app.register_error_handler(
    BadRequest, error_handler.error_badrequest)
