# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_save_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(570, 254)
        Dialog.setMinimumSize(QSize(570, 250))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(520, 180))
        self.lblDPI = QLabel(self.groupBox)
        self.lblDPI.setObjectName(u"lblDPI")
        self.lblDPI.setGeometry(QRect(10, 80, 170, 30))
        self.lblDPI.setMinimumSize(QSize(170, 30))
        self.sbSizeRight = QSpinBox(self.groupBox)
        self.sbSizeRight.setObjectName(u"sbSizeRight")
        self.sbSizeRight.setGeometry(QRect(290, 120, 75, 30))
        self.sbSizeRight.setMinimumSize(QSize(75, 30))
        self.lblSize = QLabel(self.groupBox)
        self.lblSize.setObjectName(u"lblSize")
        self.lblSize.setGeometry(QRect(10, 120, 170, 30))
        self.lblSize.setMinimumSize(QSize(170, 30))
        self.sbSizeLeft = QSpinBox(self.groupBox)
        self.sbSizeLeft.setObjectName(u"sbSizeLeft")
        self.sbSizeLeft.setGeometry(QRect(180, 120, 75, 30))
        self.sbSizeLeft.setMinimumSize(QSize(75, 30))
        self.lblX = QLabel(self.groupBox)
        self.lblX.setObjectName(u"lblX")
        self.lblX.setGeometry(QRect(270, 120, 21, 31))
        self.sbDPI = QSpinBox(self.groupBox)
        self.sbDPI.setObjectName(u"sbDPI")
        self.sbDPI.setGeometry(QRect(180, 80, 75, 31))
        self.sbDPI.setMinimumSize(QSize(75, 30))
        self.btnInput = QPushButton(self.groupBox)
        self.btnInput.setObjectName(u"btnInput")
        self.btnInput.setGeometry(QRect(390, 40, 90, 31))
        self.btnInput.setMinimumSize(QSize(90, 30))
        self.leFilePath = QLineEdit(self.groupBox)
        self.leFilePath.setObjectName(u"leFilePath")
        self.leFilePath.setGeometry(QRect(180, 40, 201, 31))
        self.leFilePath.setReadOnly(True)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 170, 30))
        self.label.setMinimumSize(QSize(170, 30))

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.btnSave = QPushButton(Dialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(230, 50))

        self.gridLayout.addWidget(self.btnSave, 1, 0, 1, 1)

        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(230, 50))

        self.gridLayout.addWidget(self.btnCancel, 1, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Video preservation", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Graph saving parameters", None))
        self.lblDPI.setText(QCoreApplication.translate("Dialog", u"DPI:", None))
        self.lblSize.setText(QCoreApplication.translate("Dialog", u"Image size:", None))
        self.lblX.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.btnInput.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.leFilePath.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select a folder to save to", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Path for saving:", None))
        self.btnSave.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

