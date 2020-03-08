import importlib
from library import CNT


class DataSet:
    def __init__(self, config_obj):
        self.config = config_obj

    def create(self):
        for dataset_object_config in self.config.OBJECTS:
            object_class = getattr(
                importlib.import_module(dataset_object_config.PATH_TO_CLASS),
                dataset_object_config.CLASS
            )
            for _ in range(dataset_object_config.GENERATION_CONFIG[CNT]):
                rect = object_class(dataset_object_config.GENERATION_CONFIG)
                rect.create()
