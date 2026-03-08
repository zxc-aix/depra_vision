from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, Signal

class RangeSlider(QWidget):
    rangeChanged = Signal(int, int)
    handleMoved = Signal(str, int)

    def __init__(self, minimum=0, maximum=10000):
        super().__init__()
        self.setMinimumHeight(30)
        self._min = minimum
        self._max = maximum
        self.start = minimum
        self.end = maximum
        self._drag = None
        self.handle_width = 10

    def paintEvent(self, event):
        painter = QPainter(self)
        w = self.width()
        h = self.height()

        x1 = self.value_to_pos(self.start)
        x2 = self.value_to_pos(self.end)

        painter.setBrush(QColor("#cccccc"))
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, h // 3, w, h // 3)

        painter.setBrush(QColor("#747474"))
        painter.drawRect(x1, h / 3, x2 - x1, h / 3)

        radius = self.handle_width * 1.5  
        cy = h / 2
        
        painter.setBrush(QColor("#363636"))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(int(x1 - radius / 2), int(cy - radius / 2), int(radius), int(radius))
        painter.drawEllipse(int(x2 - radius / 2), int(cy - radius / 2), int(radius), int(radius))

    def mousePressEvent(self, event):
        x = event.position().x()
        x1 = self.value_to_pos(self.start)
        x2 = self.value_to_pos(self.end)

        if abs(x - x1) < 10:
            self._drag = 'start'
        elif abs(x - x2) < 10:
            self._drag = 'end'

    def mouseMoveEvent(self, event):
        x = event.position().x()
        val = self.pos_to_value(x)
        if self._drag == 'start':
            self.start = min(val, self.end)
            self.handleMoved.emit('start', self.start)
        elif self._drag == 'end':
            self.end = max(val, self.start)
            self.handleMoved.emit('end', self.end)
        self.rangeChanged.emit(self.start, self.end)
        self.update()

    def mouseReleaseEvent(self, event):
        self._drag = None

    def value_to_pos(self, val):
        return int((val - self._min) / (self._max - self._min) * self.width())

    def pos_to_value(self, pos):
        val = int(pos / self.width() * (self._max - self._min) + self._min)
        return max(self._min, min(self._max, val))