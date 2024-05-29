"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets, QtCore
from b_systeminfo_widget import SysWindow
from c_weatherapi_widget import WindowWeather

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.add_sysWindow = SysWindow()
        self.add_windowWeather = WindowWeather()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.add_sysWindow)
        layout.addWidget(self.add_windowWeather)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

