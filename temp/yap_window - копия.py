# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YaP(object):
    def setupUi(self, YaP):
        YaP.setObjectName("YaP")
        YaP.setEnabled(True)
        YaP.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(YaP.sizePolicy().hasHeightForWidth())
        YaP.setSizePolicy(sizePolicy)
        YaP.setMinimumSize(QtCore.QSize(800, 600))
        YaP.setSizeIncrement(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(YaP)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.groupBox_mode = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_mode.sizePolicy().hasHeightForWidth())
        self.groupBox_mode.setSizePolicy(sizePolicy)
        self.groupBox_mode.setMinimumSize(QtCore.QSize(220, 90))
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.radioButton_single_mode = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_single_mode.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.radioButton_single_mode.setObjectName("radioButton_single_mode")
        self.radioButton_file_mode = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_file_mode.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.radioButton_file_mode.setObjectName("radioButton_file_mode")
        self.btn_fileopen = QtWidgets.QPushButton(self.groupBox_mode)
        self.btn_fileopen.setGeometry(QtCore.QRect(120, 50, 91, 23))
        self.btn_fileopen.setObjectName("btn_fileopen")
        self.gridLayout.addWidget(self.groupBox_mode, 0, 1, 1, 1)
        self.groupBox_limits = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_limits.sizePolicy().hasHeightForWidth())
        self.groupBox_limits.setSizePolicy(sizePolicy)
        self.groupBox_limits.setMinimumSize(QtCore.QSize(220, 360))
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
        self.gridLayout.addWidget(self.groupBox_limits, 1, 1, 1, 1)
        self.groupBox_main = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_main.sizePolicy().hasHeightForWidth())
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_results.sizePolicy().hasHeightForWidth())
        self.table_results.setSizePolicy(sizePolicy)
        self.table_results.setMinimumSize(QtCore.QSize(500, 475))
        self.table_results.setObjectName("table_results")
        self.table_results.setColumnCount(0)
        self.table_results.setRowCount(0)
        self.gridLayout_main.addWidget(self.table_results, 1, 0, 1, 2)
        self.btn_search = QtWidgets.QPushButton(self.groupBox_main)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_main.addWidget(self.btn_search, 0, 1, 1, 1)
        self.lineEdit_single_query = QtWidgets.QLineEdit(self.groupBox_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_single_query.sizePolicy().hasHeightForWidth())
        self.lineEdit_single_query.setSizePolicy(sizePolicy)
        self.lineEdit_single_query.setMinimumSize(QtCore.QSize(390, 0))
        self.lineEdit_single_query.setObjectName("lineEdit_single_query")
        self.gridLayout_main.addWidget(self.lineEdit_single_query, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_main, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_main, 0, 0, 5, 1)
        self.groupBox_info = QtWidgets.QGroupBox(YaP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_info.sizePolicy().hasHeightForWidth())
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
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_info)
        self.progressBar.setGeometry(QtCore.QRect(10, 100, 200, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.groupBox_info, 3, 1, 2, 1)

        self.retranslateUi(YaP)
        QtCore.QMetaObject.connectSlotsByName(YaP)

    def retranslateUi(self, YaP):
        _translate = QtCore.QCoreApplication.translate
        YaP.setWindowTitle(_translate("YaP", "Form"))
        self.groupBox_mode.setTitle(_translate("YaP", "Режим поиска"))
        self.radioButton_single_mode.setText(_translate("YaP", "Одиночный поиск"))
        self.radioButton_file_mode.setText(_translate("YaP", "Пакетный поиск"))
        self.btn_fileopen.setText(_translate("YaP", "Выбрать файл"))
        self.groupBox_limits.setTitle(_translate("YaP", "Лимиты Яндекса"))
        self.label_day_limit.setText(_translate("YaP", "Дневной лимит (минус овердрафт)"))
        self.label_hour_limit.setText(_translate("YaP", "Лимит запросов в текущем часу"))
        self.groupBox_main.setTitle(_translate("YaP", "Будет показан режим"))
        self.btn_save.setText(_translate("YaP", "Сохранить"))
        self.label_filepath.setText(_translate("YaP", "Путь к файлу статистики:   c:WindowsStatfile.xls"))
        self.btn_search.setText(_translate("YaP", "Поиск"))
        self.groupBox_info.setTitle(_translate("YaP", "Информация"))
        self.label_info.setText(_translate("YaP", "ВНИМАНИЕ!!!\n"
"Превышено допустимое\n"
"число запросов.\n"
"Поиск продолжится\n"
"через ... минут."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YaP = QtWidgets.QWidget()
    ui = Ui_YaP()
    ui.setupUi(YaP)
    YaP.show()
    sys.exit(app.exec_())

