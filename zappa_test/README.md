# zappa_test

## 最初

```cmd
python -m virtualenv venv_zappa_test
venv_zappa_test\Scripts\activate
pip install -r requirements.txt
zappa init
※↑はとりあえず全部enterでOK
zappa deploy dev
```

## 2回目以降

```cmd
cd venv_zappa_test\Scripts\activate
zappa update dev
```

## 終了時

```cmd
zappa undeploy dev
```

## zappaの仕組み

zappaがpackage時にhander.pyというファイルを生成し、その中にlambda_handler()という関数を定義している。  
※zappa package し、生成されるzipの中を見ると、hander.pyというファイルがある。  
それが含まれた状態でzipファイル生成され、lambdaにアップロードされている。  
※Lambdaにコンソールからzipファイル上げているのと同じだと思われる  

Lambdaは、ハンドル対象が handler.lambda_handler になっている。  
※zappaが生成した、hander.py内の、lambda_handler()が起点になっている。  

lambda_handler()からLambdaHandlerクラス（handler.py内）の、lambda_handler()をコールしている。  
その中で、自クラスをnewし（↓部分）、そのインスタンスのhandler()をコール※している。  
※要はLambdaHandler.handler()をコールしている。

```python
@classmethod
def lambda_handler(cls, event, context):
    handler = cls()
    # ～略～
    try:
        return handler.handler(event, context)
    except Exception as ex:
    # ～略～
```

多分その中から実際に自分が作ったpythonファイルに繋げているのだと思われる。  

## 困ったら

### zappaの再deploy, updateが出来ない

一度、undeployすると良いかも。。

```bash
zappa undeploy dev
```

### zappa deployするとスケジュールが生成される

以下の設定をfalseにする。

```json
"keep_warm": false
```

## 参考サイト

### zappaの設定をほぼ丸パクリしたサイト

https://suzu6-nuxt-blog.netlify.com/posts/4/
