def paint_predict(model_path):
    import sys
    from PyQt5.QtWidgets import QApplication
    from windows import AppWindow
    from cnn import CNN

    model = CNN()
    model.load(model_path)

    app = QApplication(sys.argv)
    window = AppWindow(model)
    window.show()
    app.exec()
