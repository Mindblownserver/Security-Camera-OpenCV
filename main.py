import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from AddCamera import AddCameraDialog
from camera import CameraWidget
import os
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        path = os.path.dirname(__file__) +"/HomeUi1.ui"
        loadUi(path, self)
        self.dictDesCameras=dict()
        #self.grid = QGridLayout(self.Cameras)
        #self.FeedLabel = QLabel()

        #self.CancelBTN = QPushButton("Cancel")
        self.RemoveCamera.clicked.connect(self.CancelFeed)
        self.AddCamera.clicked.connect(self.popup)
    def popup(self):
        
        dlg = AddCameraDialog(self.dictDesCameras)
        if dlg.exec():
            #print("Success!")
            #print(self.dictDesCameras)
            self.loadCamera()
        else:
            print("Cancel!")

    def loadCamera(self):
        num = len(self.dictDesCameras)
        x= self.Cameras.size().width()
        y=self.Cameras.size().height()
        print(x,y)
        #refresh Layout(resize children of layout to in order to add one more child)
        self.gridLayout.addWidget(CameraWidget(self.dictDesCameras[num-1], x,y),0,0,1,1,alignment=Qt.AlignmentFlag.AlignCenter)
        

    def CancelFeed(self):
        self.Camera.stop()
"""
IF YOU WANT TO DISPLAY YOUR CAM, MAKE DAMN SURE YOUR STUPID SELF.CAMERAS FRAME HAS NO LAYOUT
I FLIPPING WASTED HALF AN HOUR EVERY FRICKING DAY FOR THE SAME DAMN REASON
GOD I WISH I LEARNT FROM MY LESSON, BUT NOOOOOO, I DID NOTTTT!!!!!
- YOURS TRULY, MEEEE, AUGH!!
"""


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()

    Root.showMaximized()
    sys.exit(App.exec())