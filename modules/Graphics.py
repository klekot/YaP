#!/usr/bin/python3
# -*- coding: utf-8 -*-

# дельта в 2 дня
# delta = datetime.timedelta(days=2)

# Узнаем какое число будет через 2 дня
# now_date = now_date + delta

# или какое число было 2 дня назад
# now_date = now_date - delta

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta


class Graphics(QWidget):

    def __init__(self, parent, vLineQuantity,
                 letsDraw, db_path, fetchArr):
        super().__init__()
        self.vLineQuantity = vLineQuantity
        self.hLine = 30
        self.vLine = 610 / self.vLineQuantity
        self.letsDraw = letsDraw
        self.fetchArr = fetchArr
        self.dots = []
        # меньше на единицу специально :)
        self.scales = [[6],
                       [27, 28, 29, 30],
                       [2, 5, 11]]

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.cleanAll(qp)
        if self.letsDraw:
            self.drawDots(qp)
            self.drawLines(qp)
            self.drawText(qp)
        else:
            pass
        self.drawRectangles(qp)
        self.drawGrid(qp)
        self.letsDraw = False
        qp.end()

    def cleanAll(self, qp):
        qp.eraseRect(20, 20, 610, 510)

    def drawGrid(self, qp):
        dotLine = QPen(Qt.black, 1, Qt.DotLine)
        qp.setPen(dotLine)
        while (self.hLine < 510):
            qp.drawLine(20, self.hLine, 630, self.hLine)
            self.hLine += 50
        for i in range(self.vLineQuantity):
            qp.drawLine(self.vLine * i + 20, 20, self.vLine * i + 20, 530)

    def drawText(self, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Plain', 8))
        place = 10
        space = 50
        delta = 34
        if self.vLineQuantity == 1:
            pass
        else:
            qp.drawText(0, 34, '1')
            for i in range(1, 10):
                qp.drawText(0, (space * i + delta), str(place * i))
            if self.vLineQuantity in self.scales[0]:  # неделя
                for i in range(self.vLineQuantity):
                    qp.drawText(
                        (608 - (self.vLine) * i),
                        550,
                        str((datetime.now() -
                             timedelta(days=i)).strftime('%d.%m')))
                early_date = datetime.now() -\
                    timedelta(days=self.vLineQuantity)
                qp.drawText(0, 550, str(early_date.strftime('%d.%m')))
            if self.vLineQuantity in self.scales[1]:  # месяц
                for i in range(self.vLineQuantity):
                    qp.drawText(
                        (617 - ((self.vLine * 2)) * i),
                        550,
                        str((datetime.now() -
                             timedelta(days=i * 2)).strftime('%d.%m')))
            if self.vLineQuantity in self.scales[2]:  # квартал
                monthes = ['январь', 'февраль', 'март',
                           'апрель', 'май', 'июнь', 'июль',
                           'август', 'сентябрь', 'октябрь',
                           'ноябрь', 'декабрь']
                for i in range(self.vLineQuantity):
                    monthIndex = int(datetime.now().strftime('%m')) - i
                    if i > 0:
                        qp.drawText(
                            (620 - (
                                (self.vLine)) * i), 550, monthes[monthIndex-1])
                    else:
                        qp.drawText(
                            (600 - (
                                (self.vLine)) * i), 550, monthes[monthIndex-1])
                qp.drawText(
                    0, 550, monthes[int(
                        datetime.now().strftime('%m'))-self.vLineQuantity-1])

    def drawDots(self, qp):
        for i in range(self.vLineQuantity + 1):
            for j in range(len(self.fetchArr)):
                if (self.fetchArr[j][1] == (datetime.now() -
                                            timedelta(days=i)).strftime(
                    '%Y-%m-%d')) or\
                   (self.fetchArr[j][1] == str(
                        int(datetime.now().strftime('%m')) - i)):
                    x = 631 - ((self.vLine) * i)
                    if (self.fetchArr[j][0] == 0):
                        y = 531
                    else:
                        y = (self.fetchArr[j][0] * 5) + 30
                    self.dots.append([x, y])
                    pen = QPen(Qt.black, 1, Qt.SolidLine)
                    qp.setPen(pen)
                    qp.setBrush(QColor(0, 0, 0))
                    qp.drawRect(x - 4, y - 2, 5, 5)
                    if x > 625:
                        if int((y - 30) / 5) < 100:
                            qp.drawText(x - 20, y - 5, str(int((y - 30) / 5)))
                        else:
                            qp.drawText(x - 20, y - 5, 'NULL')
                    else:
                        if int((y - 30) / 5) < 100:
                            qp.drawText(x + 5, y - 5, str(int((y - 30) / 5)))
                        else:
                            qp.drawText(x + 5, y - 5, 'NULL')

    def drawLines(self, qp):
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        qp.setPen(pen)
        for i in range(1, len(self.dots)):
            qp.drawLine(self.dots[i - 1][0],
                        self.dots[i - 1][1],
                        self.dots[i][0],
                        self.dots[i][1])

    def drawRectangles(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QColor(0, 200, 0, 50))
        qp.drawRect(20, 20, 610, 510)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    graph = Graphics()
    graph.show()
    sys.exit(app.exec_())
