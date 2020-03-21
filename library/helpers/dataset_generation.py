from math import sqrt
import random


def dist(a, b):
    return sqrt(sum([(x_a - x_b) ** 2 for x_a, x_b in zip(a, b)]))


def random_from_variable(variable):
    return random.randint(-variable, variable)
