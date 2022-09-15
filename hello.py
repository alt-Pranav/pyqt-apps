'''Simple Hello World with PyQT6'''
import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# initialise the app
app = QApplication([])

# create the window widget and components
window = QWidget()
window.setWindowTitle("Hello World App")
window.setGeometry(100,100,280,200)
helloMsg =  QLabel("<h1>Hello World! </h1>", parent=window)

# place the text on the window
helloMsg.move(280,200)

# show the app's GUI
window.show()

# run the application's event loop
# wrapping the exec call in sys.exit() helps exit Python 
# and release memory resources when the app terminates
sys.exit(app.exec())