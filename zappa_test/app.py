import json
import threading
import os
import random
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    hoge()
    return 'hello from Flask!'


@app.route('/test1', methods=['GET', 'POST'])
def test1(event=None, context=None):
    hoge()
    return 'test1 from Flask!'


def hoge():
    print(threading.get_ident())
    # print(os.uname())
    print(os.chdir("/tmp"))
    print(os.getcwd())

    from pathlib import Path
    Path(f'test1_{random.randint(1,10000)}.txt').touch()
    print(os.listdir())
    print(len(os.listdir()))


if __name__ == '__main__':
    app.run()
