from library.constants import *
from .dataset_scripts import init_dataset
from .cnn_test import cnn_predict, cnn_train
from .paint_predict import paint_predict


scripts = {
    INIT_DATASET: {
        METHOD: init_dataset,
        DESCRIPTION: 'initialize dataset'
    },
    CNN_TRAIN: {
        METHOD: cnn_train,
        DESCRIPTION: 'train cnn'
    },
    CNN_PREDICT: {
        METHOD: cnn_predict,
        DESCRIPTION: 'cnn predict'
    },
    PAINT_PREDICT: {
        METHOD: paint_predict,
        DESCRIPTION: 'predict via paint'
    }
}


def start_project(args: list):
    if len(args) < 1:
        print(invalid_action_text(f'no action was given'))
        return

    action, params = get_action_and_params(args)

    if params is None:
        scripts[action][METHOD]()
    else:
        scripts[action][METHOD](*params)


def get_action_and_params(args: list):
    return args[0], args[1:] or None


def invalid_action_text(text) -> str:
    text += f'\n\nlist of available actions:\n'

    for action_available in scripts:
        text += f'\t{action_available} - {scripts[action_available][DESCRIPTION]}\n'

    return text
