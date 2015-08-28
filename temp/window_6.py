# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_5.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YaP(object):
    def setupUi(self, YaP):
        YaP.setObjectName("YaP")
        YaP.setEnabled(True)
        YaP.resize(908, 685)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(YaP.sizePolicy().hasHeightForWidth())
        YaP.setSizePolicy(sizePolicy)
        YaP.setMinimumSize(QtCore.QSize(800, 600))
        YaP.setSizeIncrement(QtCore.QSize(0, 0))
        self.progressBar = QtWidgets.QProgressBar(YaP)
        self.progressBar.setGeometry(QtCore.QRect(673, 626, 87, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_limits = QtWidgets.QGroupBox(YaP)
        self.groupBox_limits.setGeometry(QtCore.QRect(673, 91, 220, 413))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_limits.sizePolicy().hasHeightForWidth())
        self.groupBox_limits.setSizePolicy(sizePolicy)
        self.groupBox_limits.setMinimumSize(QtCore.QSize(220, 340))
        self.groupBox_limits.setObjectName("groupBox_limits")
        self.splitter_gb_limits = QtWidgets.QSplitter(self.groupBox_limits)
        self.splitter_gb_limits.setGeometry(QtCore.QRect(20, 20, 177, 331))
        self.splitter_gb_limits.setOrientation(QtCore.Qt.Vertical)
        self.splitter_gb_limits.setObjectName("splitter_gb_limits")
        self.label_day_limit = QtWidgets.QLabel(self.splitter_gb_limits)
        self.label_day_limit.setObjectName("label_day_limit")
        self.lcdNumber_day_limit = QtWidgets.QLCDNumber(self.splitter_gb_limits)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_day_limit.setFont(font)
        self.lcdNumber_day_limit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_day_limit.setDigitCount(3)
        self.lcdNumber_day_limit.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_day_limit.setProperty("intValue", 460)
        self.lcdNumber_day_limit.setObjectName("lcdNumber_day_limit")
        self.label_hour_limit = QtWidgets.QLabel(self.splitter_gb_limits)
        self.label_hour_limit.setObjectName("label_hour_limit")
        self.lcdNumber_hour_limit = QtWidgets.QLCDNumber(self.splitter_gb_limits)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_hour_limit.setFont(font)
        self.lcdNumber_hour_limit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_hour_limit.setDigitCount(3)
        self.lcdNumber_hour_limit.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_hour_limit.setProperty("intValue", 48)
        self.lcdNumber_hour_limit.setObjectName("lcdNumber_hour_limit")
        self.groupBox_info = QtWidgets.QGroupBox(YaP)
        self.groupBox_info.setGeometry(QtCore.QRect(673, 510, 220, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_info.sizePolicy().hasHeightForWidth())
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
        self.groupBox_mode = QtWidgets.QGroupBox(YaP)
        self.groupBox_mode.setGeometry(QtCore.QRect(673, 9, 220, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_mode.sizePolicy().hasHeightForWidth())
        self.groupBox_mode.setSizePolicy(sizePolicy)
        self.groupBox_mode.setMinimumSize(QtCore.QSize(220, 70))
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.radioButton_single_mode = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_single_mode.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.radioButton_single_mode.setObjectName("radioButton_single_mode")
        self.radioButton_file_mode = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_file_mode.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.radioButton_file_mode.setObjectName("radioButton_file_mode")
        self.tabWidget = QtWidgets.QTabWidget(YaP)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 658, 638))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_main = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.groupBox_main.sizePolicy().hasHeightForWidth())
        self.groupBox_main.setSizePolicy(sizePolicy)
        self.groupBox_main.setMinimumSize(QtCore.QSize(530, 600))
        self.groupBox_main.setSizeIncrement(QtCore.QSize(600, 0))
        self.groupBox_main.setFlat(False)
        self.groupBox_main.setCheckable(False)
        self.groupBox_main.setObjectName("groupBox_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_fileopen = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fileopen.sizePolicy().hasHeightForWidth())
        self.btn_fileopen.setSizePolicy(sizePolicy)
        self.btn_fileopen.setObjectName("btn_fileopen")
        self.gridLayout_2.addWidget(self.btn_fileopen, 0, 0, 1, 1)
        self.btn_search = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_2.addWidget(self.btn_search, 0, 4, 1, 1)
        self.table_results = QtWidgets.QTableWidget(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.table_results.sizePolicy().hasHeightForWidth())
        self.table_results.setSizePolicy(sizePolicy)
        self.table_results.setMinimumSize(QtCore.QSize(500, 496))
        self.table_results.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_results.setMidLineWidth(1)
        self.table_results.setAlternatingRowColors(True)
        self.table_results.setRowCount(1)
        self.table_results.setColumnCount(3)
        self.table_results.setObjectName("table_results")
        self.table_results.horizontalHeader().setCascadingSectionResizes(True)
        self.table_results.horizontalHeader().setDefaultSectionSize(200)
        self.table_results.horizontalHeader().setMinimumSectionSize(31)
        self.table_results.horizontalHeader().setSortIndicatorShown(True)
        self.table_results.horizontalHeader().setStretchLastSection(True)
        self.table_results.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.table_results, 1, 0, 1, 5)
        self.label_filepath = QtWidgets.QLabel(self.groupBox_main)
        self.label_filepath.setMinimumSize(QtCore.QSize(0, 42))
        self.label_filepath.setObjectName("label_filepath")
        self.gridLayout_2.addWidget(self.label_filepath, 2, 0, 1, 2)
        self.btn_search_2 = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search_2.sizePolicy().hasHeightForWidth())
        self.btn_search_2.setSizePolicy(sizePolicy)
        self.btn_search_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_search_2.setObjectName("btn_search_2")
        self.gridLayout_2.addWidget(self.btn_search_2, 2, 2, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_2.addWidget(self.btn_save, 2, 4, 1, 1)
        self.lineEdit_single_query = QtWidgets.QLineEdit(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_single_query.sizePolicy().hasHeightForWidth())
        self.lineEdit_single_query.setSizePolicy(sizePolicy)
        self.lineEdit_single_query.setMinimumSize(QtCore.QSize(37, 0))
        self.lineEdit_single_query.setObjectName("lineEdit_single_query")
        self.gridLayout_2.addWidget(self.lineEdit_single_query, 0, 1, 1, 2)
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
        self.graphWidget = QtWidgets.QWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setMinimumSize(QtCore.QSize(635, 0))
        self.graphWidget.setAutoFillBackground(False)
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_3.addWidget(self.graphWidget, 1, 0, 1, 5)
        self.timesCombo = QtWidgets.QComboBox(self.tab_2)
        self.timesCombo.setObjectName("timesCombo")
        self.gridLayout_3.addWidget(self.timesCombo, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(90, 0))
        self.label_3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_38.setGeometry(QtCore.QRect(10, 190, 321, 20))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_35.setGeometry(QtCore.QRect(10, 40, 321, 20))
        self.lineEdit_35.setObjectName("lineEdit_35")
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
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_37.setGeometry(QtCore.QRect(10, 140, 321, 20))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_36.setGeometry(QtCore.QRect(10, 90, 321, 20))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 331, 161))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_22.setGeometry(QtCore.QRect(50, 70, 31, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_32.setGeometry(QtCore.QRect(250, 120, 31, 20))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_19.setGeometry(QtCore.QRect(290, 70, 31, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(140, 40, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(300, 90, 16, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_25.setGeometry(QtCore.QRect(250, 70, 31, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 20, 31, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_20.setGeometry(QtCore.QRect(170, 70, 31, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 20, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(60, 90, 16, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_28.setGeometry(QtCore.QRect(10, 120, 31, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 20, 31, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(260, 40, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(100, 140, 16, 16))
        self.label_22.setObjectName("label_22")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_30.setGeometry(QtCore.QRect(90, 120, 31, 20))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_29.setGeometry(QtCore.QRect(170, 120, 31, 20))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_34.setGeometry(QtCore.QRect(50, 120, 31, 20))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_31.setGeometry(QtCore.QRect(210, 120, 31, 20))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_27.setGeometry(QtCore.QRect(290, 120, 31, 20))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_21.setGeometry(QtCore.QRect(130, 70, 31, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(220, 140, 16, 16))
        self.label_25.setObjectName("label_25")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(20, 90, 16, 16))
        self.label_15.setObjectName("label_15")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(260, 140, 16, 16))
        self.label_27.setObjectName("label_27")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_24.setGeometry(QtCore.QRect(10, 70, 31, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(180, 40, 16, 16))
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 40, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(100, 90, 16, 16))
        self.label_18.setObjectName("label_18")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 20, 31, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_26.setGeometry(QtCore.QRect(210, 70, 31, 20))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(140, 90, 16, 16))
        self.label_19.setObjectName("label_19")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(100, 40, 16, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_23.setGeometry(QtCore.QRect(90, 70, 31, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(180, 90, 16, 16))
        self.label_16.setObjectName("label_16")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(220, 40, 16, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(250, 20, 31, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(260, 90, 16, 16))
        self.label_14.setObjectName("label_14")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(60, 140, 16, 16))
        self.label_24.setObjectName("label_24")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(300, 140, 16, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_33.setGeometry(QtCore.QRect(130, 120, 31, 20))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(210, 20, 31, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(300, 40, 16, 16))
        self.label_11.setObjectName("label_11")
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(180, 140, 16, 16))
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(140, 140, 16, 16))
        self.label_28.setObjectName("label_28")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(20, 140, 16, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 20, 31, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(220, 90, 16, 16))
        self.label_17.setObjectName("label_17")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(200, 20, 31, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 311, 41))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
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
        self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.webView = QtWebKitWidgets.QWebView(self.tab_5)
        self.webView.setGeometry(QtCore.QRect(10, 10, 631, 591))
        self.webView.setUrl(QtCore.QUrl("file:///C:/Users/gnato/Desktop/Igor/progs/python_progs/YaP/reference.html"))
        self.webView.setObjectName("webView")
        self.tabWidget.addTab(self.tab_5, "")
        self.pushButton = QtWidgets.QPushButton(YaP)
        self.pushButton.setGeometry(QtCore.QRect(9, 653, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(YaP)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(YaP)

    def retranslateUi(self, YaP):
        _translate = QtCore.QCoreApplication.translate
        YaP.setWindowTitle(_translate("YaP", "Form"))
        self.groupBox_limits.setTitle(_translate("YaP", "Лимиты Яндекса"))
        self.label_day_limit.setText(_translate("YaP", "Дневной лимит (минус овердрафт)"))
        self.label_hour_limit.setText(_translate("YaP", "Лимит запросов в текущем часу"))
        self.groupBox_info.setTitle(_translate("YaP", "Информация"))
        self.label_info.setText(_translate("YaP", "ВНИМАНИЕ!!!\n"
"Превышено допустимое\n"
"число запросов.\n"
"Поиск продолжится\n"
"через ... минут."))
        self.groupBox_mode.setTitle(_translate("YaP", "Режим поиска"))
        self.radioButton_single_mode.setText(_translate("YaP", "Одиночный поиск"))
        self.radioButton_file_mode.setText(_translate("YaP", "Пакетный поиск"))
        self.groupBox_main.setTitle(_translate("YaP", "Будет показан режим"))
        self.btn_fileopen.setText(_translate("YaP", "Выбрать файл"))
        self.btn_search.setText(_translate("YaP", "Ввод"))
        self.table_results.setSortingEnabled(True)
        self.label_filepath.setText(_translate("YaP", "Путь к файлу статистики:   c:WindowsStatfile.xls"))
        self.btn_search_2.setText(_translate("YaP", "Поиск"))
        self.btn_save.setText(_translate("YaP", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("YaP", "Определение рейтингов"))
        self.label.setText(_translate("YaP", "Ключевая фраза:"))
        self.label_3.setText(_translate("YaP", "Выбрать период:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("YaP", "Графики"))
        self.groupBox_2.setTitle(_translate("YaP", "Исходные данные программы"))
        self.label_30.setText(_translate("YaP", "Путь к файлу с базой данных:"))
        self.label_32.setText(_translate("YaP", "Путь к лог-файлу:"))
        self.label_29.setText(_translate("YaP", "Сайт, для которого рассчитывается рейтинг:"))
        self.label_31.setText(_translate("YaP", "Путь к файлу со списком запросов(.xls):"))
        self.groupBox_3.setTitle(_translate("YaP", "Лимиты Яндекса"))
        self.groupBox.setTitle(_translate("YaP", "Разрешённое число запросов в зависимости от времени суток"))
        self.label_8.setText(_translate("YaP", "03"))
        self.label_13.setText(_translate("YaP", "15"))
        self.label_20.setText(_translate("YaP", "09"))
        self.label_9.setText(_translate("YaP", "06"))
        self.label_22.setText(_translate("YaP", "18"))
        self.label_25.setText(_translate("YaP", "21"))
        self.label_15.setText(_translate("YaP", "08"))
        self.label_27.setText(_translate("YaP", "22"))
        self.label_10.setText(_translate("YaP", "04"))
        self.label_5.setText(_translate("YaP", "00"))
        self.label_6.setText(_translate("YaP", "01"))
        self.label_18.setText(_translate("YaP", "10"))
        self.label_19.setText(_translate("YaP", "11"))
        self.label_7.setText(_translate("YaP", "02"))
        self.label_16.setText(_translate("YaP", "12"))
        self.label_12.setText(_translate("YaP", "05"))
        self.label_14.setText(_translate("YaP", "14"))
        self.label_24.setText(_translate("YaP", "17"))
        self.label_21.setText(_translate("YaP", "23"))
        self.label_11.setText(_translate("YaP", "07"))
        self.label_26.setText(_translate("YaP", "20"))
        self.label_28.setText(_translate("YaP", "19"))
        self.label_23.setText(_translate("YaP", "16"))
        self.label_17.setText(_translate("YaP", "13"))
        self.label_2.setText(_translate("YaP", "Общий лимит:"))
        self.label_4.setText(_translate("YaP", "TextLabel"))
        self.pushButton_2.setText(_translate("YaP", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("YaP", "Настройки программы"))
        self.pushButton_8.setText(_translate("YaP", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("YaP", "Лог выполнения задач"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("YaP", "Страница"))
        self.pushButton.setText(_translate("YaP", "PushButton"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YaP = QtWidgets.QWidget()
    ui = Ui_YaP()
    ui.setupUi(YaP)
    YaP.show()
    sys.exit(app.exec_())

