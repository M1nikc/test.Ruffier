from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QRadioButton
from PyQt5.QtCore import Qt
from test_rufe import *
class Last_win(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.set_appear()
        self.exp=exp
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(name_window3)
        self.resize(size_window1,size_window2)
    def initUI (self):
        self.results()
        self.index_last=QLabel("Индекс Руфье:"+str(self.index))
        self.last_result=QLabel("Работоспособность вашего сердца:"+self.results())
        y_line=QVBoxLayout()
        y_line.addWidget(self.index_last,alignment=Qt.AlignCenter)
        y_line.addWidget(self.last_result,alignment=Qt.AlignCenter)
        self.setLayout(y_line)
    def results (self):
        if self.exp.age<7:
            self.index=0
            return "Нет данных для такого возраста"
        self.index=(4*self.exp.puls1+self.exp.puls2+self.exp.puls3-200)/10
        low_level=21-((min(15,self.exp.age)-7)//2)*1.5
        if self.index>=low_level:
            return txt_res1
        elif self.index>=low_level-4:
            return txt_res2
        elif self.index>=low_level-9:
            return txt_res3
        elif self.index>=low_level-14.5:
            return txt_res4
        else:
            return txt_res5
#app=QApplication([])
#mw=Last_win()
#app.exec()