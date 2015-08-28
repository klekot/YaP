# -*- coding: utf-8 -*-

import sqlite3
# import os.path
import os
from datetime import datetime
import tempfile


class Log(object):

    def __init__(self, db_path, logs_path):
        self.db_path = db_path
        self.logs_path = logs_path
        self.bufferInMemory = tempfile.mkstemp(suffix='.txt')

    def write(self, information):
        self.conn = sqlite3.connect(self.db_path)
        self.db = self.conn.cursor()
        self.db.execute("select name from sqlite_master \
            where type='table' and name='logs'")
        if self.db.fetchone():
            self.db.execute(
                "insert into logs values (?, ?)", (
                    str(datetime.now().strftime(
                        '%Y-%m-%d %H:%M:%S')), information))
        else:
            self.db.execute("create table logs (date, information)")
            self.db.execute(
                "insert into logs values (?, ?)", (
                    str(datetime.now().strftime(
                        '%Y-%m-%d %H:%M:%S')), information))
        self.conn.commit()
        with open(self.bufferInMemory[1], mode='w') as t:
            self.db.execute("select * from logs")
            for line in self.db.fetchall():
                t.write(line[0] + '   >>>   ' + line[1])
        with open(self.logs_path, mode='w') as f:
            with open(self.bufferInMemory[1], mode='r') as t:
                for line in reversed(list(t)):
                    f.write(line.rstrip() + '\n')
        self.db.close()
        self.conn.close()

    def read(self, destination):
        if os.path.isfile(self.logs_path):
            with open(self.logs_path, mode='r') as f:
                destination.setText(f.read())
        else:
            with open(self.logs_path, mode='a') as f:
                f.write('Log starts!\n')
            with open(self.logs_path, mode='r') as f:
                destination.setText(f.read())
