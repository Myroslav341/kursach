from cnn import CNN


def cnn_predict(model_path: str, file_path: str):
    model = CNN()
    model.load(model_path)
    print(model.predict(file_path))
    return


def cnn_train(save_name: str):
    model = CNN()
    model.train(save_name)
