from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout
import cv2
class Camera(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def __init__(self, tab):
        super().__init__()
        self.tab = tab
    def run(self):
        self.ThreadActive = True
        # tab=[ip, user,passw]
        url=""
        if(self.tab[1]!="" and self.tab[2]!=""):
            url = "rtsp://{}:{}@{}/h264_ulaw.sdp"
        else:
            url = f"rtsp://{self.tab[0]}/h264_ulaw.sdp"
        Capture = cv2.VideoCapture(-1 if self.tab[0]=="" else url)
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

class CameraWidget(QWidget):
    def __init__(self,tab):
        super().__init__()
        self.feed = QLabel()
        self.box = QHBoxLayout(self)
        self.box.addWidget(self.feed)
        self.loadFeed(tab)
        #self.feed.setStyleSheet("QWidget { background-color: %s }" % QColor(0, 0, 0).name())
    def ImageUpdateSlot(self, Image):
        self.feed.show()
        self.feed.setPixmap(QPixmap.fromImage(Image))
    def loadFeed(self,tab):
        self.Camera = Camera(tab)
        self.Camera.start()
        self.Camera.ImageUpdate.connect(self.ImageUpdateSlot)
# 10.85.158.158:8080