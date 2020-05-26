import os
from library.constants import *
from .dataset_objects import *


class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATASET = {
        PATH: os.path.join(BASE_DIR, 'data'),

        OBJECTS: [
            Rectangle,
            Pyramid,
        ],

        PICTURE_SIZE: (200, 200)
    }
