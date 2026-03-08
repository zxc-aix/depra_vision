from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPainter, QPixmap, QColor, QPen
from PySide6.QtCore import Qt, QRect

class SelectableLabel(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._handler = None

        self.setMouseTracking(True)
        self.setAlignment(Qt.AlignCenter)

    def set_handler(self, handler):
        if self._handler == handler:
            return
        
        if self._handler:
            self._handler.detach()

        self._handler = handler
        if self._handler:
            self._handler.attach(self)

        self.update()

    def clear_handler(self):
        self._handler = None
        self.update()

    def mousePressEvent(self, event):
        if self._handler:
            self._handler.mouse_press_event(event)
            self.update()
            
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self._handler:
            self._handler.mouse_move_event(event)
            self.update()
            # self.end_point = event.pos()
            # self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._handler:
            self._handler.mouse_release_event(event)
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self._handler:
            return
        painter = QPainter(self)
        self._handler.paint(painter)
