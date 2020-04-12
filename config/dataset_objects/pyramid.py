from library.constants import *


class Pyramid:
    PATH_TO_DATASET = 'pyramid_'

    PATH_TO_CLASS = 'dataset_generation.dataset_objects.pyramid.pyramid'
    CLASS = 'Pyramid'

    GENERATION_CONFIG = {
        TRAIN_CNT: 2000,
        TEST_CNT: 100,

        CENTER_INIT: (100, 100, 100),
        CENTER_RANDOMIZE: 15,

        SIZE_INIT: 90,
        SIZE_RANDOMIZE: 10,

        DOT_RANDOMIZE: 5,

        # ROTATE_ANGLES: (360, 360, 360),
        ROTATE_ANGLES: ((0, 360), (0, 360), (0, 360)),

        CURVES: (1, 2),
        CURVE_DISTANCE: 1.5,

        HATCH_SIZE: 4,
        HATCH_RANDOMIZE: 1
    }
