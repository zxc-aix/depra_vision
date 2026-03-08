from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QColor, QBrush, QPen
from PySide6.QtCore import Qt, QRectF

class CrossHandler(BaseModeHandler):
    
    def __init__(self):
        super().__init__()
        self.colors = {
            "open": QColor(187, 222, 251, 150),
            "close": QColor(100, 181, 246, 150),
            "center": QColor(227, 242, 253, 150)
        }

    def paint_additional(self, painter):
        points = self.points
        n = len(points)
        if not points:
            return
        # print(points)
        rects = self._create_qrect(points[0])

        painter.setPen(QPen(Qt.black, 1))
        for key in rects.keys():
            if self.params[key]:
                painter.setBrush(QBrush(self.colors["open"]))
                # print("open")
            else:
                painter.setBrush(QBrush(self.colors["close"]))
                # print("close")

            painter.drawRect(rects[key])

    def _create_qrect(self, point):
        length = self.params['lengthArms']
        width = self.params['widthArms']
        x, y = point.x(), point.y()

        return {
            "center": QRectF(x - width/2, y - width/2, width, width),
            "up": QRectF(x - width/2, y - width/2 - length, width, length),
            "right": QRectF(x + width/2, y - width/2, length, width),
            "down": QRectF(x - width/2, y + width/2, width, length),
            "left": QRectF(x - width/2 - length, y - width/2, length, width),
        }
