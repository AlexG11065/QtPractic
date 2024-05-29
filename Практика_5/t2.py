import sys

import googletrans
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from googletrans import Translator, constants
from Практика_5.ui.form import Ui_MainWindow
from language_list import languages


class WindowApp(QMainWindow):
    def __init__(self):
        super(WindowApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.translator = Translator()
        self.setWindowTitle("Переводчик")

        languages_list = list(languages.keys())

        self.ui.pushButtonTrans.clicked.connect(self.translator_text)
        self.ui.pushButtonDel.clicked.connect(self.clear_button)

        # Передаем в comboBox список
        self.ui.comboBox.addItems(languages_list)
        self.ui.comboBox_2.addItems(languages_list)

        # Устанавливаем по умолчанию языки в comboBox \ comboBox_2
        self.ui.comboBox.setCurrentText("Russian")
        self.ui.comboBox_2.setCurrentText("English")

    def translator_text(self):
        language = self.ui.comboBox_2.currentText()
        suffix = languages[language]
        text = self.ui.textEdit.toPlainText()
        translation = self.translator.translate(text, dest=suffix)
        self.ui.textEdit_2.clear()
        self.ui.textEdit_2.setPlainText(translation.text)

    def clear_button(self):
        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowApp()
    window.show()

    app.exec()
