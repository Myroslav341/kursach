from math import cos, sin, sqrt
from library import *
from library import dist
import random


class DatasetObject:
    def __init__(self, config_obj, **kwargs):
        self.config = config_obj
        self.dots = []
        self.created = False
        self.paint_obj = None
        self.further_dot = None

    def create(self):
        pass

    def rotate(self):
        pass

    def paint(self, paint_obj):
        self.paint_obj = paint_obj
        for dot in self.dots:
            dot[0] += self.config[CENTER_INIT][0]
            dot[1] += self.config[CENTER_INIT][1]
            dot[2] += self.config[CENTER_INIT][2]

    def save(self):
        pass

    def _draw_line(self, a, b):
        if self.paint_obj is None:
            raise AttributeError('paint_obj is not given')

        curves = random.randint(self.config[CURVES][0], self.config[CURVES][1])
        k_dots = curves * 15 + 2

        dots = [(a[0] + (b[0] - a[0]) / k_dots * (i + 1),
                 a[1] + (b[1] - a[1]) / k_dots * (i + 1)) for i in range(k_dots - 2)]

        dots = [a] + dots + [b]

        dots_curved = []
        q = random.choice([-1, 1])
        for i in range(curves):
            q *= -1
            first = (k_dots // curves) * i
            last = (k_dots // curves) * (i + 1)
            if i == curves - 1:
                dots_curved += self.__curve(dots[first:], q)[1:]
                break
            elif not i == 0:
                first -= 1
                dots_curved += self.__curve(dots[first:last], q)[1:]
            else:
                dots_curved += self.__curve(dots[first:last], q)

        dot_line = False
        if self.further_dot is not None and (self.further_dot == list(a) or self.further_dot == list(b)):
            dot_line = True

        cnt, hatch_size = 0, 0
        paint = True
        for i in range(len(dots_curved) - 1):
            if not dot_line:
                self.__paint_line(dots_curved[i], dots_curved[i + 1])
                continue
            if cnt == 0:
                hatch_size = self.config[HATCH_SIZE] + random.randint(-self.config[HATCH_RANDOMIZE],
                                                                      self.config[HATCH_RANDOMIZE])
            elif cnt == hatch_size:
                cnt = -1
                paint = not paint
            if paint:
                self.__paint_line(dots_curved[i], dots_curved[i + 1])
            cnt += 1

    def __paint_line(self, a, b):
        self.paint_obj.line([a[0], a[1], b[0], b[1]], width=5, fill=128)

    def __curve(self, dots_for_curve: list, q: int):
        dots_inside = dots_for_curve[1:-1]
        try:
            normal_x, normal_y = -q / (dots_for_curve[0][0] - dots_for_curve[-1][0]), \
                     q / (dots_for_curve[0][1] - dots_for_curve[-1][1])
        except ZeroDivisionError:
            return dots_for_curve
        normal_vector_length = sqrt(normal_x ** 2 + normal_y ** 2)
        dots_curved = []
        f_dist = self.__function_for_curve_distance_generator(
            dist(dots_for_curve[0], dots_for_curve[-1])
        )
        for x in dots_inside:
            dist_coefficient = f_dist(dist(dots_for_curve[0], x))
            distance = self.config[CURVE_DISTANCE] * dist_coefficient
            dot_new = (x[0] + distance / normal_vector_length * normal_x,
                       x[1] + distance / normal_vector_length * normal_y)
            dots_curved.append(dot_new)
        dots_curved = [dots_for_curve[0]] + dots_curved + [dots_for_curve[-1]]
        return dots_curved

    @staticmethod
    def __function_for_curve_distance_generator(max_dist):
        a_curve = -4 / max_dist ** 2
        b_curve = 4 / max_dist

        def f(x):
            return a_curve * x ** 2 + b_curve * x

        return f

    def _rotate_ox(self, alpha):
        dots_new = []
        for dot in self.dots:
            dots_new.append(
                [
                    dot[0],
                    dot[1] * cos(alpha) - dot[2] * sin(alpha),
                    dot[1] * sin(alpha) + dot[2] * cos(alpha)
                ]
            )
        self.dots = dots_new

    def _rotate_oy(self, alpha):
        dots_new = []
        for dot in self.dots:
            dots_new.append(
                [
                    dot[0] * cos(alpha) + dot[2] * sin(alpha),
                    dot[1],
                    -dot[0] * sin(alpha) + dot[2] * cos(alpha)
                ]
            )
        self.dots = dots_new

    def _rotate_oz(self, alpha):
        dots_new = []
        for dot in self.dots:
            dots_new.append(
                [
                    dot[0] * cos(alpha) - dot[1] * sin(alpha),
                    dot[0] * sin(alpha) + dot[1] * cos(alpha),
                    dot[2]
                ]
            )
        self.dots = dots_new
