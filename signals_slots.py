import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Signal and Slot")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Learn Signals and Slots")

layout = QVBoxLayout()

button = QPushButton("Greet")
#widget.signal.connect(slot_function)
button.clicked.connect(greet)

layout.addWidget(button)

msgLabel = QLabel("")
layout.addWidget(msgLabel)

window.setLayout(layout)
window.show()
sys.exit(app.exec())