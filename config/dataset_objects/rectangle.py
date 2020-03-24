from library.constants import *


class Rectangle:
    PATH_TO_DATASET = '/rect/'
    PATH_TO_CLASS = 'dataset_generation.dataset_objects.rectangle.rectangle'
    CLASS = 'Rectangle'
    GENERATION_CONFIG = {
        CNT: 100,

        CENTER_INIT: (100, 100, 100),
        CENTER_RANDOMIZE: 20,

        SIZE_INIT: 40,
        SIZE_RANDOMIZE: 10,

        DOT_RANDOMIZE: 5,

        ROTATE_ANGLES: (360, 360, 360),

        CURVES: (1, 2),
        CURVE_DISTANCE: 1.5,

        HATCH_SIZE: 4,
        HATCH_RANDOMIZE: 1
    }
