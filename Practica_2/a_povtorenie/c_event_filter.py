"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""
import sys

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()

    def __initUi(self):
        self.setFixedSize(200, 100)
        self.label = QtWidgets.QLabel(self)
        self.label.move(50, 50)
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.text = "Красивая кнопка"
        self.label.setText(self.text)
        self.color_text = "<span style='color:red;'>Красивая</span> <span style='color:blue;'>кнопка</span>"

        self.label.installEventFilter(self)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent):
        if watched == self.label:
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                self.label.setText(self.color_text)
            if event.type() == QtCore.QEvent.Type.MouseButtonRelease:
                self.label.eventFilter(watched, event)
        return super().eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
