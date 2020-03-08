from library import *


class Rectangle:
    PATH_TO_DATASET = '/rect/'
    PATH_TO_CLASS = 'dataset_generation.dataset_objects.rectangle.rectangle'
    CLASS = 'Rectangle'
    GENERATION_CONFIG = {
        CNT: 1000,
        CENTER_INIT: (100, 100, 100),
        SIZE_INIT: 70,
        CENTER_RANDOMIZE: 20,
        DOT_RANDOMIZE: 5,
        SIZE_RANDOMIZE: 20,
    }
