from flask_test.controllers.thread_local1 import ThreadLocalTest1
from threading import local, current_thread


class ThreadLocalTest2:
    """route1.py の /test_thread_local から呼び出される
    """

    def call(self):
        t = current_thread()
        print("thread_id:{} get {}".format(id(t), ThreadLocalTest1.get()))
