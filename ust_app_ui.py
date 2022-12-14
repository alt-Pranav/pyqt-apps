'''
The main UST app

Features:
1. QLineEdit to input filename
2. QLineEdit to input directory path
3. QLineEdit to set OCR time interval
4. QLineEdit to set quantity name (that is being measured)
5. QTableWidget to show datatable dynamically
6. QLabel to show live camera feed
'''

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import datetime


DIMENSION = 1024

class ustApp(QWidget):

    def __init__(self):
        super().__init__(parent=None)

        self.resize(DIMENSION, DIMENSION)
        self.setWindowTitle("MULTIMETER READER")

        # for the entire app
        self.appLayout = QHBoxLayout()
        self.setLayout(self.appLayout)

        # for the Camera View and Data Table
        self.displayLayout = QVBoxLayout()


        self.displayLayout.addWidget(CameraWidget())
        self.displayLayout.addWidget(ReadingsTableWidget())
        

        self.appLayout.addWidget(InputValuesWidget())
        self.appLayout.addLayout(self.displayLayout)


class CameraWidget(QWidget):

    def __init__(self):
        super().__init__(parent = None)
        self.resize(DIMENSION//2, DIMENSION-500)
        self.show()
        # need to create separate thread for OCR

class ReadingsTableWidget(QWidget):

    def __init__(self):
        super().__init__(parent = None)
        self.resize(DIMENSION//2, DIMENSION-500)
        self.show()
        # data table
        self.table = QTableWidget()

class InputValuesWidget(QWidget):

    def __init__(self):
        super().__init__(parent = None)

        self.resize(DIMENSION, 500)
        
        # defining data members needed across multiple functions
        self.excelFilePath = "{0}.xlsx".format(datetime.date)
        self.scanInterval = 500 # in milliseconds
        self.currentMeasure = ""

        # for taking user input
        self.inputLayout = QFormLayout()

        self.fileName = QLineEdit()
        self.filePath = QLineEdit()
        self.timeInterval = QLineEdit()
        self.measureName = QLineEdit()

        self.submitUserInput = QPushButton("Submit", clicked = self.getUserInput)
        
        self.inputLayout.addRow("File Name: ", self.fileName)
        self.inputLayout.addRow("File Path: ", self.filePath)
        self.inputLayout.addRow("Scan Interval (in ms)", self.timeInterval)
        self.inputLayout.addRow("Quantity Name", self.measureName)
        self.inputLayout.addRow(self.submitUserInput)

        self.inputLayout.setVerticalSpacing(20)        
        self.show()

    def getUserInput(self):
        if self.fileName.text() and self.filePath.text():
            self.excelFilePath = "{0}/{1}.xlsx".format(self.filePath.text(), self.fileName.text())
            self.scanInterval = int(self.timeInterval.text())
            self.currentMeasure = self.measureName.text()
        else:
            if self.fileName.text():
                self.fileName.setText("INVALID INPUT")
            else:
                self.filePath.setText("INVALID INPUT")

if __name__ == "__main__":
    app = QApplication([])
    window = ustApp()
    window.show()
    sys.exit(app.exec())