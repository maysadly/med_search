from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUI('UI.ui', self)
        self.setWindowTitle('Circles')
        self.setGeometry(500, 500)
        self.pushButton.clicked.connect(self.creater)
        self.d = 0

    def creater(self):
        self.d = randint(10, 300)
        self.repaint()
    
    def paintEvent(self):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor.yellow)
        qp.drawEllipse(200, 200, self.d, self.d)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.show()
    exit(app.exec_())