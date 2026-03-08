import numpy as np
import pandas as pd
from shapely.geometry import box, Point
from shapely.ops import unary_union
from .base_analyzer import BaseAnalyzer

class CrossAnalyzer(BaseAnalyzer):
    def __init__(self, points=None, config=None, add_params=None):
        super().__init__(points, config, add_params)

    def _setting(self):
        self.cross_config = self.config.cross
        self.zones = self._create_zones(self.config.p_center)
        self.draw_zones()
        print("DEGUG: Всё настроено")

    def _create_zones(self, point):
        x, y = point
        x = x*self.pixel_size
        y = y*self.pixel_size

        length = self.cross_config['lengthArms']
        width = self.cross_config['widthArms']

        zones = {
            "center": box(x - width/2, y - width/2, x + width/2, y + width/2),
            "up": box(x - width/2, y - width/2 - length, x + width/2, y - width/2),
            "right": box(x + width/2, y - width/2, x + width/2 + length, y + width/2),
            "down": box(x - width/2, y + width/2, x + width/2, y + width/2 + length),
            "left": box(x - width/2 - length, y - width/2, x - width/2, y + width/2),
        }

        open_polygons = []
        close_polygons = []
        for key in zones.keys():
            if key == "center": continue

            if self.cross_config.get(key, False):
                open_polygons.append(zones[key])
                print(f"DEBUG: OPEN - {key}")
            else: 
                close_polygons.append(zones[key])
                print(f"DEBUG: CLOSE - {key}")
        return {
            "open": unary_union(open_polygons),
            "close": unary_union(close_polygons),
            "center": zones['center']
        }
    
    def _added_zones(self, stats, points):
        pass

    def _get_area_int(self, x, y, config):
        return "outer"
    