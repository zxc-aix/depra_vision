from PySide6.QtCore import QLineF, QPoint, QPointF, QRectF
from PySide6.QtGui import QColor, QPainter, QPen, Qt
import numpy as np
from .base_zone_drawer import BaseZoneDrawer

class TCSoneDrawer(BaseZoneDrawer):
    
    def __init__(self, data=None, settings=None, cfg=None):
        super().__init__(data, settings, cfg)
        self.colors = {
            "center": QColor(144, 202, 248, 120),
            "left": QColor(227, 242, 253, 120), 
            "right": QColor(100, 181, 246, 150),
            "object": QColor(12, 83, 204, 180)
        }
    
    def draw(self, painter: QPainter):
        visual_center = self.data["visual_center"]
        factor = self.data["factor"]

        sizePass = self.cfg["SizePass"] * factor/2

        rects, dots = self._create_qrect(visual_center, factor)
        
        painter.setPen(self.get_pen())

        for key in rects.keys():
            painter.setBrush(self.get_brush(key))
            painter.drawRect(rects[key])
      
        if self.cfg.get("countObject", 0) > 0:
            self.draw_objects(painter, self.cfg)


        pen = QPen(Qt.white, 3)  
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        for i in range(2):
            if dots[i] != -1:
                painter.drawLine(
                    QPointF(dots[i], visual_center[1] - sizePass), 
                    QPointF(dots[i], visual_center[1] + sizePass)
                )
    
    def draw_objects(self, painter: QPainter, cfg):
        points = self.data.get("visual_dots", [])
        factor = self.data["factor"]
        
        painter.setBrush(self.get_brush("object"))
        painter.setPen(self.get_pen())
        
        for i, point in enumerate(points):
            x, y = point
            radius = cfg.get('areaInt', 10) * factor / 2
            
            painter.drawEllipse(QPoint(int(x), int(y)), radius, radius)
            
            if self.should_draw_text:
                painter.setPen(QPen(QColor(255, 255, 255)))
                self.draw_text(painter, x, y, str(i + 1))
                painter.setPen(self.get_pen())

    def _create_qrect(self, p, factor):
        y = self.cfg.get("width", 0) * factor
        x = self.cfg.get("length", 0) * factor
        x1 = self.cfg.get("length_left", 0) * factor
        x2 = self.cfg.get("length_right", 0) * factor

        x2_shift = x/2 - x2
        rects = {
            "center": QRectF(p[0] - x/2, p[1] - y/2, x, y),
            "left": QRectF(p[0] - x/2, p[1] - y/2, x1, y),
            "right": QRectF(p[0] + x2_shift, p[1] - y/2, x2, y)
        }
        lines_dots = []
        
        if rects["left"].height() * rects["left"].width() > 0:
            lines_dots.append(p[0] - x/2 + x1)
        else:
            lines_dots.append(-1)
        
        if rects["right"].height() * rects["right"].width() > 0:
            lines_dots.append(p[0] + x2_shift)
        else:
            lines_dots.append(-1)
        
        return rects, lines_dots