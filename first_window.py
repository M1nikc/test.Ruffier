from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QRadioButton
from PyQt5.QtCore import Qt,QTime,QTimer
from test_rufe import *
from second_window import Second_win
class Main_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
       self.setWindowTitle(name_window1)
       self.resize(size_window1,size_window2)
    def initUI (self):
        text1=QLabel(instr)
        self.button_start=QPushButton("Начать")
        y_line1=QVBoxLayout()
        y_line1.addWidget(text1,alignment=Qt.AlignCenter)
        y_line1.addWidget(self.button_start,alignment=Qt.AlignCenter)
        self.setLayout(y_line1)
    def connects (self):
        self.button_start.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.sec_win=Second_win()
app=QApplication([])
mw=Main_win()
app.exec()
    

