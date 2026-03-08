# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_load.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(387, 210)
        Form.setStyleSheet(u"QMainWindow {\n"
"    background-color: #e9edf5;\n"
"}\n"
"")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 100, 341, 23))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 281, 31))
        self.label.setStyleSheet(u"")
        self.btnStart = QPushButton(Form)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(120, 140, 131, 41))
        self.btnStart.setStyleSheet(u"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Video processing", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Click 'Start'</p></body></html>", None))
        self.btnStart.setText(QCoreApplication.translate("Form", u"Start", None))
    # retranslateUi

