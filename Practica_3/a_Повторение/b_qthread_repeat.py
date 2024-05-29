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
import requests
from PySide6 import QtWidgets, QtCore


class WorkerTwo(QtCore.QThread):
    data_respond = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.url = None

    def signal_url(self, signal):
        self.url = signal

    def run(self) -> None:
        self.started.emit()

        try:
            response = requests.get(self.url)
            status_code = response.status_code
            self.data_respond.emit(status_code)

        except requests.RequestException:
            self.data_respond.emit(-1)

        self.finished.emit()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.initSignal()
        layout = QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit(placeholderText="Вставте url адресс")
        self.pushButtonStart = QtWidgets.QPushButton("Старт")
        self.pushButtonStart.clicked.connect(self.onPushButtonStart)
        self.pushButtonStop = QtWidgets.QPushButton("Стоп")
        self.pushButtonStop.clicked.connect(self.onPushButtonStop)
        self.plainTextEdit = QtWidgets.QPlainTextEdit()

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButtonStart)
        layout.addWidget(self.pushButtonStop)
        layout.addWidget(self.plainTextEdit)
        self.setLayout(layout)

        self.workerTwo = WorkerTwo()
        self.workerTwo.started.connect(self.onStart)
        self.workerTwo.data_respond.connect(self.codeStatus)
        self.pushButtonStart.clicked.connect(self.onPushButtonStart)

    def onStart(self):
        self.plainTextEdit.setPlainText("Подождите...")

    def finish(self):
        self.plainTextEdit.setPlainText("Проверка окончена")

    def codeStatus(self, status_code):
        """

        :param status_code:
        :return:
        """
        if status_code == -1:
            self.plainTextEdit.setPlainText("Ошибка")
        else:
            self.plainTextEdit.setPlainText(f"Сатус кода {status_code}")

    def onPushButtonStart(self):
        """

        :return:
        """
        self.workerTwo.signal_url(self.lineEdit.text())
        self.workerTwo.start()

    def onPushButtonStop(self):
        self.plainTextEdit.setPlainText("Проверка окончена")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

