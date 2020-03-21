import random
from ..dataset_object import DatasetObject
from library.constants import *
from library.helpers import dist


# todo random dot not 5
class Rectangle(DatasetObject):
    def __init__(self, config_obj, **kwargs):
        super().__init__(config_obj, **kwargs)

    def create(self):
        self.center, self.size = self._init_center_and_size()

        dots = [(self.center[0] - self.size + random.randint(-5, 5), self.center[1] - self.size + random.randint(-5, 5),
                 self.center[2] - self.size + random.randint(-5, 5)),
                (self.center[0] + self.size + random.randint(-5, 5), self.center[1] - self.size + random.randint(-5, 5),
                 self.center[2] - self.size + random.randint(-5, 5)),
                (self.center[0] + self.size + random.randint(-5, 5), self.center[1] + self.size + random.randint(-5, 5),
                 self.center[2] - self.size + random.randint(-5, 5)),
                (self.center[0] - self.size + random.randint(-5, 5), self.center[1] + self.size + random.randint(-5, 5),
                 self.center[2] - self.size + random.randint(-5, 5)),
                (self.center[0] - self.size + random.randint(-5, 5), self.center[1] - self.size + random.randint(-5, 5),
                 self.center[2] + self.size + random.randint(-5, 5)),
                (self.center[0] + self.size + random.randint(-5, 5), self.center[1] - self.size + random.randint(-5, 5),
                 self.center[2] + self.size + random.randint(-5, 5)),
                (self.center[0] + self.size + random.randint(-5, 5), self.center[1] + self.size + random.randint(-5, 5),
                 self.center[2] + self.size + random.randint(-5, 5)),
                (self.center[0] - self.size + random.randint(-5, 5), self.center[1] + self.size + random.randint(-5, 5),
                 self.center[2] + self.size + random.randint(-5, 5))
                ]

        self.dots = dots
        self.created = True

    def paint(self, paint_obj):
        def paint_lines(start, end, step=0):
            for i in range(start, end):
                self._draw_line(self.dots[i], self.dots[i + 1 + step])

        super().paint(paint_obj)

        self.further_dot = self.__find_further_dot()

        paint_lines(0, 3)
        self._draw_line(self.dots[0], self.dots[3])

        paint_lines(4, 7)
        self._draw_line(self.dots[4], self.dots[7])

        paint_lines(0, 4, 3)

    def __find_further_dot(self):
        dot_further = (0, 0, 100000)

        dot_max, dist_max = self.dots[0], dist(self.dots[0], dot_further)
        for dot in self.dots[1:]:
            dist_current = dist(dot, dot_further)

            if dist_current > dist_max:
                dot_max = dot
                dist_max = dist_current

        return dot_max
