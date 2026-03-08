import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from .base_analyzer import BaseAnalyzer

class YMTAnalyzer(BaseAnalyzer):
    def __init__(self, points=None, config=None, add_params=None):
        super().__init__(points, config, add_params)

    def _setting(self):
        self.phi0 = -90
        self.cfg = self.config.ymt
        self.zones = self._create_zones(self.config.p_center)
        self.draw_zones()
        print("DEGUG: Всё настроено")

    def _create_zones(self, point):
        x, y = self.transform_dot_to_cm(point)
        
        r = self.cfg['widthArms'] * np.sqrt(3) / 6
        
        polygons = []
        for i in range(3):
            a = np.radians(-self.cfg['angleArms'] + self.phi0 + self.cfg[f"alpha{i+1}"])
            point_center = (x + (r * np.cos(a)), y + (r * np.sin(a)))
            polygon = self.make_branch(point_center, self.cfg['lengthArms'], self.cfg['widthArms'], a)
            polygons.append(polygon)
        
        # Создаем центральный треугольник
        a = np.radians(self.cfg['angleArms'] + self.phi0 + self.cfg["alpha1"])
        b = np.radians(self.cfg['angleArms'] + self.phi0 + self.cfg["alpha2"])
        c = np.radians(self.cfg['angleArms'] + self.phi0 + self.cfg["alpha3"])
        
        r_triangle = self.cfg['widthArms'] * np.sqrt(3) / 3
        v1 = (x + r_triangle * np.cos(a), y + r_triangle * np.sin(a))
        v2 = (x + r_triangle * np.cos(b), y + r_triangle * np.sin(b))
        v3 = (x + r_triangle * np.cos(c), y + r_triangle * np.sin(c))
        polygon4 = Polygon([v1, v2, v3])
        
        return {
            "Ra": polygons[0],
            "Rb": polygons[1],
            "Rc": polygons[2],
            "center": polygon4
        }

    def make_branch(self, center: tuple, L: float, W: float, angle: float) -> Polygon:
        """Создаёт прямоугольный луч длиной L и шириной W под углом angle"""
        x_center, y_center = center
        
        # Направляющий вектор
        dx = np.cos(angle)
        dy = np.sin(angle)
        
        # Нормаль
        nx = -dy
        ny = dx
        h = W / 2.0
        
        # Ближняя левая
        p1_x = x_center + nx * h
        p1_y = y_center + ny * h
        
        # Дальняя левая
        p2_x = x_center + dx * L + nx * h
        p2_y = y_center + dy * L + ny * h
        
        # Дальняя правая
        p3_x = x_center + dx * L - nx * h
        p3_y = y_center + dy * L - ny * h
        
        # Ближняя правая
        p4_x = x_center - nx * h
        p4_y = y_center - ny * h
        
        return Polygon([(p1_x, p1_y), (p2_x, p2_y), (p3_x, p3_y), (p4_x, p4_y)])