from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap

class InteractionLabel(QLabel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._handler = None
        self._pixmap_original = None

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

    def set_unscaled_pixmap(self, pixmap: QPixmap):
        self._pixmap_original = pixmap
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        if self._handler:
            self._handler.mouse_press_event(event)
            self.update()

    # def mouseMoveEvent(self, event):
    #     if self._handler:
    #         self._handler.mouse_move_event(event)
    #         self.update()

    # def mouseReleaseEvent(self, event):
    #     if self._handler:
    #         self._handler.mouse_release_event(event)
    #         self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self._handler:
            return
        painter = QPainter(self)
        self._handler.paint(painter)
