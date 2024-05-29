import googletrans
import textblob
import translators
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from Практика_5.ui.form import Ui_MainWindow
from googletrans import Translator, constants
import sys


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Переводчик")

        # Создаю обьект класса Translator
        # self.translator = Translator

        # получаю словарь, где все языки
        self.languages = googletrans.LANGUAGES
        print(self.languages)

        # Создаю список, где буду хранить все значение ключей
        self.languages_list = list(self.languages.values())
        print(self.languages_list)

        # Передаем в comboBox список
        self.ui.comboBox.addItems(self.languages_list)
        self.ui.comboBox_2.addItems(self.languages_list)

        # Устанавливаем по умолчанию языки в comboBox \ comboBox_2
        self.ui.comboBox.setCurrentText("russian")
        self.ui.comboBox_2.setCurrentText("english")

        # Инициализация сигналов
        self.initSignal()

    def initSignal(self):
        """
        Инициализация сигналов pushButtonDel, pushButtonTrans
        :return: None
        """
        self.ui.pushButtonDel.clicked.connect(self.onpushButtonDel)
        self.ui.pushButtonTrans.clicked.connect(self.translate)

    def translate(self):

        """

        :return:
        """
        print("translate")

        try:

            for key, value in self.languages.items():
                # Находим ключ левой колонки comboBox
                if value == self.ui.comboBox.currentText():
                    languages_key = key

            for key, value in self.languages.items():
                # Находим ключ правой колонки comboBox_2
                if value == self.ui.comboBox_2.currentText():
                    to_languages_key = key

            # translator = Translator()
            # text = self.ui.textEdit.toPlainText()
            # translation = translator.translate(text, src="languages_key", dest="to_languages_key")
            # self.ui.textEdit_2.setText(translation)


            # self.ui.textEdit.setText(languages_key)
            # self.ui.textEdit_2.setText(to_languages_key)
            #
            # words = textblob.TextBlob(self.ui.textEdit.toPlainText())
            # words = words.translate(src=languages_key, desk=to_languages_key)
            #
            # self.ui.textEdit_2.setText(str(words))
            # text = self.ui.textEdit.toPlainText()
            # text = googletrans.Translator.translate(text, src="languages_key", dest="to_languages_key")
            # self.ui.textEdit_2.setText(text)

        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))

    def onpushButtonDel(self):
        """
        Подключение кнопки pushButtonDel
        :return: None
        """
        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()
        print("onpushButtonDel")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
