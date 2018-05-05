from flask import Flask
from flask_test.controllers import route1
from flask_test.controllers import error_handler
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello, world"


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
