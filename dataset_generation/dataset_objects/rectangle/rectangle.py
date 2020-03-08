import random
from ..dataset_object import DatasetObject
from library import *
from config import Config


class Rectangle(DatasetObject):
    def __init__(self, config_obj):
        self.config = config_obj

    def create(self):
        self.center, self.size = self.init_center_and_size()

        dots = []
        sign_x = 1
        for _ in range(2):
            sign_x *= -1
            sign_y = 1
            x = self.center[0] + self.size * sign_x
            for _ in range(2):
                sign_y *= -1
                sign_y = 1
                y = self.center[1] + self.size * sign_y
                for _ in range(2):
                    sign_y *= -1
                    z = self.center[2] + self.size * sign_y
                    dots.append(
                        (
                            x + random.randint(-self.config[DOT_RANDOMIZE], self.config[DOT_RANDOMIZE]),
                            y + random.randint(-self.config[DOT_RANDOMIZE], self.config[DOT_RANDOMIZE]),
                            z + random.randint(-self.config[DOT_RANDOMIZE], self.config[DOT_RANDOMIZE])
                        ),
                    )

        dots_centralize = []
        for dot in dots:
            dots_centralize.append(
                [
                    dot[0] - self.config[CENTER_INIT],
                    dot[1] - self.config[CENTER_INIT],
                    dot[2] - self.config[CENTER_INIT]
                ]
            )

    def init_center_and_size(self):
        center = (
            self.config[CENTER_INIT][0] + random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            ),
            self.config[CENTER_INIT][1] + random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            ),
            self.config[CENTER_INIT][2] + random.randint(
                -self.config[CENTER_RANDOMIZE],
                self.config[CENTER_RANDOMIZE]
            )
        )
        size = self.config[SIZE_INIT] + random.randint(-self.config[SIZE_RANDOMIZE],
                                                       min(center[0], Config.PICTURE_SIZE - center[0],
                                                           center[1], Config.PICTURE_SIZE - center[1],
                                                           center[2], Config.PICTURE_SIZE - center[2])
                                                       ) * 0.9

        return center, size
