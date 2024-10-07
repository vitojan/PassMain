# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:53:55 2023

@author: VitoJan
"""

from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CFB
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.backends import default_backend
from hashlib import md5
from os.path import isfile
from os import urandom
from sys import argv, exit
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QHBoxLayout, QPushButton, QLineEdit, QLabel, QVBoxLayout, QAbstractItemView
from PySide2.QtCore import QAbstractTableModel, Qt
from PySide2.QtGui import QFont
from ui_passmain import Ui_MainWindow
from re import match
from json import loads
from pyperclip import copy
from pandas import DataFrame, concat

def is_valid_password(password):
    if len(password) > 32 or len(password) < 4:
        return False, "密碼長度限制 4~32"
    
    pattern = r'^[a-zA-Z0-9_-]+$'
    
    if match(pattern, password):
        return True, ""
    
    return False, "密碼只限字母數字和減號、下橫線"

class ConfirmationDialogA(QDialog):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PassM')
        self.setGeometry(100, 100, 500, 200)

        layout = QVBoxLayout()

        # Text label with a larger font size
        label = QLabel(self.message)
        label.setFont(QFont("Arial", 16))  # Set the font size to 16
        layout.addWidget(label)

        button_layout = QHBoxLayout()
        
        # No button (left side)
        self.no_button = QPushButton('取消')
        self.no_button.clicked.connect(self.reject)
        button_layout.addWidget(self.no_button)

        # Yes button (right side)
        self.yes_button = QPushButton('確定')
        self.yes_button.clicked.connect(self.accept)
        button_layout.addWidget(self.yes_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        
def messbox(message):

    dialog = ConfirmationDialogA(message)
    
    result = dialog.exec_()

    if result == QDialog.Accepted:
        return True
    else:
        return False


class ConfirmationDialogB(QDialog):
    def __init__(self, message, show):
        super().__init__()
        self.message = message
        self.show = show
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('PassM')
        self.setGeometry(100, 100, 500, 200)

        layout = QVBoxLayout()

        # Text label with a larger font size
        label = QLabel(self.message)
        label.setFont(QFont("Arial", 16))  # Set the font size to 16
        layout.addWidget(label)

        button_layout = QHBoxLayout()
        
        # Text entry field
        self.input_field = QLineEdit()
        self.input_field.setAcceptDrops(False)
        self.input_field.setEchoMode(self.show)
            
            
        layout.addWidget(self.input_field)
        
        # No button (left side)
        self.no_button = QPushButton('取消')
        self.no_button.clicked.connect(self.reject)
        button_layout.addWidget(self.no_button)
        if not(self.show == QLineEdit.Normal):
            self.show_button = QPushButton('顯示')
            self.show_button.clicked.connect(self.Pshow())
            button_layout.addWidget(self.show_button)
            self.show_button.setAutoDefault(False)
            self.Phide()

        # Yes button (right side)
        self.yes_button = QPushButton('確定')
        self.yes_button.clicked.connect(self.accept)
        button_layout.addWidget(self.yes_button)
        self.no_button.setAutoDefault(False)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        
    def Pshow(self):
        self.show_button.clicked.connect(self.Phide)
        self.input_field.setEchoMode(QLineEdit.Normal)
        
    def Phide(self):
        self.show_button.clicked.connect(self.Pshow)
        self.input_field.setEchoMode(self.show)
        
        
        
def entrybox(message, show):

    dialog = ConfirmationDialogB(message, show)


    result = dialog.exec_()

    if result == QDialog.Accepted:
        return True, dialog.input_field.text()
    else:
        return False, dialog.input_field.text()

def calculate_md5(input_string):
    md5_hash = md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest().encode("utf-8")[:32]


def aes_256_encrypt(key, plaintext):
    iv = urandom(16)
    cipher = Cipher(AES(key), CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return iv + ciphertext


def aes_256_decrypt(key, encrypted_data):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    
    cipher = Cipher(AES(key), CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    unpadder = PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext


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
        self.ui.pushButton_5.clicked.connect(self.Hide)
        self.ui.pushButton_6.clicked.connect(self.Delete)
        self.ui.pushButton_8.clicked.connect(self.CP_pass)
        self.ui.pushButton_9.clicked.connect(self.CP_name)
        self.ui.pushButton_10.clicked.connect(self.Show)
        self.ui.pushButton_11.clicked.connect(self.Add)
        self.ui.pushButton_12.clicked.connect(self.Save)
        self.ui.lineEdit.setAcceptDrops(False)
        #self.ui.tableView.setSelectionMode(QAbstractItemView .SingleSelection)
        self.ui.tableView.doubleClicked.connect(self.DoubleClicked)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        
        self.lock_update()
        
    def lock_update(self):
        if lock:
            self.ui.pushButton_2.setDisabled(False)
            self.ui.pushButton_3.setDisabled(True)
            self.ui.pushButton_4.setDisabled(True)
            self.ui.pushButton_5.setDisabled(True)
            self.ui.pushButton_6.setDisabled(True)
            self.ui.pushButton_8.setDisabled(True)
            self.ui.pushButton_9.setDisabled(True)
            self.ui.pushButton_10.setDisabled(True)
            self.ui.pushButton_11.setDisabled(True)
            self.ui.pushButton_12.setDisabled(True)
            self.ui.lineEdit.setDisabled(False)
            
        else:
            self.ui.pushButton_2.setDisabled(True)
            self.ui.pushButton_3.setDisabled(False)
            self.ui.pushButton_4.setDisabled(False)
            self.ui.pushButton_5.setDisabled(False)
            self.ui.pushButton_6.setDisabled(False)
            self.ui.pushButton_8.setDisabled(False)
            self.ui.pushButton_9.setDisabled(False)
            self.ui.pushButton_10.setDisabled(False)
            self.ui.pushButton_11.setDisabled(False)
            self.ui.pushButton_12.setDisabled(False)
            self.ui.lineEdit.setText("")
            self.ui.lineEdit.setDisabled(True)


            self.update_list()
            self.ui.label_2.setText('<html><head/><body><p align="center"><span style=" font-size:20pt; font-weight:600; color:#0a5a5a;">已解密</span></p></body></html>')
    
    def Decode(self):
        global data, key, lock
        if lock:
            try:
                
                f = open(file_path, "rb")
                file = f.read()
                f.close()
                
                key = calculate_md5(self.ui.lineEdit.text())
                
                data = DataFrame.from_dict(loads(aes_256_decrypt(key, file).decode()), orient="columns").sort_index(ignore_index=True)
                
                lock = False
                
                self.update_mask()
                self.lock_update()
                
                
            except:
                
                self.ui.label_2.setText('<html><head/><body><p align="center"><span style=" font-size:20pt; font-weight:600; color:#a00a0a;">解密錯誤</span></p></body></html>')
            
    
    def DoubleClicked(self):
        cd = entrybox("更改內容", QLineEdit.Password)
        if cd[0]:
            self.ui.pushButton_12.setText("儲存*")
            y = self.ui.tableView.currentIndex().row()
            x = self.ui.tableView.currentIndex().column()
            data.loc[y, data.columns[x]] = cd[1]
            self.update_list()
            
            

        
    def CP_pass(self):
        
        y = self.ui.tableView.currentIndex().row()
        if not(y == -1):
            copy(data.at[y, "密碼"])
        
    def CP_acco(self):
        
        y = self.ui.tableView.currentIndex().row()
        if not(y == -1):
            copy(data.at[y, "帳號"])
    
    def CP_name(self):
        
        y = self.ui.tableView.currentIndex().row()
        if not(y == -1):
            copy(data.at[y, "名稱"])
        
    def CP_info(self):
        
        y = self.ui.tableView.currentIndex().row()
        if not(y == -1):
            copy(data.at[y, "備註內容"])
    
    def Show(self):
        global hide_mask_list
        
        y = self.ui.tableView.currentIndex().row()
        if not(y == -1):
            
            
            if y not in hide_mask_list:
                hide_mask_list.append(y)
                
            self.update_list()
        
    def Hide(self):
        global hide_mask_list
        
        y = self.ui.tableView.currentIndex().row()
        if not(y == -1):
            
            if y in hide_mask_list:
                hide_mask_list.remove(y)
            
            self.update_list()
        
    def Add(self):
        global data

        self.ui.pushButton_12.setText("儲存*")
        data = concat([data, DataFrame([["名稱","","",""]], columns = ["名稱", "帳號", "密碼", "備註內容"])], ignore_index=True)
        
        self.update_mask()

        
    def Delete(self):
        global data
        
        y = self.ui.tableView.currentIndex().row()
        if not(y == -1):

            self.ui.pushButton_12.setText("儲存*")
            data = data.drop(y).sort_index(ignore_index=True)

            self.update_mask()

    
    def Infomation(self):
        messbox('<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:600; color:#be4345;">歡迎使用 </span><span style=" font-size:16pt; font-weight:600; color:#e89d1b;">PassMain</span></p><p align="center"><span style=" font-size:11pt; color:#8a8a8a;">這是一個由 </span><span style=" font-size:11pt; font-weight:600; color:#9d65ab;">VitoJan</span><span style=" font-size:11pt; color:#8a8a8a;">所開發的密碼集中管理軟體。</span></p><p align="center"><br/></p><p align="center"><br/></p><p align="center"><br/></p></body></html>')
        
    

    def Save(self):
        self.ui.pushButton_12.setText("儲存")
        json_string = data.to_json(orient='columns')
        encrypted_data = aes_256_encrypt(key, json_string.encode('utf-8'))
        f = open(file_path, "wb")
        f.write(encrypted_data)
        f.close()
    
    def update_mask(self):
        global hide_mask
        
        _n = len(data)
        _l = []
        for i in range(_n):
            _l.append(["...","...","..."])
            
        hide_mask = DataFrame(_l, columns = ["帳號", "密碼", "備註內容"])
        for i in hide_mask_list:
            if i >= _n:
                hide_mask_list.remove(i)
        self.update_list()
        
        
    def update_list(self):

        _d = data.copy()
        
        _d.update(hide_mask.drop(hide_mask_list))

        self.ui.tableView.setModel(TableModel(_d))

    
#if __name__ == "__main__":
    
if not QApplication.instance():
    app = QApplication(argv)
else:
    app = QApplication.instance()
    
hide_mask_list = []

hide_mask = DataFrame([], columns = ["帳號", "密碼", "備註內容"])

    
file_path = "_Pass_Main_Data_.bin"
if isfile(file_path):
    lock = True
    
    
else:
    mtext = "請設定密碼"
    nsucc = True
    while True:
        key = entrybox(mtext, QLineEdit.Password)
        nsucc, mtext = is_valid_password(key[1])
        
        if not(key[0]):
            app.closeAllWindows()
            app.quit()
            #app.exit()
            exit(app.exec_())
            #sys.exit()
            break
        if nsucc:
            break
    mtext = "確認密碼"

    while True:
        key2 = entrybox(mtext, QLineEdit.Password)
        if key == key2:
            break
        else:
            mtext = "密碼不一致"
        if not(key2[0]):
            app.closeAllWindows()
            app.quit()
            #app.exit()
            exit(app.exec_())
            #sys.exit()
            break

    if nsucc:
        data = DataFrame([
        ], columns = ["名稱", "帳號", "密碼", "備註內容"])
        lock = False
        json_string = data.to_json(orient='columns')
        key = calculate_md5(key[1])
        encrypted_data = aes_256_encrypt(key, json_string.encode('utf-8'))
        f = open(file_path, "wb")
        f.write(encrypted_data)
        f.close()

        




    
window = MainWindow()
window.show()
exit(app.exec_())
    
