import numpy as np
import pandas as pd
from .base_analyzer import BaseAnalyzer

class MorrisAnalyzer(BaseAnalyzer):
    def __init__(self, points=None, config=None, add_params=None):
        super().__init__(points, config, add_params)

    def _setting(self):
        morris_config = self.config.morris
        self.morris_config = morris_config

        self.p_center = self.config.p_center
        self.p = self.transform_dot_to_cm(self.config.p)
        self.angle = morris_config["angle"]
        self.r_inner = morris_config["diam"]/2
        self.r_outer = morris_config["space"]/2
        self.platform = morris_config["areaInt"]
        self.custom_fileds_sizes = morris_config["custom_fields"]

        self.zones = {
            'a_inner': None, 
            'b_inner': None,
            'c_inner': None,
            'd_inner': None,
            'a_outer': None, 
            'b_outer': None,
            'c_outer': None,
            'd_outer': None,
        }
        print("DEGUG: Всё настроено")

    def transform_dot_to_cm(self, dots):
        dot_cm = []
        pixel_size = self.pixel_size
        for dot in dots:
            x, y = dot[0]* pixel_size, dot[1] * pixel_size
            dot_cm.append([x, y])

        return dot_cm

    def _get_zone(self, x: float, y: float) -> str:
        # print("DEBUG: кастомный get_zone")
        # Смещение и поворот
        dx = x - self.p_center[0]*self.pixel_size
        dy = -(y - self.p_center[1]*self.pixel_size)  # Инверсия оси Y, если нужно

        dx_rot = dx * np.cos(self.angle) + dy * np.sin(self.angle)
        dy_rot = -dx * np.sin(self.angle) + dy * np.cos(self.angle)
        theta = np.arctan2(dy_rot, dx_rot)

        if theta < 0:
            theta += 2 * np.pi

        # a: [0, π/2)
        # b: [π/2, π)
        # c: [π, 3π/2)
        # d: [3π/2, 2π)
        if 0 <= theta < np.pi / 2:
            quadrant = "a"
        elif np.pi / 2 <= theta < np.pi:
            quadrant = "b"
        elif np.pi <= theta < 3 * np.pi / 2:
            quadrant = "c"
        else:
            quadrant = "d"

        distance = np.hypot(dx, dy)
        if distance <= self.r_inner:
            zone = f"{quadrant}_inner"
        elif distance <= self.r_outer:
            zone = f"{quadrant}_outer"
        else:
            zone = "outside"
        # print(f"DEBUG: zone = {zone}")
        return zone
    
    def _added_zones(self, stats, points):
        pass

    def _get_area_int(self, x, y, config):
        return "outer"
    
    def _add_func(self, stats, points):
        points['cum_dist'] = points['distance'].cumsum()
        points["cum_time"] = points["time"].cumsum()
        x, y = self.p[0]
        points["distance_to_platform"] = np.sqrt((points["xc"] - x)**2 + (points["yc"] - y)**2)
        
        self.baseline_gallagher(stats, points.copy(), self.add_params)
        self.adjusted_gallagher(stats, self.platform/2, points.copy(), self.add_params)
        self.composite_gallagher(stats, self.platform/2, self.custom_fileds_sizes, self.r_outer*2, points.copy(), self.add_params)

        self.calculate_cumulative_error(stats, points.copy(), self.r_outer*2)
        self.calculate_angular_error(stats, points.copy(), self.p[0], self.add_params)
        self.time_in_rect(stats, points.copy(), self.p[0], self.add_params)
        self.count_zone_crossings(stats, points.copy(), self.platform, self.custom_fileds_sizes)
        self.find_escape_latency(stats, points.copy(), self.platform/2) 
        self.calculate_fields_info(stats, points.copy(), self.custom_fileds_sizes, self.add_params)
    
    def _calc_dive(self, st, points):
        groups = (points["is_hide"] != points["is_hide"].shift()).cumsum()
        dive_lengths = points[points["is_hide"]].groupby(groups).size()
        valid_periods = dive_lengths[dive_lengths >= self.add_params["ThError"]]
        dive_count = len(valid_periods)

        st["dive_count"] = dive_count
        st["total_dive_time"] = len(points[points["is_hide"]]) / self.add_params["fps"] if dive_count > 0 else 0
        st["avg_dive_time"] = st["total_dive_time"]/ dive_count if dive_count > 0 else 0

    def baseline_gallagher(self, st, df, add_params):
        """Классический расчёт без учёта радиуса платформы"""

        if add_params["TimeStart"] is not None and add_params["TimeEnd"] is not None:
            df = df[(df["cum_time"] >= add_params["TimeStart"]) & (df["cum_time"] <= add_params["TimeEnd"])]
    
        st["baseline_gallagher"] = df["distance_to_platform"].mean()

    def adjusted_gallagher(self, st, platform_radius, df, add_params):
        """Расчёт с исключением точек в радиусе платформы"""

        df["cum_time"] = df["time"].cumsum()
        if add_params["TimeStart"] is not None and add_params["TimeEnd"] is not None:
            df = df[(df["cum_time"] >= add_params["TimeStart"]) & (df["cum_time"] <= add_params["TimeEnd"])]
        
        filtered = df[df["distance_to_platform"] > platform_radius]

        st["adjusted_gallagher"] = filtered["distance_to_platform"].mean() if not filtered.empty else np.nan

    def composite_gallagher(self, st, platform_radius, zones_radius, space_radius, df, add_params):
        """Взвешенная оценка траектории движения"""

        if add_params["TimeStart"] is not None and add_params["TimeEnd"] is not None:
            df = df[(df["cum_time"] >= add_params["TimeStart"]) & (df["cum_time"] <= add_params["TimeEnd"])]

        conditions = []
        choices = []   

        conditions.append(df['distance_to_platform'] <= platform_radius)
        choices.append('on_platform')

        for i, radius in enumerate(zones_radius):
            conditions.append(df['distance_to_platform'] <= radius)
            choices.append(f'zone_{i}')

        num_zones = len(choices)
        zone_weights = np.linspace(0, 1, num_zones + 1)[1:-1].tolist()

        df['zone_near_plat'] = np.select(conditions, choices, default='far')
        weight_map = {'on_platform': 0.0, **{f'zone_{i}': w for i, w in enumerate(zone_weights)}, 'far': 1.0}
        df['weight'] = df['zone_near_plat'].map(weight_map)
        df['weighted_dist'] = df['distance_to_platform'] * df['weight']

        cgi = df['weighted_dist'].mean() / (space_radius - platform_radius)
        
        st["composite_gallagher"] = cgi
        st["time_in_zones"] = df.groupby('zone_near_plat')['time'].sum().to_dict()

    def calculate_cumulative_error(self, st, df, space_radius):
        """Считает комулятивную ошибку поиска"""
        
        time_intervals = df['time'].clip(lower=0)
        raw_error = (df['distance_to_platform'] * time_intervals).sum()

        total_time = time_intervals.sum()
        max_possible_error = space_radius * total_time
        
        normalized_error = raw_error / max_possible_error if max_possible_error > 0 else 0.0

        st["cumulative_error"] = normalized_error
        
    
    def find_escape_latency(self, st, df, platform_radius):
        """Вычисляет время до первого попадания на платформу"""

        on_platform = df['distance_to_platform'] <= platform_radius
        
        if on_platform.any():
            first_escape_idx = on_platform.idxmax()
            latency = df.loc[first_escape_idx, 'cum_time']
            st["escape_latency"] = latency
        else:
            st["escape_latency"] = None
    
    def count_zone_crossings(self, st, df, platform_diam, zone_diam):
        """Считает количество пересечений границ всех зон интереса"""
        
        all_diam = sorted([platform_diam] + list(zone_diam))
        zone_names = ['on_platform'] + [f'zone_{i}' for i in range(len(zone_diam))] + ['far']
        
        conditions = [(df['distance_to_platform'] <= diam/2) for diam in all_diam]
        
        if len(conditions) != len(zone_names) - 1:
            raise ValueError(
                f"Несоответствие количества условий ({len(conditions)}) и зон ({len(zone_names)}). "
                f"Ожидается {len(zone_names)-1} условий для зон: {zone_names[:-1]}"
            )
        df['current_zone'] = np.select(conditions, zone_names[:-1], default=zone_names[-1])
        df['zone_change'] = df['current_zone'] != df['current_zone'].shift(1)
        crossings = df[df['zone_change']].groupby('current_zone').size().to_dict()

        for zone in zone_names:
            st[zone] = crossings.get(zone, 0)
    
    def time_in_rect(self, st, df, p, add_params):
        points = df[['xc', 'yc']].to_numpy()

        A = np.array(p)
        B = points[0]
        
        AB = B - A  
        L = np.linalg.norm(AB)
        AB_norm = AB / L
        AB_perp = np.array([-AB_norm[1], AB_norm[0]])
        
        AP = points - A
        proj_length = AP.dot(AB_norm)
        proj_width = AP.dot(AB_perp)
        
        mask = (np.abs(proj_length) <= L/2) & (np.abs(proj_width) <= add_params["Thick"]/2)

        st["whishow_error"] = np.sum(mask) / add_params["fps"]

    
    def calculate_angular_error(self, st, df, p, add_params):

        total_dist = df['distance'].sum()

        dist_mask = df['cum_dist'] < add_params["AngleDist"]
        point_dist = df[~dist_mask][['xc', 'yc']].head(1).values.tolist()[0] if any(dist_mask) else None
        
        time_mask = df['cum_time'] < add_params["AngleTime"]
        point_time = df[~time_mask][['xc', 'yc']].iloc[0].tolist() if any(~time_mask) else None
        
        percent_mask = df['cum_dist'] >= total_dist * add_params["AnglePer"]/100
        point_percent = df[percent_mask][['xc', 'yc']].head(1).values.tolist()[0] if any(percent_mask) else None

        point0 = df[['xc', 'yc']].iloc[0].values
        point_plat = np.array(p)
        
        def angle_between_points(A, B, C):
            BA = A - B
            BC = C - B
            dot = np.dot(BA, BC)
            norms = np.linalg.norm(BA) * np.linalg.norm(BC)
            angle_rad = np.arccos(np.clip(dot/norms, -1, 1))
            return np.degrees(angle_rad)  
        
        if point_dist is not None:
            st['angle_error_after_distance'] = angle_between_points(point_plat, point0, point_dist)
        if point_time is not None:
            st['angle_error_after_time'] = angle_between_points(point_plat, point0, point_dist)
        if point_percent is not None:
            st['angle_error_after_percent'] = angle_between_points(point_plat, point0, point_dist)
        
    
    def calculate_fields_info(self, st, df, zones_diam, add_params):
  
        param_names = [f'P{i} {param}' for i in range(1, 7) for param in ['дистанция', 'время', 'скорость']]
        results = {
            'Параметр': param_names,
            't1': [0] * 18,
            't2': [0] * 18,
            't3': [0] * 18
        }
        t0 = add_params["T0"]
        t1 = add_params["T1"]
        t2 = add_params["T2"]
        t3 = add_params["T3"]

        time_masks = {
            't1': (df['cum_time'] >= t0) & (df['cum_time'] <= t1),
            't2': (df['cum_time'] >= t0) & (df['cum_time'] <= t2),
            't3': (df['cum_time'] >= t0) & (df['cum_time'] <= t3)
        }

        for zone_idx, diam in enumerate(zones_diam):
            in_zone = df['distance_to_platform'] <= diam/2
            row_idx = zone_idx * 3

            for time_key, time_mask in time_masks.items():
                combined_mask = time_mask & in_zone
                
                time_in_zone = df.loc[combined_mask, 'time'].sum()
                distance_in_zone = df.loc[combined_mask, 'distance'].sum()
                speed = distance_in_zone / time_in_zone if time_in_zone != 0 else 0

                results[time_key][row_idx] = distance_in_zone
                results[time_key][row_idx + 1] = time_in_zone
                results[time_key][row_idx + 2] = speed

        st["table"] = results