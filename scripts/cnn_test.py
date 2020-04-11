from __future__ import print_function

import os
from PIL import Image

from numpy import array, ndarray
import matplotlib.image as mpimg
from random import shuffle
import matplotlib.pyplot as plt
import cv2


def get_data(path):
    train_pic = os.listdir(path)

    im1 = array(Image.open(path + '\\' + train_pic[0]))  # open one image to get size
    m, n = im1.shape[0:2]  # get the size of the images

    data = ndarray(shape=(len(train_pic), 50, 50), dtype=float)
    labels = array(train_pic)

    k = 0

    for i, x in enumerate(train_pic):
        # im1 = array(Image.open(path + '\\' + x))
        # image = im1[:, :, 0]
        # data[i] = image

        img_data = cv2.imread(path + '\\' + x, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (50, 50))
        data[i] = array(img_data)

        if 'rect' in x:
            labels[i] = 0
        else:
            labels[i] = 1


    data_ = [[data[i], labels[i]] for i in range(len(train_pic))]

    shuffle(data_)

    for i, d in enumerate(data_):
        data[i] = d[0]
        labels[i] = d[1]

    return data, labels


def cnn_test():
    import keras
    from keras.datasets import mnist
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Flatten
    from keras.layers import Conv2D, MaxPooling2D
    from keras import backend as K
    from keras.preprocessing.image import ImageDataGenerator

    # datagen = ImageDataGenerator()
    # train_it = datagen.flow_from_directory('data/train/', class_mode='binary', batch_size=64)
    # test_it = datagen.flow_from_directory('data/test/', class_mode='binary', batch_size=64)

    train_path = 'D:\\univ\\3 grade\\kursach\\main\\data\\train'
    test_path = 'D:\\univ\\3 grade\\kursach\\main\\data\\test'

    x_train, y_train = get_data(train_path)
    x_test, y_test = get_data(test_path)

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.imshow(x_train[1], cmap="gray")
    # fig.show()

    batch_size = 128
    num_classes = 2
    epochs = 8

    # input image dimensions
    # img_rows, img_cols = 28, 28
    img_rows, img_cols = 50, 50

    # the data, split between train and test sets
    # (x_train, y_train), (x_test, y_test) = mnist.load_data()

    if K.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
        x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(5, 5),
                     activation='relu',
                     input_shape=input_shape))

    model.add(Conv2D(64, (5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Dropout(0.15))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              validation_data=(x_test, y_test))
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    # model = Sequential()
    # model.add(Conv2D(32, kernel_size=(5, 5),
    #                  activation='relu',
    #                  input_shape=input_shape))
    # # model.add(MaxPooling2D(2))
    #
    # model.add(Conv2D(64, (5, 5), activation='relu'))
    # # model.add(MaxPooling2D(2))
    #
    # model.add(Conv2D(128, (5, 5), activation='relu'))
    # model.add(MaxPooling2D(2))
    #
    #
    # model.add(Conv2D(32, (5, 5), activation='relu'))
    # model.add(MaxPooling2D(2))
    #
    # model.add(Flatten())
    #
    # model.add(Dense(512, activation='relu'))
    #
    # model.add(Dense(128, activation='relu'))
    #
    # model.add(Dense(64, activation='relu'))
    #
    # model.add(Dense(num_classes, activation='softmax'))
    #
    # model.compile(loss=keras.losses.categorical_crossentropy,
    #               optimizer=keras.optimizers.Adadelta(),
    #               metrics=['accuracy'])
    #
    # model.fit(x_train, y_train,
    #           batch_size=batch_size,
    #           epochs=epochs,
    #           verbose=1,
    #           validation_data=(x_test, y_test))
    # score = model.evaluate(x_test, y_test, verbose=0)
    # print('Test loss:', score[0])
    # print('Test accuracy:', score[1])

    model.save('my_model.h5')
