from math import sqrt


def dist(a, b):
    return sqrt(sum([(x_a - x_b) ** 2 for x_a, x_b in zip(a, b)]))
