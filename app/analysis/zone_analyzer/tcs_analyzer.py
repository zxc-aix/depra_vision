import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import box, Point
from .base_analyzer import BaseAnalyzer

class TCSAnalyzer(BaseAnalyzer):
    def __init__(self, points=None, config=None, add_params=None):
        super().__init__(points, config, add_params)

    def _setting(self):
        self.cfg = self.config.tcs
        self.zones = self._create_zones(self.config.p_center)

        self.draw_zones()
        print("DEGUG: Всё настроено")

    def _create_zones(self, p):
        x, y = self.transform_dot_to_cm(p)

        width = self.cfg.get("width", 0)
        length = self.cfg.get("length", 0)
        length_left = self.cfg.get("length_left", 0)
        length_right = self.cfg.get("length_right", 0)

        return {
            "left": box(
                x - length/2, 
                y - width/2, 
                x - length/2 + length_left, 
                y + width/2
            ),
            "right": box(
                x + length/2 - length_right,  
                y - width/2, 
                x + length/2,  
                y + width/2
            ), 
            "center": box(
                x - length/2 + length_left, 
                y - width/2, 
                x + length/2 - length_right,  
                y + width/2
            ) 
        }