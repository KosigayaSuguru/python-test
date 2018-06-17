from unittest.mock import patch

import pytest

# importのタイミングでグローバルに記載されているflaskの起動スクリプトが実行され、flaskが起動する
import flask_test
from flask_test.models import mock_test


def debugger_start_VisualStudioCode():
    """
    pytestでデバッガを使う_VisualStudioCode

    python -d -m pytest flask_test/tests/
    でpytestを起動させる。
    waitがかかるので、そのタイミングで、リモートデバッグを実行する
    ※事前にブレークポイントを張っておくこと
    ※pytestが標準出力と標準エラー出力をキャプチャしているので、print()の中身はでない。
      出したい時は、pytestのオプションの -s を付ける
      python -d -m pytest flask_test/tests/ -s
    """

    import ptvsd
    from time import sleep
    print('waiting...')
    ptvsd.enable_attach('my_secret', address=('0.0.0.0', 3000))
    ptvsd.wait_for_attach()
    sleep(1)
    print('Debug Start')


@pytest.fixture(autouse=True)
def client():
    """
    メソッド毎に実行される
    ※flaskをメソッド毎に起動させている
    """

    flask_test.app.config['TESTING'] = True
    flask_test.app.config['DEBUG'] = True
    client = flask_test.app.test_client()
    print("")
    print("flask run")
    yield client
    print("flask end")


@pytest.fixture(autouse=True, scope="class")
def class_fixture():
    """クラス毎に実行される
    """

    print("class_fixture() start")
    yield
    print("class_fixture() end")


class TestClass():

    def test_first(self, client, monkeypatch):
        def hoge():
            return "auauaua"

        print("test_first() run")

        # flask_test.models.mock_test.mock_test()の動作をhoge()に置き換える
        monkeypatch.setattr(flask_test.models.mock_test, "mock_test", hoge)
        assert mock_test.mock_test() == "auauaua"

    def test_2nd(self):
        print("test_2nd() run")
        assert 0 == 0

    def test_標準出力のキャプチャ(self, capsys):
        print("test_first() run")
        print("test_first() run")
        captured = capsys.readouterr()
        # pytest.set_trace()
        assert captured.out == "test_first() run\ntest_first() run\n"

    def test_pytestでデバッガを使う_VisualStudioCode(self):
        # vscでデバッグする時はコメントアウトする
        # 詳細は↓のコメント参照
        # debugger_start_VisualStudioCode()

        # vscの場合、launch.json内の、"pytestでデバッガを使う"でもデバッガ起動できる

        a = 0
        b = 1
        c = {"hoge", 123}
        print("")
