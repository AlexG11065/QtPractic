"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit(placeholderText="Вставте url адресс")
        self.pushButtonStart = QtWidgets.QPushButton("Старт")
        self.pushButtonStop = QtWidgets.QPushButton("Стоп")
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButtonStart)
        layout.addWidget(self.pushButtonStop)
        self.setLayout(layout)

        self.initSignal()

    def initSignal(self):
        self.pushButtonStart.clicked.connect(self.onPushButtonStart)
        self.pushButtonStop.clicked.connect(self.onPushButtonStop)

    def onPushButtonStart(self):
        print("onPushButtonStart")

    def onPushButtonStop(self):
        print("onPushButtonStop")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
