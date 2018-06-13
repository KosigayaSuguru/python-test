from unittest.mock import patch

import pytest

# importのタイミングでグローバルに記載されているflaskの起動スクリプトが実行され、flaskが起動する
import flask_test
from flask_test.models import mock_test


@pytest.fixture(autouse=True)
def client():
    """メソッド毎に実行される
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
