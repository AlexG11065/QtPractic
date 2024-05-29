# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_new.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(719, 311)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	border-radius: 8px;\n"
"	border: 1px solid #e0e4e7;\n"
"	padding: 5px 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color:  #0000CD;\n"
"	color: #fff;\n"
"	font-weight: 700;\n"
"	border-radius: 8px;\n"
"	border: 1px solid #0d6efd;\n"
"	padding: 5px 15px;\n"
"	margin-top: 10px;\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	background-color: #0b5ed7;\n"
"	border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border-radius: 8px;\n"
"	border: 1px solid #e0e4e7;\n"
"	padding: 5px 15px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"background-color: rgb(211, 211, 211);")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.pushButtonTrans = QPushButton(self.splitter)
        self.pushButtonTrans.setObjectName(u"pushButtonTrans")
        self.splitter.addWidget(self.pushButtonTrans)
        self.pushButtonDel = QPushButton(self.splitter)
        self.pushButtonDel.setObjectName(u"pushButtonDel")
        icon = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.pushButtonDel.setIcon(icon)
        self.splitter.addWidget(self.pushButtonDel)

        self.horizontalLayout.addWidget(self.splitter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setItalic(True)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(True)
        self.textEdit_2.setFont(font3)
        self.textEdit_2.setStyleSheet(u"background-color: rgb(211, 211, 211);")

        self.verticalLayout.addWidget(self.textEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u044f\u0437\u044b\u043a", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442...", None))
        self.pushButtonTrans.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
        self.pushButtonDel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u044f\u0437\u044b\u043a", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434...", None))
    # retranslateUi

