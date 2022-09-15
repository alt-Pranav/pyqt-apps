import sys
import PyQt6.QtWidgets as qtw


def getLayout(arg):
    if arg == "0":
        layout = qtw.QHBoxLayout()

    if arg == "1":
        layout = qtw.QVBoxLayout()

    if arg == "2":
        layout = qtw.QGridLayout()
        layout.addWidget(qtw.QPushButton("0,0"), 0 , 0)
        layout.addWidget(qtw.QPushButton("3,0"), 3, 0)
        layout.addWidget(qtw.QPushButton("0,7"), 0 , 7)
        return layout

    if arg == "3":
        layout = qtw.QFormLayout()
        layout.addRow("Name: ", qtw.QLineEdit())
        

    layout.addWidget(qtw.QPushButton("1"))
    layout.addWidget(qtw.QPushButton("2"))
    layout.addWidget(qtw.QPushButton("3"))

    return layout

app = qtw.QApplication(sys.argv)

window = qtw.QWidget()
window.setWindowTitle("different layouts")
print(app.arguments()[1])
window.setLayout(getLayout(app.arguments()[1]))

window.show()
sys.exit(app.exec())
    
