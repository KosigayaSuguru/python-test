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

### pythonのデバッグ

python起動時に -d オプションを付ける。  
※多分、IDEとかもデバッグモードで起動させる時は-dを付けてると思われる  

```bash
python -m -d
```

### VSCのデバッガ その１

デバッグコンソール使うと、java@eclipseのデバッグの"表示"的なことができる。  
※ブレークした所でその場でコード打って実行できる

### VSCのデバッガ その2

VSCはデバッグ用に 'PythonTools\visualstudio_py_launcher.py' をプロキシとして噛ませてるっぽい。  
ので、VSCからデバッガを起動させるようにすると何でもブレーク張れる。

### PyDev（eclipseのpythonプラグイン）でリモートデバッグ

```bash
pip install pydevd
```

する。デバッグしたいコード中に、

```python
import pydevd; pydevd.settrace()
```

を入れてコードを実行する。↑を入れたところでコードが止まるので、  
PyDevのデバッグビューで↓を実行する。

```code
メニュー > PyDev > "デバッグ・サーバーの開始"
```

ブレークするので、後は普通にいつもの感覚でデバッグできる（ので、とりあえず最初にブレークさせて良いかも）。  

* eclipse上であれば普段のeclipseのやり方でブレークを張る。
* コマンドラインからインタラクティブにPythonを起動している場合、pydevd.settrace()する毎にブレークする。

※注意  

* リモートデバッグ時の場合は、settrace()の引数にIP入れる。  
  * のかと思ったけど↓（リモートデバッグ）は無理だった。。
  * pydevd.settrace("192.168.0.200")みたいな感じ、多分。。  
  * [PyDev公式](http://www.pydev.org/manual_adv_remote_debugger.html) の"Important Notes"参照

## pytest

### 起動

```bash
python -m pytest
```

ファイルを指定しない場合、test_*.pyがすべて実行される。  
ファイルを指定した場合、そのファイルのみ実行される。

### print()した内容を出力する

```bash
python -m pytest -s
```

### pytestでデバッガを起動させる その1（PDBを起動させる）

ブレークさせたいところに下記を記入。

```python
import pdb;pdb.set_trace()
```

### pytestでデバッガを起動させる その2（visual studio code限定）

下記のコードを実行すると、3000ポートでリモートデバッグを受け付けるようになる。  
※接続用の起動の仕方は、launch.json の"リモートデバッグ"を参照  
※サンプルコード： test_flask.py の test_pytestでデバッガを使う_VisualStudioCode()

```python
import ptvsd
from time import sleep
print('waiting...')
ptvsd.enable_attach('my_secret', address=('0.0.0.0', 3000))
ptvsd.wait_for_attach()
sleep(1)
print('Debug Start')
```

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
