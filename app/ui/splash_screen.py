from PySide6.QtWidgets import QSplashScreen
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont

class SplashScreen(QSplashScreen):
    def __init__(self):
        pixmap = QPixmap(400, 200)
        pixmap.fill(Qt.white)
        super().__init__(pixmap)
        
        self.setFont(QFont("Arial", 12))
        self.showMessage("Loading application...", 
                        Qt.AlignBottom | Qt.AlignHCenter, 
                        Qt.black)
        
        self.show()