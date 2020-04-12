import itertools

from library.constants import *
from library.helpers import random_from_variable as _
from ..dataset_object import DatasetObject


class Rectangle(DatasetObject):
    def __init__(self, config_obj, **kwargs):
        self.ok = True
        super().__init__(config_obj, **kwargs)

    def create(self):
        self.center, self.size = self._init_center_and_size()

        dots = [(self.center[0] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] - self.size + _(self.config[DOT_RANDOMIZE])),

                (self.center[0] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] - self.size + _(self.config[DOT_RANDOMIZE])),

                (self.center[0] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] - self.size + _(self.config[DOT_RANDOMIZE])),

                (self.center[0] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] - self.size + _(self.config[DOT_RANDOMIZE])),

                (self.center[0] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] + self.size + _(self.config[DOT_RANDOMIZE])),

                (self.center[0] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] + self.size + _(self.config[DOT_RANDOMIZE])),

                (self.center[0] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] + self.size + _(self.config[DOT_RANDOMIZE])),

                (self.center[0] - self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[1] + self.size + _(self.config[DOT_RANDOMIZE]),
                 self.center[2] + self.size + _(self.config[DOT_RANDOMIZE]))
                ]

        self.dots = dots
        self.created = True

    def paint(self, paint_obj):
        def paint_lines(start, end, step=0):
            for i in range(start, end):
                a, b = self.dots[i], self.dots[i + 1 + step]
                self._draw_line(a, b, self._is_line_is_dot(a, b))

        super().paint(paint_obj)

        from library.helpers import dist

        dots = [list(dots) for dots in list(itertools.combinations(self.dots_projected, 2))]
        for x in dots:
            if dist(x[0], x[1]) < 20:
                self.ok = False

        paint_lines(0, 3)
        self._draw_line(self.dots[0], self.dots[3], self._is_line_is_dot(self.dots[0], self.dots[3]))

        paint_lines(4, 7)
        self._draw_line(self.dots[4], self.dots[7], self._is_line_is_dot(self.dots[4], self.dots[7]))

        paint_lines(0, 4, 3)

    def _is_line_is_dot(self, a, b):
        if self.further_dot is not None and (self.further_dot == list(a) or self.further_dot == list(b)):
            return True

        return False
