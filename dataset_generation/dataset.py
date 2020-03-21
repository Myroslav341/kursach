import importlib
from library.constants import CNT
from PIL import Image, ImageDraw


class DataSet:
    def __init__(self, config_obj):
        self.config = config_obj

    def create(self):
        for dataset_object_config in self.config.OBJECTS:
            object_class = getattr(
                importlib.import_module(dataset_object_config.PATH_TO_CLASS),
                dataset_object_config.CLASS
            )
            for i in range(dataset_object_config.GENERATION_CONFIG[CNT]):
                dataset_object = object_class(dataset_object_config.GENERATION_CONFIG)

                im = Image.new('RGB', (200, 200), color='red')
                draw = ImageDraw.Draw(im)

                dataset_object.create()
                dataset_object.rotate()
                dataset_object.paint(draw)

                del draw

                im.save(self.config.PATH + dataset_object_config.PATH_TO_DATASET + f'{i}.png')
