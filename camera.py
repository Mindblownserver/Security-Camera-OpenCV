from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout
from ultralytics import YOLO
import cv2
class Camera(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def __init__(self, tab,x,y):
        super().__init__()
        self.tab = tab
        self.x=x
        self.y=y
    def run(self):
        self.ThreadActive = True
        # tab=[ip, user,passw]
        # Stream selection
        url=""
        if(self.tab[1]!="" and self.tab[2]!=""):
            url = "rtsp://{}:{}@{}/h264_ulaw.sdp"
        else:
            url = f"rtsp://{self.tab[0]}/h264_ulaw.sdp"
        Capture = cv2.VideoCapture(-1 if self.tab[0]=="" else url)
        # Ensure that the video feed program works in a different Thread
        while self.ThreadActive:
            #start of Video Feed code
            ret, frame = Capture.read()
            if ret:
                """ # here the magic starts
                ## declare variables & model
                model = YOLO("./License_detector.pt")  # load a custom model
                threshold = 0.5
                results = model(frame)[0]
                ## Get Results from model
                for result in results.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = result
                    ## put the results in frame
                    if score > threshold:
                        print("DETECTED THE MOTHERFLIPPER\tFOUND\nDETECTED\n")
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 4)
                        cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA) """
                ## put the 'frame' in PyQt5
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(self.x, self.y,aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

class CameraWidget(QWidget):
    def __init__(self,tab,x,y):
        super().__init__()
        self.box = QHBoxLayout(self)
        self.feed = QLabel()
        self.box.addWidget(self.feed)
        self.loadFeed(tab,x,y)
        #self.feed.setStyleSheet("QWidget { background-color: %s }" % QColor(0, 0, 0).name())
    def ImageUpdateSlot(self, Image):
        self.feed.show()
        self.feed.setPixmap(QPixmap.fromImage(Image))
    def loadFeed(self,tab,x,y):
        self.Camera = Camera(tab,x,y)
        self.Camera.start()
        self.Camera.ImageUpdate.connect(self.ImageUpdateSlot)
# 10.85.158.158:8080