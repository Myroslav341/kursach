from library.constants import *


class Pyramid:
    PATH_TO_DATASET = 'pyramid_'

    PATH_TO_CLASS = 'dataset_generation.dataset_objects.pyramid.pyramid'
    CLASS = 'Pyramid'

    GENERATION_CONFIG = {
        TRAIN_CNT: 20,
        TEST_CNT: 0,

        CENTER_INIT: (100, 100, 100),
        CENTER_RANDOMIZE: 0,

        SIZE_INIT: 90,
        SIZE_RANDOMIZE: 0,

        DOT_RANDOMIZE: 0,

        ROTATE_ANGLES: ((20, 160), (20, 160), (20, 160)),

        CURVES: (1, 2),
        CURVE_DISTANCE: 0,

        HATCH_SIZE: 4,
        HATCH_RANDOMIZE: 0,
    }

    CREATION_CONFIG = {
        CENTER_INIT: (100, 100, 100),
        CENTER_RANDOMIZE: 0,

        SIZE_INIT: 120,
        SIZE_RANDOMIZE: 0,

        DOT_RANDOMIZE: 0,

        ROTATE_ANGLES: ((60, 60), (60, 60), (60, 60)),

        CURVES: (0, 0),
        CURVE_DISTANCE: 0,

        HATCH_SIZE: 4,
        HATCH_RANDOMIZE: 0,
    }
