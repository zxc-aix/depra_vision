import numpy as np
from PySide6.QtGui import QImage, Qt, QPainter, QPolygon, QPen, QColor, QBrush, QFont
from PySide6.QtCore import QPoint, QObject
from .zones_drawer import BoxZoneDrawer, CrossZoneDrawer, MorrisZoneDrawer, YMTZoneDrawer, LDTZoneDrawer, TCSoneDrawer

class AnalysisVisual(QObject):
    def __init__(self, mode, data, settings, config):
        super().__init__()
        self.mode = mode
        self.data = data
        self.settings = settings
        self.config = config
        
    def create_visualization(self):
        target_size = self.data["target_size"]
        image = QImage(target_size, target_size, QImage.Format_ARGB32)
        image.fill(Qt.white)

        painter = QPainter(image)

        self.draw_zones(painter, self.mode)
        self.draw_trajectory(painter)

        painter.end()
        return image

    def draw_zones(self, painter, mode):

        if mode == "box":
            drawer = BoxZoneDrawer(self.data, self.settings, self.config.box)
            # print("DEBUG: box_drawer activated")

        elif mode == "cross":
            drawer = CrossZoneDrawer(self.data, self.settings, self.config.cross)
            # print("DEBUG: cross_drawer activated")

        elif mode == "morris":
            drawer = MorrisZoneDrawer(self.data, self.settings, self.config.morris)
            # print("DEBUG: morris_drawer activated")
        
        elif mode == "ymt":
            drawer = YMTZoneDrawer(self.data, self.settings, self.config.ymt)
            # print("DEBUG: ymt_drawer activated")

        elif mode == "ldt":
            drawer = LDTZoneDrawer(self.data, self.settings, self.config.ldt)
            # print("DEBUG: ldt_drawer activated")
        
        elif mode == "tcs":
            drawer = TCSoneDrawer(self.data, self.settings, self.config.tcs)
            # print("DEBUG: tcs_drawer activated")

        else:
            print(f"Unknown analysis mode: {mode}")
            return

        drawer.draw(painter)
        print("DEBUG: drawer end")

    def draw_trajectory(self, painter):        
        points = []
        is_invalid_flags = []
        data = self.data
        settings = self.settings
        
        for _, row in data["visual_points"].iterrows():
            points.append(QPoint(int(row["xc"]), int(row["yc"])))
            is_invalid_flags.append(row["is_invalid"])

        traj_width = max(0.5, settings["WidthTraj"])
        blue_pen = QPen(QColor(13, 71, 161), traj_width)
        blue_pen.setCosmetic(False)
        red_pen = QPen(QColor(231, 18, 36), traj_width)
        red_pen.setCosmetic(False)
        painter.setPen(blue_pen) 

        flag = settings["DiveTraj"]
        prev_valid = None
        last_before_gap = None  
        invalid_count = 0  
        framess = settings["ThError"] * settings["fps"]
        
        for i, (current, is_invalid) in enumerate(zip(points, is_invalid_flags)):
            if is_invalid:
                invalid_count += 1  
                if prev_valid is not None and flag: 
                    last_before_gap = prev_valid
                prev_valid = None
                continue

            if prev_valid is None and last_before_gap is not None and flag:
                if invalid_count >= framess and self.mode == "morris":
                    
                    painter.setPen(red_pen)  
                else:
                    painter.setPen(blue_pen)  
                painter.drawLine(last_before_gap, current)
                painter.setPen(blue_pen)  
                last_before_gap = None  

            if prev_valid is not None:
                painter.drawLine(prev_valid, current)

            prev_valid = current
            invalid_count = 0

        valid_points = data["visual_points"][~data["visual_points"]["is_invalid"]]

        if not valid_points.empty:
            first_valid_point = QPoint(int(valid_points.iloc[0]["xc"]), 
                                    int(valid_points.iloc[0]["yc"]))
            last_valid_point = QPoint(int(valid_points.iloc[-1]["xc"]), 
                                    int(valid_points.iloc[-1]["yc"]))
        else:
            first_valid_point = last_valid_point = None

        if settings["ShStEn"] and first_valid_point is not None and last_valid_point is not None:
            temp_pen = QPen(QColor(10, 147, 150, 250), 1)
            temp_pen.setCosmetic(False)
            
            painter.setPen(temp_pen)  
            painter.setBrush(QColor(10, 147, 150, 250))  
            
            dot_radius = settings["field_size"] * 0.075 * settings["Scale"]
            painter.drawEllipse(first_valid_point, dot_radius, dot_radius)  
            
            temp_pen = QPen(QColor(192, 0, 0, 250), 1)
            temp_pen.setCosmetic(False)

            painter.setPen(temp_pen)
            painter.setBrush(QColor(192, 0, 0, 250))
            painter.drawEllipse(last_valid_point, dot_radius, dot_radius)

        if settings["BuildBr"] and first_valid_point is not None:
            x_dot, y_dot = data["visual_dots"][0]
            new_point = QPoint(int(x_dot), int(y_dot))

            self._draw_rectangle_with_center_line(painter, first_valid_point, new_point, )

    def _draw_rectangle_with_center_line(self, painter, point1, point2, ):
        width_ = self.settings["Thick"] * self.settings["Scale"]
        points_np = self.find_rectangle_vertices(point1, point2, width_)
        qpoints = [QPoint(int(x), int(y)) for x, y in points_np]

        painter.setBrush(Qt.NoBrush)

        pen_width = max(0.5, self.settings["WidthMarkup"])

        temp_pen = QPen(QColor(33,150,243), pen_width)
        temp_pen.setCosmetic(False)

        painter.setPen(temp_pen)
        polygon = QPolygon(qpoints + [qpoints[0]])
        painter.drawPolygon(polygon)

        temp_pen = QPen(QColor(33,150,243), pen_width, Qt.DashLine)
        temp_pen.setCosmetic(False)
        painter.setPen(temp_pen)
        painter.drawLine(point1, point2)

    @staticmethod
    def find_rectangle_vertices(p1, p2, width):
        M = np.array([int(p1.x()), int(p1.y())])
        N = np.array([int(p2.x()), int(p2.y())])
        
        MN = N - M
        perp = np.array([-MN[1], MN[0]])
        
        perp_normalized = perp / np.linalg.norm(perp)
        offset = (width / 2) * perp_normalized
        
        # Находим вершины
        A = M + offset
        B = M - offset
        D = N + offset
        C = N - offset
        
        return [A, B, C, D]

