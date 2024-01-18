import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.uic import loadUi
from AddCamera import AddCameraDialog
from camera import CameraWidget
import os
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        path = os.path.dirname(__file__) +"/HomeUi.ui"
        loadUi(path, self)
        self.dictDesCameras=dict()
        self.grid = QGridLayout(self.Cameras)

        #self.FeedLabel = QLabel()

        #self.CancelBTN = QPushButton("Cancel")
        self.RemoveCamera.clicked.connect(self.CancelFeed)
        self.AddCamera.clicked.connect(self.popupg)
    def popup(self):
        
        dlg = AddCameraDialog(self.dictDesCameras)
        if dlg.exec():
            #print("Success!")
            #print(self.dictDesCameras)
            self.loadCamera()
        else:
            print("Cancel!")

    def loadCamera(self):
        self.grid.addWidget(CameraWidget(self.dictDesCameras[len(self.dictDesCameras)-1]))
        

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
    Root.show()
    sys.exit(App.exec())