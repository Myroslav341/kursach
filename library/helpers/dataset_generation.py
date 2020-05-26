from math import sqrt, pi, acos
import random
import itertools


def dist(a, b):
    return sqrt(sum([(x_a - x_b) ** 2 for x_a, x_b in zip(a, b)]))


def random_from_variable(variable):
    return random.randint(-variable, variable)


def function_for_curve_distance_generator(max_dist):
    a_curve = -4 / max_dist ** 2
    b_curve = 4 / max_dist

    def f(x):
        return a_curve * x ** 2 + b_curve * x

    return f


def is_dot_inside_triangle(dot, triangle_dots) -> bool:
    triangles = [[pair[0], pair[1], dot] for pair in list(itertools.combinations(triangle_dots, 2))]

    sum_triangles_square = sum([triangle_square(dots) for dots in triangles])
    main_triangle_square = triangle_square(triangle_dots)

    return abs(sum_triangles_square - main_triangle_square) < 1


def triangle_square(dots):
    if not len(dots) == 3:
        raise AttributeError('dots count must be 3')

    d = [dist(dots[i], dots[i - 1]) for i in range(len(dots))]

    p = sum(d) / 2

    return sqrt(p * (p - d[0]) * (p - d[1]) * (p - d[2]))


def angle(dot, dots: list) -> float:
    if not len(dots) == 2:
        raise AttributeError('dots count must be 2')

    a, b, c = dist(dots[0], dots[1]), dist(dot, dots[0]), dist(dot, dots[1])

    return acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180 / pi
