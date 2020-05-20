import random
from math import pi
from string import ascii_lowercase
from config import Config
from PyQt5.QtGui import QPainter, QImage, QPen, QColor
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QFileDialog
from .ui import PaintUI
from dataset_generation.dataset_objects import Rectangle as RectangleObject
from dataset_generation.dataset_objects import Pyramid as PyramidObject
from config.dataset_objects import Rectangle, Pyramid


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

        self.mode_paint = True
        self.center = (180, 180, 200)
        self.alpha = 2 * pi / 180

    def predict(self):
        path = self.save()
        r = self.model.predict(path)
        self.textEdit.setText(str(r[0][0]))
        self.textEdit_2.setText(str(r[0][1]))

        if r[0][0] > r[0][1]:
            self.create_cube()

        if r[0][0] < r[0][1]:
            self.create_pyramid()

        self.mode_paint = False
        self.update()

    def create_cube(self):
        self.object = RectangleObject(Rectangle.CREATION_CONFIG)
        self.object.create()
        self.paint_order = [[0, 1], [1, 2], [2, 3], [0, 3], [4, 5], [5, 6], [6, 7], [4, 7],
                            [0, 4], [1, 5], [2, 6], [3, 7]]

    def create_pyramid(self):
        self.object = PyramidObject(Pyramid.CREATION_CONFIG)
        self.object.create()
        self.paint_order = [[0, 1], [1, 2], [0, 2], [0, 3], [1, 3], [2, 3]]

    def clear(self):
        self.image.fill(Qt.white)
        self.object = None
        self.mode_paint = True
        self.textEdit.setText('')
        self.textEdit_2.setText('')

        self.update()

    def paintEvent(self, event):
        def draw_line():
            if self.object._is_line_is_dot(self.object.dots[a], self.object.dots[b]):
                self.myLineColor.setRgb(255, 0, 0)
                qp.setPen(self.myLineColor)
                qp.drawLine(QPoint(dots_[a][0], dots_[a][1]), QPoint(dots_[b][0], dots_[b][1]))
            else:
                self.myLineColor.setRgb(0, 0, 0)
                qp.setPen(self.myLineColor)
                qp.drawLine(QPoint(dots_[a][0], dots_[a][1]), QPoint(dots_[b][0], dots_[b][1]))

        if self.mode_paint:
            canvasPainter = QPainter(self)
            canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
            return

        qp = QPainter()
        qp.begin(self)

        dots_ = []
        for dot in self.object.dots:
            dots_.append([dot[0] + self.center[0], dot[1] + self.center[1], dot[2] + self.center[2]])

        self.myLineColor = QColor()
        self.myLineColor.setRgb(0, 0, 0)
        qp.setPen(self.myLineColor)

        self.object.paint(None)

        for a, b in self.paint_order:
            draw_line()

        qp.end()

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
        if e.key() == Qt.Key_J:
            self.object.rotate_oy(-self.alpha)
        if e.key() == Qt.Key_L:
            self.object.rotate_oy(self.alpha)
        if e.key() == Qt.Key_I:
            self.object.rotate_ox(-self.alpha)
        if e.key() == Qt.Key_K:
            self.object.rotate_ox(self.alpha)
        if e.key() == Qt.Key_A:
            self.object.rotate_oz(-self.alpha)
        if e.key() == Qt.Key_D:
            self.object.rotate_oz(self.alpha)
        self.update()

    def paint(self):
        pass
