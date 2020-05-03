import os
from random import shuffle

import cv2
from keras.engine.saving import load_model
from numpy import array, ndarray
from matplotlib import pyplot as plt
from config import Config


def test():
    model = load_model(Config.BASE_DIR + '\\cnn\\models\\' + 'test_refact2_2.h5')

    train_path = 'D:\\univ\\3 grade\\kursach\\main\\data\\train'

    l = os.listdir(train_path)

    for i, x in enumerate(l):
        img_data = cv2.imread(train_path + '\\' + x, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (64, 64))

        img = img_data

        img_data = img_data.astype('float32')
        img_data /= 255
        img_data = img_data.reshape(1, 64, 64, 1)

        f = model.predict(img_data)

        path = 'D:\\univ\\3 grade\\kursach\\main\\data\\tested'
        if 'rect' in x:
            print(f[0][0])
            if f[0][0] < 0.5:
                plt.imsave(f'{path}\\{i}_{f[0][0]}.png', img)
            # plt.waitforbuttonpress()

        if 'pyramid' in x and f[0][1] < 0.5:
            # plt.imshow(img)
            plt.imsave(f'{path}\\{i}_{f[0][1]}.png', img)
            # plt.waitforbuttonpress()
