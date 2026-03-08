from shapely.geometry import Point
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class BaseAnalyzer:
    def __init__(self, points, config, add_params):
        super().__init__()
        self.points = points
        self.config = config
        self.add_params = add_params
        self.pixel_size = config.pixel_size
        self.cfg = {}
        self.zones = {}

        self.points = self._prepare_points(points)
        self._setting()

    def _setting(self):
        pass
        
    def run(self):
        points = self.points.copy()

        points['zone'] = points.apply(lambda row: self._get_zone(row['xc'], row['yc']), axis=1)
        points['area'] = points.apply(lambda row: self._get_area_int(row['xc'], row['yc'], self.cfg), axis=1)

        stats = {}
        self._calc_distance_and_time(stats, points)
        self._calc_transitions(stats, points)
        self._calc_mean(stats, points)
        self._calc_freeze(stats, points)

        self._added_zones(stats, points.copy())
        self._add_func(stats, points)

        return {
            "stats": stats,
            "points": points,
            "warnings": []
        }
    
    def _add_func(self, stats, points):
        pass

    def _prepare_points(self, points):
        if len(points) < 2:
            return {
            "stats": {},
            "points": points,
            "warnings": ["Недостаточно точек"]
        }

        # Убираем is_hide у точек, в которых модель не определила объект
        points['is_hide'] = (points['xc'] <= 5) & (points['yc'] <= 5)
        
        groups = (points["is_hide"] != points["is_hide"].shift()).cumsum()
        hide_group_sizes = points[points["is_hide"]].groupby(groups).size()
        valid_hide_groups = hide_group_sizes[
            hide_group_sizes >= self.add_params["ThError"]
        ].index.tolist()
        points["is_hide"] = points["is_hide"] & groups.isin(valid_hide_groups)
        
        points['xc'] = points['xc'].where(~points['is_hide'], np.nan)
        points['yc'] = points['yc'].where(~points['is_hide'], np.nan)
        
        points['xc'] = points['xc'].interpolate(limit_area='inside')
        points['yc'] = points['yc'].interpolate(limit_area='inside')
        points['xc'] = points['xc'].ffill()
        points['yc'] = points['yc'].ffill()
        points['xc'] = points['xc'].bfill()
        points['yc'] = points['yc'].bfill()

        points[['xc', 'yc']] *= self.pixel_size

        points['dx'] = points['xc'].diff() 
        points['dy'] = points['yc'].diff()
        points['distance'] = np.hypot(points['dx'], points['dy'])
        points['speed'] = points['distance'] * self.add_params["fps"]
        points['time'] = 1 / self.add_params["fps"]

        points['movement_type'] = pd.cut(
            points['speed'],
            bins=[0, self.add_params["freeze_threshold"], self.add_params["speed_threshold"], np.inf],
            labels=['freeze', 'slow', 'fast'],
            right=False
        ).fillna('freeze')

        # Фильтрация замираний по длительности
        freeze_mask = points['movement_type'] == 'freeze'
        freeze_events = points[freeze_mask].groupby((~freeze_mask).cumsum())
        valid_freezes = [
            event for _, event in freeze_events 
            if len(event) / self.add_params["fps"] >= self.add_params["min_freeze_duration"]
        ]
        for event in valid_freezes:
            points.loc[event.index, 'movement_type'] = 'freeze'

        points[['xc', 'yc', 'dx', 'dy', 'distance', 'speed']] = points[['xc', 'yc', 'dx', 'dy', 'distance', 'speed']].fillna(0)

        return points

    def _get_zone(self, x, y):
        point = Point(x, y)
        for name, region in self.zones.items():
            if region.covers(point):
                # print(f"DEBUG: zone = {name}")
                return name
        # print(f"DEBUG: zone = outside")
        return "outside"
    
    def _get_area_int(self, x: float, y: float, config) -> str:
        points = self.config.p
        for i in range(config["countObject"]):
            x_raw, y_raw = points[i]
            dx = x - x_raw * self.pixel_size
            dy = y - y_raw * self.pixel_size
            dist = np.sqrt(dx*dx + dy*dy)
            if dist <= config["areaInt"]/2:
                return str(i+1)
        return "outer"
    
    def _calc_distance_and_time(self, st, points):
        zone_names = list(self.zones.keys()) + ["outside"]

        for p in ["distance", "time"]:
            total = points[p].sum()
            st[f"total_{p}"] = total

            st[f"{p}_slow"] = points[points['movement_type'] == 'slow']['time'].sum()
            st[f"{p}_fast"] = points[points['movement_type'] == 'fast']['time'].sum()

            for name in zone_names:
                buf = points[points['zone'] == name][p].sum()

                st[f"{p}_{name}"] = buf
                st[f"{p}_{name}_ratio"] = buf / total * 10
                st[f"{p}_slow_{name}"] = points[(points['movement_type'] == 'slow') & (points['zone'] == name)][p].sum()
                st[f"{p}_fast_{name}"] = points[(points['movement_type'] == 'fast') & (points['zone'] == name)][p].sum()

    def _calc_transitions(self, st, points):
        zone_names = list(self.zones.keys()) + ["outside"]
        if len(zone_names) > 1:
            points['prev_zone'] = points['zone'].shift(1)
            points['next_xc'] = points['xc'].shift(-1)
            points['next_yc'] = points['yc'].shift(-1)

            valid_transitions = points[
                (points['zone'] != points['prev_zone']) & 
                (~points['prev_zone'].isna()) &
                (points['next_xc'] != 0) & 
                (points['next_yc'] != 0) &
                (points['xc'] != 0) & 
                (points['yc'] != 0)
            ]
            st['total_transitions'] = len(valid_transitions)

            for i in range(len(zone_names)):
                for j in range(i+1, len(zone_names)):
                    # if prev_zone == zone: continue

                    transitions = valid_transitions[
                        ((valid_transitions['zone'] == zone_names[i]) & (valid_transitions['prev_zone'] == zone_names[j])) |
                        ((valid_transitions['zone'] == zone_names[j]) & (valid_transitions['prev_zone'] == zone_names[i]))
                    ]
                    st[f"transitions_{zone_names[i]}_{zone_names[j]}"] = len(transitions)

    def _calc_mean(self, st, points):
        zone_names = list(self.zones.keys()) + ["outside"]
        moving_points = points[points['movement_type'] != 'freeze']

        for name in zone_names:
            visits = points[points['zone'] == name].groupby((points['zone'] != points['zone'].shift()).cumsum())

            st[f"avg_{name}_distance"] = visits['distance'].sum().mean() if len(visits) > 0 else 0
            st[f"avg_{name}_time"] = visits['time'].sum().mean() if len(visits) > 0 else 0
            st[f"avg_{name}_speed"] = points[points['zone'] == name]['speed'].mean()
            st[f"avg_{name}_speed_no_freeze"] = moving_points[moving_points['zone'] == name]['speed'].mean()

        st['max_speed'] = float(points['speed'].max())
        st['min_speed'] = float(points['speed'].min())

        st['avg_speed'] = points['speed'].mean()
        st['avg_speed_no_freeze'] = moving_points['speed'].mean()

    def _calc_freeze(self, st, points):
        st['freeze_count'] = points[(points['movement_type'] == 'freeze')].shape[0]
        st['freeze_time'] = st['freeze_count'] / self.add_params["fps"]
        st['avg_freeze_time'] = st['freeze_time'] / st['freeze_count'] if st['freeze_count'] > 0 else 0

    def _added_zones(self, st, points):
        count_obj = self.cfg.get("countObject", 0)
        if count_obj > 0:
            points['prev_area'] = points['area'].shift(1)
            valid_transitions = points[
                    (points['area'] != points['prev_area']) 
                    & (~points['prev_area'].isna())
                ]
            
            for i in range(count_obj):
                visits = valid_transitions[
                    ((valid_transitions['area'] == str(i+1)) & (valid_transitions['prev_area'] != str(i+1))) |
                    ((valid_transitions['area'] != str(i+1)) & (valid_transitions['prev_area'] == str(i+1)))
                ]
                
                distance = points[points['area'] == str(i+1)]['distance'].sum()
                time = points[points['area'] == str(i+1)]['time'].sum()
                speed = points[points['area'] == str(i+1)]['speed'].sum()
                
                st[f'visits_in_{i+1}'] = len(visits)
                st[f'distance_in_{i+1}'] = round(distance, 1)
                st[f'time_in_{i+1}'] = round(time, 1)
                st[f'speed_in_{i+1}'] = round(speed, 1)

    def transform_dot_to_cm(self, dot):
        x, y = dot[0]* self.pixel_size, dot[1] * self.pixel_size
        return [x, y]
    
    def draw_zones(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        colors = ['lightblue', 'lightgreen', 'lightcoral']
        alphas = [0.3, 0.4, 0.5]
        
        for (name, zone), color, alpha in zip(self.zones.items(), colors, alphas):
            # Определяем список полигонов для отрисовки
            polygons = [zone] if zone.geom_type == 'Polygon' else zone.geoms
            
            for polygon in polygons:
                x, y = polygon.exterior.xy
                ax.fill(x, y, alpha=alpha, color=color, label=name)
                
                centroid = polygon.centroid
                ax.text(centroid.x, centroid.y, name, 
                        fontsize=10, fontweight='bold', 
                        ha='center', va='center')
        
        # Настройки графика
        ax.set_aspect('equal')
        ax.set_title("Три зоны", fontsize=16)
        ax.set_xlabel("X координата")
        ax.set_ylabel("Y координата")
        ax.grid(True, alpha=0.3)
        
        # Убираем дубли в легенде
        handles, labels = ax.get_legend_handles_labels()
        unique = dict(zip(labels, handles))
        ax.legend(unique.values(), unique.keys())
        
        plt.show()