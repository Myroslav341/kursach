from .dataset_objects import *


class Config:
    class DataSet:
        PATH = '../data/'
        OBJECTS = [
            Rectangle,
        ]
    PICTURE_SIZE = (200, 200)
