from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QFont
from PySide6.QtWidgets import QWidget

class BaseZoneDrawer:
    
    def __init__(self, data, settings, cfg):
        super().__init__()
        self.data = data
        self.settings = settings
        self.cfg = cfg
        self.colors = {}
        
    def draw(self, painter: QPainter):
        pass
    
    def get_pen(self, style=Qt.SolidLine):
        if not self.settings.get("Wrap", False):
            return Qt.NoPen
        
        color = Qt.black if not self.settings.get("AddZones", True) else QColor(33, 150, 243)
        pen_width = max(0.5, self.settings.get("WidthMarkup", 1))
        
        pen = QPen(color, pen_width, style)
        pen.setCosmetic(False)
        return pen
    
    def get_brush(self, zone_type=None):
        if not self.settings.get("AddZones", True):
            return Qt.NoBrush
        
        if zone_type:
            colors = self.colors
            return QBrush(colors.get(zone_type, QColor(200, 200, 0, 50)))
        
        return Qt.NoBrush
    
    def draw_text(self, painter: QPainter, x, y, text):
        font_metrics = painter.fontMetrics()
        text_width = font_metrics.horizontalAdvance(text)
        text_height = font_metrics.height()
        text_x = x - text_width / 2
        text_y = y + text_height / 4
        
        painter.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        painter.drawText(int(text_x), int(text_y), text)
    
    @property
    def should_draw_text(self):
        return self.settings.get("Wrap", False) or self.settings.get("AddZones", False)