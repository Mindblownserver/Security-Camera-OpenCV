from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout
import cv2
class Camera(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(-1)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

class LL(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Heya")

class CameraWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.feed = QLabel()
        self.box = QHBoxLayout(self)
        self.box.addWidget(self.feed)
        self.loadFeed()
        #self.feed.setStyleSheet("QWidget { background-color: %s }" % QColor(0, 0, 0).name())
    def ImageUpdateSlot(self, Image):
        self.feed.show()
        self.feed.setPixmap(QPixmap.fromImage(Image))
    def loadFeed(self):
        self.Camera = Camera()
        self.Camera.start()
        self.Camera.ImageUpdate.connect(self.ImageUpdateSlot)