from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import os
class AddCameraDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        path = os.path.dirname(__file__) + "/"
        uic.loadUi(path+'AddCamera.ui', self)
        self.AddBtn.clicked.connect(self.add)
    def add(self):
        usr = self.username.text()
        passw=self.password.text()
        ip = self.CameraIp.text()
        