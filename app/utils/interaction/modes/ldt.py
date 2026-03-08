from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QColor, QPainter, QPen, QBrush
from PySide6.QtCore import Qt, QRectF, QPointF

class LDTHandler(BaseModeHandler):
    
    def __init__(self):
        super().__init__()
        self.colors = {
            "radius": QColor(33, 150, 243, 180), 
            "light": QColor(227, 242, 253, 150), 
            "dark": QColor(187, 222, 251, 170)  
            
        }

    def paint_additional(self, painter):
        points = self.points
        n = len(points)
        if not points:
            return
        
        colors = self.colors
        
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 1))

        p = points[0]
        rects = self._create_qrect(p)

        painter.setPen(QPen(Qt.black, 1))
        for key in rects.keys():
            painter.setBrush(QBrush(self.colors[key]))
            painter.drawRect(rects[key])

        painter.setBrush(QBrush(colors["radius"]))
        painter.drawEllipse(p, self.params['radius'], self.params['radius'])

        pen = QPen(Qt.white, 3)  
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(
            QPointF(p.x() - self.params["SizePass"]/2, p.y()), 
            QPointF(p.x() + self.params["SizePass"]/2, p.y())
        )

    def _create_qrect(self, point):
        length_light = self.params['lengthArmsLight']
        width_light = self.params['widthArmsLight']
        length_dark = self.params['lengthArmsDark']
        width_dark = self.params['widthArmsDark']

        x, y = point.x(), point.y()

        return {
            "light": QRectF(x - length_light/2, y - width_light, length_light, width_light),
            "dark": QRectF(x - length_dark/2, y, length_dark, width_dark),
        }
        