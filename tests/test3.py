import threading
from PyQt5.QtCore import QThread


class MyThread(QThread):

    def run(self):
        for i in range(10):
            print(i)

print('outside thread')
MyThread().start()
for i in range(10):
    print(str(i) + 'outside thread')
