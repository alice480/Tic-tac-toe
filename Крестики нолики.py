import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cross_zero.ui', self)
        self.count = 0
        self.radioButton.clicked.connect(self.first_move)
        self.radioButton_2.clicked.connect(self.first_move)
        self.pushButton_10.clicked.connect(self.first_move)
        self.pushButton.clicked.connect(self.change_text_1)
        self.pushButton_2.clicked.connect(self.change_text_2)
        self.pushButton_3.clicked.connect(self.change_text_3)
        self.pushButton_4.clicked.connect(self.change_text_4)
        self.pushButton_5.clicked.connect(self.change_text_5)
        self.pushButton_6.clicked.connect(self.change_text_6)
        self.pushButton_7.clicked.connect(self.change_text_7)
        self.pushButton_8.clicked.connect(self.change_text_8)
        self.pushButton_9.clicked.connect(self.change_text_9)

    def first_move(self):
        if self.radioButton.isChecked():
            self.flag_x = True
        else:
            self.flag_x = False
        self.unblocking()

    def change_text_1(self):
        if self.flag_x:
            self.pushButton.setText('X')
            self.flag_x = False
        else:
            self.pushButton.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_2(self):
        if self.flag_x:
            self.pushButton_2.setText('X')
            self.flag_x = False
        else:
            self.pushButton_2.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_3(self):
        if self.flag_x:
            self.pushButton_3.setText('X')
            self.flag_x = False
        else:
            self.pushButton_3.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_4(self):
        if self.flag_x:
            self.pushButton_4.setText('X')
            self.flag_x = False
        else:
            self.pushButton_4.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_5(self):
        if self.flag_x:
            self.pushButton_5.setText('X')
            self.flag_x = False
        else:
            self.pushButton_5.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_6(self):
        if self.flag_x:
            self.pushButton_6.setText('X')
            self.flag_x = False
        else:
            self.pushButton_6.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_7(self):
        if self.flag_x:
            self.pushButton_7.setText('X')
            self.flag_x = False
        else:
            self.pushButton_7.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_8(self):
        if self.flag_x:
            self.pushButton_8.setText('X')
            self.flag_x = False
        else:
            self.pushButton_8.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def change_text_9(self):
        if self.flag_x:
            self.pushButton_9.setText('X')
            self.flag_x = False
        else:
            self.pushButton_9.setText('O')
            self.flag_x = True
        self.count += 1
        self.check()

    def check(self):
        if ((self.pushButton.text() == self.pushButton_5.text() == self.pushButton_9.text()) or\
                (self.pushButton_3.text() == self.pushButton_5.text() == self.pushButton_7.text())) and\
                self.pushButton_5.text() != '':
            if self.pushButton_5.text() == 'X':
                self.label.setText('Выиграл X!')
            else:
                self.label.setText('Выиграл O!')
            self.blocking()
        elif self.pushButton.text() == self.pushButton_2.text() == self.pushButton_3.text() and\
                        self.pushButton.text() != '':
            if self.pushButton.text() == 'X':
                self.label.setText('Выиграл X!')
            else:
                self.label.setText('Выиграл O!')
            self.blocking()
        elif self.pushButton_4.text() == self.pushButton_5.text() == self.pushButton_6.text() and\
                self.pushButton_4.text() != '':
            if self.pushButton_4.text() == 'X':
                self.label.setText('Выиграл X!')
            else:
                self.label.setText('Выиграл O!')
            self.blocking()
        elif self.pushButton_7.text() == self.pushButton_8.text() == self.pushButton_9.text() and\
                self.pushButton_7.text() != '':
            if self.pushButton_7.text() == 'X':
                self.label.setText('Выиграл X!')
            else:
                self.label.setText('Выиграл O!')
            self.blocking()
        elif self.pushButton.text() == self.pushButton_4.text() == self.pushButton_7.text() and\
                self.pushButton.text() != '':
            if self.pushButton.text() == 'X':
                self.label.setText('Выиграл X!')
            else:
                self.label.setText('Выиграл O!')
            self.blocking()
        elif self.pushButton_2.text() == self.pushButton_5.text() == self.pushButton_8.text() and\
                self.pushButton_2.text() != '':
            if self.pushButton_2.text() == 'X':
                self.label.setText('Выиграл X!')
            else:
                self.label.setText('Выиграл O!')
            self.blocking()
        elif self.pushButton_3.text() == self.pushButton_6.text() == self.pushButton_9.text() and\
                self.pushButton_3.text() != '':
            if self.pushButton_3.text() == 'X':
                self.label.setText('Выиграл X!')
            else:
                self.label.setText('Выиграл O!')
            self.blocking()
        else:
            if self.count == 9:
                self.label.setText('Ничья')
                self.blocking()

    def blocking(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)

    def unblocking(self):
        self.count = 0
        self.label.setText('')
        self.pushButton.setText('')
        self.pushButton_2.setText('')
        self.pushButton_3.setText('')
        self.pushButton_4.setText('')
        self.pushButton_5.setText('')
        self.pushButton_6.setText('')
        self.pushButton_7.setText('')
        self.pushButton_8.setText('')
        self.pushButton_9.setText('')
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.setWindowTitle("Крестики-нолики")
    sys.excepthook = except_hook
    sys.exit(app.exec())