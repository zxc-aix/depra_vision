# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_theme_language.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(485, 280)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cbTheme = QComboBox(self.groupBox)
        self.cbTheme.addItem("")
        self.cbTheme.setObjectName(u"cbTheme")
        self.cbTheme.setMinimumSize(QSize(120, 50))

        self.gridLayout.addWidget(self.cbTheme, 0, 1, 1, 1)

        self.lblTheme = QLabel(self.groupBox)
        self.lblTheme.setObjectName(u"lblTheme")
        self.lblTheme.setMinimumSize(QSize(160, 50))

        self.gridLayout.addWidget(self.lblTheme, 0, 0, 1, 1)

        self.lblLanguage = QLabel(self.groupBox)
        self.lblLanguage.setObjectName(u"lblLanguage")
        self.lblLanguage.setMinimumSize(QSize(160, 50))

        self.gridLayout.addWidget(self.lblLanguage, 1, 0, 1, 1)

        self.cbLanguage = QComboBox(self.groupBox)
        self.cbLanguage.addItem("")
        self.cbLanguage.setObjectName(u"cbLanguage")
        self.cbLanguage.setMinimumSize(QSize(120, 50))

        self.gridLayout.addWidget(self.cbLanguage, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)

        self.btnAccept = QPushButton(Dialog)
        self.btnAccept.setObjectName(u"btnAccept")
        self.btnAccept.setMinimumSize(QSize(130, 50))

        self.gridLayout_2.addWidget(self.btnAccept, 1, 0, 1, 1)

        self.btnReject = QPushButton(Dialog)
        self.btnReject.setObjectName(u"btnReject")
        self.btnReject.setMinimumSize(QSize(130, 50))

        self.gridLayout_2.addWidget(self.btnReject, 1, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Application settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Parameters", None))
        self.cbTheme.setItemText(0, QCoreApplication.translate("Dialog", u"Fusion", None))

        self.lblTheme.setText(QCoreApplication.translate("Dialog", u"Select a topic", None))
        self.lblLanguage.setText(QCoreApplication.translate("Dialog", u"Select language", None))
        self.cbLanguage.setItemText(0, QCoreApplication.translate("Dialog", u"eu", None))

        self.btnAccept.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.btnReject.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

