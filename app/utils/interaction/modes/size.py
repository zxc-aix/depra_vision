from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QFont
from PySide6.QtGui import QPen, QColor, QPainter

from PySide6.QtCore import QPoint, QPointF, Qt

class SizeHandler(BaseModeHandler):

    def __init__(self):
        super().__init__()

    def paint_additional(self, painter):
        if self.points and len(self.points) == 2:
            pen = QPen(Qt.red, 2, Qt.DashLine)
            painter.setPen(pen)
            p1 = self.points[0]
            p2 = self.points[1]
            painter.drawLine(int(p1.x()), int(p1.y()), int(p2.x()), int(p2.y()))

            mid_x = (p1.x() + p2.x()) / 2   
            mid_y = (p1.y() + p2.y()) / 2
            distance = ((p2.x() - p1.x())**2 + (p2.y() - p1.y())**2 )**0.5
            text = f"{distance:.2f} px"
            text_x = mid_x + 5
            text_y = mid_y - 5
            painter.setPen(QPen(Qt.black))
            # painter.setBrush(QColor(255, 255, 255, 200))
            # painter.drawRect(int(text_x)-2, int(text_y)-15, int(painter.fontMetrics().horizontalAdvance(text))+4, 18)
            painter.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            painter.drawText(int(text_x), int(text_y), text)
