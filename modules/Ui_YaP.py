# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets  # , QtWebKitWidgets
from modules.TableWidget import TableWidget
from modules.Graphics import Graphics
from modules.table_input import table_input
from modules.remove_empty_rows import remove_empty_rows
from modules.search import search
from modules.graphicsBuilder import graphicsBuilder
from modules.allKeywords import allKeywords
from modules.Log import Log
import time
from datetime import datetime
from modules.timerThread import timerThread


class Ui_YaP(object):

    table_row = 0
    call_count = 0

    def __init__(self, table_list, table_add, limit_data,
                 day_limit, table_indexes, rank, search_work,
                 query_url, req_date, day_overdraft, limit_police,
                 hour, res_list, rate_url, query, db_path, xls_path,
                 logs_path, ref_path):
        self.db_path = db_path
        self.xls_path = xls_path
        self.logs_path = logs_path
        self.query = query
        self.rate_url = rate_url
        self.res_list = res_list
        self.hour = hour
        self.limit_police = limit_police
        self.day_overdraft = day_overdraft
        self.req_date = req_date
        self.query_url = query_url
        self.search_work = search_work
        self.rank = rank
        self.table_indexes = table_indexes
        self.table_list = table_list
        self.table_add = table_add
        self.limit_data = limit_data
        self.day_limit = day_limit
        self.mode_header = 'f'
        self.timesComboCurrentText = 'неделя'
        self.keywordsComboCurrentText = ''
        self.tableDivision = 1
        self.letsDraw = False
        self.fetchArr = []
        self.value = 0
        self.new_limit = 0
        self.circle = 0
        self.alive = True
        self.ref_path = ref_path
        self.data_source = 'file'
        self.search_count = 0
        self.file_search_count = False

    def setupUi(self, YaP):
        self.log = Log(self.db_path, self.logs_path)
        YaP.setObjectName("YaP")
        YaP.setEnabled(True)
        YaP.resize(908, 685)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(YaP.sizePolicy().hasHeightForWidth())
        YaP.setSizePolicy(sizePolicy)
        YaP.setMinimumSize(QtCore.QSize(800, 600))
        YaP.setSizeIncrement(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(YaP)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 2, 1, 1)
        '''
        self.btn_exit = QtWidgets.QPushButton(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 5, 2, 1, 1)
        '''
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
        self.splitter_gb_limits.setGeometry(QtCore.QRect(20, 20, 177, 331))
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
            "intValue", (self.day_limit - self.limit_data[2]) - 1)
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
        self.gridLayout.addWidget(self.groupBox_limits, 1, 2, 1, 1)
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
        self.gridLayout.addWidget(self.groupBox_info, 2, 2, 2, 1)
        self.tabWidget = QtWidgets.QTabWidget(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_main = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(
            self.groupBox_main.sizePolicy().hasHeightForWidth())
        self.groupBox_main.setSizePolicy(sizePolicy)
        self.groupBox_main.setMinimumSize(QtCore.QSize(530, 600))
        self.groupBox_main.setSizeIncrement(QtCore.QSize(600, 0))
        self.groupBox_main.setFlat(False)
        self.groupBox_main.setCheckable(False)
        self.groupBox_main.setObjectName("groupBox_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_fileopen = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_fileopen.sizePolicy().hasHeightForWidth())
        self.btn_fileopen.setSizePolicy(sizePolicy)
        self.btn_fileopen.setObjectName("btn_fileopen")
        self.gridLayout_2.addWidget(self.btn_fileopen, 0, 0, 1, 1)
        if self.limit_data[1] != 0:
            self.btn_fileopen.setDisabled(False)
        else:
            self.btn_fileopen.setDisabled(True)
        self.btn_input = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_input.sizePolicy().hasHeightForWidth())
        self.btn_input.setSizePolicy(sizePolicy)
        self.btn_input.setObjectName("btn_input")
        self.gridLayout_2.addWidget(self.btn_input, 0, 3, 1, 1)
        self.btn_input.setDisabled(True)
        self.table_results = TableWidget(
            self.table_list, self.table_indexes, self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(
            self.table_results.sizePolicy().hasHeightForWidth())
        self.table_results.setSizePolicy(sizePolicy)
        self.table_results.setMinimumSize(QtCore.QSize(500, 496))
        self.table_results.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_results.setMidLineWidth(1)
        self.table_results.setAlternatingRowColors(True)
        self.table_results.setRowCount(0)
        self.table_results.setColumnCount(3)
        self.table_results.setHorizontalHeaderLabels(
            "КЛЮЧЕВОЕ СЛОВО;МЕСТО В ПОИСКЕ;ДАТА ЗАПРОСА".split(";"))
        self.table_results.setObjectName("table_results")
        self.table_results.horizontalHeader().setCascadingSectionResizes(True)
        self.table_results.horizontalHeader().setDefaultSectionSize(200)
        self.table_results.horizontalHeader().setMinimumSectionSize(31)
        self.table_results.horizontalHeader().setSortIndicatorShown(True)
        self.table_results.horizontalHeader().setStretchLastSection(True)
        self.table_results.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.table_results, 1, 0, 1, 4)
        self.label_filepath = QtWidgets.QLabel(self.groupBox_main)
        self.label_filepath.setMinimumSize(QtCore.QSize(0, 42))
        self.label_filepath.setObjectName("label_filepath")
        self.gridLayout_2.addWidget(self.label_filepath, 2, 0, 1, 2)
        self.btn_search = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setDisabled(True)
        self.gridLayout_2.addWidget(self.btn_search, 2, 2, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_2.addWidget(self.btn_save, 2, 3, 1, 1)
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
        self.gridLayout_2.addWidget(self.lineEdit_single_query, 0, 1, 1, 2)
        self.lineEdit_single_query.setDisabled(True)
        self.horizontalLayout.addWidget(self.groupBox_main)
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(100, 16777215))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.graphicsView = Graphics(self.tab_2, self.tableDivision,
                                     self.letsDraw, self.db_path,
                                     self.fetchArr)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 1, 0, 1, 6)
        self.tabWidget.addTab(self.tab_2, "")
        self.timesCombo = QtWidgets.QComboBox(self.tab_2)
        self.timesCombo.setObjectName("timesCombo")
        self.gridLayout_3.addWidget(self.timesCombo, 0, 5, 1, 1)
        self.timesCombo.addItems(["Неделя",
                                  "Месяц",
                                  "Квартал",
                                  "Полугодие",
                                  "Год",
                                  "Всё время (in progress)"])
        self.timesCombo.activated[str].connect(
            self.setTimesComboCurrentText)
        self.timesCombo.activated[str].connect(self.graphicsRequest)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(90, 0))
        self.label_3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 4, 1, 1)
        self.keywordsCombo = QtWidgets.QComboBox(self.tab_2)
        self.keywordsCombo.setEditable(False)
        self.keywordsCombo.setObjectName("keywordsCombo")
        self.gridLayout_3.addWidget(self.keywordsCombo, 0, 1, 1, 2)
        self.keywordsCombo.addItems(allKeywords(self.db_path))
        self.keywordsCombo.activated[str].connect(
            self.setKeywordsComboCurrentText)
        self.keywordsCombo.activated[str].connect(self.graphicsRequest)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.setLogFilePath_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.setLogFilePath_lineEdit.setGeometry(
            QtCore.QRect(10, 190, 450, 20))
        self.setLogFilePath_lineEdit.setObjectName("setLogFilePath_lineEdit")
        self.setLogFilePath_lineEdit.setText(self.logs_path)
        self.setSiteAddres_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.setSiteAddres_lineEdit.setGeometry(QtCore.QRect(10, 40, 450, 20))
        self.setSiteAddres_lineEdit.setObjectName("setSiteAddres_lineEdit")
        self.setSiteAddres_lineEdit.setText(self.rate_url)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_30.setObjectName("label_30")
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(10, 170, 161, 16))
        self.label_32.setObjectName("label_32")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(10, 20, 241, 16))
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setGeometry(QtCore.QRect(10, 120, 211, 16))
        self.label_31.setObjectName("label_31")
        self.setXlsFilePath_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.setXlsFilePath_lineEdit.setGeometry(
            QtCore.QRect(10, 140, 450, 20))
        self.setXlsFilePath_lineEdit.setObjectName("setXlsFilePath_lineEdit")
        self.setXlsFilePath_lineEdit.setText(self.xls_path)
        self.setDbFilePath_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.setDbFilePath_lineEdit.setGeometry(QtCore.QRect(10, 90, 450, 20))
        self.setDbFilePath_lineEdit.setObjectName("setDbFilePath_lineEdit")
        self.setDbFilePath_lineEdit.setText(self.db_path)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 331, 161))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_h09 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h09.setGeometry(QtCore.QRect(50, 70, 31, 20))
        self.lineEdit_h09.setObjectName("lineEdit_h09")
        self.lineEdit_h09.setText(str(self.limit_police[9][0]))
        self.lineEdit_h22 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h22.setGeometry(QtCore.QRect(250, 120, 31, 20))
        self.lineEdit_h22.setObjectName("lineEdit_h22")
        self.lineEdit_h22.setText(str(self.limit_police[22][0]))
        self.lineEdit_h15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h15.setGeometry(QtCore.QRect(290, 70, 31, 20))
        self.lineEdit_h15.setObjectName("lineEdit_h15")
        self.lineEdit_h15.setText(str(self.limit_police[15][0]))
        self.label_h03 = QtWidgets.QLabel(self.groupBox)
        self.label_h03.setGeometry(QtCore.QRect(140, 40, 16, 16))
        self.label_h03.setObjectName("label_h03")
        self.label_h15 = QtWidgets.QLabel(self.groupBox)
        self.label_h15.setGeometry(QtCore.QRect(300, 90, 16, 16))
        self.label_h15.setObjectName("label_h15")
        self.lineEdit_h14 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h14.setGeometry(QtCore.QRect(250, 70, 31, 20))
        self.lineEdit_h14.setObjectName("lineEdit_h14")
        self.lineEdit_h14.setText(str(self.limit_police[14][0]))
        self.lineEdit_h07 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h07.setGeometry(QtCore.QRect(290, 20, 31, 20))
        self.lineEdit_h07.setObjectName("lineEdit_h07")
        self.lineEdit_h07.setText(str(self.limit_police[7][0]))
        self.lineEdit_h12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h12.setGeometry(QtCore.QRect(170, 70, 31, 20))
        self.lineEdit_h12.setObjectName("lineEdit_h12")
        self.lineEdit_h12.setText(str(self.limit_police[12][0]))
        self.lineEdit_h03 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h03.setGeometry(QtCore.QRect(130, 20, 31, 20))
        self.lineEdit_h03.setObjectName("lineEdit_h03")
        self.lineEdit_h03.setText(str(self.limit_police[3][0]))
        self.label_h09 = QtWidgets.QLabel(self.groupBox)
        self.label_h09.setGeometry(QtCore.QRect(60, 90, 16, 16))
        self.label_h09.setObjectName("label_h09")
        self.lineEdit_h16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h16.setGeometry(QtCore.QRect(10, 120, 31, 20))
        self.lineEdit_h16.setObjectName("lineEdit_h16")
        self.lineEdit_h16.setText(str(self.limit_police[16][0]))
        self.lineEdit_h02 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h02.setGeometry(QtCore.QRect(90, 20, 31, 20))
        self.lineEdit_h02.setObjectName("lineEdit_h02")
        self.lineEdit_h02.setText(str(self.limit_police[2][0]))
        self.label_h06 = QtWidgets.QLabel(self.groupBox)
        self.label_h06.setGeometry(QtCore.QRect(260, 40, 16, 16))
        self.label_h06.setObjectName("label_h06")
        self.label_h18 = QtWidgets.QLabel(self.groupBox)
        self.label_h18.setGeometry(QtCore.QRect(100, 140, 16, 16))
        self.label_h18.setObjectName("label_h18")
        self.lineEdit_h18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h18.setGeometry(QtCore.QRect(90, 120, 31, 20))
        self.lineEdit_h18.setObjectName("lineEdit_h18")
        self.lineEdit_h18.setText(str(self.limit_police[18][0]))
        self.lineEdit_h20 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h20.setGeometry(QtCore.QRect(170, 120, 31, 20))
        self.lineEdit_h20.setObjectName("lineEdit_h20")
        self.lineEdit_h20.setText(str(self.limit_police[20][0]))
        self.lineEdit_h17 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h17.setGeometry(QtCore.QRect(50, 120, 31, 20))
        self.lineEdit_h17.setObjectName("lineEdit_h17")
        self.lineEdit_h17.setText(str(self.limit_police[17][0]))
        self.lineEdit_h21 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h21.setGeometry(QtCore.QRect(210, 120, 31, 20))
        self.lineEdit_h21.setObjectName("lineEdit_h21")
        self.lineEdit_h21.setText(str(self.limit_police[21][0]))
        self.lineEdit_h23 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h23.setGeometry(QtCore.QRect(290, 120, 31, 20))
        self.lineEdit_h23.setObjectName("lineEdit_h23")
        self.lineEdit_h23.setText(str(self.limit_police[23][0]))
        self.lineEdit_h11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h11.setGeometry(QtCore.QRect(130, 70, 31, 20))
        self.lineEdit_h11.setObjectName("lineEdit_h11")
        self.lineEdit_h11.setText(str(self.limit_police[11][0]))
        self.label_h21 = QtWidgets.QLabel(self.groupBox)
        self.label_h21.setGeometry(QtCore.QRect(220, 140, 16, 16))
        self.label_h21.setObjectName("label_h21")
        self.label_h08 = QtWidgets.QLabel(self.groupBox)
        self.label_h08.setGeometry(QtCore.QRect(20, 90, 16, 16))
        self.label_h08.setObjectName("label_h08")
        self.label_h22 = QtWidgets.QLabel(self.groupBox)
        self.label_h22.setGeometry(QtCore.QRect(260, 140, 16, 16))
        self.label_h22.setObjectName("label_h22")
        self.lineEdit_h08 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h08.setGeometry(QtCore.QRect(10, 70, 31, 20))
        self.lineEdit_h08.setObjectName("lineEdit_h08")
        self.lineEdit_h08.setText(str(self.limit_police[8][0]))
        self.label_h04 = QtWidgets.QLabel(self.groupBox)
        self.label_h04.setGeometry(QtCore.QRect(180, 40, 16, 16))
        self.label_h04.setObjectName("label_h04")
        self.label_h00 = QtWidgets.QLabel(self.groupBox)
        self.label_h00.setGeometry(QtCore.QRect(20, 40, 16, 16))
        self.label_h00.setObjectName("label_h00")
        self.label_h01 = QtWidgets.QLabel(self.groupBox)
        self.label_h01.setGeometry(QtCore.QRect(60, 40, 16, 16))
        self.label_h01.setObjectName("label_h01")
        self.label_h10 = QtWidgets.QLabel(self.groupBox)
        self.label_h10.setGeometry(QtCore.QRect(100, 90, 16, 16))
        self.label_h10.setObjectName("label_h10")
        self.lineEdit_h04 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h04.setGeometry(QtCore.QRect(170, 20, 31, 20))
        self.lineEdit_h04.setObjectName("lineEdit_h04")
        self.lineEdit_h04.setText(str(self.limit_police[4][0]))
        self.lineEdit_h13 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h13.setGeometry(QtCore.QRect(210, 70, 31, 20))
        self.lineEdit_h13.setObjectName("lineEdit_h13")
        self.lineEdit_h13.setText(str(self.limit_police[13][0]))
        self.label_h11 = QtWidgets.QLabel(self.groupBox)
        self.label_h11.setGeometry(QtCore.QRect(140, 90, 16, 16))
        self.label_h11.setObjectName("label_h11")
        self.label_h02 = QtWidgets.QLabel(self.groupBox)
        self.label_h02.setGeometry(QtCore.QRect(100, 40, 16, 16))
        self.label_h02.setObjectName("label_h02")
        self.lineEdit_h10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h10.setGeometry(QtCore.QRect(90, 70, 31, 20))
        self.lineEdit_h10.setObjectName("lineEdit_h10")
        self.lineEdit_h10.setText(str(self.limit_police[10][0]))
        self.label_h12 = QtWidgets.QLabel(self.groupBox)
        self.label_h12.setGeometry(QtCore.QRect(180, 90, 16, 16))
        self.label_h12.setObjectName("label_h12")
        self.label_h05 = QtWidgets.QLabel(self.groupBox)
        self.label_h05.setGeometry(QtCore.QRect(220, 40, 16, 16))
        self.label_h05.setObjectName("label_h05")
        self.lineEdit_h06 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h06.setGeometry(QtCore.QRect(250, 20, 31, 20))
        self.lineEdit_h06.setObjectName("lineEdit_h06")
        self.lineEdit_h06.setText(str(self.limit_police[6][0]))
        self.lineEdit_h00 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h00.setGeometry(QtCore.QRect(10, 20, 31, 20))
        self.lineEdit_h00.setObjectName("lineEdit_h00")
        self.lineEdit_h00.setText(str(self.limit_police[0][0]))
        self.label_h14 = QtWidgets.QLabel(self.groupBox)
        self.label_h14.setGeometry(QtCore.QRect(260, 90, 16, 16))
        self.label_h14.setObjectName("label_h14")
        self.label_h17 = QtWidgets.QLabel(self.groupBox)
        self.label_h17.setGeometry(QtCore.QRect(60, 140, 16, 16))
        self.label_h17.setObjectName("label_h17")
        self.label_h23 = QtWidgets.QLabel(self.groupBox)
        self.label_h23.setGeometry(QtCore.QRect(300, 140, 16, 16))
        self.label_h23.setObjectName("label_h23")
        self.lineEdit_h19 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h19.setGeometry(QtCore.QRect(130, 120, 31, 20))
        self.lineEdit_h19.setObjectName("lineEdit_h19")
        self.lineEdit_h19.setText(str(self.limit_police[19][0]))
        self.lineEdit_h05 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h05.setGeometry(QtCore.QRect(210, 20, 31, 20))
        self.lineEdit_h05.setObjectName("lineEdit_h05")
        self.lineEdit_h05.setText(str(self.limit_police[5][0]))
        self.label_h07 = QtWidgets.QLabel(self.groupBox)
        self.label_h07.setGeometry(QtCore.QRect(300, 40, 16, 16))
        self.label_h07.setObjectName("label_h07")
        self.label_h20 = QtWidgets.QLabel(self.groupBox)
        self.label_h20.setGeometry(QtCore.QRect(180, 140, 16, 16))
        self.label_h20.setObjectName("label_h20")
        self.label_h19 = QtWidgets.QLabel(self.groupBox)
        self.label_h19.setGeometry(QtCore.QRect(140, 140, 16, 16))
        self.label_h19.setObjectName("label_h19")
        self.label_h16 = QtWidgets.QLabel(self.groupBox)
        self.label_h16.setGeometry(QtCore.QRect(20, 140, 16, 16))
        self.label_h16.setObjectName("label_h16")
        self.lineEdit_h01 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_h01.setGeometry(QtCore.QRect(50, 20, 31, 20))
        self.lineEdit_h01.setObjectName("lineEdit_h01")
        self.lineEdit_h01.setText(str(self.limit_police[1][0]))
        self.label_h13 = QtWidgets.QLabel(self.groupBox)
        self.label_h13.setGeometry(QtCore.QRect(220, 90, 16, 16))
        self.label_h13.setObjectName("label_h13")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_allLimits = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_allLimits.setGeometry(QtCore.QRect(200, 20, 31, 20))
        self.lineEdit_allLimits.setObjectName("lineEdit_allLimits")
        self.lineEdit_allLimits.setText(str(self.day_limit))
        self.verticalLayout.addWidget(self.groupBox_3)

        self.saveSettings_pushButton = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.saveSettings_pushButton.sizePolicy().hasHeightForWidth())
        self.saveSettings_pushButton.setSizePolicy(sizePolicy)
        self.saveSettings_pushButton.setObjectName("saveSettings_pushButton")
        self.verticalLayout.addWidget(self.saveSettings_pushButton)

        self.label_save = QtWidgets.QLabel(self.groupBox_3)
        self.label_save.setGeometry(QtCore.QRect(10, 270, 400, 16))
        self.label_save.setObjectName("label_save")

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setEnabled(True)
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.log.read(self.textEdit)
        self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_8.setVisible(False)
        self.tabWidget.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.textEdit_ref = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_ref.setGeometry(QtCore.QRect(10, 10, 631, 591))
        self.textEdit_ref.setReadOnly(True)
        self.textEdit_ref.setObjectName("textEdit_ref")
        self.tabWidget.addTab(self.tab_5, "")
        '''
        self.webView = QtWebKitWidgets.QWebView(self.tab_5)
        self.webView.setGeometry(QtCore.QRect(10, 10, 631, 591))
        self.webView.setUrl(QtCore.QUrl("file:///C:/Users/gnato/Desktop/Igor/progs/python_progs/YaP/reference.html"))
        self.webView.setObjectName("webView")
        '''
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 5, 1)
        self.groupBox_mode = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_mode.sizePolicy().hasHeightForWidth())
        self.groupBox_mode.setSizePolicy(sizePolicy)
        self.groupBox_mode.setMinimumSize(QtCore.QSize(220, 70))
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.radioButton_single_mode = QtWidgets.QRadioButton(
            self.groupBox_mode)
        self.radioButton_single_mode.setGeometry(QtCore.QRect(10, 40, 161, 21))
        self.radioButton_single_mode.setObjectName("radioButton_single_mode")
        self.radioButton_single_mode.autoExclusive()
        self.radioButton_file_mode = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_file_mode.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.radioButton_file_mode.setObjectName("radioButton_file_mode")
        self.radioButton_file_mode.autoExclusive()
        self.radioButton_file_mode.setChecked(True)
        self.gridLayout.addWidget(self.groupBox_mode, 0, 2, 1, 1)

        self.retranslateUi(YaP)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(YaP)

    def retranslateUi(self, YaP):
        _translate = QtCore.QCoreApplication.translate
        YaP.setWindowTitle(
            _translate(
                "YaP",
                "YaP - Yandex xml Parser for gathering keyword's statistics."))
        self.groupBox_limits.setTitle(_translate("YaP", "Лимиты Яндекса"))
        self.label_day_limit.setText(
            _translate("YaP", "Дневной лимит (минус овердрафт)"))
        self.label_hour_limit.setText(
            _translate("YaP", "Лимит запросов в текущем часу"))
        self.groupBox_info.setTitle(_translate("YaP", "Информация"))
        self.label_info.setText(_translate("YaP", ""))
        if self.mode_header == 's':
            self.groupBox_main.setTitle(
                _translate("YaP", "Одиночный ввод запросов"))
        elif self.mode_header == 'f':
            self.groupBox_main.setTitle(
                _translate("YaP", "Пакетный ввод запросов"))
        self.btn_fileopen.setText(_translate("YaP", "Выбрать файл"))
        self.btn_input.setText(_translate("YaP", "Ввод"))
        # self.btn_exit.setText(_translate("YaP", "Выйти из программы"))
        self.table_results.setSortingEnabled(False)
        self.label_filepath.setText(_translate("YaP", ""))
        self.btn_search.setText(_translate("YaP", "Пуск!"))
        self.btn_save.setText(_translate("YaP", "Сохранить в {}".format(self.xls_path)))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            _translate("YaP", "Определение рейтингов"))
        self.label.setText(_translate("YaP", "Ключевая фраза:"))
        self.label_3.setText(_translate("YaP", "Диапазон дат: "))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("YaP", "Графики"))
        self.groupBox_2.setTitle(
            _translate("YaP", "Исходные данные программы"))
        self.label_30.setText(
            _translate("YaP", "Путь к файлу с базой данных:"))
        self.label_32.setText(_translate("YaP", "Путь к лог-файлу:"))
        self.label_29.setText(
            _translate("YaP", "Сайт, для которого рассчитывается рейтинг:"))
        self.label_31.setText(
            _translate("YaP", "Путь к файлу со списком запросов(.xls):"))
        self.groupBox_3.setTitle(_translate("YaP", "Лимиты Яндекса"))
        self.groupBox.setTitle(
            _translate("YaP", "Разрешённое число запросов в зависимости от времени суток"))
        self.label_h03.setText(_translate("YaP", "<b>03</b>"))
        self.label_h15.setText(_translate("YaP", "<b>15</b>"))
        self.label_h09.setText(_translate("YaP", "<b>09</b>"))
        self.label_h06.setText(_translate("YaP", "<b>06</b>"))
        self.label_h18.setText(_translate("YaP", "<b>18</b>"))
        self.label_h21.setText(_translate("YaP", "<b>21</b>"))
        self.label_h08.setText(_translate("YaP", "<b>08</b>"))
        self.label_h22.setText(_translate("YaP", "<b>22</b>"))
        self.label_h04.setText(_translate("YaP", "<b>04</b>"))
        self.label_h00.setText(_translate("YaP", "<b>00</b>"))
        self.label_h01.setText(_translate("YaP", "<b>01</b>"))
        self.label_h10.setText(_translate("YaP", "<b>10</b>"))
        self.label_h11.setText(_translate("YaP", "<b>11</b>"))
        self.label_h02.setText(_translate("YaP", "<b>02</b>"))
        self.label_h12.setText(_translate("YaP", "<b>12</b>"))
        self.label_h05.setText(_translate("YaP", "<b>05</b>"))
        self.label_h14.setText(_translate("YaP", "<b>14</b>"))
        self.label_h17.setText(_translate("YaP", "<b>17</b>"))
        self.label_h23.setText(_translate("YaP", "<b>23</b>"))
        self.label_h07.setText(_translate("YaP", "<b>07</b>"))
        self.label_h20.setText(_translate("YaP", "<b>20</b>"))
        self.label_h19.setText(_translate("YaP", "<b>19</b>"))
        self.label_h16.setText(_translate("YaP", "<b>16</b>"))
        self.label_h13.setText(_translate("YaP", "<b>13</b>"))
        self.label_save.setText(_translate(
            "YaP", "<p><font color=\"red\"><b>ВНИМАНИЕ! При сохранении настроек программа завершится!</b></font></p>"))
        self.label_2.setText(_translate("YaP", "Общий лимит:"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), _translate("YaP", "Настройки программы"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5), _translate("YaP", "О проргамме"))
        self.pushButton_8.setText(_translate("YaP", "Очистить"))
        self.saveSettings_pushButton.setText(_translate("YaP", "Сохранить"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            _translate("YaP", "Лог выполнения задач"))
        self.groupBox_mode.setTitle(_translate("YaP", "Режим запросов"))
        self.radioButton_single_mode.setText(
            _translate("YaP", "Ввести одиночный запрос"))
        self.radioButton_file_mode.setText(
            _translate("YaP", "Пакетный ввод запросов"))

        self.textEdit_ref.setText(_translate("YaP", "\
\
<h1><center>О программе \"ЯП\"</center></h1>\
<p><b>\"ЯП\"</b> (расшифровывается как \"<b>Я</b>ндекс xml-парсер для поисковых запросов компании \"<b>П</b>ОЛИГОН\"\") - это программный комплекс для оценки положения ссылок на сайт компании \"ПОЛИГОН\" в результатах поисковой выдачи Яндекса по интересующим ключевым фразам.<br />\
В комплекте \"ЯП\" находятся две программы: это основная программа <b>yap_main.exe</b>, предоставляющая графический интерфейс пользователя, и её консольный аналог <b>yapco.exe</b>,\
обладающая сжатым функционалом, и предназначенная, в основном, для запуска по расписанию с целью сбора регулярных статистических данных в автоматическом режиме.</p>\
<p>Работа программы построена на обработке запросов к сервису \"Яндекс.XML\". Для пользователей этого сервиса Яндекс устанавливает определённые ограничения на количество возможных запросов в зависимости от времени суток и общего количества запросов за сутки. В связи с этим \"ЯП\" (и консольная и графическая версия) предусматривает перенос обработки запросов на ближайший допустимый временной интервал в случае превышения текущего лимита, что позволяет запускать на обработку список с запросами любой длины. При изпользовании графической версии программы пользователю всегда доступно состояние лимитов на правой панели приложения.</p>\
<h2>О вкладке \"Определение рейтингов\"</h2>\
<p>Вкладка \"Определение рейтингов\" открывается при запуске программы. Здесь у пользователя есть возможность выбрать один из двух режимов подачи запросов.<br /><span>По умолчанию выбран \"Пакетный ввод запросов\". Кнопкой \"Выбрать файл\" открывается диалог выбора файла со списком запросов. Есть жёсткое требование к формату и содержимому этого файла: он должен быть в формате именно \".xls\" и все запросы в нём должны располагаться обязательно в первом столбце таблицы. После того, как файл выбран, список запросов из него помещается в таблицу программы \"ЯП\". Нажатием кнопки \"Пуск!\" стартует отправка запросов из списка и обработка полученных данных. Ход обработки запросов сопровождается индикацией прогресса. После завершения обработки в таблицу программы напротив каждого запроса выводятся данные по месту в поисковой выдаче Яндекса и дате отправки запроса. Полученные данные автоматически сохраняются в Базу Данных. При желании пользователь может сохранить результат работы программы в xls-файл. Местоположение этого файла предварительно задаётся в настройках программы. Логично, если это будет тот же файл, который содержал список запросов. В этом случае результаты отображены напротив каждого запроса как и в таблице программы.</span><br />\
<span>В режиме \"Ввести одиночный запрос\" становится доступно поле ввода текста, при помощи которого пользователь может ввести набор ключевых фраз в таблицу программы, после чего при нажатии на кнопку \"Пуск!\" стартует процесс обработки запросов с последующим выводом результатов в таблицу программы, тождественно тому как это происходит в случае подачи запросов из файла. Также как и в случае пакетного ввода, пользователь имеет возможность сохранить результат в файл.</span>\
<h2>О вкладке \"Графики\"</h2>\
<p>На данной вкладке представлена возможность визуализировать полученные ранее данные для дальнейшего анализа. Все отправленные ранее запросы вместе с их результатами и датой отправки сохраняются в Базе Данных программы. Пользователь при помощи выбора из ниспадающего списка задаёт интересующий его запрос, а при помощи списка с диапазоном дат задаёт интересующий его временной диапазон. После чего на графике отношения позиции в выдаче Яндекса к дате запроса отображаются точки, соединённые для наглядности прямыми отрезками. Заметьте, что при выборе диапазона дат от квартала (3 месяца) и более, для позиций в поиске вычисляются усреднённые (за месяц) значения.<br /><b>Важно!!!</b><i> Обязательно явным образом выбирать из списков временных диапазонов требуемые интервалы, даже если при выборе следующего запроса уже показывается нужный, так как явное задание интервала дат активирует отрисовку графика.</i></p>\
<h2>О вкладке \"Настройки программы\"</h2>\
<p>Настройки программы разбиты на две группы: \"Исходные данные программы\" и \"Лимиты Яндекса\". В группе \"Исходные данные программы\" можно задать адрес сайта, для которого проводится ранжирование запросов, то есть вполне возможно проанализировать запросы и по другому ресурсу, например \"tele-power-net.ru\" или \"benedict-rus.ru\". Программа использует Базу Данных типа sqlite3, которая сохраняется в одном файле с расширением \".db\". При необходимости можно изменить путь к этому файлу, указав его в гастройках. Здесь же можно задать путь к файлу для вывода результатов работы программы. Также, для логирования действий пользователя в настройках задаётся путь к текстовому файлу.<br />\
В секции \"Лимиты Яндекса\" можно задать предоставленные лимиты и при необходимости изменить их на другие при изменении политики Яндекса в отношении данного пользователя.\
<br /><i>Все настройки являются общими для программы с графическим интерфейсом и для консольной версии. Этот факт необходимо учитывать при внесении изменений.</i>\
<br /><font color=\"red\"><b>В данной версии программы сохранение любых изменений в настройках требует повторного запуска программы, поэтому нажатие на кнопку \"Сохранить\" помимо непосредственно сохранения настроек приводит к завершению программы. Возможно, в дальнейшем этот аспект работы прогрммы будет переосмыслен, но пока так...</b></font></p>\
<h2>О вкладке \"Лог выполнения задач\"</h2>\
<p>В лог заносятся данные по использованию программы \"ЯП\", причём как в графическом, так и в консольном режиме. Отметка о режиме работы программы также содержится в логе. Заметьте, что прежде всего данные логов заносятся в Базу Данных, а уже потом в лог-файл, путь к которому указан в настройках программы. Поэтому, в случае потери файла со списком логов, программа создаст новый файл сразу после отправки ближайшего запроса. Причём, в новый лог-файл будут включены все записи, которые сохранены в Базе Данных.</p>\
<h2>О консольной программе</h2>\
<p>Консольная программа <b>yapco.exe</b> принимает два именованных аргумента: исходный xls-файл со списком запросов (его полное имя указывается после флага -i) и результирующий xls-файл (его полное имя указывается после флага -o). Если эти аргументы не будут указаны, то по умолчанию за исходный и результирующий файл будет принят тот, который указан в настройках графической программы. Получив на вход список, содержащий количество запросов, превышающих допустимый лимит, программа перейдёт в режим ожидания до наступления следующей возможности отправлять xml-запросы Яндексу. Так как yapco.exe использует абсолютно те же настройки и базу данных, что и \"большой ЯП\", соответственно все данные, полученные с её помощью, будут доступны, например, для построения графиков, а также будут отражаться в логах работы программы \"ЯП\".</p>\
<h2>Инструментарий разработки</h2>\
<p>Программа написана на языке программирования Python версии 3.4.3<br />Графический интерфейс пользователя разработан при помощи библиотеки PyQt5<br />\
Для отправки HTTP-запросов использовалась библиотека requests<br />Хранение данных реализовано при помощи базы данных sqlite3<br />\
Исполняемые файлы для работы в среде Windows подготовлены утилитой cx_freeze<br />Разработка велась в августе 2015 года<br />Разработчик: Игорь Клекотнев.</p>\
"))

    def mode_selector(self, YaP, event):
        if self.radioButton_single_mode.isChecked() == True:
            self.btn_fileopen.setDisabled(True)
            self.btn_search.setDisabled(True)
            if self.limit_data[1] != 0:
                self.btn_input.setDisabled(False)
                self.lineEdit_single_query.setDisabled(False)
            else:
                self.btn_input.setDisabled(True)
                self.lineEdit_single_query.setDisabled(True)
            self.radioButton_file_mode.setDisabled(True)
            # self.table_results.setRowCount(0)
            self.mode_header = 's'
        else:
            if self.limit_data[1] != 0:
                self.btn_fileopen.setDisabled(False)
            else:
                self.btn_fileopen.setDisabled(True)
            self.btn_search.setDisabled(True)
            self.btn_input.setDisabled(True)
            self.lineEdit_single_query.setDisabled(True)
            self.mode_header = 'f'
        self.retranslateUi(YaP)

    def set_query(self, event):
        self.table_add = []
        # введенный текст -> в запрос
        if (self.lineEdit_single_query.text() != ''):
            line_query = self.lineEdit_single_query.text()
            # обнулили показатель позиции в поиске
            self.rank = 0
            # очистили поле ввода запроса
            self.lineEdit_single_query.setText('')
            self.table_list.append([line_query, False])
            self.table_indexes.append(len(self.table_list))
            self.table_add.append([line_query, False])
            self.btn_search.setDisabled(False)
            self.progressBar.setProperty("value", 0)
            # print('self.table_list')
            # print(self.table_list)
            # print('self.table_add')
            # print(self.table_add)
        else:
            self.label_info.setText("Был введён пустой запрос,\n\
повторите ввод.")

    def add_line(self, event):
        # print("self.search_count is ", end='')
        # print(self.search_count)
        self.table_row = len(self.table_list) + self.search_count - 1
        self.data_source = 'line'
        self.file_search_count = table_input(self.table_add,
                    self.table_row,
                    self.table_results,
                    self.data_source, self.search_count, self.file_search_count)

    def start_search(self, YaP, event):
        wait_timer = timerThread(self.alive)
        # print('start_search begins ...')
        false_count = 0
        queriesInWork = []
        for item in self.table_list:
            if item[1] is False:
                false_count += 1
                queriesInWork.append(item[0])
        # print('start_search: queriesInWork is ', end='')
        # print(queriesInWork)
        if (false_count > 1):
            for i, q in enumerate(queriesInWork):
                if (self.limit_data[1] > 0):
                    # print("i = ", end="")
                    # print(i)
                    # print(
                    #     'start search: if (self.limit_data[1] > 0): before search limit_data[1] is ', end='')
                    # print(self.limit_data[1])
                    self.limit_data.pop(1)
                    self.limit_data.insert(1, search(
                        self.search_work, self.table_list, q,
                        self.query_url, self.db_path, self.req_date,
                        self.day_limit,
                        self.day_overdraft, self.limit_police, self.hour,
                        self.res_list, self.rank, self.label_info,
                        self.table_results,
                        self.rate_url, self.lcdNumber_hour_limit,
                        self.lcdNumber_day_limit, self.progressBar, self.value,
                        self.log, self.btn_search, self.lineEdit_single_query,
                        self.btn_input, self.new_limit, self.circle, self.data_source, self.search_count)[0])
                    # print(
                    #     'start search: if (self.limit_data[1] > 0): after search limit_data[1] is ', end='')
                    # print(self.limit_data[1])
                else:
                    # print("i = ", end="")
                    # print(i)
                    wait_timer.start()
                    time.sleep(
                       (60 - int(datetime.now().strftime('%M'))) * 60.0)
                    # print('awake!')
                    wait_timer.stop()
                    self.hour = int(datetime.now().strftime('%H'))
                    # print("hour = ", end="")
                    # print(self.hour)
                    # print(
                    #     'start search: if (self.limit_data[1] > 0): before search limit_data[1] is ', end='')
                    # print(self.limit_data[1])
                    self.limit_data.pop(1)
                    self.limit_data.insert(1, search(
                        self.search_work, self.table_list, q,
                        self.query_url, self.db_path, self.req_date,
                        self.day_limit,
                        self.day_overdraft, self.limit_police, self.hour,
                        self.res_list, self.rank, self.label_info,
                        self.table_results,
                        self.rate_url, self.lcdNumber_hour_limit,
                        self.lcdNumber_day_limit, self.progressBar, self.value,
                        self.log, self.btn_search, self.lineEdit_single_query,
                        self.btn_input, self.new_limit, self.circle, self.data_source, self.search_count)[0])
                    # print(
                    #    'start search: if (self.limit_data[1] > 0): after search limit_data[1] is ', end='')
                    # print(self.limit_data[1])
            remove_empty_rows(0, self.table_results)
            self.btn_search.setDisabled(True)
            self.keywordsCombo.addItems(allKeywords(self.db_path))
            self.log.read(self.textEdit)
            self.table_list = []
            self.search_count += 1
        else:
            self.query = queriesInWork[0]
            # print('start search: if false_count (else): query is ', end='')
            self.search_count = search(
                self.search_work, self.table_list, self.query,
                self.query_url, self.db_path, self.req_date,
                self.day_limit,
                self.day_overdraft, self.limit_police, self.hour,
                self.res_list, self.rank, self.label_info, self.table_results,
                self.rate_url, self.lcdNumber_hour_limit,
                self.lcdNumber_day_limit, self.progressBar, self.value,
                self.log, self.btn_search, self.lineEdit_single_query,
                self.btn_input, self.new_limit, self.circle, self.data_source, self.search_count)[1]
        remove_empty_rows(0, self.table_results)
        self.btn_search.setDisabled(True)
        self.keywordsCombo.addItems(allKeywords(self.db_path))
        self.log.read(self.textEdit)
        self.btn_search.setDisabled(True)
        false_count = 0
        self.table_list = []
        return self.search_count

    def graphicsRequest(self, choice):
        graphicsBuilder(choice,
                        self.timesComboCurrentText,
                        self.keywordsComboCurrentText,
                        self.tableDivision, self.tab_2,
                        self.gridLayout_3, self.graphicsView,
                        self.letsDraw, self.db_path, self.fetchArr,
                        self.label_info)

    def setKeywordsComboCurrentText(self, text):
        self.keywordsComboCurrentText = text

    def setTimesComboCurrentText(self, text):
        self.timesComboCurrentText = text
