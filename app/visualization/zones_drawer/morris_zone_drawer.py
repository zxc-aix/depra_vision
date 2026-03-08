from PySide6.QtGui import QPainter, QPen, Qt, QColor, QBrush
from PySide6.QtCore import QLineF, QPointF
import numpy as np
from .base_zone_drawer import BaseZoneDrawer

class MorrisZoneDrawer(BaseZoneDrawer):
    
    def __init__(self, data=None, settings=None, cfg=None):
        super().__init__(data, settings, cfg)
        self.colors = {
            "space": QColor(227, 242, 253, 120), 
            "areaInt": QColor(144, 202, 249, 255), 
            "diam": QColor(33, 150, 243, 150), 
            "custom1": QColor(168,246,196, 150),
            "custom2": QColor(171,240,243, 200),
            "custom3": QColor(165,221,249, 220),
            "custom4": QColor(33,150,243, 220),
            "custom5": QColor(66,165,245, 190),
            "custom6": QColor(100,181,246, 150),

            # "custom_fields": [
            #     QColor(100,181,246, 150),    
            #     QColor(66,165,245, 190),     
            #     QColor(33,150,243, 220),     
            #     QColor(165,221,249, 220),   
            #     QColor(171,240,243, 200),   
            #     QColor(168,246,196, 150),   
            # ]
        }
    
    def draw(self, painter: QPainter):
        visual_center = self.data["visual_center"]
        center = QPointF(visual_center[0], visual_center[1])

        visual_dot = self.data["visual_dots"][0]
        # print(f"DEBUG: visual_dot = {visual_dot}")
        dot = QPointF(visual_dot[0], visual_dot[1])
        factor = self.data["factor"]

        space_radius = self.cfg["space"] * factor /2
        platform_radius = self.cfg['areaInt'] * factor /2
        radius = self.cfg['diam'] * factor /2
        field_size = self.settings['field_size'] * factor /2
        
        painter.setPen(self.get_pen())

        # Основное поле
        painter.setBrush(self.get_brush("space"))
        painter.drawEllipse(center, space_radius, space_radius)

        custom_diams = self.cfg.get("custom_fields", np.array([]))
        if len(custom_diams) > 0:
            for i in range(len(custom_diams)-1, -1, -1):
                painter.setBrush(self.get_brush(f"custom{i}"))
                painter.drawEllipse(dot, custom_diams[i]*factor/2, custom_diams[i]*factor/2)


        painter.setBrush(self.get_brush("areaInt"))
        painter.drawEllipse(dot, platform_radius, platform_radius)

        painter.setBrush(self.get_brush("diam"))
        painter.drawEllipse(center, radius, radius)
        
        line_h = QLineF(-field_size, 0, field_size, 0)
        line_v = QLineF(0, -field_size, 0, field_size)
        
        painter.save()  
        painter.translate(center)
        painter.rotate(self.cfg['angle'])
        
        painter.setPen(QPen(QColor("white"), 2, Qt.DashLine))
        painter.drawLine(line_h)
        painter.drawLine(line_v)
        
        painter.restore() 

  