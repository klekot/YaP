# -*- coding: utf-8 -*-
import threading
from time import sleep
# from datetime import datetime


class timerThread(threading.Thread):

    def __init__(self, alive):
        threading.Thread.__init__(self)
        self.alive = alive

    def run(self):
        # delta_sec = (60 - int(datetime.now().strftime('%M'))) * 60
        count = 0
        while self.alive:
            # print(str(delta_sec - count))
            count += 1
            sleep(1)

    def stop(self):
        self.alive = False
        self.join()
