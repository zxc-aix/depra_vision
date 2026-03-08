import numpy as np
import pandas as pd
from shapely.geometry import box, Point
from .base_analyzer import BaseAnalyzer

class LDTAnalyzer(BaseAnalyzer):
    def __init__(self, points=None, config=None, add_params=None):
        super().__init__(points, config, add_params)

    def _setting(self):
        self.cfg = self.config.ldt
        self.zones = self._create_zones(self.config.p_center)
        self.draw_zones()
        print("DEGUG: Всё настроено")

    def _create_zones(self, point):
        x, y = self.transform_dot_to_cm(point)

        length_light = self.cfg['lengthArmsLight']
        width_light = self.cfg['widthArmsLight']
        length_dark = self.cfg['lengthArmsDark']
        width_dark = self.cfg['widthArmsDark']

        return {
            "light": box(x - length_light/2, y - width_light, x + length_light/2, y),
            "dark": box(x - length_dark/2, y, x + length_dark/2, y + width_dark)
        }
    
    def _get_zone(self, x, y):
        point = Point(x, y)
        for name, region in self.zones.items():
            if region.covers(point):
                # print(f"DEBUG: zone = {name}")
                return name
        # print(f"DEBUG: zone = outside")
        return "dark"
    
    def _get_area_int(self, x: float, y: float, config) -> str:
        x_raw, y_raw = self.transform_dot_to_cm(self.config.p_center)
        dx = x - x_raw
        dy = y - y_raw
        dist = np.sqrt(dx*dx + dy*dy)
        if dist <= config["radius"]:
            return "1"
        return "outer"
    
    def _added_zones(self, st, points):
        points['prev_area'] = points['area'].shift(1)
        valid_transitions = points[
                (points['area'] != points['prev_area']) 
            & (~points['prev_area'].isna())
        ]
            
        visits = valid_transitions[
            ((valid_transitions['area'] == str(1)) & (valid_transitions['prev_area'] == "outer")) |
            ((valid_transitions['area'] == "outer") & (valid_transitions['prev_area'] == str(1)))
        ]
        
        distance = points[points['area'] == str(1)]['distance'].sum()
        time = points[points['area'] == str(1)]['time'].sum()
        speed = points[points['area'] == str(1)]['speed'].sum()
        
        st[f'visits_in_1'] = len(visits)
        st[f'distance_in_1'] = round(distance, 1)
        st[f'time_in_1'] = round(time, 1)
        st[f'speed_in_1'] = round(speed, 1)