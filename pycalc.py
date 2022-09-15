"""PyCalc is a simple calculator built with Python and PyQt."""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    # necessary for View 
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

# for controller class
# to send values via signals to slots
from functools import partial

# these values represent pixels
# Note: When it comes to widget size, you’ll rarely find measurement units in the PyQt documentation. The measurement unit is assumed to be pixels, except when you’re working with QPrinter class, which uses points.
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

ERROR_MSG = "ERROR"

class PyCalcWindow(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle("Calculator App")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

        # this is a self defined variable
        self.generalLayout = QVBoxLayout()

        # This object will be the parent of all the required GUI components in the calculator app.
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createDisplay()
        self._createButtons()

    # creates the calculator's display
    # hence it is read only
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()

        keyboard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        ''' sets the display's text '''
        self.display.setText(text)
        self.display.setFocus()
    
    def displayText(self):
        ''' get the display's text '''
        return self.display.text()
    
    def clearDisplay(self):
        ''' clears the display '''
        self.setDisplayText("")


# model implementation
def evaluateExpression(expression):
    ''' evaluates an expression '''
    try:
        # eval is an inbuilt function
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result


'''
controller class needs to perform three main tasks:

Access the GUI's public interface.
Handle the creation of math expressions.
Connect all the buttons' .clicked signals with the appropriate slots.
'''

class calcController:

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + subExpression

        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(partial(self._buildExpression, keySymbol))

        self._view.buttonMap["="].clicked.connect(self._calculateResult)

        self._view.display.returnPressed.connect(self._calculateResult)

        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

def main():
    pyCalcApp = QApplication([])
    window = PyCalcWindow()
    window.show()
    calcController(model=evaluateExpression, view=window)
    sys.exit(pyCalcApp.exec()) 

if __name__ == "__main__":
    main()