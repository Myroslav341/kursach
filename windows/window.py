import random
from string import ascii_lowercase
from config import Config
from PyQt5.QtGui import QPainter, QImage, QPen
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from .ui import PaintUI


class AppWindow(QtWidgets.QMainWindow, PaintUI):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setupUi(self)
        self.lastPoint = None
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.actionsave.triggered.connect(self.save)
        self.actionclear.triggered.connect(self.clear)
        self.pushButton.clicked.connect(self.predict)

    def predict(self):
        path = self.save()
        r = self.model.predict(path)
        self.textEdit.setText(str(r[0][0]))
        self.textEdit_2.setText(str(r[0][1]))

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, 7, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def save(self, path=None):
        if path is not None:
            path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                      "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

            if path == "":
                return
            self.image.save(path)
        else:
            name = ''.join([random.choice(ascii_lowercase) for _ in range(8)]) + '.png'
            self.image.save(Config.BASE_DIR + '/tests/' + name)
            return Config.BASE_DIR + '/tests/' + name

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Left:
            self.object.rotate_oy(-self.alpha)
        if e.key() == Qt.Key_Right:
            self.object.rotate_oy(self.alpha)
        if e.key() == Qt.Key_Up:
            self.object.rotate_ox(-self.alpha)
        if e.key() == Qt.Key_Down:
            self.object.rotate_ox(self.alpha)
        if e.key() == Qt.Key_A:
            self.object.rotate_oz(-self.alpha)
        if e.key() == Qt.Key_D:
            self.object.rotate_oz(self.alpha)
        self.update()

    def paint(self):
        pass
