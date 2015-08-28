# -*- coding: utf-8 -*-
from datetime import datetime
import sqlite3
from modules.Graphics import Graphics


now = datetime.now()
weekday = datetime.today().weekday()


def graphicsBuilder(choice, timesComboCurrentText,
                    keywordsComboCurrentText, tableDivision,
                    tab_2, gridLayout_3, graphicsView,
                    letsDraw, db_path, fetchArr, label_info):
    def db_request():
        conn = sqlite3.connect(db_path)
        # print('graphicsBuilder.py db connect')
        db = conn.cursor()
        k = (keywordsComboCurrentText.encode('utf-8').decode('cp1251'),)
        db.execute("select * from requests \
                where keyword=?", k)
        fetchArr = []
        for fetchLine in db.fetchall():
            if [fetchLine[1], fetchLine[2]] not in fetchArr:
                fetchArr.append([fetchLine[1], fetchLine[2]])
        db.close()
        conn.close()
        # print('graphicsBuilder.py db close')
        return fetchArr

    def monthDaysQuantity(monthNumber, monthYear):
        month31 = [1, 3, 5, 7, 8, 10, 12]
        month30 = [4, 6, 9, 11]
        if monthNumber in month31:
            return 31
        elif monthNumber in month30:
            return 30
        elif monthNumber == 2:
            if (monthYear % 4 == 0) and\
               ((monthYear % 100 != 0) or
                ((monthYear % 100 == 0 and
                  monthYear % 400 == 0))):
                return 29
            else:
                return 28

    letsDraw = True
    if choice == 'Неделя':
        tableDivision = 7 - 1
        graphicsView = Graphics(tab_2, tableDivision,
                                letsDraw, db_path, db_request())
        gridLayout_3.addWidget(graphicsView, 1, 0, 1, 6)

    elif choice == 'Месяц':
        monthNumber = int(datetime.now().strftime('%m'))
        monthYear = int(datetime.now().strftime('%Y'))
        graphicsView = Graphics(tab_2,
                                (monthDaysQuantity(
                                    monthNumber, monthYear) - 1),
                                letsDraw, db_path, db_request())
        gridLayout_3.addWidget(graphicsView, 1, 0, 1, 6)
    elif choice == 'Квартал':
        monthNumber = int(datetime.now().strftime('%m'))
        monthYear = int(datetime.now().strftime('%Y'))
        allMonthesData = []
        fetchArrQuartal = []
        for i in range(3):
            curMonthData = []
            for item in db_request():
                if int(item[1][5:7]) == (
                        int(datetime.now().strftime('%m')) - i):
                    curMonthData.append(item[0])
            allMonthesData.append(curMonthData)
        for m, item in enumerate(allMonthesData):
            curMonthDataSumma = 0
            for j in range(len(item)):
                curMonthDataSumma += item[j]
            if len(item) > 0:
                fetchArrQuartal.append(
                    [(curMonthDataSumma / len(item)),
                     str(int(datetime.now().strftime('%m')) - m)])
            else:
                fetchArrQuartal.append(
                    [0, str(int(datetime.now().strftime('%m')) - m)])
        graphicsView = Graphics(tab_2, (3 - 1),
                                letsDraw, db_path, fetchArrQuartal)
        gridLayout_3.addWidget(graphicsView, 1, 0, 1, 6)
        label_info.setText(
            "При диапазоне дат,\nбольших чем один месяц,\nиспользуются усреднёные\nзначения.")
    elif choice == 'Полугодие':
        monthNumber = int(datetime.now().strftime('%m'))
        monthYear = int(datetime.now().strftime('%Y'))
        allMonthesData = []
        fetchArrQuartal = []
        for i in range(6):
            curMonthData = []
            for item in db_request():
                if int(item[1][5:7]) == (
                        int(datetime.now().strftime('%m')) - i):
                    curMonthData.append(item[0])
            allMonthesData.append(curMonthData)
        for m, item in enumerate(allMonthesData):
            curMonthDataSumma = 0
            for j in range(len(item)):
                curMonthDataSumma += item[j]
            if len(item) > 0:
                fetchArrQuartal.append(
                    [(curMonthDataSumma / len(item)),
                     str(int(datetime.now().strftime('%m')) - m)])
            else:
                fetchArrQuartal.append(
                    [0, str(int(datetime.now().strftime('%m')) - m)])
        graphicsView = Graphics(tab_2, (6 - 1),
                                letsDraw, db_path, fetchArrQuartal)
        gridLayout_3.addWidget(graphicsView, 1, 0, 1, 6)
        label_info.setText(
            "При диапазоне дат,\nбольших чем один месяц,\nиспользуются усреднёные значения.")
    elif choice == 'Год':
        monthNumber = int(datetime.now().strftime('%m'))
        monthYear = int(datetime.now().strftime('%Y'))
        allMonthesData = []
        fetchArrQuartal = []
        for i in range(12):
            curMonthData = []
            for item in db_request():
                if int(item[1][5:7]) == (
                        int(datetime.now().strftime('%m')) - i):
                    curMonthData.append(item[0])
            allMonthesData.append(curMonthData)
        for m, item in enumerate(allMonthesData):
            curMonthDataSumma = 0
            for j in range(len(item)):
                curMonthDataSumma += item[j]
            if len(item) > 0:
                fetchArrQuartal.append(
                    [(curMonthDataSumma / len(item)),
                     str(int(datetime.now().strftime('%m')) - m)])
            else:
                fetchArrQuartal.append(
                    [0, str(int(datetime.now().strftime('%m')) - m)])
        graphicsView = Graphics(tab_2, (12 - 1),
                                letsDraw, db_path, fetchArrQuartal)
        gridLayout_3.addWidget(graphicsView, 1, 0, 1, 6)
        label_info.setText(
            "При диапазоне дат,\nбольших чем один месяц,\nиспользуются усреднёные значения.")
    elif choice == 'Всё время':
        tableDivision = 1
        graphicsView = Graphics(tab_2, tableDivision,
                                letsDraw, db_path, db_request())
        gridLayout_3.addWidget(graphicsView, 1, 0, 1, 6)
    else:
        pass
        '''
        k = (choice.encode('utf-8').decode('cp1251'),)
        db.execute("select * from requests \
                where keyword=?", k)
        for position in db.fetchall():
            # print('place ' + str(position[1]))
            # print('date ' + str(position[2]))
        '''
