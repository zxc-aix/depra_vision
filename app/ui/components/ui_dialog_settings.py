# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_settings.ui'
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
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(565, 260)
        Dialog.setMinimumSize(QSize(565, 260))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.lblPathTr = QLabel(self.groupBox)
        self.lblPathTr.setObjectName(u"lblPathTr")
        self.lblPathTr.setGeometry(QRect(20, 110, 171, 30))
        self.lblPathTr.setMinimumSize(QSize(170, 30))
        self.lePathDet = QLineEdit(self.groupBox)
        self.lePathDet.setObjectName(u"lePathDet")
        self.lePathDet.setGeometry(QRect(190, 70, 251, 30))
        self.lePathDet.setMinimumSize(QSize(250, 30))
        self.lePathVideo = QLineEdit(self.groupBox)
        self.lePathVideo.setObjectName(u"lePathVideo")
        self.lePathVideo.setGeometry(QRect(190, 30, 251, 30))
        self.lePathVideo.setMinimumSize(QSize(250, 30))
        self.btnPathDet = QPushButton(self.groupBox)
        self.btnPathDet.setObjectName(u"btnPathDet")
        self.btnPathDet.setGeometry(QRect(450, 70, 80, 30))
        self.btnPathDet.setMinimumSize(QSize(75, 30))
        self.lblPathDet = QLabel(self.groupBox)
        self.lblPathDet.setObjectName(u"lblPathDet")
        self.lblPathDet.setGeometry(QRect(20, 70, 170, 30))
        self.lblPathDet.setMinimumSize(QSize(170, 30))
        self.btnPathVideo = QPushButton(self.groupBox)
        self.btnPathVideo.setObjectName(u"btnPathVideo")
        self.btnPathVideo.setGeometry(QRect(450, 30, 80, 30))
        self.btnPathVideo.setMinimumSize(QSize(75, 30))
        self.lblPathVideo = QLabel(self.groupBox)
        self.lblPathVideo.setObjectName(u"lblPathVideo")
        self.lblPathVideo.setGeometry(QRect(20, 30, 170, 30))
        self.lblPathVideo.setMinimumSize(QSize(170, 30))
        self.btnPathTr = QPushButton(self.groupBox)
        self.btnPathTr.setObjectName(u"btnPathTr")
        self.btnPathTr.setGeometry(QRect(450, 110, 80, 30))
        self.btnPathTr.setMinimumSize(QSize(75, 30))
        self.lePathTr = QLineEdit(self.groupBox)
        self.lePathTr.setObjectName(u"lePathTr")
        self.lePathTr.setGeometry(QRect(190, 110, 251, 30))
        self.lePathTr.setMinimumSize(QSize(250, 30))
        self.lblPathHm = QLabel(self.groupBox)
        self.lblPathHm.setObjectName(u"lblPathHm")
        self.lblPathHm.setGeometry(QRect(20, 150, 171, 30))
        self.lblPathHm.setMinimumSize(QSize(170, 30))
        self.lePathHm = QLineEdit(self.groupBox)
        self.lePathHm.setObjectName(u"lePathHm")
        self.lePathHm.setGeometry(QRect(190, 150, 251, 30))
        self.lePathHm.setMinimumSize(QSize(250, 30))
        self.btnPathHm = QPushButton(self.groupBox)
        self.btnPathHm.setObjectName(u"btnPathHm")
        self.btnPathHm.setGeometry(QRect(450, 150, 80, 30))
        self.btnPathHm.setMinimumSize(QSize(75, 30))

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.btnAccept = QPushButton(Dialog)
        self.btnAccept.setObjectName(u"btnAccept")
        self.btnAccept.setMinimumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.btnAccept, 1, 0, 1, 1)

        self.btnReject = QPushButton(Dialog)
        self.btnReject.setObjectName(u"btnReject")
        self.btnReject.setMinimumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.btnReject, 1, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Application settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Parameters", None))
        self.lblPathTr.setText(QCoreApplication.translate("Dialog", u"Trajectory preservation", None))
        self.lePathDet.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select a folder for detections", None))
        self.lePathVideo.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select a folder for the video", None))
        self.btnPathDet.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.lblPathDet.setText(QCoreApplication.translate("Dialog", u"Detection preservation", None))
        self.btnPathVideo.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.lblPathVideo.setText(QCoreApplication.translate("Dialog", u"Path to video", None))
        self.btnPathTr.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.lePathTr.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select a folder for trajectories", None))
        self.lblPathHm.setText(QCoreApplication.translate("Dialog", u"Saving heat maps", None))
        self.lePathHm.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select a folder for heat maps", None))
        self.btnPathHm.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.btnAccept.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.btnReject.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

