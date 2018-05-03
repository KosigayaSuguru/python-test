# python

## 環境設定

### windows環境にinstallする

<https://www.python.jp/install/windows/index.html> が分かりやすい

### pipコマンドからinstall出来ない時

<https://pypi.org/project/virtualenv/#files>

から、入れたいパッケージのwhlをダウンロードして、

```bash
python -m pip install "filename.whl"
```

で手動で入れれる。

### virtualenvのPython仮想環境をVisual Studio Codeにも有効させる

<https://qiita.com/thatbin/items/2de0a0c1ea21af10f6e3>

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
