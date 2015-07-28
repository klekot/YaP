import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QProgressBar,
    QPushButton, QLabel, QLineEdit, QFileDialog)
from PyQt5.QtCore import QBasicTimer
import requests
import sqlite3
from datetime import datetime
from xlwt import Workbook
from xlwt import easyxf
import xlrd
from modules.limit import limit


class YaP(QWidget):
    rate_url = 'poligon.info'
    query = ''
    query_list = []
    res_label = ''
    file_path_label = ''
    rank = 0
    file_taken = False
    res_list = []
    file_queries = []
    fname = ''
    r_count = 0
    db_path = 'keywords.db'
    xls_path = 'rating.xls'
    yandex_limits = [
        [0,  230, 0],  [1,  276, 0],  [2,  276, 0],
        [3,  276, 0],  [4,  276, 0],  [5,  230, 0],
        [6,  161, 0],  [7,  92,  0],  [8,  46,  0],
        [9,  46,  0],  [10, 46,  0],  [11, 46,  0],
        [12, 46,  0],  [13, 46,  0],  [14, 46,  0],
        [15, 46,  2],  [16, 46,  0],  [17, 46,  0],
        [18, 46,  0],  [19, 46,  0],  [20, 92,  0],
        [21, 161, 0],  [22, 230, 0],  [23, 240, 0]
    ]
    # req_date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    req_date = str(datetime.now().strftime('%Y-%m-%d'))
    query_url = 'https://yandex.ru/search/xml?user=webmaster-poligon\
                                  &key=03.279908682:25776a70171503eb70359c5bd5b820dc&l10n=ru\
                                  &groupby=groups-on-page%3D100&lr=2&query='

    def __init__(self):
        super().__init__()
        self.initUI()
        self.search_btn.clicked.connect(self.set_query)
        self.search_btn.clicked.connect(self.start_search)
        self.qfile_btn.clicked.connect(self.showOpenDialog)
        self.sfile_btn.clicked.connect(self.db_xls)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        lbl = QLabel('Выбран запрос: ')
        grid.addWidget(lbl, 0, 0)
        lbl1 = QLabel('Поиск по запросу: ')
        grid.addWidget(lbl1, 3, 0)
        self.label = QLabel(self)
        grid.addWidget(self.label, 0, 1)
        self.field = QLineEdit(self)
        grid.addWidget(self.field, 3, 1)
        self.field.textChanged[str].connect(self.push_query)
        self.search_btn = QPushButton('Поиск')
        grid.addWidget(self.search_btn, 3, 2)
        self.qfile_btn = QPushButton('Файл запросов')
        grid.addWidget(self.qfile_btn, 5, 0)
        self.sfile_btn = QPushButton('Сохранить')
        grid.addWidget(self.sfile_btn, 5, 2)
        label_fake = QLabel()
        grid.addWidget(label_fake, 4, 0)
        label_fake1 = QLabel()
        grid.addWidget(label_fake1, 2, 0)
        self.label_done = QLabel()
        grid.addWidget(self.label_done, 6, 1)
        self.label_r = QLabel(self.res_label)
        grid.addWidget(self.label_r, 4, 1)
        self.label_fp = QLabel(self.file_path_label)
        grid.addWidget(self.label_fp, 5, 1)
        self.setGeometry(700, 350, 600, 200)
        self.setWindowTitle('\"YaP\" - is a Yandex ratings for Poligon.info')

        self.pbar = QProgressBar(self)
        grid.addWidget(self.pbar, 7, 1)
        self.timer = QBasicTimer()
        self.step = 0

        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def sql_con(self, res_list):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute("select name from sqlite_master \
            where type='table' and name='requests'")
        if db.fetchone():
            for res in self.res_list:
                if len(self.file_queries) == 0:
                    k = (self.query.encode('utf-8').decode('cp1251'),
                         self.req_date,)
                    db.execute("select * from requests \
                            where keyword=? and date=?", k)
                    if db.fetchone():
                        db.execute("delete from requests \
                            where keyword=? and date=?", k)
                    else:
                        continue
                else:
                    for q in self.file_queries:
                        k = (q, self.req_date,)
                        db.execute("select * from requests \
                                where keyword=? and date=?", k)
                        if db.fetchone():
                            db.execute("delete from requests \
                                where keyword=? and date=?", k)
                        else:
                            continue
            db.executemany(
                "insert into requests values (?, ?, ?)",
                self.res_list)
        else:
            db.execute("create table requests (keyword, position, date)")
            db.executemany(
                "insert into requests values (?, ?, ?)",
                self.res_list)
        conn.commit()
        db.close()
        conn.close()

    def db_xls(self):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute("select name from sqlite_master \
            where type='table' and name='requests'")
        wb = Workbook()
        ws = wb.add_sheet('keywords')
        plain = easyxf('')
        if db.fetchone():
            for r, row in enumerate(db.execute("select * from requests")):
                for c, col in enumerate(row):
                    if (type(col) is int) != True:
                        ws.write(r, c, col.encode('cp1251')
                                 .decode('utf-8'), plain)
                    else:
                        ws.write(r, c, col, plain)
                    print(col)
                wb.save(self.xls_path)
        db.close()
        conn.close()

    def showOpenDialog(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                                    'C:\\Users\\gnato\\\
                                                    Desktop\\Igor\\progs\\\
                                                    python_progs\\YaP\\')
        if len(self.fname) > 0:
            book = xlrd.open_workbook(self.fname, 'rt', formatting_info=True)
            sh = book.sheet_by_index(0)
        else:
            pass
        for i in range(sh.nrows):
            self.query_list.append(sh.cell_value(i, 0))
        print('query_list is: ')
        for l in self.query_list:
            print(l.encode('utf-8').decode('cp1251'))
        self.file_taken = True
        fname_chars = []
        for char in self.fname:
            if (char == '/'):
                fname_chars.append('\\')
            else:
                fname_chars.append(char)
        win_path = ''.join(fname_chars)
        self.label_fp.setText(win_path)
        self.label_fp.adjustSize()
        self.start_search(self.event)

    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_Escape:
                self.close()
            elif event.key() == Qt.Key_Return:
                self.set_query(self)
                self.start_search(self)

    def set_query(self, event):
        self.query = self.field.text()
        self.rank = 0
        self.file_queries = []

    def push_query(self, query):
        self.label.setText(query)
        self.label.adjustSize()

    def start_search(self, event):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)
            self.label_done.setText(
                'Запросы обработаны, результаты занесены в базу данных.\n\
Для сохранения в файл нажмите кнопку \"Сохранить\".')
        if self.file_taken:
            for j, item in enumerate(self.query_list):
                self.query = self.query_list[j]
                r = requests.get(self.query_url + self.query)
                self.r_count += 1
                # функция limit() может быть вызвана только один раз          #
                # во избежание неправильных показателей счётчика.             #
                limit_data = limit(self.r_count, self.db_path, self.req_date) #
                # ########################################################### #
                if (limit_data[0]):
                    result = r.text
                    result_list = result.split('<url>')
                    for i, item in enumerate(result_list):
                        if self.rate_url in item:
                            self.rank += i
                            break
                    self.res_list.append((
                        self.query.encode('utf-8').decode('cp1251'),
                        self.rank,
                        self.req_date,))
                    self.file_queries.append(
                        self.query.encode('utf-8').decode('cp1251'))
                    limit_resume = str(limit_data[1]) + ' - Winter is close!'
                else:
                    limit_resume = str(limit_data[1]) +\
                        'Hour limit is here... Wait about ' +\
                        str(60 - int(datetime.now().strftime('%M'))) +\
                        ' minuntes, please!'
            self.sql_con(self.res_list)
            print(limit_resume)
            print(int(datetime.now().strftime('%Y-%m-%d')))
            print(int(datetime.now().strftime('%Y-%m-%d'))-1)
        else:
            r = requests.get(self.query_url + self.query)
            self.r_count += 1
            result = r.text
            result_list = result.split('<url>')
            for i, item in enumerate(result_list):
                if self.rate_url in item:
                    self.rank += i
                    break
            if self.rank != 0:
                self.res_label = ('По запросу \"' + self.query + '\" сайт poligon.info \
находится на ' + str(self.rank) + '-й позиции.\nДата запроса : '
                    + self.req_date + '.')
                self.label_r.setText(self.res_label)
                self.label_r.adjustSize()
                self.res_list.append((
                    self.query.encode('utf-8').decode('cp1251'),
                    self.rank,
                    self.req_date,))
                self.sql_con(self.res_list)
            else:
                self.res_label = ('По запросу \"' + self.query + '\" сайт poligon.info \
находится ниже 100-й позиции.\nДата запроса : '
                                  + self.req_date + '.')
                self.label_r.setText(self.res_label)
                self.label_r.adjustSize()
                self.res_list.append((
                    self.query.encode('utf-8').decode('cp1251'),
                    self.rank,
                    self.req_date,))
                self.sql_con(self.res_list)
                print('end')
                print(self.res_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    yap = YaP()
    sys.exit(app.exec_())
