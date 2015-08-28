# -*- coding: utf-8 -*-
import threading
from time import sleep


class pbarThread(threading.Thread):

    def __init__(self, progressBar, value):
        threading.Thread.__init__(self)
        self.progressBar = progressBar
        self.value = value
        self.alive = True

    def run(self):
        try:
            while self.alive:
                for i in range(101):
                    self.progressBar.setProperty("value", self.value)
                    self.value += 1
                    sleep(0.03)
        finally:
            self.progressBar.setProperty("value", 0)

    def stop(self):
        self.alive = False
        self.join()
