from PySide6.QtWidgets import QDialog, QVBoxLayout, QMessageBox, QColorDialog
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QPixmap, QImage, QColor

from app.ui.components import UI_Trimmer
from app.utils.selectable import SelectableLabel

class VideoTrimmerDialog(QDialog):
    mode_changed = Signal(str) 
    color_changed = Signal(tuple)
    delete_zone_clicked = Signal()
    clear_zone_clicked = Signal()
    angle_changed = Signal(float)
    clear_crop_clicked = Signal()
    save_clicked = Signal()

    def __init__(self):
        super().__init__()
        self.ui = UI_Trimmer()
        self.ui.setupUi(self)

        self.image = None
        self.rgb_values = (0, 0, 255)
        self.is_mode_active = False
        
        self._replace_label_with_selectable_label()
        self._elements_settings()
        self._setup_signals()

    def setup_slider(self, slider):
        self.slider = slider
        layout = QVBoxLayout(self.ui.sliderContiner)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.slider)

    def _setup_signals(self):
        self.ui.btnSelectZone.clicked.connect(lambda: self.mode_changed.emit("select_zone"))
        self.ui.btnDeleteZone.clicked.connect(self.delete_zone_clicked)
        self.ui.btnResetSelected.clicked.connect(self.clear_zone_clicked)
        self.ui.dsbAngle.valueChanged.connect(self.angle_changed)
        self.ui.btnCrop.clicked.connect(lambda: self.mode_changed.emit("crop_zone"))
        self.ui.btnResetCrop.clicked.connect(self.clear_crop_clicked)
        self.ui.btnSave.clicked.connect(self.save_clicked)
        self.ui.btnCancel.clicked.connect(self.reject)

    def _elements_settings(self):
        self.ui.lblInfo.setAlignment(Qt.AlignCenter)

        self.ui.frameColor.setLineWidth(2)
        self.ui.frameColor.setStyleSheet(f"border: 1px solid black; background-color: rgb{self.rgb_values};")
        self.ui.frameColor.setCursor(Qt.PointingHandCursor)
        self.ui.frameColor.mousePressEvent = self.choose_color
        self.color_changed.emit(self.rgb_values)

        self.ui.dsbAngle.setRange(-90, 90)
        self.ui.dsbAngle.setDecimals(1)
        self.ui.dsbAngle.setSingleStep(0.1)
        self.ui.dsbAngle.setValue(0.0)

    def _replace_label_with_selectable_label(self):
        old_label = self.ui.lblImage
        parent = old_label.parent()
        geometry = old_label.geometry()
        
        new_label = SelectableLabel(parent)
        new_label.setObjectName(old_label.objectName())
        new_label.setGeometry(geometry)
        new_label.setAlignment(Qt.AlignCenter)
        
        self.ui.lblImage = new_label
        old_label.hide()
        old_label.deleteLater()

    def set_label_info(self, start, end):
        self.ui.lblInfo.setText(f"Start: {start}, End: {end}")
    
    def set_image(self, image):
        h, w, _ = image.shape
        qimage = QImage(image.data, w, h, w * 3, QImage.Format_RGB888)

        
        pixmap = QPixmap.fromImage(qimage)
        
        scaled = pixmap.scaled(
            self.ui.lblImage.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.ui.lblImage.setPixmap(scaled)


    def choose_color(self, event):
        if event.button() == Qt.LeftButton:
            current_color = QColor(*self.rgb_values)
            color = QColorDialog.getColor(current_color, None, "Choose color for zone")
            
            if color.isValid():
                self.rgb_values = (color.red(), color.green(), color.blue())
                self.ui.frameColor.setStyleSheet(f"border: 1px solid black; background-color: rgb{self.rgb_values};")
                self.color_changed.emit(self.rgb_values)

    def get_video_add(self):
        return self.ui.cbVideoAdd.isChecked()

    @Slot(str)
    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

    @Slot(str)
    def show_warning(self, msg: str):
        QMessageBox.warning(self, "Warning", msg)

    @Slot(str)
    def show_info(self, msg: str):
        QMessageBox.information(self, "Success", msg)

