"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QSettings


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__loadSettings()

    def __initUi(self):
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.plainTextEdit)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.saveSettings()

    def saveSettings(self):
        set = QtCore.QSettings('plainTextEdit')
        set.setValue("text", self.plainTextEdit.toPlainText())

    def __loadSettings(self):
        set = QtCore.QSettings("plainTextEdit")
        text = set.value("text")
        if text is not None:
            self.plainTextEdit.setPlainText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
