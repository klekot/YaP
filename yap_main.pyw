# -*- coding: utf-8 -*-

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.showOpenDialog import showOpenDialog
from modules.db_xls import db_xls
from modules.Ui_YaP import Ui_YaP
from initSettings import *
# from PyQt5 import QtWebKitWidgets
# from PyQt5.QtWidgets import QWidget


class yap(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.value = 0

    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_Escape:
                self.close()
                sys.exit()
            elif event.key() == QtCore.Qt.Key_Return:
                if (ui.lineEdit_single_query.text() != ''):
                    Ui_YaP.set_query(ui, event)
                    Ui_YaP.add_line(ui, event)
                elif ((ui.lineEdit_single_query.text() == '') and (len(ui.table_list) != 0)):
                    Ui_YaP.start_search(ui, YaP, event)

    def closeEvent(self, event):
        try:
            self.close()
            sys.exit()
        finally:
            pass

    def word_input(self, event):
        Ui_YaP.set_query(ui, event)
        Ui_YaP.add_line(ui, event)

    def mode_selection(self, event):
        Ui_YaP.mode_selector(ui, YaP, event)

    def open_file(self):
        ui.file_search_count = showOpenDialog(YaP, fname, ui.label_filepath, ui.label_info,
                       ui.btn_search, ui.table_list, ui.table_indexes,
                       ui.table_add, ui.table_row, ui.table_results,
                       ui.search_count, ui.file_search_count)

    def searching(self, event):
        # print('searching: call start_search...')
        Ui_YaP.start_search(ui, YaP, event)

    def save(self):
        db_xls(db_path, xls_path, req_date)

    def program_exit(self, event):
        if conn:
            conn.close()
        self.close()
        sys.exit()

    def saveSettings(self):
        conn = sqlite3.connect(db_path)
        # print('yap_main.py db connect')
        db = conn.cursor()
        # ###############################################################
        k1 = (ui.setSiteAddres_lineEdit.text(), 'rate_url')
        db.execute("update settings set value=? where variable=?", k1)
        k2 = (ui.setDbFilePath_lineEdit.text(), 'db_path')
        db.execute("update settings set value=? where variable=?", k2)
        k3 = (ui.setXlsFilePath_lineEdit.text(), 'xls_path')
        db.execute("update settings set value=? where variable=?", k3)
        k4 = (ui.setLogFilePath_lineEdit.text(), 'logs_path')
        db.execute("update settings set value=? where variable=?", k4)
        # ###############################################################
        h24 = (ui.lineEdit_allLimits.text(), 'all_day')
        db.execute("update time_limits set `limit`=? where times=?", h24)
        h00 = (int(ui.lineEdit_h00.text()), '0')
        db.execute("update time_limits set `limit`=? where times=?", h00)
        h01 = (int(ui.lineEdit_h01.text()), '1')
        db.execute("update time_limits set `limit`=? where times=?", h01)
        h02 = (int(ui.lineEdit_h02.text()), '2')
        db.execute("update time_limits set `limit`=? where times=?", h02)
        h03 = (int(ui.lineEdit_h03.text()), '3')
        db.execute("update time_limits set `limit`=? where times=?", h03)
        h04 = (int(ui.lineEdit_h04.text()), '4')
        db.execute("update time_limits set `limit`=? where times=?", h04)
        h05 = (int(ui.lineEdit_h05.text()), '5')
        db.execute("update time_limits set `limit`=? where times=?", h05)
        h06 = (int(ui.lineEdit_h06.text()), '6')
        db.execute("update time_limits set `limit`=? where times=?", h06)
        h07 = (int(ui.lineEdit_h07.text()), '7')
        db.execute("update time_limits set `limit`=? where times=?", h07)
        h08 = (int(ui.lineEdit_h08.text()), '8')
        db.execute("update time_limits set `limit`=? where times=?", h08)
        h09 = (int(ui.lineEdit_h09.text()), '9')
        db.execute("update time_limits set `limit`=? where times=?", h09)
        h10 = (int(ui.lineEdit_h10.text()), '10')
        db.execute("update time_limits set `limit`=? where times=?", h10)
        h11 = (int(ui.lineEdit_h11.text()), '11')
        db.execute("update time_limits set `limit`=? where times=?", h11)
        h12 = (int(ui.lineEdit_h12.text()), '12')
        db.execute("update time_limits set `limit`=? where times=?", h12)
        h13 = (int(ui.lineEdit_h13.text()), '13')
        db.execute("update time_limits set `limit`=? where times=?", h13)
        h14 = (int(ui.lineEdit_h14.text()), '14')
        db.execute("update time_limits set `limit`=? where times=?", h14)
        h15 = (int(ui.lineEdit_h15.text()), '15')
        db.execute("update time_limits set `limit`=? where times=?", h15)
        h16 = (int(ui.lineEdit_h16.text()), '16')
        db.execute("update time_limits set `limit`=? where times=?", h16)
        h17 = (int(ui.lineEdit_h17.text()), '17')
        db.execute("update time_limits set `limit`=? where times=?", h17)
        h18 = (int(ui.lineEdit_h18.text()), '18')
        db.execute("update time_limits set `limit`=? where times=?", h18)
        h19 = (int(ui.lineEdit_h19.text()), '19')
        db.execute("update time_limits set `limit`=? where times=?", h19)
        h20 = (int(ui.lineEdit_h20.text()), '20')
        db.execute("update time_limits set `limit`=? where times=?", h20)
        h21 = (int(ui.lineEdit_h21.text()), '21')
        db.execute("update time_limits set `limit`=? where times=?", h21)
        h22 = (int(ui.lineEdit_h22.text()), '22')
        db.execute("update time_limits set `limit`=? where times=?", h22)
        h23 = (int(ui.lineEdit_h23.text()), '23')
        db.execute("update time_limits set `limit`=? where times=?", h23)
        conn.commit()
        db.close()
        conn.close()
        self.close()
        sys.exit()
        # print('yap_main.py db close')

    def infoForGraphics(self):
        ui.label_info.setText("Для вывода графика\nсначала явно выбрать\nключевую фразу,\nа после явно выбрать\nдиапазон дат.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    YaP = yap()
    ui = Ui_YaP(table_list, table_add, limit_data, day_limit,
                table_indexes, rank, search_work, query_url,
                req_date, day_overdraft, limit_police, hour,
                res_list, rate_url, query, db_path, xls_path,
                logs_path, ref_path)
    ui.setupUi(YaP)
    '''
    webView = QtWebKitWidgets.QWebView(ui.tab_5)
    webView.setGeometry(QtCore.QRect(10, 10, 631, 591))
    webView.setUrl(QtCore.QUrl(ui.ref_path))
    webView.setObjectName("webView")
    '''
    ui.btn_input.clicked.connect(YaP.word_input)
    # ui.btn_exit.clicked.connect(YaP.program_exit)
    ui.btn_search.clicked.connect(YaP.searching)
    ui.btn_fileopen.clicked.connect(YaP.open_file)
    ui.btn_save.clicked.connect(YaP.save)
    ui.radioButton_single_mode.toggled.connect(YaP.mode_selection)
    ui.radioButton_file_mode.toggled.connect(YaP.mode_selection)
    ui.saveSettings_pushButton.clicked.connect(YaP.saveSettings)
    ui.label_info.setText("Добро пожаловать в \"ЙаП\"!")
    YaP.show()
    sys.exit(app.exec_())
