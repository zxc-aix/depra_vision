from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QColor, QPolygonF, QPen
from PySide6.QtCore import QPointF, Qt
import numpy as np

class YMTHandler(BaseModeHandler):
    
    def __init__(self):
        super().__init__()
        self.colors = {
            0: QColor(187, 222, 251, 180),
            1: QColor(227, 242, 253, 180),
            2: QColor(144, 202, 248, 180)
        }
        self.phi0 = -90

    def paint_additional(self, painter):
        points = self.points
        n = len(points)

        if not points:
            return
    
        colors = self.colors
        r = self.params['widthArms'] * np.sqrt(3) / 6
        p1 = points[0]

        painter.setPen(QPen(Qt.black, 1))
        for i in range(3):
            a = np.radians(self.params['angleArms'] + self.phi0 + self.params[f"alpha{i+1}"])
            point = QPointF(p1.x() + (r * np.cos(a)), p1.y() + (r * np.sin(a)))
            polygon = self.make_branch(point, self.params['lengthArms'], self.params['widthArms'], a)

            painter.setBrush(colors[i])
            painter.drawPolygon(polygon)


        if self.params["countObject"] > 0 and n > 1:
            painter.setBrush(QColor(12, 83, 204, 180)) 

            for i in range(1, n):
                painter.drawEllipse(points[i], self.params['areaInt']/2, self.params['areaInt']/2)


    def make_branch(self, A: QPointF, L: float, W: float, angle: float) -> QPolygonF:
        """Создаёт прямоугольный луч длиной L и шириной W под углом angle"""
        # Направляющий вектор
        dx = np.cos(angle)
        dy = np.sin(angle)

        # Нормаль
        nx = -dy
        ny = dx

        h = W / 2.0
        # 4 вершины прямоугольного луча
        p1 = QPointF(A.x() + nx * h, A.y() + ny * h)
        p2 = QPointF(A.x() + dx * L + nx * h, A.y() + dy * L + ny * h)
        p3 = QPointF(A.x() + dx * L - nx * h, A.y() + dy * L - ny * h)
        p4 = QPointF(A.x() - nx * h, A.y() - ny * h)

        return QPolygonF([p1, p2, p3, p4])