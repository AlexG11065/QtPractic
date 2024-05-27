"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore

from Practica_2.b_Самостоятельная.ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Объект для сохранения параметров
        self.settings = QtCore.QSettings("MyApp")

        # отображение в различных системах счисления (oct, hex, bin, dec)
        self.comboBox.addItems(["Oct", "Hex", "Bin", "Dec"])

        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        self.loadSetings()
        # self.initSignal()


    def loadSetings(self):
        pass






if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
