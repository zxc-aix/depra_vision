from app.utils.interaction.modes.base_mode import BaseModeHandler
from PySide6.QtGui import QPainter

class DefaultHandler(BaseModeHandler):

    def __init__(self):
        super().__init__()

    def on_mouse_press(self, event):
        pass
    def paint(self, painter: QPainter):
        pass
