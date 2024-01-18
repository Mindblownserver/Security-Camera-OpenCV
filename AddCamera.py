from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import os
class AddCameraDialog(QDialog):
    def __init__(self, dictDesCameras):
        super().__init__()
        
        path = os.path.dirname(__file__) + "/"
        uic.loadUi(path+'AddCamera.ui', self)
        self.AddBtn.clicked.connect(lambda x: self.add(dictDesCameras))
    def add(self,dictDesCameras):
        usr = self.username.text()
        passw=self.password.text()
        ip = self.CameraIp.text()
        dictDesCameras[len(dictDesCameras)] = [ip,usr,passw]
        self.done(1)