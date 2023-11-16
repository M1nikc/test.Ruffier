from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QRadioButton,QLineEdit
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont
from test_rufe import *
from last_windw import Last_win
time="0"
class Expirement ():
    def __init__(self,age,puls1,puls2,puls3):
        self.age=age
        self.puls1=puls1
        self.puls2=puls2
        self.puls3=puls3
class Second_win(QWidget):
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
        txt1=QLabel(win2_text1)
        self.edit1=QLineEdit('Ф.И.О')
        txt2=QLabel(win2_text2)
        self.edit2=QLineEdit('0')
        txt3=QLabel(win2_text3)
        self.test_timer1=QPushButton("Начать первый тест")
        self.edit3=QLineEdit('0')
        txt4=QLabel(win2_text4) 
        self.start_test1=QPushButton("Начать делать приседания")
        txt5=QLabel(win2_text5)
        self.start_finel_test=QPushButton("Начать финальный тест")
        self.result1=QLineEdit('0')
        self.result2=QLineEdit('0')
        self.send_result=QPushButton("Отправить результаты")
        self.text_timer=QLabel("00:00:15")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        y_line1=QVBoxLayout()
        y_line2=QVBoxLayout()
        x_line1=QHBoxLayout()
        y_line1.addWidget(txt1,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.edit1,alignment=Qt.AlignLeft)
        y_line1.addWidget(txt2,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.edit2,alignment=Qt.AlignLeft)
        y_line1.addWidget(txt3,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.test_timer1,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.edit3,alignment=Qt.AlignLeft)
        y_line1.addWidget(txt4,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.start_test1,alignment=Qt.AlignLeft)
        y_line1.addWidget(txt5,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.start_finel_test,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.result1,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.result2,alignment=Qt.AlignLeft)
        y_line1.addWidget(self.send_result,alignment=Qt.AlignCenter)
        y_line2.addWidget(self.text_timer,alignment=Qt.AlignCenter)
        x_line1.addLayout(y_line1)
        x_line1.addLayout(y_line2)
        self.setLayout(x_line1)
    def timer1 (self):
        global time
        time=QTime(0,0,15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1event)
        self.timer.start(1000)
    def timer1event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36))
        self.text_timer.setStyleSheet('Color:rgb(0,255,0)')
    def timer2 (self):
        global time
        time=QTime(0,0,30)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer2event)
        self.timer.start(1500)
    def timer2event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36))
        self.text_timer.setStyleSheet('Color:rgb(0,0,0)')
    def timer3 (self):
        global time
        time=QTime(0,1,0)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(1000)
    def timer3event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet('Color:rgb(0,255,0)')
        if 15<int(time.toString("hh:mm:ss")[6:8]) <45:
            self.text_timer.setStyleSheet('Color:rgb(0,0,0)')
        if int(time.toString("hh:mm:ss")[6:8]) < 15:
            self.text_timer.setStyleSheet('Color:rgb(0,255,0)')
        if time.toString("hh:mm:ss")=="00:00:00":
            self.timer.stop()
    def connects (self):
        self.test_timer1.clicked.connect(self.timer1)
        self.start_test1.clicked.connect(self.timer2)
        self.start_finel_test.clicked.connect(self.timer3)
        self.send_result.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.exp=Expirement(int(self.edit2.text()),int(self.edit3.text()),int(self.result1.text()),int(self.result2.text()))
        self.last_win=Last_win(self.exp)
#app=QApplication([])
#mw=Second_win()
#app.exec()