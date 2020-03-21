import random
from math import sqrt
from ..dataset_object import DatasetObject
from library.constants import *
from library.helpers import dist, random_from_variable as _


class Pyramid(DatasetObject):
    def __init__(self, config_obj, **kwargs):
        super().__init__(config_obj, **kwargs)

    def create(self):
        self.center, self.size = self._init_center_and_size()


        dots = [
            (self.center[0] - 3 * self.size / 4 + _(self.config[DOT_RANDOMIZE]),
             self.center[1] - self.size * sqrt(3) / 4 + _(self.config[DOT_RANDOMIZE]),
             self.center[2] - self.size / 2 + _(self.config[DOT_RANDOMIZE])),

            (self.center[0] + _(self.config[DOT_RANDOMIZE]),
             self.center[1] + self.size * sqrt(3) / 2 + _(self.config[DOT_RANDOMIZE]),
             self.center[2] - self.size / 2 + _(self.config[DOT_RANDOMIZE])),

            (self.center[0] + self.size * 3 / 4 + _(self.config[DOT_RANDOMIZE]),
             self.center[1] - self.size * sqrt(3) / 4 + _(self.config[DOT_RANDOMIZE]),
             self.center[2] - self.size / 2 + _(self.config[DOT_RANDOMIZE])),

            (self.center[0] + _(self.config[DOT_RANDOMIZE]),
             self.center[1] + _(self.config[DOT_RANDOMIZE]),
             self.center[2] + self.size + _(self.config[DOT_RANDOMIZE])),
        ]

        self.dots = dots
        self.created = True

    def paint(self, paint_obj):
        super().paint(paint_obj)

        self._draw_line(self.dots[0], self.dots[1])
        self._draw_line(self.dots[0], self.dots[3])

        self._draw_line(self.dots[1], self.dots[2])
        self._draw_line(self.dots[1], self.dots[3])

        self._draw_line(self.dots[2], self.dots[0])
        self._draw_line(self.dots[2], self.dots[3])

        # def paint_lines(start, end, step=0):
        #     for i in range(start, end):
        #         self._draw_line(self.dots[i], self.dots[i + 1 + step])
        #
        # super().paint(paint_obj)
        #
        # # self.further_dot = self.__find_further_dot()
        #
        # paint_lines(0, 3)
        # self._draw_line(self.dots[0], self.dots[3])
        #
        # paint_lines(4, 7)
        # self._draw_line(self.dots[4], self.dots[7])
        #
        # paint_lines(0, 4, 3)
