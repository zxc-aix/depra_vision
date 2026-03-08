import sys

from PySide6.QtCore import QLibraryInfo, QLocale, QTranslator
from PySide6.QtWidgets import QApplication, QStyleFactory

from app.config.paths import PREDICTIONS_DIR, VIDEOS_DIR, ensure_dirs
from app.controllers.app_controller import AppController
from app.state import StateManager
from app.ui import SplashScreen, VideoPlayer


def run():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    
    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))

    translator = QTranslator()

    qt_translations_path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)

    translator.load("qtbase_en", qt_translations_path)
    app.installTranslator(translator)

    # print(translator.load("qtbase_en", qt_translations_path))
    # print(qt_translations_path)

    splash = SplashScreen()


    window = create_application()
    finish_startup(splash, window)

    sys.exit(app.exec())

def create_application():
    ensure_dirs()
    main_window = VideoPlayer()
    state = StateManager()
    controller = AppController(main_window, state, PREDICTIONS_DIR, VIDEOS_DIR)
    main_window.controller = controller

    return main_window

def finish_startup(splash, window):
    window.show()
    splash.finish(window)
