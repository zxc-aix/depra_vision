# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_heatmap.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1550, 600)
        Form.setMinimumSize(QSize(1550, 600))
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblLV = QLabel(Form)
        self.lblLV.setObjectName(u"lblLV")
        self.lblLV.setMinimumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.lblLV, 0, 0, 1, 1)

        self.lvFolderList = QListView(Form)
        self.lvFolderList.setObjectName(u"lvFolderList")

        self.gridLayout_2.addWidget(self.lvFolderList, 1, 0, 1, 1)

        self.btnAddFolder = QPushButton(Form)
        self.btnAddFolder.setObjectName(u"btnAddFolder")
        self.btnAddFolder.setMinimumSize(QSize(180, 40))

        self.gridLayout_2.addWidget(self.btnAddFolder, 2, 0, 1, 1)

        self.btnRemove = QPushButton(Form)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setMinimumSize(QSize(180, 40))

        self.gridLayout_2.addWidget(self.btnRemove, 3, 0, 1, 1)

        self.btnClearFolder = QPushButton(Form)
        self.btnClearFolder.setObjectName(u"btnClearFolder")
        self.btnClearFolder.setMinimumSize(QSize(180, 40))

        self.gridLayout_2.addWidget(self.btnClearFolder, 4, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 6, 1)

        self.horizontalSpacer_3 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(25, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 3, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 4, 4, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblInfo = QLabel(Form)
        self.lblInfo.setObjectName(u"lblInfo")
        self.lblInfo.setMinimumSize(QSize(200, 30))

        self.gridLayout_3.addWidget(self.lblInfo, 0, 0, 1, 1)

        self.btnBuildGraph = QPushButton(Form)
        self.btnBuildGraph.setObjectName(u"btnBuildGraph")
        self.btnBuildGraph.setMinimumSize(QSize(200, 50))

        self.gridLayout_3.addWidget(self.btnBuildGraph, 1, 0, 1, 1)

        self.lblFillter = QLabel(Form)
        self.lblFillter.setObjectName(u"lblFillter")
        self.lblFillter.setMinimumSize(QSize(200, 30))

        self.gridLayout_3.addWidget(self.lblFillter, 2, 0, 1, 1)

        self.cbFillter = QComboBox(Form)
        self.cbFillter.addItem("")
        self.cbFillter.addItem("")
        self.cbFillter.addItem("")
        self.cbFillter.addItem("")
        self.cbFillter.addItem("")
        self.cbFillter.addItem("")
        self.cbFillter.addItem("")
        self.cbFillter.setObjectName(u"cbFillter")
        self.cbFillter.setMinimumSize(QSize(200, 50))

        self.gridLayout_3.addWidget(self.cbFillter, 3, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 2, 2, 2)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(25, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 3, 4, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 5, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(25, 37, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 4, 1, 1, 1)

        self.btnSaveImage = QPushButton(Form)
        self.btnSaveImage.setObjectName(u"btnSaveImage")
        self.btnSaveImage.setMinimumSize(QSize(220, 40))

        self.gridLayout_4.addWidget(self.btnSaveImage, 5, 2, 1, 2)

        self.gbParametrs = QGroupBox(Form)
        self.gbParametrs.setObjectName(u"gbParametrs")
        self.gridLayout = QGridLayout(self.gbParametrs)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chbOverlaps = QCheckBox(self.gbParametrs)
        self.chbOverlaps.setObjectName(u"chbOverlaps")
        self.chbOverlaps.setMinimumSize(QSize(220, 40))

        self.gridLayout.addWidget(self.chbOverlaps, 0, 0, 1, 1)

        self.lblGamma = QLabel(self.gbParametrs)
        self.lblGamma.setObjectName(u"lblGamma")
        self.lblGamma.setMinimumSize(QSize(120, 40))
        self.lblGamma.setMaximumSize(QSize(120, 40))

        self.gridLayout.addWidget(self.lblGamma, 0, 1, 1, 1)

        self.dsbGamma = QDoubleSpinBox(self.gbParametrs)
        self.dsbGamma.setObjectName(u"dsbGamma")
        self.dsbGamma.setMinimumSize(QSize(70, 40))

        self.gridLayout.addWidget(self.dsbGamma, 0, 2, 1, 1)

        self.lblColorGamma = QLabel(self.gbParametrs)
        self.lblColorGamma.setObjectName(u"lblColorGamma")
        self.lblColorGamma.setMinimumSize(QSize(220, 30))

        self.gridLayout.addWidget(self.lblColorGamma, 1, 0, 1, 1)

        self.lblAlpha = QLabel(self.gbParametrs)
        self.lblAlpha.setObjectName(u"lblAlpha")
        self.lblAlpha.setMinimumSize(QSize(120, 40))
        self.lblAlpha.setMaximumSize(QSize(140, 40))

        self.gridLayout.addWidget(self.lblAlpha, 1, 1, 1, 1)

        self.dsbAlpha = QDoubleSpinBox(self.gbParametrs)
        self.dsbAlpha.setObjectName(u"dsbAlpha")
        self.dsbAlpha.setMinimumSize(QSize(70, 40))

        self.gridLayout.addWidget(self.dsbAlpha, 1, 2, 1, 1)

        self.cbColorGamma = QComboBox(self.gbParametrs)
        self.cbColorGamma.setObjectName(u"cbColorGamma")
        self.cbColorGamma.setMinimumSize(QSize(200, 30))
        self.cbColorGamma.setMaximumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.cbColorGamma, 2, 0, 1, 1)

        self.lblContrast = QLabel(self.gbParametrs)
        self.lblContrast.setObjectName(u"lblContrast")
        self.lblContrast.setMinimumSize(QSize(140, 40))

        self.gridLayout.addWidget(self.lblContrast, 2, 1, 1, 1)

        self.dsbContrast = QDoubleSpinBox(self.gbParametrs)
        self.dsbContrast.setObjectName(u"dsbContrast")
        self.dsbContrast.setMinimumSize(QSize(60, 40))

        self.gridLayout.addWidget(self.dsbContrast, 2, 2, 1, 1)

        self.chbMarkup = QCheckBox(self.gbParametrs)
        self.chbMarkup.setObjectName(u"chbMarkup")
        self.chbMarkup.setMinimumSize(QSize(180, 40))

        self.gridLayout.addWidget(self.chbMarkup, 3, 0, 1, 1)

        self.lblBoxScale = QLabel(self.gbParametrs)
        self.lblBoxScale.setObjectName(u"lblBoxScale")
        self.lblBoxScale.setMinimumSize(QSize(120, 40))

        self.gridLayout.addWidget(self.lblBoxScale, 3, 1, 1, 1)

        self.dsbBoxScale = QDoubleSpinBox(self.gbParametrs)
        self.dsbBoxScale.setObjectName(u"dsbBoxScale")
        self.dsbBoxScale.setMinimumSize(QSize(70, 40))

        self.gridLayout.addWidget(self.dsbBoxScale, 3, 2, 1, 1)

        self.chbAddPlatform = QCheckBox(self.gbParametrs)
        self.chbAddPlatform.setObjectName(u"chbAddPlatform")
        self.chbAddPlatform.setMinimumSize(QSize(180, 40))

        self.gridLayout.addWidget(self.chbAddPlatform, 4, 0, 1, 1)

        self.lbZoom = QLabel(self.gbParametrs)
        self.lbZoom.setObjectName(u"lbZoom")
        self.lbZoom.setMinimumSize(QSize(130, 40))

        self.gridLayout.addWidget(self.lbZoom, 4, 1, 1, 1)

        self.dsbZoom = QDoubleSpinBox(self.gbParametrs)
        self.dsbZoom.setObjectName(u"dsbZoom")
        self.dsbZoom.setMinimumSize(QSize(70, 40))

        self.gridLayout.addWidget(self.dsbZoom, 4, 2, 1, 1)

        self.cbInterpolate = QCheckBox(self.gbParametrs)
        self.cbInterpolate.setObjectName(u"cbInterpolate")
        self.cbInterpolate.setMinimumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.cbInterpolate, 5, 0, 1, 1)

        self.lblGausSigma = QLabel(self.gbParametrs)
        self.lblGausSigma.setObjectName(u"lblGausSigma")
        self.lblGausSigma.setMinimumSize(QSize(130, 40))

        self.gridLayout.addWidget(self.lblGausSigma, 5, 1, 1, 1)

        self.sbGausSigma = QSpinBox(self.gbParametrs)
        self.sbGausSigma.setObjectName(u"sbGausSigma")
        self.sbGausSigma.setMinimumSize(QSize(70, 40))

        self.gridLayout.addWidget(self.sbGausSigma, 5, 2, 1, 1)

        self.cbAddColorbar = QCheckBox(self.gbParametrs)
        self.cbAddColorbar.setObjectName(u"cbAddColorbar")
        self.cbAddColorbar.setMinimumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.cbAddColorbar, 6, 0, 1, 1)

        self.lblColor = QLabel(self.gbParametrs)
        self.lblColor.setObjectName(u"lblColor")

        self.gridLayout.addWidget(self.lblColor, 6, 1, 1, 1)

        self.frameColor = QFrame(self.gbParametrs)
        self.frameColor.setObjectName(u"frameColor")
        self.frameColor.setMinimumSize(QSize(40, 40))
        self.frameColor.setMaximumSize(QSize(40, 40))
        self.frameColor.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameColor.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frameColor, 6, 2, 1, 1)


        self.gridLayout_4.addWidget(self.gbParametrs, 0, 7, 6, 1)

        self.lblImage = QLabel(Form)
        self.lblImage.setObjectName(u"lblImage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImage.sizePolicy().hasHeightForWidth())
        self.lblImage.setSizePolicy(sizePolicy)
        self.lblImage.setMinimumSize(QSize(580, 580))
        self.lblImage.setStyleSheet(u"background-color: black;")

        self.gridLayout_4.addWidget(self.lblImage, 0, 5, 6, 1)

        self.horizontalSpacer_4 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(25, 37, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)

        self.gbParametrs.raise_()
        self.lblImage.raise_()
        self.btnSaveImage.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Building activity maps", None))
        self.lblLV.setText(QCoreApplication.translate("Form", u"List of selected files", None))
        self.btnAddFolder.setText(QCoreApplication.translate("Form", u"Add folder", None))
        self.btnRemove.setText(QCoreApplication.translate("Form", u"Delete the last folder", None))
        self.btnClearFolder.setText(QCoreApplication.translate("Form", u"Clear list", None))
        self.lblInfo.setText(QCoreApplication.translate("Form", u"Folders selected: 0", None))
        self.btnBuildGraph.setText(QCoreApplication.translate("Form", u"Build an activity map", None))
        self.lblFillter.setText(QCoreApplication.translate("Form", u"Display data", None))
        self.cbFillter.setItemText(0, QCoreApplication.translate("Form", u"all", None))
        self.cbFillter.setItemText(1, QCoreApplication.translate("Form", u"across the open field", None))
        self.cbFillter.setItemText(2, QCoreApplication.translate("Form", u"through the raised cross-shaped maze", None))
        self.cbFillter.setItemText(3, QCoreApplication.translate("Form", u"according to Morris", None))
        self.cbFillter.setItemText(4, QCoreApplication.translate("Form", u"according to the Dark-Light Camera", None))
        self.cbFillter.setItemText(5, QCoreApplication.translate("Form", u"through the Y-maze", None))
        self.cbFillter.setItemText(6, QCoreApplication.translate("Form", u"according to the Three-Chamber Social Test", None))

        self.btnSaveImage.setText(QCoreApplication.translate("Form", u"Save activity map", None))
        self.gbParametrs.setTitle(QCoreApplication.translate("Form", u"Parameters", None))
        self.chbOverlaps.setText(QCoreApplication.translate("Form", u"Consider only intersections", None))
        self.lblGamma.setText(QCoreApplication.translate("Form", u"Gamma:", None))
        self.lblColorGamma.setText(QCoreApplication.translate("Form", u"Color range:", None))
        self.lblAlpha.setText(QCoreApplication.translate("Form", u"Alpha", None))
        self.lblContrast.setText(QCoreApplication.translate("Form", u"Contrast:", None))
        self.chbMarkup.setText(QCoreApplication.translate("Form", u"Add markup ", None))
        self.lblBoxScale.setText(QCoreApplication.translate("Form", u"Boxing coefficient:", None))
        self.chbAddPlatform.setText(QCoreApplication.translate("Form", u"Display platform", None))
        self.lbZoom.setText(QCoreApplication.translate("Form", u"Scale coefficient:", None))
        self.cbInterpolate.setText(QCoreApplication.translate("Form", u"Interpolate data", None))
        self.lblGausSigma.setText(QCoreApplication.translate("Form", u"Gaussian sigma:", None))
        self.cbAddColorbar.setText(QCoreApplication.translate("Form", u"Add color scale ", None))
        self.lblColor.setText(QCoreApplication.translate("Form", u"Platform color", None))
        self.lblImage.setText("")
    # retranslateUi

