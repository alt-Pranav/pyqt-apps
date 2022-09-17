import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QVBoxLayout,
)

import pandas as pd

DIMENSIONS = 400

class DataStorer(QWidget):

    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle("Data Storer")
        self.resize(DIMENSIONS, DIMENSIONS)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.button = QPushButton("Export to Excel", clicked=self.exportToExcel)
        self.layout.addWidget(self.button)

        self.loadDummyData()

    def exportToExcel(self):
        columnHeads = []

        # create column header list
        for col in range(self.table.model().columnCount()):
            columnHeads.append(self.table.horizontalHeaderItem(col).text())

        df = pd.DataFrame(columns=columnHeads)
        print(columnHeads)

        # set records in dataframe
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                df.at[row, columnHeads[col]] = self.table.item(row, col).text()

        df.to_excel("dummy_file.xlsx", index=False)
        print("Excel file exported")


    def loadDummyData(self):
        self.headerLabels = list("ABCDEFG")
        n = 300
        self.table.setRowCount(n)
        self.table.setColumnCount(len(self.headerLabels))
        self.table.setHorizontalHeaderLabels(self.headerLabels)

        for row in range(n):
            for col in range(0, len(self.headerLabels)):
                item = QTableWidgetItem('Cell {0}-{1}'.format(self.headerLabels[col],row+1))
                self.table.setItem(row, col, item)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()



if __name__ == "__main__":
    app = QApplication([])
    window = DataStorer()
    window.show()
    sys.exit(app.exec()) 