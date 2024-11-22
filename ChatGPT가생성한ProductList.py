import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3
import os

# DB파일 초기화
con = sqlite3.connect("ProductList.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
)

# 디자인 파일 로딩
form_class = uic.loadUiType("ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 초기값 설정
        self.id = 0
        self.name = ""
        self.price = 0

        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setHorizontalHeaderLabels(["제품 ID", "제품 명", "제품 가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 엔터키로 다음 컨트롤 이동
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

    def addProduct(self):
        self.name = self.prodName.text().strip()
        self.price = self.prodPrice.text().strip()

        if not self.name or not self.price.isdigit():
            QMessageBox.warning(self, "입력 오류", "올바른 제품명과 가격을 입력하세요.")
            return

        cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (self.name, int(self.price)))
        con.commit()
        self.getProduct()

    def updateProduct(self):
        self.id = self.prodID.text().strip()
        self.name = self.prodName.text().strip()
        self.price = self.prodPrice.text().strip()

        if not self.id.isdigit() or not self.name or not self.price.isdigit():
            QMessageBox.warning(self, "입력 오류", "올바른 ID, 제품명, 가격을 입력하세요.")
            return

        cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (self.name, int(self.price), int(self.id)))
        con.commit()
        self.getProduct()

    def removeProduct(self):
        self.id = self.prodID.text().strip()

        if not self.id.isdigit():
            QMessageBox.warning(self, "입력 오류", "올바른 ID를 입력하세요.")
            return

        cur.execute("DELETE FROM Products WHERE id = ?;", (int(self.id),))
        con.commit()
        self.getProduct()

    def getProduct(self):
        cur.execute("SELECT * FROM Products;")
        records = cur.fetchall()

        self.tableWidget.setRowCount(len(records))
        for row, item in enumerate(records):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text().strip())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text().strip())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text().strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()

    # 앱 종료 후 리소스 정리
    exit_code = app.exec_()
    con.close()
    sys.exit(exit_code)
