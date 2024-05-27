# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 469)
        MainWindow.setStyleSheet(u"background-color: rgb(113, 113, 113);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setItalic(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        font2 = QFont()
        font2.setPointSize(10)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"background-color: rgb(211, 211, 211);")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButtonTrans = QPushButton(self.centralwidget)
        self.pushButtonTrans.setObjectName(u"pushButtonTrans")

        self.verticalLayout_3.addWidget(self.pushButtonTrans)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButtonDel = QPushButton(self.centralwidget)
        self.pushButtonDel.setObjectName(u"pushButtonDel")

        self.verticalLayout_3.addWidget(self.pushButtonDel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
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


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044f\u0437\u044b\u043a \u0441 \u043a\u0430\u043a\u043e\u0433\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044f\u0437\u044b\u043a \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0430...", None))
        self.pushButtonTrans.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
        self.pushButtonDel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434...", None))
    # retranslateUi

