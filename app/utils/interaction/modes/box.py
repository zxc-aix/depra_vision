from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QColor, QBrush, QPen
from PySide6.QtCore import Qt, QRect

class BoxHandler(BaseModeHandler):

    def __init__(self):
        super().__init__()
        self.colors = {
            "large": QColor(227, 242, 253, 150), 
            "medium": QColor(187, 222, 251, 170), 
            "small": QColor(144, 202, 248, 180)
        }

    def paint_additional(self, painter):
        points = self.points
        n = len(points)
        if not points:
            return

        rects = self._create_qrect(points[0])
        painter.setPen(QPen(Qt.black, 1))
        for key in rects.keys():
            painter.setBrush(QBrush(self.colors[key]))
            painter.drawRect(rects[key])

        if self.params["countObject"] > 0 and n > 1:
            painter.setBrush(QColor(12, 83, 204, 180)) 
            # print("[DRAW AREA]")
            
            for i in range(1, n):
                painter.drawEllipse(points[i], self.params['areaInt']/2, self.params['areaInt']/2)
                # text = str(i) 
                # font_metrics = painter.fontMetrics()

                # text_width = font_metrics.horizontalAdvance(text)
                # text_height = font_metrics.height()
                # text_x = points[i].x() - text_width / 2
                # text_y = points[i].y() + text_height / 4 
                
                # painter.setPen(QColor(255, 255, 255))
                # painter.setFont(QFont("Arial", 10, QFont.Weight.Bold))
                # painter.drawText(int(text_x), int(text_y), text)
                # painter.setPen(Qt.NoPen)
        
                

    def _create_qrect(self, p_center):
        return {
            "large": QRect(p_center.x()-self.params["large"]/2, p_center.y()-self.params["large"]/2, self.params["large"], self.params["large"]),
            "medium": QRect(p_center.x()-self.params["medium"]/2, p_center.y()-self.params["medium"]/2, self.params["medium"], self.params["medium"]),
            "small": QRect(p_center.x()-self.params["small"]/2, p_center.y()-self.params["small"]/2, self.params["small"], self.params["small"])
        }
            

