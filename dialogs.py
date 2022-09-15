import sys
import PyQt6.QtWidgets as q

# this Window class inherits from QDialog
class Window(q.QDialog):

    def __init__(self):
        #base class’s initializer. Again, the parent argument is set to None because this is your app’s main window, so it must not have a parent.
        super().__init__(parent=None)

        self.setWindowTitle("Qdialog")

        dialogLayout = q.QVBoxLayout()
        formLayout = q.QFormLayout()

        formLayout.addRow("Name: ", q.QLineEdit())
        formLayout.addRow("Weight: ", q.QLineEdit())
        formLayout.addRow("Height: ", q.QLineEdit())
        formLayout.addRow("Age: ", q.QLineEdit())

        # we can nest layouts using this
        dialogLayout.addLayout(formLayout)

        buttons = q.QDialogButtonBox()
        buttons.setStandardButtons(
            q.QDialogButtonBox.StandardButton.Cancel | q.QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


if __name__ == "__main__":
    app = q.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())