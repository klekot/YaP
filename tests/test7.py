import threading
from time import sleep
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def main_process(self):
        th = MyThread(10)
        th.start()
        for i in range(10):
            print("main process")
            sleep(2)

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.main_process)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()


class MyThread(threading.Thread):

    def __init__(self, a):
        threading.Thread.__init__(self)
        self.a = a

    def run(self):
        for i in range(self.a):
            print(i)
            sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
