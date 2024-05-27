"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""
from datetime import datetime

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QtWidgets.QLabel("<h1>Добро пожаловать</h1>")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(2000)

        self.timer.timeout.connect(self.initSignal)
        self.timer.start()

    def initSignal(self):
        print(f"Вызвана функция ---> initSignal")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
