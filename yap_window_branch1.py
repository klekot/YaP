# -*- coding: utf-8 -*-

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
                Ui_YaP.add_line(ui, event)
                # Ui_YaP.start_search(ui, event)


class TableWidget(QtWidgets.QTableWidget):

    def __init__(self, parent=None):

        QtWidgets.QTableWidget.__init__(self, parent)

    def contextMenuEvent(self, event):
        self.menu = QtWidgets.QMenu(self)
        renameAction = QtWidgets.QAction('Удалить из списка', self)
        renameAction.triggered.connect(self.del_row)
        self.menu.addAction(renameAction)
        # add other required actions
        self.menu.popup(QtGui.QCursor.pos())

    def del_row(self):
        rows = sorted(set(index.row() for index in
                          ui.table_results.selectedIndexes()))
        for row in rows:
            ui.table_results.removeRow(row)
            ui.table_list.pop(ui.table_indexes[row])


class Ui_YaP(object):
    # сайт для которого рассситывается рейтинг
    rate_url = 'poligon.info'
    # ключевое слово, для которого вычисляется позиция в выдаче Яндекса
    query = ''
    # список результатов рейтинга
    res_list = []
    # позиция в выдаче Яндекса
    rank = 0
    # имя xls-файла для списка запросов и вывода по ним статистики рейтингов
    fname = ''
    # счётчик запросов к Яндексу
    r_count = 0
    # путь к файлу с базой данных sqlite3
    db_path = 'keywords.db'
    # путь к файлу с данными по рейтингам запросов
    xls_path = 'rating.xls'
    # кол-во столбцов в таблице представления данных
    table_row = 0
    # дневной лимит запросов, предоставленный Яндексом
    day_limit = 460
    # превышение лимита запросов за предыдущий день
    day_overdraft = 0
    # лимит запросов в текущем часу
    recent_limit = 0
    # список запросов, отображаемых в таблице
    table_list = []
    # список номеров строк в таблице с текущими запросами
    table_indexes = []
    # сюда поступают одиночные запросы перед добавлением в таблицу
    table_add = []
    # переключатель для функции подссёта лимитов(чтобы не считал вхолостую)
    search_work = False
    # показатель для смены заголовка режима работы в группе поиска
    mode_header = 's'
    # данные по текущим лимитам, заполняются возвратом от функции limit()
    limit_data = [True, 46, 460]
    # политика Яндекса по распределению лимитов по времени суток
    # первая позиция - лимит запросов, следующие - это часы от 0 до 23,
    # в течение которых действуют указанные лимиты
    limit_police = [[230, 0, 5, 22, 23],
                    [276, 1, 2, 3, 4],
                    [161, 6, 21],
                    [92, 7, 20],
                    [46, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    # текущий час суток
    # формат: strftime('%Y-%m-%d %H:%M:%S')
    hour = int(datetime.now().strftime('%H'))
    # текущая дата
    req_date = str(datetime.now().strftime('%Y-%m-%d'))
    # URL запроса к Яндексу
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
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
        self.radioButton_file_mode.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.radioButton_file_mode.setObjectName("radioButton_file_mode")
        self.radioButton_file_mode.autoExclusive()
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_mode)
        self.checkBox.setGeometry(QtCore.QRect(10, 60, 211, 21))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.groupBox_mode, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.groupBox_limits = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_limits.sizePolicy().hasHeightForWidth())
        self.groupBox_limits.setSizePolicy(sizePolicy)
        self.groupBox_limits.setMinimumSize(QtCore.QSize(220, 340))
        self.groupBox_limits.setObjectName("groupBox_limits")
        self.splitter_gb_limits = QtWidgets.QSplitter(self.groupBox_limits)
        self.splitter_gb_limits.setGeometry(QtCore.QRect(20, -10, 177, 331))
        self.splitter_gb_limits.setOrientation(QtCore.Qt.Vertical)
        self.splitter_gb_limits.setObjectName("splitter_gb_limits")
        self.label_day_limit = QtWidgets.QLabel(self.splitter_gb_limits)
        self.label_day_limit.setObjectName("label_day_limit")
        self.lcdNumber_day_limit = QtWidgets.QLCDNumber(
            self.splitter_gb_limits)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_day_limit.setFont(font)
        self.lcdNumber_day_limit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_day_limit.setDigitCount(3)
        self.lcdNumber_day_limit.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_day_limit.setProperty(
                    "intValue", (self.day_limit - self.limit_data[2])-1)
        self.lcdNumber_day_limit.setObjectName("lcdNumber_day_limit")
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
        self.lcdNumber_hour_limit.setProperty("intValue", self.limit_data[1])
        self.lcdNumber_hour_limit.setObjectName("lcdNumber_hour_limit")
        self.gridLayout.addWidget(self.groupBox_limits, 1, 1, 1, 1)
        self.groupBox_info = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_info.sizePolicy().hasHeightForWidth())
        self.groupBox_info.setSizePolicy(sizePolicy)
        self.groupBox_info.setMinimumSize(QtCore.QSize(0, 110))
        self.groupBox_info.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_info.setObjectName("groupBox_info")
        self.label_info = QtWidgets.QLabel(self.groupBox_info)
        self.label_info.setGeometry(QtCore.QRect(20, 10, 188, 81))
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
        self.gridLayout.addWidget(self.groupBox_info, 3, 1, 2, 1)
        self.btn_save = QtWidgets.QPushButton(YaP)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 5, 1, 1, 1)
        self.groupBox_main = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_main.sizePolicy().hasHeightForWidth())
        self.groupBox_main.setSizePolicy(sizePolicy)
        self.groupBox_main.setMinimumSize(QtCore.QSize(530, 600))
        self.groupBox_main.setSizeIncrement(QtCore.QSize(600, 0))
        self.groupBox_main.setFlat(False)
        self.groupBox_main.setCheckable(False)
        self.groupBox_main.setObjectName("groupBox_main")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_main)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_main = QtWidgets.QGridLayout()
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.btn_search = QtWidgets.QPushButton(self.groupBox_main)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_main.addWidget(self.btn_search, 0, 4, 1, 1)
        self.lineEdit_single_query = QtWidgets.QLineEdit(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_single_query.sizePolicy().hasHeightForWidth())
        self.lineEdit_single_query.setSizePolicy(sizePolicy)
        self.lineEdit_single_query.setMinimumSize(QtCore.QSize(37, 0))
        self.lineEdit_single_query.setObjectName("lineEdit_single_query")
        self.gridLayout_main.addWidget(self.lineEdit_single_query, 0, 1, 1, 3)
        self.btn_fileopen = QtWidgets.QPushButton(self.groupBox_main)
        self.btn_fileopen.setObjectName("btn_fileopen")
        self.gridLayout_main.addWidget(self.btn_fileopen, 0, 0, 1, 1)
        self.btn_fileopen.setDisabled(True)
        self.table_results = TableWidget(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.table_results.sizePolicy().hasHeightForWidth())
        self.table_results.setSizePolicy(sizePolicy)
        self.table_results.setMinimumSize(QtCore.QSize(500, 496))
        self.table_results.setRowCount(0)
        self.table_results.setColumnCount(3)
        self.table_results.setHorizontalHeaderLabels(
                    "КЛЮЧЕВОЕ СЛОВО;МЕСТО В ПОИСКЕ;ДАТА ЗАПРОСА".split(";"))
        self.table_results.setObjectName("table_results")
        self.table_results.horizontalHeader().setCascadingSectionResizes(False)
        self.table_results.horizontalHeader().setDefaultSectionSize(170)
        self.table_results.horizontalHeader().setMinimumSectionSize(31)
        self.table_results.horizontalHeader().setSortIndicatorShown(False)
        self.table_results.horizontalHeader().setStretchLastSection(False)
        self.table_results.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_main.addWidget(self.table_results, 1, 0, 1, 5)
        self.label_filepath = QtWidgets.QLabel(self.groupBox_main)
        self.label_filepath.setMinimumSize(QtCore.QSize(0, 42))
        self.label_filepath.setObjectName("label_filepath")
        self.gridLayout_main.addWidget(self.label_filepath, 2, 0, 1, 5)
        self.gridLayout_3.addLayout(self.gridLayout_main, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_main, 0, 0, 6, 1)

        self.retranslateUi(YaP)
        QtCore.QMetaObject.connectSlotsByName(YaP)

    def retranslateUi(self, YaP):
        _translate = QtCore.QCoreApplication.translate
        YaP.setWindowTitle(
            _translate(
                "YaP",
        "YaP - Yandex xml Parser for gathering of keyword's rating statistics."))
        self.groupBox_mode.setTitle(_translate("YaP", "Режим поиска"))
        self.radioButton_single_mode.setText(
                        _translate("YaP", "Одиночный поиск"))
        self.radioButton_file_mode.setText(_translate("YaP", "Пакетный поиск"))
        self.checkBox.setText(
            _translate("YaP", "Очищать таблицу при смене режима"))
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
                        _translate("YaP", ""))
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

    def clean_table(self):
        if self.checkBox.isChecked():
            self.table_results.setRowCount(0)
            self.table_results.setItem(0, 0, QtWidgets.QTableWidgetItem(''))
            self.table_results.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
            self.table_results.setItem(0, 2, QtWidgets.QTableWidgetItem(''))
            self.table_row = 0
            self.table_list = []

    def set_query(self, event):
        self.table_add = []
        # введенный текст -> в запрос
        line_query = self.lineEdit_single_query.text()
        # обнулили показатель позиции в поиске
        self.rank = 0
        # очистили поле ввода запроса
        self.lineEdit_single_query.setText('')
        self.table_list.append([line_query, False])
        self.table_indexes.append(len(self.table_list))
        self.table_add.append([line_query, False])

    def add_line(self, event):
        # self.remove_empty_rows(0)
        self.table_input(self.table_add)
        # self.remove_empty_rows(0)

    def showOpenDialog(self):
        self.remove_empty_rows(0)
        # обнулили показатель позиции в поиске
        self.rank = 0
        # обнулили путь к файлу xls в окошке программы
        self.label_filepath.setText('')
        # обнулили информацию в окне программы
        self.label_info.setText('')
        # вызываем диалог выбора файла
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            YaP, 'Open file',
            'C:\\Users\\gnato\\Desktop\\Igor\\progs\\python_progs\\YaP\\')
        if len(self.fname) > 0:
            book = xlrd.open_workbook(self.fname, 'rt', formatting_info=True)
            sh = book.sheet_by_index(0)
            self.btn_search.setDisabled(False)
        else:
            # обработали вариант когда выбор файла отменён
            self.label_info.setText('Файл не выбран!')
            return
        # помещаем запросы из файла в список
        for i in range(sh.nrows):
            self.table_list.append([sh.cell_value(i, 0), False])
        for i in range(len(self.table_list)):
            self.table_indexes.append(i)
        self.table_input(self.table_list)
        # формируем строку для отображения пути к оркрытому xls-файлу
        ################################################################
        fname_chars = []
        for char in self.fname:
            if (char == '/'):
                fname_chars.append('\\')
            else:
                fname_chars.append(char)
        win_path = ''.join(fname_chars)
        self.label_filepath.setText(win_path)
        #################################################################

    def table_input(self, add_list):
        # выводим в таблицу список уникальных запросов из файла
        for i, item in enumerate(add_list):
            # self.table_row += 1
            self.table_results.setRowCount(self.table_row + 1)
            self.table_results.setItem(
                self.table_row, 0,
                QtWidgets.QTableWidgetItem(item[0]))
            # self.table_row -= 1
        # self.remove_empty_rows(0)

    def start_search(self, event):
        # поднимаем флаг search_work для подсчёта лимитов
        self.search_work = True
        #################################################################
        for i, item in enumerate(self.table_list):
            self.query = self.table_list[i][0]
            print(self.query)
            if (len(self.query) != 0):
                if (self.table_list[i][1] != True):
                    r = requests.get(self.query_url + self.query)
                    self.r_count += 1
                    self.table_list[i][1] = True
                    self.limit_data = limit(
                                    self.r_count, self.db_path, self.req_date,
                                    self.day_limit, self.day_overdraft,
                                    self.limit_police, self.hour,
                                    self.search_work)
                    # Проверяем не исчерпан ли часовой лимит на запросы.
                    if (self.limit_data[0]) and (self.limit_data[2] > 0):
                        # лимит в этом часу доступен и суточный не исчерпан
                        self.ranking(r)
                        self.sql_con(self.res_list)
                        # self.remove_empty_rows(1)
                        self.display_results()
                        # self.remove_empty_rows(1)
                        self.res_list = []
                        self.rank = 0
                    elif (self.limit_data[0] == False) and (self.limit_data[2] > 0):
                        # лимит в этом часу исчерпан, но суточный еще доступен
                        self.label_info.setText(
                            'Превышен лимит запросов!\nОжидайте ' +
                            str(60 - int(datetime.now().strftime('%M'))) +
                            ' минут.')
                        self.remove_empty_rows(1)
                        return
                    else:
                        # суточный лимит не доступен
                        self.label_info.setText(
                            'Превышен суточный лимит запросов!\n\
Заходите завтра :)')
                        # self.remove_empty_rows(1)
                        return
                    self.sql_con(self.res_list)
                    self.res_list = []
                    self.rank = 0
                    self.recent_limit = self.limit_data[1] - 1
                else:
                    continue
            else:
                # случай пустого запроса
                self.label_info.setText('Внимание!\nБыл выбран пустой запрос.')
                self.remove_empty_rows(1)
        self.search_work = False

    def ranking(self, r):
        print('ranking')
        result = r.text
        result_list = result.split('<url>')
        for i, item in enumerate(result_list):
            if self.rate_url in item:
                self.rank += i
                break
        self.limits_show()
        self.res_list.append((
            self.query.encode('utf-8').decode('cp1251'),
            self.rank,
            self.req_date,))

    def limits_show(self):
        self.recent_limit = self.limit_data[1]
        self.lcdNumber_hour_limit.setProperty(
            "intValue", self.recent_limit)
        self.lcdNumber_day_limit.setProperty(
            "intValue", (self.day_limit - self.limit_data[2]-1))

    def sql_con(self, res_list):
        print('sql_con start')
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute("select name from sqlite_master \
            where type='table' and name='requests'")
        if db.fetchone():
            for res in self.res_list:
                k = (self.query.encode('utf-8').decode('cp1251'),
                     self.req_date,)
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
        print('sql_con end')

    def display_results(self):
        print('display_results starts')
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        k = (self.query.encode('utf-8').decode('cp1251'),
             self.req_date,)
        db.execute("select * from requests where keyword=? and date=?", k)
        arr = []
        for res in db.fetchone():
            if res != 0:
                arr.append(res)
            else:
                arr.append('> 100')
        for i in range(len(arr)):
            self.table_results.setRowCount(
                self.table_row + 1)
            self.table_results.setItem(
                self.table_row, i, QtWidgets.QTableWidgetItem(
                    str(arr[i]).encode('cp1251').decode('utf-8')))
        self.table_row += 1
        db.close()
        conn.close()
        self.remove_empty_rows(1)
        print('display_results end')

    def remove_empty_rows(self, col):
        for i in range(self.table_results.rowCount()):
            if (self.table_results.item(i, col) == None):
                self.table_results.removeRow(i)

    def db_xls(self):  # все записи БД из таблицы request переносит в xls-файл
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
            wb.save(self.xls_path)
        db.close()
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YaP = yap()
    ui = Ui_YaP()
    ui.setupUi(YaP)
    # ui.btn_search.clicked.connect(ui.set_query)
    # ui.btn_search.clicked.connect(ui.add_line)
    ui.btn_search.clicked.connect(ui.start_search)
    ui.btn_fileopen.clicked.connect(ui.showOpenDialog)
    ui.btn_save.clicked.connect(ui.db_xls)
    ui.radioButton_single_mode.toggled.connect(ui.mode_selector)
    ui.radioButton_single_mode.toggled.connect(ui.clean_table)
    ui.radioButton_file_mode.toggled.connect(ui.mode_selector)
    ui.radioButton_file_mode.toggled.connect(ui.clean_table)
    YaP.show()
    sys.exit(app.exec_())
