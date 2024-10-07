# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passmain.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ico_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icon/ico3.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QSize(48, 48))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(750, 550, 41, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icon/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(32, 32))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(630, 10, 141, 141))
        self.label.setPixmap(QPixmap(u":/icon/ico2.png"))
        self.label.setScaledContents(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(720, 230, 75, 31))
        self.pushButton_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(600, 230, 113, 31))
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setCursorPosition(0)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 20, 571, 521))
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(700, 290, 91, 41))
        icon2 = QIcon()
        icon2.addFile(u":/icon/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(700, 340, 91, 41))
        icon3 = QIcon()
        icon3.addFile(u":/icon/documents.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(710, 400, 75, 31))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(710, 450, 75, 31))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(600, 290, 91, 41))
        icon4 = QIcon()
        icon4.addFile(u":/icon/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QSize(30, 30))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(600, 340, 91, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icon/Name.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QSize(30, 30))
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(610, 400, 75, 31))
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(610, 450, 75, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(610, 160, 171, 51))
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(614, 500, 171, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PassM", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fd\u5e33\u865f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fd\u5167\u5bb9", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u96b1\u85cf", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fd\u5bc6\u78bc", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fd\u540d\u7a31", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#5a5a5a;\">\u8acb\u8f38\u5165\u5bc6\u9470</span></p></body></html>", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u5132\u5b58", None))
    # retranslateUi

