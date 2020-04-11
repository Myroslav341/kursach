from library.constants import *


class Rectangle:
    PATH_TO_DATASET = 'rect_'

    PATH_TO_CLASS = 'dataset_generation.dataset_objects.rectangle.rectangle'
    CLASS = 'Rectangle'

    GENERATION_CONFIG = {
        TRAIN_CNT: 2000,
        TEST_CNT: 100,

        CENTER_INIT: (100, 100, 100),
        CENTER_RANDOMIZE: 20,

        SIZE_INIT: 45,
        SIZE_RANDOMIZE: 10,

        DOT_RANDOMIZE: 3,

        ROTATE_ANGLES: (60, 60, 60),

        CURVES: (1, 2),
        CURVE_DISTANCE: 1.5,

        HATCH_SIZE: 4,
        HATCH_RANDOMIZE: 1
    }
