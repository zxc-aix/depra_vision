# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_trimmer.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QDoubleSpinBox,
    QFrame, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1110, 710)
        Dialog.setMinimumSize(QSize(1110, 710))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(831, 9, 270, 600))
        self.groupBox.setMinimumSize(QSize(270, 480))
        self.lblColor = QLabel(self.groupBox)
        self.lblColor.setObjectName(u"lblColor")
        self.lblColor.setGeometry(QRect(20, 30, 180, 41))
        self.lblColor.setMinimumSize(QSize(180, 30))
        self.frameColor = QFrame(self.groupBox)
        self.frameColor.setObjectName(u"frameColor")
        self.frameColor.setGeometry(QRect(220, 30, 41, 41))
        self.frameColor.setMinimumSize(QSize(40, 40))
        self.frameColor.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameColor.setFrameShadow(QFrame.Shadow.Raised)
        self.btnSelectZone = QPushButton(self.groupBox)
        self.btnSelectZone.setObjectName(u"btnSelectZone")
        self.btnSelectZone.setGeometry(QRect(20, 90, 241, 40))
        self.btnSelectZone.setMinimumSize(QSize(240, 40))
        self.btnDeleteZone = QPushButton(self.groupBox)
        self.btnDeleteZone.setObjectName(u"btnDeleteZone")
        self.btnDeleteZone.setGeometry(QRect(20, 140, 241, 40))
        self.btnDeleteZone.setMinimumSize(QSize(240, 40))
        self.btnResetSelected = QPushButton(self.groupBox)
        self.btnResetSelected.setObjectName(u"btnResetSelected")
        self.btnResetSelected.setGeometry(QRect(20, 190, 241, 40))
        self.btnResetSelected.setMinimumSize(QSize(240, 40))
        self.btnCrop = QPushButton(self.groupBox)
        self.btnCrop.setObjectName(u"btnCrop")
        self.btnCrop.setGeometry(QRect(20, 250, 241, 40))
        self.btnCrop.setMinimumSize(QSize(240, 40))
        self.btnResetCrop = QPushButton(self.groupBox)
        self.btnResetCrop.setObjectName(u"btnResetCrop")
        self.btnResetCrop.setGeometry(QRect(20, 300, 241, 40))
        self.btnResetCrop.setMinimumSize(QSize(240, 40))
        self.lblAngle = QLabel(self.groupBox)
        self.lblAngle.setObjectName(u"lblAngle")
        self.lblAngle.setGeometry(QRect(20, 350, 151, 41))
        self.lblAngle.setMinimumSize(QSize(150, 40))
        self.dsbAngle = QDoubleSpinBox(self.groupBox)
        self.dsbAngle.setObjectName(u"dsbAngle")
        self.dsbAngle.setGeometry(QRect(190, 350, 71, 41))
        self.dsbAngle.setMinimumSize(QSize(70, 40))
        self.cbVideoAdd = QCheckBox(self.groupBox)
        self.cbVideoAdd.setObjectName(u"cbVideoAdd")
        self.cbVideoAdd.setGeometry(QRect(20, 400, 241, 31))
        self.cbVideoAdd.setMinimumSize(QSize(240, 30))
        self.sliderContiner = QWidget(Dialog)
        self.sliderContiner.setObjectName(u"sliderContiner")
        self.sliderContiner.setGeometry(QRect(9, 615, 800, 40))
        self.sliderContiner.setMinimumSize(QSize(800, 30))
        self.lblInfo = QLabel(Dialog)
        self.lblInfo.setObjectName(u"lblInfo")
        self.lblInfo.setGeometry(QRect(9, 661, 800, 40))
        self.lblInfo.setMinimumSize(QSize(800, 40))
        self.btnSave = QPushButton(Dialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(831, 615, 271, 40))
        self.btnSave.setMinimumSize(QSize(240, 40))
        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(831, 661, 271, 40))
        self.btnCancel.setMinimumSize(QSize(240, 40))
        self.lblImage = QLabel(Dialog)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setGeometry(QRect(10, 10, 800, 600))
        self.lblImage.setMinimumSize(QSize(800, 600))
        self.lblImage.setStyleSheet(u"background-color: white;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Trimmer Video", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Parameters", None))
        self.lblColor.setText(QCoreApplication.translate("Dialog", u"Selecting the fill color for areas", None))
        self.btnSelectZone.setText(QCoreApplication.translate("Dialog", u"Highlight the area", None))
        self.btnDeleteZone.setText(QCoreApplication.translate("Dialog", u"Delete last area", None))
        self.btnResetSelected.setText(QCoreApplication.translate("Dialog", u"Reset zone area", None))
        self.btnCrop.setText(QCoreApplication.translate("Dialog", u"Crop video at the edges", None))
        self.btnResetCrop.setText(QCoreApplication.translate("Dialog", u"Reset crop selection", None))
        self.lblAngle.setText(QCoreApplication.translate("Dialog", u"Video rotation angle:", None))
        self.cbVideoAdd.setText(QCoreApplication.translate("Dialog", u"Set video in main window", None))
        self.lblInfo.setText(QCoreApplication.translate("Dialog", u"Start: , End:", None))
        self.btnSave.setText(QCoreApplication.translate("Dialog", u"Save video", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.lblImage.setText("")
    # retranslateUi

