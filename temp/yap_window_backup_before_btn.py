# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import sqlite3
from datetime import datetime
from xlwt import Workbook
from xlwt import easyxf
import xlrd
from modules.limit import limit


class yap(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_Escape:
                self.close()
            elif event.key() == QtCore.Qt.Key_Return:
                Ui_YaP.set_query(ui, event)
                Ui_YaP.start_search(ui, event)


class Ui_YaP(object):
    rate_url = 'poligon.info'
    query = ''
    query_list = []
    recent_requests = []
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
    cell_word = ''
    cell_rank = ''
    cell_date = ''
    table_row = 0
    day_limit = 460
    counter_sum = 0
    day_overdraft = 0
    recent_limit = 0
    search_work = False
    mode_header = 's'
    limit_data = [True, 46, 460]
    limit_police = [[230, 0, 5, 22, 23],
                    [276, 1, 2, 3, 4],
                    [161, 6, 21],
                    [92, 7, 20],
                    [46, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    hour = int(datetime.now().strftime('%H'))
    # req_date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    req_date = str(datetime.now().strftime('%Y-%m-%d'))
    query_url = 'https://yandex.ru/search/xml?user=webmaster-poligon\
                &key=03.279908682:25776a70171503eb70359c5bd5b820dc&l10n=ru\
                &groupby=groups-on-page%3D100&lr=2&query='

    def setupUi(self, YaP):
        self.limit_data = limit(self.r_count, self.db_path, self.req_date,
                                self.day_limit, self.day_overdraft,
                                self.limit_police, self.hour, self.search_work)
        YaP.setObjectName("YaP")
        YaP.setEnabled(True)
        YaP.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(YaP.sizePolicy().hasHeightForWidth())
        YaP.setSizePolicy(sizePolicy)
        YaP.setMinimumSize(QtCore.QSize(800, 600))
        YaP.setSizeIncrement(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(YaP)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.groupBox_mode = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.groupBox_mode.sizePolicy().hasHeightForWidth())
        self.groupBox_mode.setSizePolicy(sizePolicy)
        self.groupBox_mode.setMinimumSize(QtCore.QSize(220, 90))
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.radioButton_single_mode = QtWidgets.QRadioButton(
                                                            self.groupBox_mode)
        self.radioButton_single_mode.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.radioButton_single_mode.setObjectName("radioButton_single_mode")
        self.radioButton_single_mode.autoExclusive()
        self.radioButton_single_mode.setChecked(True)
        self.radioButton_file_mode = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_file_mode.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.radioButton_file_mode.setObjectName("radioButton_file_mode")
        self.radioButton_file_mode.autoExclusive()
        self.btn_fileopen = QtWidgets.QPushButton(self.groupBox_mode)
        self.btn_fileopen.setGeometry(QtCore.QRect(120, 50, 91, 23))
        self.btn_fileopen.setObjectName("btn_fileopen")
        self.btn_fileopen.setDisabled(True)
        self.gridLayout.addWidget(self.groupBox_mode, 0, 1, 1, 1)
        self.groupBox_limits = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
                                        QtWidgets.QSizePolicy.Fixed,
                                        QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.groupBox_limits.sizePolicy().hasHeightForWidth())
        self.groupBox_limits.setSizePolicy(sizePolicy)
        self.groupBox_limits.setMinimumSize(QtCore.QSize(220, 360))
        self.groupBox_limits.setObjectName("groupBox_limits")
        self.splitter_gb_limits = QtWidgets.QSplitter(self.groupBox_limits)
        self.splitter_gb_limits.setGeometry(QtCore.QRect(20, 20, 177, 331))
        self.splitter_gb_limits.setOrientation(QtCore.Qt.Vertical)
        self.splitter_gb_limits.setObjectName("splitter_gb_limits")
        self.label_day_limit = QtWidgets.QLabel(self.splitter_gb_limits)
        self.label_day_limit.setObjectName("label_day_limit")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_day_limit = QtWidgets.QLCDNumber(
                                                    self.splitter_gb_limits)
        self.lcdNumber_day_limit.setFont(font)
        self.lcdNumber_day_limit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_day_limit.setDigitCount(3)
        self.lcdNumber_day_limit.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_day_limit.setObjectName("lcdNumber_day_limit")
        self.lcdNumber_day_limit.setProperty(
                    "intValue", (self.day_limit - self.limit_data[2])-1)
        self.label_hour_limit = QtWidgets.QLabel(self.splitter_gb_limits)
        self.label_hour_limit.setObjectName("label_hour_limit")
        self.lcdNumber_hour_limit = QtWidgets.QLCDNumber(
                                                    self.splitter_gb_limits)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_hour_limit.setFont(font)
        self.lcdNumber_hour_limit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_hour_limit.setDigitCount(3)
        self.lcdNumber_hour_limit.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_hour_limit.setObjectName("lcdNumber_hour_limit")
        self.lcdNumber_hour_limit.setProperty("intValue", self.limit_data[1])
        self.gridLayout.addWidget(self.groupBox_limits, 1, 1, 1, 1)
        self.groupBox_main = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.groupBox_main.sizePolicy().hasHeightForWidth())
        self.groupBox_main.setSizePolicy(sizePolicy)
        self.groupBox_main.setMinimumSize(QtCore.QSize(530, 500))
        self.groupBox_main.setSizeIncrement(QtCore.QSize(600, 0))
        self.groupBox_main.setFlat(False)
        self.groupBox_main.setCheckable(False)
        self.groupBox_main.setObjectName("groupBox_main")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_main)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_main = QtWidgets.QGridLayout()
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.btn_save = QtWidgets.QPushButton(self.groupBox_main)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_main.addWidget(self.btn_save, 2, 1, 1, 1)
        self.label_filepath = QtWidgets.QLabel(self.groupBox_main)
        self.label_filepath.setMinimumSize(QtCore.QSize(0, 42))
        self.label_filepath.setObjectName("label_filepath")
        self.gridLayout_main.addWidget(self.label_filepath, 2, 0, 1, 1)
        self.table_results = QtWidgets.QTableWidget(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.table_results.sizePolicy().hasHeightForWidth())
        self.table_results.setSizePolicy(sizePolicy)
        self.table_results.setMinimumSize(QtCore.QSize(500, 475))
        self.table_results.setObjectName("table_results")
        self.table_results.setColumnCount(3)
        self.table_results.setHorizontalHeaderLabels(
                    "КЛЮЧЕВОЕ СЛОВО;МЕСТО В ПОИСКЕ;ДАТА ЗАПРОСА".split(";"))
        self.table_results.horizontalHeaderItem(0).setTextAlignment(
                                                        QtCore.Qt.AlignLeft)
        self.table_results.horizontalHeaderItem(1).setTextAlignment(
                                                        QtCore.Qt.AlignHCenter)
        self.table_results.horizontalHeaderItem(2).setTextAlignment(
                                                        QtCore.Qt.AlignRight)
        self.table_results.resizeColumnsToContents()
        self.gridLayout_main.addWidget(self.table_results, 1, 0, 1, 2)
        self.btn_search = QtWidgets.QPushButton(self.groupBox_main)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_main.addWidget(self.btn_search, 0, 1, 1, 1)
        self.lineEdit_single_query = QtWidgets.QLineEdit(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
                                        QtWidgets.QSizePolicy.MinimumExpanding,
                                        QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                self.lineEdit_single_query.sizePolicy().hasHeightForWidth())
        self.lineEdit_single_query.setSizePolicy(sizePolicy)
        self.lineEdit_single_query.setMinimumSize(QtCore.QSize(390, 0))
        self.lineEdit_single_query.setObjectName("lineEdit_single_query")
        self.gridLayout_main.addWidget(self.lineEdit_single_query, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_main, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_main, 0, 0, 5, 1)
        self.groupBox_info = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
                                        QtWidgets.QSizePolicy.Preferred,
                                        QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                self.groupBox_info.sizePolicy().hasHeightForWidth())
        self.groupBox_info.setSizePolicy(sizePolicy)
        self.groupBox_info.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox_info.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_info.setObjectName("groupBox_info")
        self.label_info = QtWidgets.QLabel(self.groupBox_info)
        self.label_info.setGeometry(QtCore.QRect(10, 10, 188, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setTextFormat(QtCore.Qt.AutoText)
        self.label_info.setScaledContents(False)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        '''
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_info)
        self.progressBar.setGeometry(QtCore.QRect(10, 100, 200, 18))
        sizePolicy = QtWidgets.QSizePolicy(
                                        QtWidgets.QSizePolicy.Minimum,
                                        QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        '''
        self.gridLayout.addWidget(self.groupBox_info, 3, 1, 2, 1)

        self.retranslateUi(YaP)
        QtCore.QMetaObject.connectSlotsByName(YaP)

    def retranslateUi(self, YaP):
        _translate = QtCore.QCoreApplication.translate
        YaP.setWindowTitle(_translate("YaP", "Form"))
        self.groupBox_mode.setTitle(_translate("YaP", "Режим поиска"))
        self.radioButton_single_mode.setText(
                        _translate("YaP", "Одиночный поиск"))
        self.radioButton_file_mode.setText(_translate("YaP", "Пакетный поиск"))
        self.btn_fileopen.setText(_translate("YaP", "Выбрать файл"))
        self.groupBox_limits.setTitle(
                        _translate("YaP", "Лимиты Яндекса"))
        self.label_day_limit.setText(
                        _translate("YaP", "Дневной лимит (минус овердрафт)"))
        self.label_hour_limit.setText(
                        _translate("YaP", "Лимит запросов в текущем часу"))
        if self.mode_header == 's':
            self.groupBox_main.setTitle(_translate("YaP", "Одиночный поиск"))
        elif self.mode_header == 'f':
            self.groupBox_main.setTitle(_translate("YaP", "Пакетный поиск"))
        self.btn_save.setText(_translate("YaP", "Сохранить"))
        self.label_filepath.setText(
                        _translate("YaP", "Путь к файлу статистики:"))
        self.btn_search.setText(_translate("YaP", "Поиск"))
        self.groupBox_info.setTitle(_translate("YaP", "Информация"))
        self.label_info.setText(_translate("YaP", ""))

    def mode_selector(self, event):
        if self.radioButton_single_mode.isChecked() == True:
            self.btn_fileopen.setDisabled(True)
            self.btn_search.setDisabled(False)
            self.lineEdit_single_query.setDisabled(False)
            self.mode_header = 's'
        else:
            self.btn_fileopen.setDisabled(False)
            self.btn_search.setDisabled(True)
            self.lineEdit_single_query.setDisabled(True)
            self.mode_header = 'f'
        self.retranslateUi(YaP)

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
        '''
        self.xls_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            YaP, 'Open file',
            'C:\\Users\\gnato\\Desktop\\Igor\\progs\\python_progs\\YaP\\')
        '''
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        wb = Workbook()
        ws = wb.add_sheet('keywords')
        plain = easyxf('')
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
        self.query_list = []
        self.recent_requests = []
        self.table_row = 0
        self.rank = 0
        self.label_filepath.setText('')
        self.table_results.setRowCount(0)
        self.table_results.setItem(0, 0, QtWidgets.QTableWidgetItem(''))
        self.table_results.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
        self.table_results.setItem(0, 2, QtWidgets.QTableWidgetItem(''))
        self.label_info.setText('')
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            YaP, 'Open file',
            'C:\\Users\\gnato\\Desktop\\Igor\\progs\\python_progs\\YaP\\')
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
        self.label_filepath.setText(win_path)
        # self.label_filepath.adjustSize()
        self.start_search(YaP.event)

    def set_query(self, event):
        self.query = self.lineEdit_single_query.text()
        self.rank = 0
        self.file_queries = []
        self.lineEdit_single_query.setText('')

    def start_search(self, event):
        self.search_work = True
        # YaP.timer = QtCore.QBasicTimer()
        # if YaP.timer.isActive():
        #     YaP.timer.stop()
        # else:
        #     YaP.timer.start(100, YaP)
        if self.file_taken:
            for j, item in enumerate(self.query_list):
                self.query = self.query_list[j]
                r = requests.get(self.query_url + self.query)
                self.r_count += 1
                self.limit_data = limit(
                                self.r_count, self.db_path, self.req_date,
                                self.day_limit, self.day_overdraft,
                                self.limit_police, self.hour, self.search_work)
                if (self.limit_data[0]):
                    result = r.text
                    result_list = result.split('<url>')
                    for i, item in enumerate(result_list):
                        if self.rate_url in item:
                            self.rank += i
                            break
                    if self.rank != 0:
                        self.cell_rank = str(self.rank)
                    else:
                        self.cell_rank = "< 100"
                    self.cell_date = self.req_date
                    # print(len(self.recent_requests))
                    if (self.query not in self.recent_requests):
                        self.cell_word = self.query
                        self.recent_requests.append(self.query)
                        self.table_results.setRowCount(self.table_row + 1)
                        self.table_results.setItem(
                            self.table_row, 0,
                            QtWidgets.QTableWidgetItem(self.cell_word))
                        self.table_results.setItem(
                            self.table_row, 1,
                            QtWidgets.QTableWidgetItem(self.cell_rank))
                        self.table_results.setItem(
                            self.table_row, 2,
                            QtWidgets.QTableWidgetItem(self.cell_date))
                        self.table_row += 1
                        self.label_info.setText('Запрос обработан.\nДля сохранения статистики\nнажмите кнопку \"Сохранить\".')
                    else:
                        self.label_info.setText('Этот запрос уже обработан.\nВведите другой запрос.')
                    self.recent_limit = self.limit_data[1]
                    self.lcdNumber_hour_limit.setProperty(
                        "intValue", self.recent_limit)
                    self.lcdNumber_day_limit.setProperty(
                        "intValue", (self.day_limit - self.limit_data[2]-1))
                    self.res_list.append((
                        self.query.encode('utf-8').decode('cp1251'),
                        self.rank,
                        self.req_date,))
                    self.sql_con(self.res_list)
                    self.res_list = []
                    self.rank = 0
                    self.recent_limit = self.limit_data[1] - 1
                    limit_resume = str(self.recent_limit) + '\
                                     - Winter is close!'
                else:
                    limit_resume = str(self.recent_limit) + '\
                            Hour limit is here... Wait about ' +\
                        str(60 - int(datetime.now().strftime('%M'))) +\
                        ' minuntes, please!'
            self.sql_con(self.res_list)
            self.res_list = []
            self.rank = 0
            self.file_taken = False
            # print(limit_resume)
        else:
            r = requests.get(self.query_url + self.query)
            self.r_count += 1
            self.limit_data = limit(
                                self.r_count, self.db_path, self.req_date,
                                self.day_limit, self.day_overdraft,
                                self.limit_police, self.hour, self.search_work)
            result = r.text
            result_list = result.split('<url>')
            for i, item in enumerate(result_list):
                if self.rate_url in item:
                    self.rank += i
                    break
            if self.rank != 0:
                self.cell_rank = str(self.rank)
            else:
                self.cell_rank = "< 100"
            self.cell_date = self.req_date
            # print(len(self.recent_requests))
            if (self.query not in self.recent_requests):
                self.cell_word = self.query
                self.recent_requests.append(self.query)
                self.table_results.setRowCount(self.table_row + 1)
                self.table_results.setItem(
                        self.table_row, 0,
                        QtWidgets.QTableWidgetItem(self.cell_word))
                self.table_results.setItem(
                        self.table_row, 1,
                        QtWidgets.QTableWidgetItem(self.cell_rank))
                self.table_results.setItem(
                        self.table_row, 2,
                        QtWidgets.QTableWidgetItem(self.cell_date))
                self.table_row += 1
                self.label_info.setText(
                        'Запрос обработан.\nДля сохранения статистики\nнажмите кнопку \"Сохранить\".')
            else:
                self.label_info.setText('Этот запрос уже обработан.\nВведите другой запрос.')
            self.recent_limit = self.limit_data[1]
            self.lcdNumber_hour_limit.setProperty(
                "intValue", self.recent_limit)
            self.lcdNumber_day_limit.setProperty(
                "intValue", (self.day_limit - self.limit_data[2]-1))
            self.res_list.append((
                self.query.encode('utf-8').decode('cp1251'),
                self.rank,
                self.req_date,))
            self.sql_con(self.res_list)
            self.res_list = []
        self.search_work = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YaP = yap()
    ui = Ui_YaP()
    ui.setupUi(YaP)
    ui.btn_search.clicked.connect(ui.set_query)
    ui.btn_search.clicked.connect(ui.start_search)
    ui.btn_fileopen.clicked.connect(ui.showOpenDialog)
    ui.btn_save.clicked.connect(ui.db_xls)
    ui.radioButton_single_mode.toggled.connect(ui.mode_selector)
    YaP.show()
    sys.exit(app.exec_())
