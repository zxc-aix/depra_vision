import numpy as np
import pandas as pd
from shapely.geometry import box, Point
from .base_analyzer import BaseAnalyzer

class BoxAnalyzer(BaseAnalyzer):
    def __init__(self, points=None, config=None, add_params=None):
        super().__init__(points, config, add_params)

    def _setting(self):
        self.cfg = self.config.box
        self.zones = self._create_zones(self.config.p_center)
        print("DEGUG: Всё настроено")

    def _create_zones(self, point):
        x, y = point
        x = x*self.pixel_size
        y = y*self.pixel_size

        zones = {}
        zone_names = ["small", "medium", "large"]

        for name in zone_names:
            size = self.cfg.get(name, 0)
            if size > 0:
                zones[name] = box(
                    x - size/2, y - size/2,
                    x + size/2, y + size/2
                )
        return zones