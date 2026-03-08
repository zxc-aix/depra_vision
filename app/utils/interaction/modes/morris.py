from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QColor, QPainter, QPen, Qt, QBrush, QFont
from PySide6.QtCore import QLineF, QPointF
import numpy as np

class MorrisHandler(BaseModeHandler):
    
    def __init__(self):
        super().__init__()
        self.colors = {
            "space": QColor(227, 242, 253, 120), 
                "areaInt": QColor(144, 202, 249, 255), 
                "diam": QColor(33, 150, 243, 150), 
                "custom_fields": [
                    QColor(100,181,246, 150),    
                    QColor(66,165,245, 190),     
                    QColor(33,150,243, 220),     
                    QColor(165,221,249, 220),   
                    QColor(171,240,243, 200),   
                    QColor(168,246,196, 150),   
                ]
        }

    def paint_additional(self, painter):
        points = self.points
        n = len(points)

        if not points:
            return
        
        colors = self.colors
        params = self.params
        points_restored = self.points_restored
        
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 1))

        # Основное поле
        painter.setBrush(QBrush(colors["space"]))
        painter.drawEllipse(points[0], params["space"]/2, params["space"]/2)

        if n > 1:
            custom_diams = params.get("custom_fields", np.array([]))
            custom_colors = colors["custom_fields"]

            if len(custom_diams) > 0:
                for i in range(len(custom_diams)-1, -1, -1):
                    painter.setBrush(QBrush(custom_colors[i]))
                    painter.drawEllipse(points[1], custom_diams[i]/2, custom_diams[i]/2)

            painter.setBrush(QBrush(colors["areaInt"]))
            painter.drawEllipse(points[1], params['areaInt']/2, params['areaInt']/2)

        elif points_restored and len(points_restored) > 1:
            painter.setPen(QPen(Qt.gray, 4))
            dx = points[0].x() / points_restored[0].x()
            dy = points[0].y() / points_restored[0].y()

            p_restored = QPointF(points_restored[1].x() * dx, points_restored[1].y() * dy)
            painter.drawPoint(p_restored)

            font_metrics = painter.fontMetrics()
            text = "P restored"
            text_width = font_metrics.horizontalAdvance(text)
            text_height = font_metrics.height()
            text_x = p_restored.x() - text_width / 2
            text_y = p_restored.y() - text_height / 4 
            painter.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            painter.drawText(int(text_x), int(text_y), text)

            painter.setPen(QPen(Qt.black, 1))

        painter.setBrush(QBrush(colors["diam"]))
        painter.drawEllipse(points[0], params['diam']/2, params['diam']/2)
        
        line_h = QLineF(-params['field_size']/2, 0, params['field_size']/2, 0)
        line_v = QLineF(0, -params['field_size']/2, 0, params['field_size']/2)
        
        painter.save()  
        painter.translate(points[0])
        painter.rotate(params['angle'])
        
        painter.setPen(QPen(QColor("white"), 2, Qt.DashLine))
        painter.drawLine(line_h)
        painter.drawLine(line_v)
        
        painter.restore() 

