# -*- coding: utf-8 -*-

from initSettings import *
import requests
import ssl
from functools import wraps
import xlrd
import threading
from time import sleep
from datetime import datetime
from xlwt import Workbook
from xlwt import easyxf
import sqlite3
import argparse
from modules.Log import Log


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputFile',
                        nargs='?', default=xls_path)
    parser.add_argument('-o', '--outputFile',
                        nargs='?', default=xls_path)
    return parser


class timerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.alive = True

    def run(self):
        delta_sec = (60 - int(datetime.now().strftime('%M'))) * 60
        count = 0
        while self.alive:
            print(str(delta_sec - count))
            count += 1
            sleep(1)

    def stop(self):
        self.alive = False
        threading.Thread.join(self)


def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)


def coreFunction(query_url, query, rate_url, rank, res_list,
                 req_date, day_limit, limit_data, table_list,
                 db_path, log):
    r = requests.get(
        (query_url + query),
        verify="cacert.pem")
    result = r.text
    result_list = result.split('<url>')
    for i, item in enumerate(result_list):
        if rate_url in item:
            rank += i
            break
    res_list.append((
        query.encode('utf-8').decode('cp1251'),
        rank,
        req_date,))
    conn = sqlite3.connect(db_path)
    db = conn.cursor()
    db.execute("select name from sqlite_master \
        where type='table' and name='requests'")
    if db.fetchone():
        for res in res_list:
            k = (query.encode('utf-8').decode('cp1251'),
                 req_date,)
            db.execute("select * from requests \
                    where keyword=? and date=?", k)
            if db.fetchone():
                db.execute("delete from requests \
                    where keyword=? and date=?", k)
            else:
                continue
        db.executemany(
            "insert into requests values (?, ?, ?)",
            res_list)
    else:
        db.execute("create table requests (keyword, position, date)")
        db.executemany(
            "insert into requests values (?, ?, ?)",
            res_list)
    conn.commit()
    db.close()
    conn.close()
    log.write('Поиск из консоли по запросу "' + query + '";\n')
    res_list = []
    rank = 0


def search(query, log):
    search_work = False
    limit_data = limit(db_path, req_date, day_limit,
                       day_overdraft, limit_police, hour,
                       search_work, 1, 0, 0)
    search_work = True
    limit_data = limit(db_path, req_date, day_limit, day_overdraft,
                       limit_police, hour, search_work, 0,
                       0, 0)
    coreFunction(query_url, query, rate_url, rank, res_list,
                 req_date, day_limit, limit_data, table_list,
                 db_path, log)
    search_work = False
    return limit_data[1]


def db_xls(db_path, outputFile, table_list):
    conn = sqlite3.connect(db_path)
    db = conn.cursor()
    wb = Workbook()
    ws = wb.add_sheet('keywords')
    plain = easyxf('')
    for i in table_list:
        # for launch from cmd use this line:
        print(i)
        # for launch from sublime console - use this line:
        # print(i.encode('utf-8').decode('cp1251'))
    print("--------------------------")
    temp_arr = []
    temp_col = []
    db.execute("select * from requests where date=?", (req_date,))
    for r, row in enumerate(db.fetchall()):
        # print(row[0].encode('cp1251').decode('utf-8'))
        if (row[0].encode('cp1251').decode('utf-8') != '') and\
           (row[0].encode('cp1251').decode('utf-8') not in temp_col) and\
           (row[0].encode('cp1251').decode('utf-8') in table_list):
            temp_col.append(row[0].encode('cp1251').decode('utf-8'))
            temp_arr.append(row)
    for r, row in enumerate(temp_arr):
        # for launch from sublime console - use this lines:
        # print(str(row[0]) +
        #       ' :: ' + str(row[1]) +
        #       ' :: ' + str(row[2]))
        print(str(row[0].encode('cp1251').decode('utf-8')) +
              ' :: ' + str(row[1]) +
              ' :: ' + str(row[2]))
        for c, col in enumerate(row):
            if (type(col) is int) != True:
                ws.write(r, c, col.encode('cp1251').decode('utf-8'), plain)
            else:
                ws.write(r, c, col, plain)
        wb.save(outputFile)
    db.close()
    conn.close()


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    inputFile = "{}".format(namespace.inputFile)
    outputFile = "{}".format(namespace.outputFile)
    log = Log(db_path, logs_path)

    print("hi!")
    limit_data = limit(db_path, req_date, day_limit, day_overdraft,
                       limit_police, hour, search_work, 1, 0, 0)

    book = xlrd.open_workbook(inputFile, 'rt', formatting_info=True)
    sh = book.sheet_by_index(0)
    # список уже ранее добавленных позиций
    table_list_items = []
    for item in table_list:
        table_list_items.append(item[0])
    # помещаем  ранее не внесённые запросы из файла в список
    for i in range(sh.nrows):
        if sh.cell_value(i, 0) not in table_list_items:
            table_list.append(sh.cell_value(i, 0))
    for i, item in enumerate(table_list):
        if (limit_data[1] > 0):
            limit_data.pop(1)
            limit_data.insert(1, search(item, log))
        else:
            wait_timer = timerThread()
            wait_timer.start()
            sleep((60 - int(datetime.now().strftime('%M'))) * 60.0)
            wait_timer.stop()
            hour = int(datetime.now().strftime('%H'))
            limit_data.pop(1)
            limit_data.insert(1, search(item, log))
    db_xls(db_path, outputFile, table_list)
    print("bye!")
