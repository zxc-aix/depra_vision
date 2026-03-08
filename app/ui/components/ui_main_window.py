# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1050, 811)
        mainWindow.setMinimumSize(QSize(800, 500))
        mainWindow.setStyleSheet(u"")
        self.action_settings = QAction(mainWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.action_about = QAction(mainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_theme_language = QAction(mainWindow)
        self.action_theme_language.setObjectName(u"action_theme_language")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setMinimumSize(QSize(140, 50))
        self.btnStop.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnStop, 18, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.viewVideo = QGraphicsView(self.centralwidget)
        self.viewVideo.setObjectName(u"viewVideo")
        self.viewVideo.setMinimumSize(QSize(800, 600))
        self.viewVideo.setStyleSheet(u"background-color: black;")

        self.verticalLayout.addWidget(self.viewVideo)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 13, 3)

        self.btnOpen = QPushButton(self.centralwidget)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setMinimumSize(QSize(140, 50))
        self.btnOpen.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnOpen, 4, 3, 1, 1)

        self.progressSlider = QSlider(self.centralwidget)
        self.progressSlider.setObjectName(u"progressSlider")
        self.progressSlider.setMinimumSize(QSize(580, 30))
        self.progressSlider.setStyleSheet(u"")
        self.progressSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.progressSlider, 16, 0, 1, 3)

        self.btnPlay = QPushButton(self.centralwidget)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setMinimumSize(QSize(140, 50))
        self.btnPlay.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnPlay, 18, 0, 1, 1)

        self.btnPause = QPushButton(self.centralwidget)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setMinimumSize(QSize(140, 50))
        self.btnPause.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnPause, 18, 1, 1, 1)

        self.btnSettings = QPushButton(self.centralwidget)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(140, 50))
        self.btnSettings.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnSettings, 5, 3, 1, 1)

        self.lblTime = QLabel(self.centralwidget)
        self.lblTime.setObjectName(u"lblTime")
        self.lblTime.setMinimumSize(QSize(580, 20))
        self.lblTime.setStyleSheet(u"")
        self.lblTime.setScaledContents(False)
        self.lblTime.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lblTime, 15, 0, 1, 3)

        self.btnAnimalCard = QPushButton(self.centralwidget)
        self.btnAnimalCard.setObjectName(u"btnAnimalCard")
        self.btnAnimalCard.setMinimumSize(QSize(140, 50))
        self.btnAnimalCard.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnAnimalCard, 6, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(180, 50))
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.TextFormat.AutoText)

        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)

        self.btnTrim = QPushButton(self.centralwidget)
        self.btnTrim.setObjectName(u"btnTrim")
        self.btnTrim.setMinimumSize(QSize(140, 50))
        self.btnTrim.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnTrim, 7, 3, 1, 1)

        self.btnTrajectory = QPushButton(self.centralwidget)
        self.btnTrajectory.setObjectName(u"btnTrajectory")
        self.btnTrajectory.setMinimumSize(QSize(140, 50))
        self.btnTrajectory.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnTrajectory, 13, 3, 1, 1)

        self.btnHeatmap = QPushButton(self.centralwidget)
        self.btnHeatmap.setObjectName(u"btnHeatmap")
        self.btnHeatmap.setMinimumSize(QSize(140, 50))
        self.btnHeatmap.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnHeatmap, 12, 3, 1, 1)

        self.btnDetect = QPushButton(self.centralwidget)
        self.btnDetect.setObjectName(u"btnDetect")
        self.btnDetect.setMinimumSize(QSize(140, 50))
        self.btnDetect.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnDetect, 11, 3, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1050, 22))
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_settings.setToolTipsVisible(True)
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_about.setToolTipsVisible(True)
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_settings.addAction(self.action_settings)
        self.menu_settings.addAction(self.action_theme_language)
        self.menu_about.addAction(self.action_about)
        self.menu_about.addSeparator()

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"DepraAI", None))
        self.action_settings.setText(QCoreApplication.translate("mainWindow", u"Path", None))
        self.action_about.setText(QCoreApplication.translate("mainWindow", u"About author", None))
        self.action_theme_language.setText(QCoreApplication.translate("mainWindow", u"Change theme and language", None))
        self.btnStop.setText(QCoreApplication.translate("mainWindow", u"Stop", None))
        self.btnOpen.setText(QCoreApplication.translate("mainWindow", u"Open video file", None))
        self.btnPlay.setText(QCoreApplication.translate("mainWindow", u"Play", None))
        self.btnPause.setText(QCoreApplication.translate("mainWindow", u"Pause", None))
        self.btnSettings.setText(QCoreApplication.translate("mainWindow", u"File parameters", None))
        self.lblTime.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">00:00 / 00:00</span></p></body></html>", None))
        self.btnAnimalCard.setText(QCoreApplication.translate("mainWindow", u"Animal card", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btnTrim.setText(QCoreApplication.translate("mainWindow", u"Trim video", None))
        self.btnTrajectory.setText(QCoreApplication.translate("mainWindow", u"Trajectory", None))
        self.btnHeatmap.setText(QCoreApplication.translate("mainWindow", u"Activity map", None))
        self.btnDetect.setText(QCoreApplication.translate("mainWindow", u"Detect", None))
        self.menu_settings.setTitle(QCoreApplication.translate("mainWindow", u"Settings", None))
        self.menu_about.setTitle(QCoreApplication.translate("mainWindow", u"Reference", None))
    # retranslateUi

