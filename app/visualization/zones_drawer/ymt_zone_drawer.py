from PySide6.QtGui import QPainter, QPen, Qt, QColor, QBrush, QPolygonF
from PySide6.QtCore import QLineF, QPoint, QPointF
import numpy as np
from .base_zone_drawer import BaseZoneDrawer

class YMTZoneDrawer(BaseZoneDrawer):
    
    def __init__(self, data=None, settings=None, cfg=None):
        super().__init__(data, settings, cfg)
        self.colors = {
            "0": QColor(187, 222, 251, 180),
            "1": QColor(227, 242, 253, 180),
            "2": QColor(144, 202, 248, 180),
            "object": QColor(12, 83, 204, 180)
        }
    
    def draw(self, painter: QPainter):
        visual_center = self.data["visual_center"]
        factor = self.data["factor"]
        self.phi0 = -90
        lengthArms = self.cfg['lengthArms'] * factor
        widthArms = self.cfg['widthArms'] * factor
        
        
        painter.setPen(self.get_pen())

        r = widthArms * np.sqrt(3) / 6
        for i in range(3):
            a = np.radians(self.phi0 + self.cfg[f"alpha{i+1}"]) # self.cfg['angleArms'] + 
            point = QPointF(visual_center[0] + (r * np.cos(a)), visual_center[1] + (r * np.sin(a)))
            polygon = self.make_branch(point, lengthArms, widthArms, a)

            painter.setBrush(self.get_brush(str(i)))
            painter.drawPolygon(polygon)
        
        # Рисуем объекты
        if self.cfg.get("countObject", 0) > 0:
            self.draw_objects(painter, self.cfg)

        self.data["visual_points"] = self.rotate_points_around_center(self.data["visual_points"], self.cfg['angleArms'], visual_center)
        
    
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
    

    def rotate_points_around_center(self, df, angle_degrees, center, x_col='xc', y_col='yc'):
        result = df.copy()
        
        theta = np.radians(angle_degrees)
        
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        
        x_relative = result[x_col] - center[0]
        y_relative = result[y_col] - center[1]
        
        x_rotated = x_relative * cos_theta - y_relative * sin_theta
        y_rotated = x_relative * sin_theta + y_relative * cos_theta
        
        result[f'{x_col}'] = x_rotated + center[0]
        result[f'{y_col}'] = y_rotated + center[1]
        
        return result