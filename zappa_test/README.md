# zappa_test

## 最初

```cmd
python -m virtualenv venv_zappa_test
venv_zappa_test\Scripts\activate
pip install -r requirements.txt
```

## 困ったら

### zappaの再deploy, updateが出来ない

一度、undeployすると良いかも。。

```bash
zappa undeploy dev
```

## 参考サイト

### zappaの設定をほぼ丸パクリしたサイト

https://suzu6-nuxt-blog.netlify.com/posts/4/
