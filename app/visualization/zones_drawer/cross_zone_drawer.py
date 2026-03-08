from PySide6.QtGui import QPainter, QPen, Qt, QColor, QPainterPath
from PySide6.QtCore import QPoint, QRectF
from .base_zone_drawer import BaseZoneDrawer

class CrossZoneDrawer(BaseZoneDrawer):

    def __init__(self, data=None, settings=None, cfg=None):
        super().__init__(data, settings, cfg)
        self.colors = {
            "open": QColor(187, 222, 251, 150),
            "close": QColor(100, 181, 246, 150),
            "center": QColor(227, 242, 253, 150)
        }
    
    def draw(self, painter: QPainter):
        visual_center = self.data["visual_center"]
        factor = self.data["factor"]

        open_path = QPainterPath()
        close_path = QPainterPath()
        center_path = QPainterPath()
        
        rects = self._create_qrect(visual_center, factor)

        for key in rects.keys():
            path = QPainterPath()
            path.addRect(rects[key]) 
            
            if key == "center": center_path.addPath(path)
            if self.cfg[key]:
                open_path.addPath(path)
            else:
                close_path.addPath(path)

        painter.setPen(self.get_pen())
        if not open_path.isEmpty():
            painter.setBrush(self.get_brush("open"))
            painter.drawPath(open_path)

        if not close_path.isEmpty():
            painter.setBrush(self.get_brush("close"))
            painter.drawPath(close_path)

        painter.setBrush(self.get_brush("center"))
        painter.drawPath(center_path)

    def _create_qrect(self, point, factor):
        length = self.cfg['lengthArms'] * factor
        width = self.cfg['widthArms'] * factor
        x, y = point

        return {
            "center": QRectF(x - width/2, y - width/2, width, width),
            "up": QRectF(x - width/2, y - width/2 - length, width, length),
            "right": QRectF(x + width/2, y - width/2, length, width),
            "down": QRectF(x - width/2, y + width/2, width, length),
            "left": QRectF(x - width/2 - length, y - width/2, length, width),
        }