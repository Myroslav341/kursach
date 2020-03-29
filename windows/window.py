from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, pyqtSlot, QRect
from .ui.main_window import Ui_MainWindow
from math import sin, cos, pi
from dataset_generation.dataset_objects.dataset_object import DatasetObject


class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, object: DatasetObject):
        super().__init__()
        self.setupUi(self)
        self.alpha = 2 * pi / 180
        self.center = (200, 200, 200)
        self.object = object

    def paintEvent(self, e):
        def draw_line(a, b):
            if self.object._is_line_is_dot(self.object.dots[a], self.object.dots[b]):
                self.myLineColor.setRgb(255, 0, 0)
                qp.setPen(self.myLineColor)
                qp.drawLine(QPoint(dots_[a][0], dots_[a][1]), QPoint(dots_[b][0], dots_[b][1]))
            else:
                self.myLineColor.setRgb(0, 0, 0)
                qp.setPen(self.myLineColor)
                qp.drawLine(QPoint(dots_[a][0], dots_[a][1]), QPoint(dots_[b][0], dots_[b][1]))

        qp = QPainter()
        qp.begin(self)

        dots_ = []
        for dot in self.object.dots:
            dots_.append([dot[0] + self.center[0], dot[1] + self.center[1], dot[2] + self.center[2]])

        self.myLineColor = QColor()
        self.myLineColor.setRgb(0, 0, 0)
        qp.setPen(self.myLineColor)

        self.object.paint(None)


        draw_line(0, 1)
        draw_line(0, 3)

        draw_line(1, 2)
        draw_line(1, 3)

        draw_line(2, 0)
        draw_line(2, 3)

        qp.drawEllipse(self.object.further_dot_projected[0] - 5 + self.center[0], self.object.further_dot_projected[1] - 5 + self.center[1], 10, 10)
        # qp.drawLine(QPoint(dots_[0][0], dots_[0][1]), QPoint(dots_[3][0], dots_[3][1]))
        #
        # qp.drawLine(QPoint(dots_[1][0], dots_[1][1]), QPoint(dots_[2][0], dots_[2][1]))
        # qp.drawLine(QPoint(dots_[1][0], dots_[1][1]), QPoint(dots_[3][0], dots_[3][1]))
        #
        # qp.drawLine(QPoint(dots_[2][0], dots_[2][1]), QPoint(dots_[0][0], dots_[0][1]))
        # qp.drawLine(QPoint(dots_[2][0], dots_[2][1]), QPoint(dots_[3][0], dots_[3][1]))

        qp.end()

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

    def rotate_OX(self, alpha):
        dots = []
        for dot in self.dots:
            dots.append([dot[0], dot[1] * cos(alpha) - dot[2] * sin(alpha), dot[1] * sin(alpha) + dot[2] * cos(alpha)])
        self.dots = dots

    def rotate_OY(self, alpha):
        dots = []
        for dot in self.dots:
            dots.append([dot[0] * cos(alpha) + dot[2] * sin(alpha), dot[1], -dot[0] * sin(alpha) + dot[2] * cos(alpha)])
        self.dots = dots

    def rotate_OZ(self, alpha):
        dots = []
        for dot in self.dots:
            dots.append([dot[0] * cos(alpha) - dot[1] * sin(alpha), dot[0] * sin(alpha) + dot[1] * cos(alpha), dot[2]])
        self.dots = dots

    def paint(self):
        pass
