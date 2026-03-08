# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_output_results.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_resultInput(object):
    def setupUi(self, resultInput):
        if not resultInput.objectName():
            resultInput.setObjectName(u"resultInput")
        resultInput.resize(1000, 750)
        resultInput.setMinimumSize(QSize(1000, 750))
        self.gridLayout = QGridLayout(resultInput)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(resultInput)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 2)

        self.btnConfirm = QPushButton(resultInput)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setMinimumSize(QSize(80, 40))

        self.gridLayout.addWidget(self.btnConfirm, 1, 0, 1, 1)

        self.btnCancel = QPushButton(resultInput)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(80, 40))

        self.gridLayout.addWidget(self.btnCancel, 1, 1, 1, 1)


        self.retranslateUi(resultInput)

        QMetaObject.connectSlotsByName(resultInput)
    # setupUi

    def retranslateUi(self, resultInput):
        resultInput.setWindowTitle(QCoreApplication.translate("resultInput", u"Saving results to a table", None))
        self.btnConfirm.setText(QCoreApplication.translate("resultInput", u"Confirm", None))
        self.btnCancel.setText(QCoreApplication.translate("resultInput", u"Cancel", None))
    # retranslateUi

