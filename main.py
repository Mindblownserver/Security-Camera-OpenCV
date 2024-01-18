import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QHBoxLayout
from PyQt5.uic import loadUi
from AddCamera import AddCameraDialog
from camera import CameraWidget
import os
from camera import *

""" class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)

        # Create a QLabel to be housed in the custom widget
        self.label = QLabel('Hello from CustomWidget')

        # Set up the layout for the custom widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()

        # Create an instance of the custom widget
        custom_widget = CustomWidget()

        # Create other widgets for the main widget
        button = QPushButton('Click Me')

        # Set up the layout for the main widget
        layout = QVBoxLayout(self)
        layout.addWidget(custom_widget)
        layout.addWidget(button) """
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        path = os.path.dirname(__file__) +"/HomeUi.ui"
        loadUi(path, self)
        self.grid = QGridLayout(self.Cameras)
        #self.FeedLabel = QLabel()

        #self.CancelBTN = QPushButton("Cancel")
        self.RemoveCamera.clicked.connect(self.CancelFeed)
        self.AddCamera.clicked.connect(self.popup)
    def popup(self):
        
        dlg = AddCameraDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")


    def ImageUpdateSlot(self, Image):
        label = QLabel()
        label.setParent(self.Cameras)
        label.show()
        label.setPixmap(QPixmap.fromImage(Image))


    def loadCamera(self):
        t = CameraWidget()
        self.grid.addWidget(t)
        

    def CancelFeed(self):
        self.Camera.stop()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())