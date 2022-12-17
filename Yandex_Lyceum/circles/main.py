from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Circles')
        self.setGeometry(300, 300, 500, 500)
        self.pushButton.clicked.connect(self.creater)
        self.d = 0

    def creater(self):
        self.d = randint(10, 300)
        self.repaint()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(250, 250, 0))
        qp.drawEllipse(250 - (self.d // 2), 250 - (self.d // 2), self.d, self.d)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    exit(app.exec_())