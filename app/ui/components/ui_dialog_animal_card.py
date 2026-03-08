# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_animal_card.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_animalCard(object):
    def setupUi(self, animalCard):
        if not animalCard.objectName():
            animalCard.setObjectName(u"animalCard")
        animalCard.resize(430, 471)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(animalCard.sizePolicy().hasHeightForWidth())
        animalCard.setSizePolicy(sizePolicy)
        animalCard.setMinimumSize(QSize(430, 470))
        self.gridLayout = QGridLayout(animalCard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.leId = QLineEdit(animalCard)
        self.leId.setObjectName(u"leId")
        self.leId.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.leId, 2, 1, 1, 1)

        self.btnCancel = QPushButton(animalCard)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.btnCancel, 12, 1, 1, 1)

        self.leAge = QLineEdit(animalCard)
        self.leAge.setObjectName(u"leAge")
        self.leAge.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.leAge, 3, 1, 1, 1)

        self.btnReset = QPushButton(animalCard)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setMinimumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.btnReset, 11, 0, 1, 1)

        self.lblCountAnimal = QLabel(animalCard)
        self.lblCountAnimal.setObjectName(u"lblCountAnimal")
        self.lblCountAnimal.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblCountAnimal, 1, 0, 1, 1)

        self.leWeight = QLineEdit(animalCard)
        self.leWeight.setObjectName(u"leWeight")
        self.leWeight.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.leWeight, 4, 1, 1, 1)

        self.cbColor = QComboBox(animalCard)
        self.cbColor.setObjectName(u"cbColor")
        self.cbColor.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.cbColor, 5, 1, 1, 1)

        self.cbSubLine = QComboBox(animalCard)
        self.cbSubLine.setObjectName(u"cbSubLine")
        self.cbSubLine.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.cbSubLine, 9, 1, 1, 1)

        self.cbModel = QComboBox(animalCard)
        self.cbModel.setObjectName(u"cbModel")
        self.cbModel.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.cbModel, 7, 1, 1, 1)

        self.chbDefault = QCheckBox(animalCard)
        self.chbDefault.setObjectName(u"chbDefault")
        self.chbDefault.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.chbDefault, 0, 1, 1, 1)

        self.lblName = QLabel(animalCard)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)

        self.lblId = QLabel(animalCard)
        self.lblId.setObjectName(u"lblId")
        self.lblId.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblId, 2, 0, 1, 1)

        self.lblColor = QLabel(animalCard)
        self.lblColor.setObjectName(u"lblColor")
        self.lblColor.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblColor, 5, 0, 1, 1)

        self.cbType = QComboBox(animalCard)
        self.cbType.setObjectName(u"cbType")
        self.cbType.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.cbType, 6, 1, 1, 1)

        self.lblLine = QLabel(animalCard)
        self.lblLine.setObjectName(u"lblLine")
        self.lblLine.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblLine, 8, 0, 1, 1)

        self.lblAge = QLabel(animalCard)
        self.lblAge.setObjectName(u"lblAge")
        self.lblAge.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblAge, 3, 0, 1, 1)

        self.lblWeight = QLabel(animalCard)
        self.lblWeight.setObjectName(u"lblWeight")
        self.lblWeight.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblWeight, 4, 0, 1, 1)

        self.lblModel = QLabel(animalCard)
        self.lblModel.setObjectName(u"lblModel")
        self.lblModel.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblModel, 7, 0, 1, 1)

        self.lblType = QLabel(animalCard)
        self.lblType.setObjectName(u"lblType")
        self.lblType.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblType, 6, 0, 1, 1)

        self.lblSubLine = QLabel(animalCard)
        self.lblSubLine.setObjectName(u"lblSubLine")
        self.lblSubLine.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.lblSubLine, 9, 0, 1, 1)

        self.btnAccept = QPushButton(animalCard)
        self.btnAccept.setObjectName(u"btnAccept")
        self.btnAccept.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.btnAccept, 12, 0, 1, 1)

        self.cbLine = QComboBox(animalCard)
        self.cbLine.setObjectName(u"cbLine")
        self.cbLine.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.cbLine, 8, 1, 1, 1)

        self.spinbCountAnimal = QSpinBox(animalCard)
        self.spinbCountAnimal.setObjectName(u"spinbCountAnimal")
        self.spinbCountAnimal.setMinimumSize(QSize(200, 30))

        self.gridLayout.addWidget(self.spinbCountAnimal, 1, 1, 1, 1)

        self.checkbSave = QCheckBox(animalCard)
        self.checkbSave.setObjectName(u"checkbSave")
        self.checkbSave.setMinimumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.checkbSave, 11, 1, 1, 1)


        self.retranslateUi(animalCard)

        QMetaObject.connectSlotsByName(animalCard)
    # setupUi

    def retranslateUi(self, animalCard):
        animalCard.setWindowTitle(QCoreApplication.translate("animalCard", u"Animal card", None))
        self.btnCancel.setText(QCoreApplication.translate("animalCard", u"Cancel", None))
        self.btnReset.setText(QCoreApplication.translate("animalCard", u"Reset", None))
        self.lblCountAnimal.setText(QCoreApplication.translate("animalCard", u"Number of animals", None))
        self.chbDefault.setText(QCoreApplication.translate("animalCard", u"by default", None))
        self.lblName.setText(QCoreApplication.translate("animalCard", u"Animal card", None))
        self.lblId.setText(QCoreApplication.translate("animalCard", u"Individual animal number", None))
        self.lblColor.setText(QCoreApplication.translate("animalCard", u"Animal color", None))
        self.lblLine.setText(QCoreApplication.translate("animalCard", u"-", None))
        self.lblAge.setText(QCoreApplication.translate("animalCard", u"Age of animal, weeks", None))
        self.lblWeight.setText(QCoreApplication.translate("animalCard", u"Animal weight, g", None))
        self.lblModel.setText(QCoreApplication.translate("animalCard", u"Model animal", None))
        self.lblType.setText(QCoreApplication.translate("animalCard", u"Type of animal", None))
        self.lblSubLine.setText(QCoreApplication.translate("animalCard", u"-", None))
        self.btnAccept.setText(QCoreApplication.translate("animalCard", u"Confirm", None))
        self.checkbSave.setText(QCoreApplication.translate("animalCard", u"save the entered parameters", None))
    # retranslateUi

