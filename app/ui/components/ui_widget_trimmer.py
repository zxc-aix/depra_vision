# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_trimmer.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1120, 732)
        Form.setMinimumSize(QSize(1110, 710))
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblInfo = QLabel(Form)
        self.lblInfo.setObjectName(u"lblInfo")
        self.lblInfo.setMinimumSize(QSize(800, 40))

        self.gridLayout.addWidget(self.lblInfo, 1, 0, 1, 1)

        self.sliderContiner = QWidget(Form)
        self.sliderContiner.setObjectName(u"sliderContiner")
        self.sliderContiner.setMinimumSize(QSize(800, 30))

        self.gridLayout.addWidget(self.sliderContiner, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.lblFrame = QLabel(Form)
        self.lblFrame.setObjectName(u"lblFrame")
        self.lblFrame.setMinimumSize(QSize(800, 600))
        self.lblFrame.setStyleSheet(u"background-color: white;")

        self.gridLayout_3.addWidget(self.lblFrame, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 2, 1)

        self.horizontalSpacer = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(240, 40))

        self.gridLayout_2.addWidget(self.btnSave, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
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
        self.cbSize = QCheckBox(self.groupBox)
        self.cbSize.setObjectName(u"cbSize")
        self.cbSize.setGeometry(QRect(20, 440, 240, 30))
        self.cbSize.setMinimumSize(QSize(240, 30))
        self.sbSize = QSpinBox(self.groupBox)
        self.sbSize.setObjectName(u"sbSize")
        self.sbSize.setGeometry(QRect(50, 471, 71, 41))
        self.sbSize.setMinimumSize(QSize(70, 40))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 480, 20, 21))
        self.label.setMinimumSize(QSize(20, 20))
        self.sbSize_2 = QSpinBox(self.groupBox)
        self.sbSize_2.setObjectName(u"sbSize_2")
        self.sbSize_2.setGeometry(QRect(170, 470, 71, 41))
        self.sbSize_2.setMinimumSize(QSize(70, 40))

        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 2, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0432\u0438\u0434\u0435\u043e", None))
        self.lblInfo.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u043b\u043e: , \u041a\u043e\u043d\u0435\u0446:", None))
        self.lblFrame.setText("")
        self.btnSave.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.lblColor.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u043e\u0440 \u0446\u0432\u0435\u0442 \u0437\u0430\u043b\u0438\u0432\u043a\u0438 \u0437\u043e\u043d", None))
        self.btnSelectZone.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0437\u043e\u043d\u0443", None))
        self.btnDeleteZone.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.btnResetSelected.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0437\u043e\u043d", None))
        self.btnCrop.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0440\u0435\u0437\u0430\u0442\u044c \u0432\u0438\u0434\u0435\u043e \u043f\u043e \u043a\u0440\u0430\u044f\u043c", None))
        self.btnResetCrop.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043e\u0431\u0440\u0435\u0437\u043a\u0438", None))
        self.lblAngle.setText(QCoreApplication.translate("Form", u"\u0423\u0433\u043e\u043b \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430 \u0432\u0438\u0434\u0435\u043e:", None))
        self.cbVideoAdd.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u0438\u0434\u0435\u043e \u0432 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.cbSize.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0441\u0442\u043e\u043c\u043d\u044b\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u044b \u0432\u0438\u0434\u0435\u043e", None))
        self.label.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

