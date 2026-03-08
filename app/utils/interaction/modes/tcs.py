from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QColor, QPen, QBrush
from PySide6.QtCore import QPointF, Qt, QRectF

class TCSHandler(BaseModeHandler):

    def __init__(self):
        super().__init__()
        self.colors = {
            "center": QColor(144, 202, 248, 120),
            "left": QColor(227, 242, 253, 120), 
            "right": QColor(100, 181, 246, 150)
        }

    def paint_additional(self, painter):
        points = self.points
        n = len(points)

        if not points:
            return
        
        colors = self.colors
        p1 = points[0]
        
        rects, dots = self._create_qrect(p1)

        painter.setPen(QPen(Qt.black, 1))
        for rect, color in zip(rects, colors.values()):
            painter.setBrush(QBrush(color))
            painter.drawRect(rect)


        if self.params["countObject"] > 0 and n > 1:
            painter.setBrush(QColor(12, 83, 204, 180)) 
            # print("[DRAW AREA]")
            
            for i in range(1, n):
                painter.drawEllipse(points[i], self.params['areaInt']/2, self.params['areaInt']/2)

        pen = QPen(Qt.white, 1)  
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        for i in range(2):
            if dots[i] != -1:
                painter.drawLine(
                    QPointF(dots[i], p1.y()- self.params["SizePass"]/2), 
                    QPointF(dots[i], p1.y()+ self.params["SizePass"]/2)
                    )
                
    def _create_qrect(self, p):
        y = self.params.get("width", 0)
        x = self.params.get("length", 0)
        x1 = self.params.get("length_left", 0)
        x2 = self.params.get("length_right", 0)

        x2_shift = x/2 - x2
        rects = [
            QRectF(p.x() - x/2, p.y() - y/2, x, y), # center
            QRectF(p.x() - x/2, p.y() - y/2, x1, y), # left
            QRectF(p.x() + x2_shift, p.y() - y/2, x2, y) # right
        ]
        lines_dots = []
        
        if rects[1].height() * rects[1].width() > 0:
            lines_dots.append(p.x() - x/2 + x1)
        else:
            lines_dots.append(-1)
        
        if rects[2].height() * rects[2].width() > 0:
            lines_dots.append(p.x() + x2_shift)
        else:
            lines_dots.append(-1)
        
        return rects, lines_dots