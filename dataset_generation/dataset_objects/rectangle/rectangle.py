import random
from math import pi
from ..dataset_object import DatasetObject
from library import *
from library import dist


class Rectangle(DatasetObject):
    def __init__(self, config_obj, **kwargs):
        super().__init__(config_obj, **kwargs)

    def create(self):
        self.center, self.size = self.__init_center_and_size()

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

        dots_centralized = []
        for dot in dots:
            dots_centralized.append(
                [
                    dot[0] - self.config[CENTER_INIT][0],
                    dot[1] - self.config[CENTER_INIT][1],
                    dot[2] - self.config[CENTER_INIT][2]
                ]
            )
        self.dots = dots_centralized
        self.created = True

    def rotate(self):
        def chose_angle_and_rotate(func, number):
            alpha = random.randint(0, self.config[ROTATE_ANGLES][number]) * pi / 180
            getattr(self, func)(alpha)

        chose_angle_and_rotate('_rotate_ox', 0)
        chose_angle_and_rotate('_rotate_oy', 1)
        chose_angle_and_rotate('_rotate_oz', 2)

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

    def save(self):
        pass

    def __find_further_dot(self):
        dot_further = (0, 0, 100000)

        dot_max, dist_max = self.dots[0], dist(self.dots[0], dot_further)
        for dot in self.dots[1:]:
            dist_current = dist(dot, dot_further)

            if dist_current > dist_max:
                dot_max = dot
                dist_max = dist_current

        return dot_max

    def __init_center_and_size(self):
        center = (
            self.config[CENTER_INIT][0] + random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            ),
            self.config[CENTER_INIT][1] + random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            ),
            self.config[CENTER_INIT][2] + random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            )
        )
        size = self.config[SIZE_INIT] + random.randint(-self.config[SIZE_RANDOMIZE],
                                                       self.config[SIZE_RANDOMIZE])

        return center, size
