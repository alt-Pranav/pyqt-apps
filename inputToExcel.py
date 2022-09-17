'''Test appending to excel'''

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)

import pandas as pd

DIMENSIONS = 400

class mainAppWindow(QWidget):

    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle("Test appending to excel")
        self.resize(DIMENSIONS, DIMENSIONS)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.inputItem = QLineEdit()
        self.layout.addWidget(self.inputItem)
        

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.buttonLayout = QHBoxLayout()
        self.newButton = QPushButton("New File", clicked = self.createFile)
        self.appendButton = QPushButton("Add to File", clicked = self.appendToFile)
        self.buttonLayout.addWidget(self.newButton)
        self.buttonLayout.addWidget(self.appendButton)

        self.layout.addLayout(self.buttonLayout)

        self.exportButton = QPushButton("Export to Excel", clicked = self.exportFile)
        self.layout.addWidget(self.exportButton)

        self.colIndex = 0


    def createFile(self):

        self.columnHeaders = list("ASDFGHJ")
        self.n = 10

        self.table.setRowCount(self.n)
        self.table.setColumnCount(len(self.columnHeaders))
        self.table.setHorizontalHeaderLabels(self.columnHeaders)

        for row in range(self.n):
            for col in range(len(self.columnHeaders)):
                tableItem = QTableWidgetItem("Cell {0}-{1}".format(self.columnHeaders[col], row+1))
                self.table.setItem(row, col, tableItem)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        print("created")

    def appendToFile(self):

        item = self.inputItem.text()
        row = self.n 

        self.table.insertRow(self.n)
        numcols = self.table.columnCount()
        numrows = self.table.rowCount()           
        self.table.setRowCount(numrows)
        self.table.setColumnCount(numcols)
        
        tableItem = QTableWidgetItem(item)
        self.table.setItem(row, self.colIndex, tableItem)

        self.colIndex  = (self.colIndex + 1) % self.table.columnCount()
        print("appended")

    def exportFile(self):

        headerNames = []
        for col in range(self.table.columnCount()):
            headerNames.append(self.table.horizontalHeaderItem(col).text())

        df = pd.DataFrame(columns=headerNames)

        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                try:
                    df.at[row, headerNames[col]] = self.table.item(row, col).text()
                except:
                    print("Row = {0}, Col = {1}".format(row, col))

        df.to_excel("AppendTestfile.xlsx", index=False)
        print("exported")




if __name__ == "__main__":
    app = QApplication([])
    window = mainAppWindow()
    window.show()
    sys.exit(app.exec())
    