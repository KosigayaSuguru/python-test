import asyncio
from random import randint
from threading import Thread, current_thread
from time import sleep

import dataset


class SubThread(Thread):

    def __init__(self, db):
        super().__init__()
        self.db = db
        pass

    def run(self):
        print(f'{id(current_thread())} {self.db["table1_children"].find_one(id=1)}')
        # wait
        sleep(randint(5,10))
        print(f'{id(current_thread())}')
        self.db.executable.close()
        pass

# コネクションプールを2接続に設定（max_overflowを0にするのがキモ）
db1 = dataset.connect("mysql://root:password@localhost:3306","ruby_on_rails-test", engine_kwargs={"pool_size":2, "max_overflow":0})

# スレッドで同時に4SQL流すが、プールサイズが2件なので2スレッドがSQLを流した時点でwaitがかかる
t1 = SubThread(db1)
t2 = SubThread(db1)
t3 = SubThread(db1)
t4 = SubThread(db1)

t1.start()
t2.start()
t3.start()
t4.start()
t4.join()

print("")
