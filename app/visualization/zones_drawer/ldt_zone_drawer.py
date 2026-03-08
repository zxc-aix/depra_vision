from PySide6.QtGui import QPainter, QPen, Qt, QColor
from PySide6.QtCore import QPointF, QRectF
from .base_zone_drawer import BaseZoneDrawer

class LDTZoneDrawer(BaseZoneDrawer):

    def __init__(self, data=None, settings=None, cfg=None):
        super().__init__(data, settings, cfg)
        self.colors = {
            "radius": QColor(33, 150, 243, 180), 
            "light": QColor(227, 242, 253, 150), 
            "dark": QColor(187, 222, 251, 170)   
        }
    
    def draw(self, painter: QPainter):
        visual_center = self.data["visual_center"]
        center = QPointF(visual_center[0], visual_center[1])
        factor = self.data["factor"]
        radius = self.cfg['radius'] * factor
        sizePass = self.cfg["SizePass"] * factor/2

        rects = self._create_qrect(visual_center, factor)

        painter.setPen(self.get_pen())
        for key in rects.keys():
            painter.setBrush(self.get_brush(key))
            painter.drawRect(rects[key])

        painter.setBrush(self.get_brush("radius"))
        painter.drawEllipse(center, radius, radius)

        pen = QPen(Qt.white, 3)  
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(
            QPointF(visual_center[0] - sizePass, visual_center[1]), 
            QPointF(visual_center[0] + sizePass, visual_center[1])
        )

    def _create_qrect(self, point, factor):
        length_light = self.cfg['lengthArmsLight'] * factor
        width_light = self.cfg['widthArmsLight'] * factor
        length_dark = self.cfg['lengthArmsDark'] * factor
        width_dark = self.cfg['widthArmsDark'] * factor

        x, y = point

        return {
            "light": QRectF(x - length_light/2, y - width_light, length_light, width_light),
            "dark": QRectF(x - length_dark/2, y, length_dark, width_dark),
        }