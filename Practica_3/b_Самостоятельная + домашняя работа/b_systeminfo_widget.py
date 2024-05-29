"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets, QtCore
from a_threads import SystemInfo


class SysWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Мониторинг CPU / RAM")
        # self.setFixedSize(350, 200) в обледенении двух виджетов , плохое поведение не подстраивается под размер

        self.spinBox = QtWidgets.QSpinBox()
        self.cpu_label = QtWidgets.QLabel("Загрузка CPU")
        self.textEditCPU = QtWidgets.QTextEdit()
        self.ram_label = QtWidgets.QLabel("Загрузка RAM")
        self.textEditRam = QtWidgets.QTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.spinBox)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.textEditCPU)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.textEditRam)
        self.setLayout(layout)

        self.flow_signal = SystemInfo()
        self.flow_signal.systemInfoReceived.connect(self.infoSis)
        self.flow_signal.start()
        self.spinBox.valueChanged.connect(self.onDelay)

    def onDelay(self, delay):
        self.flow_signal.delay = delay

    def infoSis(self, data):
        cpu_value, ram_value = data
        self.textEditCPU.setText(f"{cpu_value}%")
        self.textEditRam.setText(f"{ram_value}%")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SysWindow()
    window.show()

    app.exec()
