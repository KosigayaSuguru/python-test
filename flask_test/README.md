# Flaskメモ

## 起動

### ローカルで起動する

下記の環境変数の設定が必要

* FLASK_APP
  1. 起動するPythonファイルを指定する
    ※未指定の場合、app.pyがデフォルトっぽい？
  2. \__init__.py が含まれるフォルダ名を指定する
* FLASK_ENV
  * development とか
    * 指定しないとローカル起動時に怒られる（かも。。

#### DOSプロンプトからファイル名を指定して起動するコマンド

```code
set FLASK_APP=main.py
set FLASK_ENV=development
flask run
```

#### \__init__.py を持つフォルダを指定して起動するコマンド

下記のようなフォルダ構成の状態で、

```code
c:\self\program\python-test\flask_test
│  __init__.py
```

下記、実行

```code
cd c:\self\program\python-test
set FLASK_APP=flask_test
set FLASK_ENV=development
flask run

※ カレントが c:\self\program\python-test で　flask run することに注意
```
