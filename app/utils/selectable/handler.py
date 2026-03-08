from PySide6.QtCore import Qt, Signal, Qt, Signal, QPoint, QPointF, QObject, QRect, QRectF
from PySide6.QtGui import QPainter, QPen, QColor, QPolygonF, QTransform, QPainterPath, QRegion
import numpy as np

class Handler(QObject):
    def __init__(self, mode):
        super().__init__()
        self.mode = mode

        self.label = None
        self.start_point = None
        self.end_point = None
        self.is_drawing = False

        self.color_areas = QColor(0, 0, 255)
        self.color_crop = QColor(255, 0, 0)
        self.current_color = QColor(0, 0, 255)

        self.scale_factor = 1
        self.offset_x = 0
        self.offset_y = 0
        self.image_path = QPainterPath()

        self.selected_areas = []
        self.crop_area = None
        
    # lifecycle
    def attach(self, label):
        self.label = label

    def detach(self):
        self.start_point = None
        self.end_point = None

    def mouse_press_event(self, event):
        if not self.mode: 
            return
        
        pos = event.position()
        self.start_point = pos
        self.end_point = pos
        self.is_drawing = True

    def mouse_move_event(self, event):
        if not self.is_drawing or self.start_point is None:
            return

        pos = event.position()
        self.end_point = pos
    
    def mouse_release_event(self, event):
        if not self.is_drawing or self.start_point is None:
            return

        pos = event.position()
        self.end_point = pos
        self.is_drawing = False

        polygon = self.create_rect_polygon(
            self.start_point, 
            self.end_point
        )
        
        self.added_polygon(polygon)
        
        self.start_point = None
        self.end_point = None

    def set_mode(self, mode):
        self.mode = mode

    def set_color(self, rgb_values):
        self.color_areas = QColor(*rgb_values)
        self.update_display()
  
    def set_areas(self, crop_area, selected_areas):
        self.crop_area = crop_area
        self.selected_areas = selected_areas

        self.update_display()

    def set_real_size(self, width_, height_):
        if not self.label:
            return

        self.scale_factor = min(self.label.width()/width_, self.label.height()/height_)
        self.width_ = width_ * self.scale_factor
        self.height_ = height_ * self.scale_factor

        self.offset_x = (self.label.width() - self.width_)/2
        self.offset_y = (self.label.height() - self.height_)/2

        self.image_path = QPainterPath()
        self.image_path.addRect(QRectF(self.offset_x, self.offset_y, self.width_, self.height_))
    
    def get_scale(self):
        return self.scale_factor
    
    def get_color(self):
        return (self.color_areas.blue(), self.color_areas.green(), self.color_areas.red())

    def create_rect_polygon(self, p1, p2):
        x1, y1 = p1.x(), p1.y()
        x2, y2 = p2.x(), p2.y()

        left, right = min(x1, x2), max(x1, x2)
        top, bottom = min(y1, y2), max(y1, y2)

        return QPolygonF([
            QPointF(left, top),
            QPointF(right, top),
            QPointF(right, bottom),
            QPointF(left, bottom)
        ])
    
    def added_polygon(self, polygon):
        if self.mode == "select_zone":
            self.selected_areas.append(polygon)
        elif self.mode == "crop_zone":
            self.crop_area = polygon

    def delete_last_area(self):
        if self.selected_areas:
            self.selected_areas.pop()
            self.update_display()
        
    def clear_select_areas(self):
        self.selected_areas.clear()
        self.update_display()

    def clear_crop(self):
        self.crop_area = None
        self.update_display()

    def update_display(self):
        if self.label:
            self.label.update()

    def paint(self, painter: QPainter):
        painter.setClipPath(self.image_path)

        for area in self.selected_areas:
            painter.setPen(QPen(self.color_areas, 2))
            color_alpha = QColor(self.color_areas)
            color_alpha.setAlphaF(0.3)

            painter.setBrush(color_alpha)
            painter.drawPolygon(area)

        if self.crop_area:
            painter.setPen(QPen(self.color_crop, 2))
            color_alpha = QColor(self.color_crop)
            color_alpha.setAlphaF(0.3)

            painter.setBrush(color_alpha)
            painter.drawPolygon(self.crop_area)
        
        if self.is_drawing and self.start_point and self.end_point:
            x1, y1 = self.start_point.x(), self.start_point.y()
            x2, y2 = self.end_point.x(), self.end_point.y()

            qrect = QRect(int(min(x1, x2)), int(min(y1, y2)), int(abs(x2-x1)), int(abs(y2-y1)))
            pen = QPen(self.current_color, 2)
            pen.setStyle(Qt.PenStyle.DashLine)
            painter.setPen(pen)

            color_alpha = QColor(self.current_color)
            color_alpha.setAlphaF(0.3)
            painter.setBrush(color_alpha)
            painter.drawRect(qrect)

    def get_areas(self, is_scaled=False):
        if is_scaled:
            scaled_selected_areas = []
            for area in self.selected_areas:
                clipped_area = self.clip_polygon(area, self.image_path)
                if clipped_area.isEmpty():
                    continue
                pts = np.array([
                    [
                        int((p.x() - self.offset_x) / self.scale_factor),
                        int((p.y() - self.offset_y) / self.scale_factor)
                    ] for p in clipped_area
                ], dtype=np.int32)
                scaled_selected_areas.append(pts)
            
            if self.crop_area:
                clipped_crop = self.clip_polygon(self.crop_area, self.image_path)
                if clipped_crop.isEmpty():
                    scaled_crop_area = None
                else:
                    scaled_crop_area = np.array([
                        [
                            int((p.x() - self.offset_x) / self.scale_factor),
                            int((p.y() - self.offset_y) / self.scale_factor)
                        ] for p in clipped_crop
                    ], dtype=np.int32)
            else:
                scaled_crop_area = None

            return scaled_crop_area, scaled_selected_areas

        return self.crop_area, self.selected_areas

    @staticmethod
    def clip_polygon(polygon: QPolygonF, clip_path: QPainterPath) -> QPolygonF:
        if polygon.isEmpty():
            return QPolygonF()

        poly_path = QPainterPath()
        poly_path.addPolygon(polygon)

        return poly_path.intersected(clip_path).toFillPolygon()
