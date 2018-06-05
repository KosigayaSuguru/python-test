from threading import local, current_thread

tl = local()

cnt = 0


def cntt():
    global cnt
    cnt += 1
    return cnt


class ThreadLocalTest1:
    """route1.py の /test_thread_local から呼び出される
    """

    @staticmethod
    def set():
        t = current_thread()
        tl.a = "thread_local_value:" + str(cntt())
        print("thread_id:{} set {}".format(id(t), ThreadLocalTest1.get()))

    @staticmethod
    def get():
        return tl.a
