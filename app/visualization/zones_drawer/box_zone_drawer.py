from PySide6.QtGui import QPainter, QPen, Qt, QColor
from PySide6.QtCore import QPoint
from .base_zone_drawer import BaseZoneDrawer

class BoxZoneDrawer(BaseZoneDrawer):

    def __init__(self, data=None, settings=None, cfg=None):
        super().__init__(data, settings, cfg)
        self.colors = {
            "small": QColor(144, 202, 248, 250),
            "medium": QColor(187, 222, 251, 250),
            "large": QColor(227, 242, 253, 250),
            "object": QColor(12, 83, 204, 180)
        }
    
    def draw(self, painter: QPainter):
        visual_center = self.data["visual_center"]
        factor = self.data["factor"]
        
        # Рисуем зоны
        for zone_name in ["large", "medium", "small"]:
            size = self.cfg.get(zone_name, 0) / 2 * factor
            
            painter.setBrush(self.get_brush(zone_name))
            
            if zone_name in ["small", "medium"]:
                painter.setPen(self.get_pen(Qt.DashLine))
            else:
                painter.setPen(self.get_pen())
            
            painter.drawRect(
                visual_center[0] - size,
                visual_center[1] - size,
                size * 2,
                size * 2
            )
        
        # Рисуем объекты
        if self.cfg.get("countObject", 0) > 0:
            self.draw_objects(painter, self.cfg)
    
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