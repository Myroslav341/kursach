import random
from math import cos, sin, sqrt, pi
from library.constants import *
from library.helpers import dist, function_for_curve_distance_generator


class DatasetObject:
    def __init__(self, config_obj, **kwargs):
        self.config = config_obj
        self.dots = []
        self.dots_projected = []
        self.created = False

        self.paint_obj = None
        self.further_dot = None
        self.further_dot_projected = None

    def create(self):
        pass

    def rotate(self):
        def chose_angle_and_rotate(func, number):
            alpha = random.randint(self.config[ROTATE_ANGLES][number][0],
                                   self.config[ROTATE_ANGLES][number][1]) * pi / 180
            func(alpha)

        chose_angle_and_rotate(self.rotate_ox, 0)
        chose_angle_and_rotate(self.rotate_oy, 1)
        chose_angle_and_rotate(self.rotate_oz, 2)

    def paint(self, paint_obj):
        self.paint_obj = paint_obj

        self.further_dot = self.__find_further_dot()
        self.further_dot_projected = [self.further_dot[0], self.further_dot[1]]

        dots_projected = []

        for dot in self.dots:
            dots_projected.append([dot[0], dot[1]])

        self.dots_projected = dots_projected

    def _is_line_is_dot(self, a, b) -> bool:
        pass

    def _draw_line(self, a, b, dot_line=False):
        def prepare_dot(dot):
            dot = dot.copy()
            for i in range(len(dot)):
                dot[i] += self.config[CENTER_INIT][i]
            return dot

        if self.paint_obj is None:
            raise AttributeError('paint_obj is not given')

        a = prepare_dot(a)
        b = prepare_dot(b)

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

    def _init_center_and_size(self):
        center = (
            random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            ),
            random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            ),
            random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            )
        )
        size = self.config[SIZE_INIT] + random.randint(-self.config[SIZE_RANDOMIZE],
                                                       self.config[SIZE_RANDOMIZE])

        return center, size

    def rotate_ox(self, alpha):
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

    def rotate_oy(self, alpha):
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

    def rotate_oz(self, alpha):
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

    def __paint_line(self, a, b):
        self.paint_obj.line([a[0], a[1], b[0], b[1]], width=5, fill='black')

    def __curve(self, dots_for_curve: list, q: int):
        dots_inside = dots_for_curve[1:-1]

        try:
            normal_x, normal_y = -q / (dots_for_curve[0][0] - dots_for_curve[-1][0]), \
                     q / (dots_for_curve[0][1] - dots_for_curve[-1][1])
        except ZeroDivisionError:
            return dots_for_curve

        normal_vector_length = sqrt(normal_x ** 2 + normal_y ** 2)

        dots_curved = []

        f_dist = function_for_curve_distance_generator(
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

    def __find_further_dot(self):
        dot_further = (0, 0, 100000)

        dot_max, dist_max = self.dots[0], dist(self.dots[0], dot_further)
        for dot in self.dots[1:]:
            dist_current = dist(dot, dot_further)

            if dist_current > dist_max:
                dot_max = dot
                dist_max = dist_current

        return dot_max
