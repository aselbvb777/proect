from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from instr import *
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
            self.vline = QVBoxLayout()
            self.hline = QHBoxLayout()
            self.l1 = QLabel("Индекс Руфье:")
            self.vline.addWidget(self.l1,alignment = Qt.AlignCenter)
            self.l2 = QLabel("Работоспособность")
            self.vline.addWidget(self.l2,alignment = Qt.AlignCenter)
            self.setLayout(self.vline)
            