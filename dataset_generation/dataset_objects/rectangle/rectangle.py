import random
from ..dataset_object import DatasetObject


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
                a, b = self.dots[i], self.dots[i + 1 + step]
                self._draw_line(a, b, self._is_line_is_dot(a, b))

        super().paint(paint_obj)

        paint_lines(0, 3)
        self._draw_line(self.dots[0], self.dots[3], self._is_line_is_dot(self.dots[0], self.dots[3]))

        paint_lines(4, 7)
        self._draw_line(self.dots[4], self.dots[7], self._is_line_is_dot(self.dots[4], self.dots[7]))

        paint_lines(0, 4, 3)

    def _is_line_is_dot(self, a, b):
        if self.further_dot is not None and (self.further_dot == list(a) or self.further_dot == list(b)):
            return True

        return False
