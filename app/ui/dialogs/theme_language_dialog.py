from PySide6.QtWidgets import QDialog
from app.ui.components import UI_ThemeLanguage

class ThemeLanguageDialog(QDialog, UI_ThemeLanguage):
    def __init__(self, app_configure, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.app_configure = app_configure

        self._setup_signals()
        self.set_settings()

    def _setup_signals(self):
        self.btnAccept.clicked.connect(self.accept)
        self.btnReject.clicked.connect(self.reject)

    def get_configure(self):
        return {
            "theme": self.cbTheme.currentText(),
            "language": self.cbLanguage.currentText()
        }
    
    def set_settings(self, theme="Fusion", language="eu"):
        self.cbTheme.setCurrentText(self.app_configure.theme)
        self.cbLanguage.setCurrentText(self.app_configure.language)