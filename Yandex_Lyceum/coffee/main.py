import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget


class Form(QWidget):
    def __init__(self, dbv):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.dbv = dbv
        self.pushButton.clicked.connect(self.add_coffee)

    def add_coffee(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.comboBox.currentText()
        d = self.lineEdit_4.text()
        e = self.lineEdit_5.text()
        f = self.lineEdit_6.text()
        if a != '' and b != '' and d != '' and e != '' and f != '':
            query = '''INSERT INTO
            coffee(varieties, roast_level, processing, taste_description, price, package_size)
            VALUES(?, ?, ?, ?, ?, ?)'''
            self.dbv.connection.cursor().execute(query, (a, b, c, d, e, f))
            self.dbv.select_data()
            self.dbv.connection.commit()
            self.close()
    
 
class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.pushButton.clicked.connect(self.select_data)
        self.textEdit.setPlainText("SELECT * FROM coffee")
        self.pushButton_2.clicked.connect(self.add_coffee)
        self.select_data()
        self.form = Form(self)

    def select_data(self):
        query = self.textEdit.toPlainText()
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
    
    def add_coffee(self):
        self.form.show()
        self.textEdit.setPlainText("SELECT * FROM coffee")

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())