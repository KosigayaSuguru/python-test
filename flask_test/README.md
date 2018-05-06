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

## 実装部分

### Flask の Blueprint で app オブジェクトが欲しくなったら

↓の app を参照したい時、

```python
app = Flask(__name__)
```

別のファイルから呼び出す場合は、

```python
from flask import current_app

current_app.logger.info("hogehoge")
```

みたいな感じで呼び出せる。

※参考 http://d.hatena.ne.jp/heavenshell/20110824/1314190929

### 設定ファイルから設定値を取得する

* app.config.from_pyfile() を使う。  
* instance_relative_config=True にすると、インスタンスフォルダからの相対になる。  
  ※不要な設定な気がする。。
* 成功すると、app.config にkey:valueで値が追加される。  

※参考

* [Flaskにおける設定ファイルのベストプラクティス](https://qiita.com/nanakenashi/items/e272ff1aafb3889230bc)
* [Python公式](http://flask.pocoo.org/docs/1.0/config/)

### コントローラを分割する

* Blueprint を使う。
* app.register_blueprint() で Blueprint で設定したルーティングを Flask の app に登録する。

※参考

* [[Python] FlaskアプリケーションでBlueprintを用いてコントローラーを分割する](https://www.yoheim.net/blog.php?q=20160507)

### エラーハンドリング

* app.register_error_handler() 使う。  
* 継承してるクラスもSpringと同じ感覚で使える。  
  例：  
  Exception を対象としていて、Exceptionを継承しているSubExceptionがある場合、Exceptionで処理可能である。  
  SubException を対象とするハンドラも同時に存在する場合、そちらが優先される。
