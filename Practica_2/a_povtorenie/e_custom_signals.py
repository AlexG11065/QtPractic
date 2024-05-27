"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore
import hashlib


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h1>Пройдите регистрацию</h1>")

        self.__pushButton = QtWidgets.QPushButton(self)
        self.__pushButton.setText("Зарегистрироваться")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.__pushButton)

        self.setLayout(layout)

    def __initSignals(self):
        self.__pushButton.clicked.connect(self.openRegistration)

    def openRegistration(self):
        print("openRegistration")
        other_window = OtherWindow(self)
        other_window.registration.connect(self.labelText)
        other_window.exec()

    def labelText(self, login):
        self.label.setText(f"<h1>Добро пожаловать {login}</h1>")


class OtherWindow(QtWidgets.QDialog):
    registration = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle("Регистрация")
        self.setFixedSize(400, 150)
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите логин")

        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setPlaceholderText("Введите пароль")

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText("Зарегистрироваться")
        self.pushButton.clicked.connect(self.register)

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.lineEdit_2)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def register(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        salt = "5gz"
        dataBase_password = password + salt
        hashed = hashlib.md5(dataBase_password.encode())

        print(f"Захешированный пароль --->", hashed.hexdigest())
        print("Не Захешированный пароль --->", password)

        self.registration.emit(login)
        self.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
