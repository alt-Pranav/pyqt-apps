import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract.exe"

class AppWindow(QWidget):

    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle("threaded opencv")

        self.VBL = QVBoxLayout()


        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.ocrText = "N/A"
        self.ocrLabel = QLineEdit()
        self.ocrLabel.setReadOnly(True)
        self.ocrLabel.setText(self.ocrText)
        self.VBL.addWidget(self.ocrLabel)

        self.videoGetter = VideoHandler()

        self.videoGetter.start()

        self.videoGetter.ImageUpdate.connect(self.ImageUpdateSlot)
        self.videoGetter.ocrUpdate.connect(self.ocrUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, img):
        self.FeedLabel.setPixmap(QPixmap.fromImage(img))

    def ocrUpdateSlot(self, words):
        self.ocrLabel.setText(words)


class VideoHandler(QThread): 

    ImageUpdate = pyqtSignal(QImage)
    ocrUpdate = pyqtSignal(str)
    stream = cv2.VideoCapture(0)
    (grabbed, frame) = stream.read()
    stopped = False


    def run(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                Image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

                self.ocrUpdate.emit(pytesseract.image_to_string(Image))

    def stop(self):
        self.stopped = True
        

if __name__ == "__main__":
    app = QApplication([])
    window = AppWindow()
    window.show()
    sys.exit(app.exec())