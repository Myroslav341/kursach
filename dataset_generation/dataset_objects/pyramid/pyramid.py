import itertools
from math import sqrt
from ..dataset_object import DatasetObject
from library.constants import *
from library.exceptions import FurtherDotMissed
from library.helpers import random_from_variable as _, is_dot_inside_triangle, dist, angle


class Pyramid(DatasetObject):
    def __init__(self, config_obj, **kwargs):
        self.ok = True
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

        dots = [list(dots) for dots in list(itertools.combinations(self.dots_projected, 2))]
        for x in dots:
            if dist(x[0], x[1]) < 20:
                self.ok = False

        if paint_obj is None:
            return

        self._draw_line(self.dots[0], self.dots[1], self._is_line_is_dot(self.dots[0], self.dots[1]))
        self._draw_line(self.dots[0], self.dots[3], self._is_line_is_dot(self.dots[0], self.dots[3]))

        self._draw_line(self.dots[1], self.dots[2], self._is_line_is_dot(self.dots[1], self.dots[2]))
        self._draw_line(self.dots[1], self.dots[3], self._is_line_is_dot(self.dots[1], self.dots[3]))

        self._draw_line(self.dots[2], self.dots[0], self._is_line_is_dot(self.dots[2], self.dots[0]))
        self._draw_line(self.dots[2], self.dots[3], self._is_line_is_dot(self.dots[2], self.dots[3]))

    def _is_line_is_dot(self, a, b) -> bool:
        if self.further_dot is None:
            raise FurtherDotMissed

        triangle_dots = [list(dots) for dots in list(itertools.combinations(self.dots_projected, 3))]

        inside = False
        dot_inside = []

        for dots in triangle_dots:
            dot_check = [dot for dot in self.dots_projected if dot not in dots][0]
            if is_dot_inside_triangle(dot_check, dots):
                inside = True
                dot_inside = self.dots[self.dots_projected.index(dot_check)]
                break

        if inside:
            dots_on_plane = [dot for dot in self.dots if not dot == dot_inside]

            dot_on_plane = [
                (dots_on_plane[0][0] + dots_on_plane[1][0] + dots_on_plane[2][0]) / 3,
                (dots_on_plane[0][1] + dots_on_plane[1][1] + dots_on_plane[2][1]) / 3,
                (dots_on_plane[0][2] + dots_on_plane[1][2] + dots_on_plane[2][2]) / 3
            ]
            distant_dot = [0, 0, 10000000]

            dist_to_plane = dist(distant_dot, dot_on_plane)
            dist_to_further_dot = dist(dot_inside, distant_dot)

            if dist_to_further_dot > dist_to_plane:
                if list(a) == dot_inside or list(b) == dot_inside:
                    return True

        else:
            triangle_dots = [dot for dot in self.dots_projected if not dot == self.further_dot_projected]

            triangle_dots_pairs = [list(dots) for dots in itertools.combinations(triangle_dots, 2)]

            angles = [angle(self.further_dot_projected, dots) for dots in triangle_dots_pairs]
            angle_max = max(angles)

            dots_can_see = triangle_dots_pairs[angles.index(angle_max)]

            for dot in triangle_dots:
                if dot in dots_can_see:
                    continue

                if ([a[0], a[1]] == dot and [b[0], b[1]] == self.further_dot_projected) or \
                        ([a[0], a[1]] == self.further_dot_projected and [b[0], b[1]] == dot):
                    return True

        return False
