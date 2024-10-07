# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:13:13 2023

@author: VitoJan
"""


import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QAbstractTableModel, Qt
from ui_passmain import Ui_MainWindow
from time import time
import pandas as pd

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Infomation)
        self.ui.pushButton_2.clicked.connect(self.Decode)
        self.ui.pushButton_3.clicked.connect(self.CP_acco)
        self.ui.pushButton_4.clicked.connect(self.CP_info)
        self.ui.pushButton_5.clicked.connect(self.Edit)
        self.ui.pushButton_6.clicked.connect(self.Delete)
        self.ui.pushButton_8.clicked.connect(self.CP_pass)
        self.ui.pushButton_9.clicked.connect(self.CP_name)
        self.ui.pushButton_10.clicked.connect(self.Show_Hide)
        self.ui.pushButton_11.clicked.connect(self.Add)


    def Decode(self):
        
        print(time(), "Decode", self.ui.lineEdit.text())

    def CP_pass(self):

        print(self.ui.tableView)

        data = pd.DataFrame([
          [1, 9, 2, 0],
          [1, 0, -1, 0],
          [3, 5, 2, 0],
          [3, 3, 2, 0],
          [5, 8, 9, 0],
        ],  columns = ["名稱", "帳號", "密碼", "備註內容"])

        self.model = TableModel(data)
        self.model.headerData(0, Qt.Horizontal, Qt.DisplayRole)
        self.ui.tableView.setModel(self.model)

        print(time(), "CP_pass")

    def CP_acco(self):

        print(time(), "CP_acco")

    def CP_name(self):

        print(time(), "CP_name")

    def CP_info(self):

        print(time(), "CP_info")

    def Show_Hide(self):

        print(time(), "Show_Hide")

    def Edit(self):

        print(time(), "Edit")

    def Add(self):

        self.ui.progressBar.setValue(self.ui.progressBar.value() + 10)

        print(time(), "Add")

    def Delete(self):

        self.ui.progressBar.setValue(self.ui.progressBar.value() - 10)

        print(time(), "Delete")

    def Infomation(self):

        print(time(), "Infomation")





if __name__ == "__main__":


    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
        
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())