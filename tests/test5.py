#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QGridLayout, QSizePolicy, QPushButton
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QSize


class Ui_YaP(object):
    def setupUi(self, YaP):
        YaP.setGeometry(300, 300, 270, 270)
        YaP.setWindowTitle('YaP')
        YaP.show()
        self.gridLayout_3 = QGridLayout(YaP)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView = QWidget(YaP)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setGeometry(0, 0, 270, 270)
        self.graphicsView.setStyleSheet("QWidget { background-color: blue}")
        self.gridLayout_3.addWidget(self.graphicsView, 1, 0, 1, 6)

        self.btn_save = QPushButton(YaP)
        sizePolicy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMaximumSize(QSize(16777215, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_3.addWidget(self.btn_save, 2, 3, 1, 1)






class Graphics(QWidget):

    def __init__(self):
        super().__init__()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(0, 270, 10, 250)

        qp.setPen(pen)
        qp.drawLine(10, 250, 20, 210)

        qp.setPen(pen)
        qp.drawLine(20, 210, 30, 240)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    graph = Graphics()
    graph.show()
    sys.exit(app.exec_())
