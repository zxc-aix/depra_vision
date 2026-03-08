from PySide6.QtCore import Qt, Signal, QPoint, QPointF, QObject
from PySide6.QtGui import QPainter, QPen, QFont

class BaseModeHandler(QObject):
    points_changed = Signal()
    selection_changed = Signal(int)

    def __init__(self):
        super().__init__()
        self.label = None
        self.points: list[QPointF] = []
        self.points_restored: list[tuple] = []
        self.params: dict = {}
        self.selected_index = 0
        self.MAX_POINTS = 10
        self._scale = 1.0
        
    # lifecycle
    def attach(self, label):
        self.label = label

    def detach(self):
        self.points = []
        self.label = None

    # params
    def set_params(self, params: dict):
        self.params.update(params)

    def set_max_points(self, max_points: int):
        self.MAX_POINTS = max_points

    def set_points(self, points_updated: list[QPointF]):
        self.points = points_updated

    def set_points_restored(self, points: list):
        if points:
            self.points_restored = [QPointF(x, y) for x, y in points]

    # def dump(self) -> dict:
    #     return {
    #         "points": [(p.x(), p.y()) for p in self.points],
    #         "params": self.params.copy(),
    #     }

    # mouse events
    def mouse_press_event(self, event):
        self.on_mouse_press(event)

    # input
    def on_mouse_press(self, event):
        # print("ModeHandler: on_mouse_press")
        if self.label is None or len(self.points) >= self.MAX_POINTS:
            return

        pos = event.position()
        self.points.append(QPointF(pos.x(), pos.y()))
        print(f"ModeHandler: добавлена точка ({pos.x()}, {pos.y()})")

        self.points_changed.emit()

    def get_points(self) -> list[QPointF]:
        return self.points

    # painting
    def paint(self, painter: QPainter):
        self.paint_additional(painter)
        pen = QPen(Qt.black, 4)
        painter.setPen(pen)
        for i, pos in enumerate(self.points):
            painter.drawPoint(pos)
            
            font_metrics = painter.fontMetrics()
            text = str(i+1)
            text_width = font_metrics.horizontalAdvance(text)
            text_height = font_metrics.height()
            text_x = pos.x() - text_width / 2
            text_y = pos.y() - text_height / 4 
            painter.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            painter.drawText(int(text_x), int(text_y), text)
    
    def paint_additional(self, painter: QPainter):
        pass

    # selection
    def select(self, index: int):
        if 0 <= index < len(self.points):
            self.selected_index = index
            self.selection_changed.emit(index)
            self.label.update()

    def move_selected(self, dx=0, dy=0):
        if self.selected_index is not None and self.points:
            pos = self.points[self.selected_index]
            new_pos = QPoint(pos.x() + dx, pos.y() + dy)
            self.points[self.selected_index] = new_pos
            self.points_changed.emit()
            self.label.update()

    def update_display(self):
        if self.label:
            self.label.update()
