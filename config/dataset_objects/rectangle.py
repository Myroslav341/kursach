from library.constants import *


class Rectangle:
    PATH_TO_DATASET = 'rect_'

    PATH_TO_CLASS = 'dataset_generation.dataset_objects.rectangle.rectangle'
    CLASS = 'Rectangle'

    GENERATION_CONFIG = {
        TRAIN_CNT: 20,
        TEST_CNT: 0,

        CENTER_INIT: (100, 100, 100),
        CENTER_RANDOMIZE: 20,

        SIZE_INIT: 45,
        SIZE_RANDOMIZE: 10,

        DOT_RANDOMIZE: 3,

        ROTATE_ANGLES: ((20, 60), (20, 60), (20, 60)),

        CURVES: (1, 2),
        CURVE_DISTANCE: 1.5,

        HATCH_SIZE: 4,
        HATCH_RANDOMIZE: 1,
    }

    CREATION_CONFIG = {
        CENTER_INIT: (100, 100, 100),
        CENTER_RANDOMIZE: 0,

        SIZE_INIT: 70,
        SIZE_RANDOMIZE: 0,

        DOT_RANDOMIZE: 0,

        ROTATE_ANGLES: ((60, 60), (60, 60), (60, 60)),

        CURVES: (0, 0),
        CURVE_DISTANCE: 0,

        HATCH_SIZE: 4,
        HATCH_RANDOMIZE: 0,
    }
