import sys
from PySide2.QtWidgets import QApplication, QDialog, QHBoxLayout, QPushButton, QMessageBox, QLineEdit, QLabel, QVBoxLayout
from PySide2.QtGui import QFont

class ConfirmationDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Confirmation Dialog')
        self.setGeometry(100, 100, 500, 200)

        layout = QVBoxLayout()

        # Text label with a larger font size
        label = QLabel(self.message)
        label.setFont(QFont("Arial", 16))  # Set the font size to 16
        layout.addWidget(label)

        button_layout = QHBoxLayout()
        
        # Text entry field
        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)
        
        # No button (left side)
        self.no_button = QPushButton('No')
        self.no_button.clicked.connect(self.reject)
        button_layout.addWidget(self.no_button)

        # Yes button (right side)
        self.yes_button = QPushButton('Yes')
        self.yes_button.clicked.connect(self.accept)
        button_layout.addWidget(self.yes_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

def get_user_confirmation_with_input(message):
    app = QApplication(sys.argv)
    dialog = ConfirmationDialog(message)
    
    result = dialog.exec_()

    if result == QDialog.Accepted:
        return True, dialog.input_field.text()
    else:
        return False, ''

if __name__ == '__main__':
    message = "Are you sure you want to proceed?"
    confirmed, user_input = get_user_confirmation_with_input(message)
    
    if confirmed:
        print(f'You clicked Yes. Input: {user_input}')
    else:
        print('You clicked No')
