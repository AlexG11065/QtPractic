"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()

        self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
        self.pushButtonClear = QtWidgets.QPushButton('Clear')

        laout = QtWidgets.QVBoxLayout()
        laout.addWidget(self.lineEditInput)
        laout.addWidget(self.lineEditMirror)
        laout.addWidget(self.pushButtonMirror)
        laout.addWidget(self.pushButtonClear)

        self.setLayout(laout)

    def __initSignals(self):
        self.pushButtonMirror.clicked.connect(self.__onPushButtonMirrorClicked)
        self.pushButtonClear.clicked.connect(self.__onPushButtonClearClicked)
        print("Вызван метод __initSignals")

    def __onPushButtonMirrorClicked(self):
        input_text = self.lineEditInput.text()
        mir_t = input_text[::-1]
        self.lineEditMirror.setText(mir_t)
        print("Вызван метод __onPushButtonMirrorClicked")

    def __onPushButtonClearClicked(self):
        self.lineEditInput.clear()
        self.lineEditMirror.clear()
        print("Вызван метод __onPushButtonClearClicked")

    def __onLineEditMirrorTextChanged(self, text):
        print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
