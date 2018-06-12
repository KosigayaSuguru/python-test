# python

## 環境設定

### windows環境にinstallする

<https://www.python.jp/install/windows/index.html> が分かりやすい


### Python実行時に個別でパスを通したい時

環境変数 PYTHONPATH に個別に追加したいパスを登録する。  
  
※参考

* [PYTHONPATHとは](https://ja.stackoverflow.com/questions/12174/pythonpath%E3%81%A8%E3%81%AF)
* launch.jsonの　"flask runを使わないで起動させる"　の env のところ

### Python実行時に検索対象となるモジュール


* 入力されたスクリプトのあるディレクトリ (あるいはファイルが指定されなかったときはカレントディレクトリ)。
* PYTHONPATH (ディレクトリ名のリスト。シェル変数の PATH と同じ構文)。
* インストールごとのデフォルト。
* ※上記のパス"のみ"が対象で、そこから下の階層を再帰的に検索するわけではないので要注意
  * 下の階層も対象にしたい場合は個別に追加する必要がある

pythonコマンド実行時点でどこを検索しに行っているかを確認するのは、

```python
import sys
sys.path
```

※参考

* [公式](https://docs.python.jp/3/tutorial/modules.html) の"モジュール検索パス"

### pipコマンドからinstall出来ない時

<https://pypi.org/project/virtualenv/#files>

から、入れたいパッケージのwhlをダウンロードして、

```bash
python -m pip install "filename.whl"
```

で手動で入れれる。

### virtualenvのPython仮想環境をVisual Studio Codeにも有効させる

<https://qiita.com/thatbin/items/2de0a0c1ea21af10f6e3>

### virtualenvのPython仮想環境をVisual Studio Codeにも有効させる2

下記のような感じで、virtualenvが追加したpython, ライブラリのパスを入れるでも一応OKかも。  
※venv_flask が仮想環境名  
※venv を起動してから code.exe するのを推奨

```code
"python.pythonPath": "C:\self\program\python-test\venv_flask\Scripts\python.exe"
"python.autoComplete.extraPaths": ["C:\self\program\python-test\venv_flask\Lib\site-packages"]
```

## 基本

### モジュール化（自作を import する）

\__init__.py がいるところがモジュールの起点になる。

```code
c:\self\program\python-test\flask_test
│  __init__.py
│
└─controllers
   └─ route1.py
```

上記の状態の場合、\__init__.py から見た route1.py は、

```python
from flask_test.controllers import route1
```

になる。

## デバッグ

### VSCのデバッガ

デバッグコンソール使うと、java@eclipseの"表示"的なことができる。  
※ブレークした所でその場でコード打って実行できる


## Flask

### 事前準備

※Flaskプロジェクト用のpackage.json作ってるのと同じ感じ

1. virtualenvを入れる。
2. 下記、実行

```cmd
cd flaskの開発用フォルダ
virtualenv venv_flask ※仮想環境の生成
\venv_flask\Scripts\activate.bat ※仮想環境への切替
```

コンソールが↓のような表示になったら、

```cmd
(venv_flask) c:\file_path>
```

仮想環境に対して、Flaskをインストールする。

```cmd
pip install flask
```

エディタやIDEも仮想環境下で実行する必要があるため、仮想環境のコマンドラインから起動する。

例 visualStudioCodeを起動：

```cmd
(venv_flask) c:\file_path> code.exe ※実際にはVSCへのフルパス
```
