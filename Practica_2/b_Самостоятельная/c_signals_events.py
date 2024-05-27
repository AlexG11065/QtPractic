"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtCore, QtGui
from Practica_2.b_Самостоятельная.ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.width_window, self.height_window = QtWidgets.QApplication.primaryScreen().size().toTuple()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonLT.clicked.connect(lambda: self.move(0, 0))
        self.ui.pushButtonLB.clicked.connect(lambda: self.move(0, self.height_window - self.height()))

        self.ui.pushButtonRT.clicked.connect(lambda: self.move(self.width_window - self.width(), 0))
        self.ui.pushButtonRB.clicked.connect(lambda: self.move(self.width_window - self.width(), self.height_window - self.height()))

        self.ui.pushButtonCenter.clicked.connect(lambda: self.move(self.width_window // 2 - self.width() // 2, self.height_window // 2 - self.height() // 2))

        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoords)

        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetData)

    def onPushButtonMoveCoords(self):
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def onPushButtonGetData(self):
        number_screens = len(QtWidgets.QApplication.screens())
        add_number_screens = f"* Кол-во экранов: {number_screens}"
        self.ui.plainTextEdit.appendPlainText(str(add_number_screens))

        current_window = QtWidgets.QApplication.primaryScreen().name()
        add_current_window = f"* Текущее основное окно: {current_window}"
        self.ui.plainTextEdit.appendPlainText((str(add_current_window)))

        screen_resolution = QtWidgets.QApplication.primaryScreen().size()
        add_screen_resolution = f"* Разрешение экрана: {screen_resolution.width()} x {screen_resolution.height()}"
        self.ui.plainTextEdit.appendPlainText(str(add_screen_resolution))

        screen_window_on = f"* На каком экране окно находится: {current_window}"
        self.ui.plainTextEdit.appendPlainText(screen_window_on)

        window_size = self.size()
        add_window_size = f"* Размеры окна: {window_size.width()} x {window_size.height()}"
        self.ui.plainTextEdit.appendPlainText(add_window_size)

        min_size_window = self.minimumSize()
        add_min_size_window = f"* Минимальные размеры окна: {min_size_window.width()} x {min_size_window.height()}"
        self.ui.plainTextEdit.appendPlainText(add_min_size_window)

        coordinates_windows = self.pos()
        add_coordinates_windows = f"* Текущее положение (координаты) окна: X {coordinates_windows.x()}, Y {coordinates_windows.y()}"
        self.ui.plainTextEdit.appendPlainText(add_coordinates_windows)

        centre_coordinates = self.rect().center()
        add_centre_coordinates = f"* Координаты центра приложения: X {centre_coordinates.x()}, Y{centre_coordinates.y()}"
        self.ui.plainTextEdit.appendPlainText(add_centre_coordinates)

        window_state = self.windowState()
        add_window_state = f"* Состояние окна: {window_state}"
        self.ui.plainTextEdit.appendPlainText(add_window_state)

        # string = "Конец"
        # new_string = string.center(50, '*')
        # self.ui.plainTextEdit.appendPlainText(new_string)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
