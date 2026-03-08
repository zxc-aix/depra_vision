from PySide6.QtWidgets import QDialog, QLabel, QMessageBox, QSpinBox, QSizePolicy
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Signal, Qt, Slot
import numpy as np

from app.ui.components import UI_FieldSettings 
from app.utils.interaction import InteractionLabel as InteractionLabelClass

class FieldSettingsDialog(QDialog):
    
    mode_size_activated = Signal(str)
    field_type_changed = Signal(str)
    field_param_changed = Signal()

    # Передвижение точек
    move_point_up_clicked = Signal()
    move_point_down_clicked = Signal()
    move_point_left_clicked = Signal()
    move_point_right_clicked = Signal()

    point_selected = Signal(int) # Индекс выбранной точки

    accept = Signal()

    def __init__(self, temp_file):
        super().__init__()
        self.ui = UI_FieldSettings()
        self.ui.setupUi(self)

        self._setup_signals()
        self._elements_settings()
        self._replace_label_with_interaction_label(temp_file)

        self.custom_field_counter = 0
        self.custom_fields = []
        self.MAX_CUSTOM_FIELDS = 6
        # self._scale=1.0

    def _replace_label_with_interaction_label(self, temp_file):
        old_label = self.ui.lblImage
        parent = old_label.parent()
        geometry = old_label.geometry()
        
        new_label = InteractionLabelClass(parent)
        new_label.setObjectName(old_label.objectName())
        new_label.setGeometry(geometry)
        new_label.setAlignment(Qt.AlignCenter)
        
        self.ui.lblImage = new_label
        old_label.hide()
        old_label.deleteLater()
        
        pixmap = self._update_image(temp_file)
        new_label.setPixmap(pixmap)
        new_label.show()

    def _update_image(self, image_path):
        qimage = QImage(image_path)
        if qimage.isNull():
            print(f"Не удалось загрузить изображение: {image_path}")
            return

        pixmap = QPixmap.fromImage(qimage)
        if pixmap.isNull():
            print(f"Не удалось создать QPixmap из изображения: {image_path}")
            return

        scaled_pixmap = pixmap.scaled(
            self.ui.lblImage.width(),
            self.ui.lblImage.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.calculate_scale_value(pixmap, scaled_pixmap)
        self.pixmap_sizes = {
            "label": [self.ui.lblImage.width(), self.ui.lblImage.height()],
            "source": [pixmap.width(), pixmap.height()]
        }
        return scaled_pixmap

    def _elements_settings(self):
        # init
        self.ui.stackedWidget.hide()
        self.ui.spinbSize.setRange(0, 1000)

        # Box
        self.ui.sbBOXCountObject.setRange(0, 13)
        self.ui.sbBOXAreaInt.setRange(0, 300)

        # Morris
        self.ui.lblBaseField_2.setVisible(False)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.ui.sbPlatform.setRange(0, 300)
        self.ui.sbSpace.setRange(1, 400)

        self.ui.tabWidget.setTabText(0, "Область интереса")
        self.ui.tabWidget.setTabText(1, "Разметка")

        self.ui.sbDiam.hide()
        self.ui.lblDiam.hide()

        self.ui.sbDiam.setRange(0, 400)
        self.ui.sbAngle.setRange(-90, 90)

        # Cross
        self.ui.dsbCrossLegthArms.setSingleStep(0.1)
        self.ui.dsbCrossLegthArms.setDecimals(1)
        self.ui.dsbCrossLegthArms.setValue(15)

        self.ui.dsbCrossWidthArms.setSingleStep(0.1)
        self.ui.dsbCrossWidthArms.setDecimals(1)
        self.ui.dsbCrossWidthArms.setValue(4)

        # Ldt
        self.ui.dsbLDTSizePass.setSingleStep(0.1)
        self.ui.dsbLDTradius.setSingleStep(0.1)

        self.ui.dsbLDTLegthArmsLight.setSingleStep(0.1)
        self.ui.dsbLDTLegthArmsLight.setDecimals(1)
        self.ui.dsbLDTLegthArmsLight.setValue(20)

        self.ui.dsbLDTWidthArmsLight.setSingleStep(0.1)
        self.ui.dsbLDTWidthArmsLight.setDecimals(1)
        self.ui.dsbLDTWidthArmsLight.setValue(20)

        self.ui.dsbLDTLegthArmsDark.setSingleStep(0.1)
        self.ui.dsbLDTLegthArmsDark.setDecimals(1)
        self.ui.dsbLDTLegthArmsDark.setValue(20)

        self.ui.dsbLDTWidthArmsDark.setSingleStep(0.1)
        self.ui.dsbLDTWidthArmsDark.setDecimals(1)
        self.ui.dsbLDTWidthArmsDark.setValue(20)
        
        # Ymt
        self.ui.dsbLegthArms.setSingleStep(0.1)
        self.ui.dsbLegthArms.setDecimals(1)
        self.ui.dsbLegthArms.setValue(32.5)

        self.ui.dsbWidthArms.setSingleStep(0.1)
        self.ui.dsbWidthArms.setDecimals(1)
        self.ui.dsbWidthArms.setValue(8.5)

        self.ui.sbAngleArms.setRange(-90, 90)
        self.ui.sblCountObject.setRange(0, 2)

        self.ui.sbYMTalpha1.setRange(0, 360)
        self.ui.sbYMTalpha2.setRange(0, 360)
        self.ui.sbYMTalpha3.setRange(0, 360)

        self.previous_values = [
            self.ui.sbYMTalpha1.value(), 
            self.ui.sbYMTalpha2.value(), 
            self.ui.sbYMTalpha3.value()
        ]
        self.ui.tabWidget_2.setTabText(0, "Markup")
        self.ui.tabWidget_2.setTabText(1, "Angle")

        # Tcs
        self.ui.dsbTCSwidth.setSingleStep(0.1)
        self.ui.dsbTCSwidth.setDecimals(1)
        self.ui.dsbTCSwidth.setRange(0, 300)

        self.ui.dsbTCSlenght.setSingleStep(0.1)
        self.ui.dsbTCSlenght.setDecimals(1)
        self.ui.dsbTCSlenght.setRange(0, 300)

        self.ui.dsbTCSleftlegth.setSingleStep(0.1)
        self.ui.dsbTCSleftlegth.setDecimals(1)
        self.ui.dsbTCSleftlegth.setRange(0, 300)

        self.ui.sbTCSCountObject.setRange(0, 2)

        self.ui.sbTCSAreaInt.setValue(0)
        self.ui.sbTCSAreaInt.setRange(0, 300)

        self.ui.sbTCSSizePass.setRange(0, 300)

    def _setup_signals(self):
        self.ui.btnAccept.clicked.connect(self.accept)
        self.ui.btnReject.clicked.connect(self.reject)

        self.ui.btnUp.clicked.connect(self.move_point_up_clicked)
        self.ui.btnDown.clicked.connect(self.move_point_down_clicked)
        self.ui.btnLeft.clicked.connect(self.move_point_left_clicked)
        self.ui.btnRight.clicked.connect(self.move_point_right_clicked)

        self.ui.cbPoints.currentIndexChanged.connect(self.point_selected)

        self.ui.btnAdd.clicked.connect(self.add_custom_field)
        self.ui.btnRemove.clicked.connect(self.remove_last_custom_field)
        self.ui.btnReset.clicked.connect(self.reset_to_default_fields)
        self.ui.btnResetAngle.clicked.connect(self.reset_to_default_angle)

        self.ui.cbMarkup.currentIndexChanged.connect(self.on_markup_morris)
        self.ui.cbHasDarkRoom.stateChanged.connect(self.has_dark_room)
        
        self.ui.btnScale.clicked.connect(self.mode_size)

        self.ui.cbFieldType.currentTextChanged.connect(self.field_type_changed)

        spinboxes = [
            self.ui.spinb1, self.ui.spinb2, self.ui.spinb3,
            self.ui.sbBOXCountObject, self.ui.sbBOXAreaInt, self.ui.spinbSize,
            self.ui.sbPlatform, self.ui.sbSpace, self.ui.sbDiam, 
            self.ui.sbAngle, self.ui.dsbLDTradius, self.ui.dsbLDTSizePass,
            self.ui.dsbLegthArms, self.ui.dsbWidthArms, self.ui.sbAngleArms,
            self.ui.sblCountObject, self.ui.sblAreaInt, self.ui.dsbTCSwidth,
            self.ui.dsbTCSlenght, self.ui.dsbTCSleftlegth, self.ui.dsbTCSrightlegth,
            self.ui.sbTCSCountObject, self.ui.sbTCSAreaInt, self.ui.sbTCSSizePass,
            self.ui.dsbCrossLegthArms, self.ui.dsbCrossWidthArms, self.ui.dsbLDTLegthArmsLight,
            self.ui.dsbLDTWidthArmsLight, self.ui.dsbLDTLegthArmsDark, self.ui.dsbLDTWidthArmsDark,
        ]
        for sb in spinboxes:
            sb.valueChanged.connect(lambda _: self.field_param_changed.emit())

        self.ui.sbYMTalpha1.valueChanged.connect(lambda v: self.adjust_values(0, v))
        self.ui.sbYMTalpha2.valueChanged.connect(lambda v: self.adjust_values(1, v))
        self.ui.sbYMTalpha3.valueChanged.connect(lambda v: self.adjust_values(2, v))

        comboboxes = [
            self.ui.cbModel, self.ui.cbMarkup
        ]
        for cb in comboboxes:
            cb.currentTextChanged.connect(lambda _: self.field_param_changed.emit())

        checkboxes = [
            self.ui.checkbCenter, self.ui.checkbUp, self.ui.cbHasDarkRoom,
            self.ui.checkbDown, self.ui.checkbRight, self.ui.checkbLeft,
        ]
        for cb in checkboxes:
            cb.stateChanged.connect(lambda _: self.field_param_changed.emit())

    def add_custom_field(self):
        if len(self.custom_fields) >= self.MAX_CUSTOM_FIELDS:
            QMessageBox.warning(self, "Limit", f"Maximum {self.MAX_CUSTOM_FIELDS} fields.")
            return
        label = QLabel(f"Field {self.custom_field_counter + 1}:")
        spinbox = QSpinBox()
        spinbox.setRange(0, 400)
        
        label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        spinbox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        spinbox.valueChanged.connect(self.field_param_changed)

        self.ui.formLayout.addRow(label, spinbox)
        self.custom_fields.append((label, spinbox))
        self.custom_field_counter += 1

        self._update_extra_label_visibility()

    def remove_last_custom_field(self):
        if self.custom_fields:
            label, spinbox = self.custom_fields.pop()

            self.ui.formLayout.removeWidget(label)
            self.ui.formLayout.removeWidget(spinbox)

            label.deleteLater()
            spinbox.deleteLater()

            self.custom_field_counter -= 1

            self.ui.scrollAreaWidgetContents_2.adjustSize()
            self.ui.scrollAreaWidgetContents_2.updateGeometry()
            self.ui.scrollArea.updateGeometry()

            self._update_extra_label_visibility()

    def reset_to_default_fields(self):
        while self.custom_fields:
            self.remove_last_custom_field(self.custom_fields)

        self.ui.scrollAreaWidgetContents_2.adjustSize()
        self.ui.scrollAreaWidgetContents_2.updateGeometry()
        self.ui.scrollArea.updateGeometry()
        self._update_extra_label_visibility()

    def _update_extra_label_visibility(self):
        self.ui.lblBaseField_2.setVisible(bool(self.custom_fields))
        self.field_param_changed.emit()

    def on_markup_morris(self, value):
        if value >= 1:
            self.ui.lblDiam.show()
            self.ui.sbDiam.show()
        else:
            self.ui.lblDiam.hide()
            self.ui.sbDiam.hide()
            self.ui.sbDiam.setValue(0)

    def has_dark_room(self, state):
        self.ui.dsbLDTWidthArmsDark.setEnabled(state)
        self.ui.dsbLDTLegthArmsDark.setEnabled(state)

        if not state:
            self.ui.dsbLDTWidthArmsDark.setValue(0)
            self.ui.dsbLDTLegthArmsDark.setValue(0)

    def mode_size(self):
        self.ui.cbFieldType.setCurrentIndex(0)
        self.mode_size_activated.emit("size")

    def calculate_scale_value(self, original_pixmap: QPixmap, displayed_pixmap: QPixmap):
        if not original_pixmap or not displayed_pixmap:
            return 1.0

        orig_w = original_pixmap.width()
        orig_h = original_pixmap.height()
        label_w = displayed_pixmap.width()
        label_h = displayed_pixmap.height()

        self._scale = min(label_w / orig_w, label_h / orig_h)
        print(f"DEBUG: scale = {self._scale}")

    def get_scale_value(self) -> float:
        return self._scale
    
    def adjust_values(self, changed_index, new_value):
        spinboxes = [self.ui.sbYMTalpha1, self.ui.sbYMTalpha2, self.ui.sbYMTalpha3]
        values = [sb.value() for sb in spinboxes]
        values[changed_index] = new_value
        
        total = sum(values)
        
        if total > 360:
            excess = total - 360
            other_indices = [i for i in range(3) if i != changed_index]
            
            while excess > 0 and any(values[i] > 1 for i in other_indices):
                for i in other_indices:
                    if values[i] > 1 and excess > 0:
                        values[i] -= 1
                        excess -= 1
            
            if excess > 0:
                values[changed_index] -= excess
                if values[changed_index] < 1:
                    values[changed_index] = 1
            
            self.block_signals(True)
            for i, sb in enumerate(spinboxes):
                sb.setValue(values[i])
            self.block_signals(False)
        
        self.previous_values = values.copy()
        self.update_sum_label()
        self.field_param_changed.emit()

    def update_sum_label(self):
        total = sum([self.ui.sbYMTalpha1.value(), 
                     self.ui.sbYMTalpha2.value(), 
                     self.ui.sbYMTalpha3.value()])
        
        color = "green" if total <= 360 else "red"
        self.ui.lblYMTsumAngle.setText(
            f"Сумма углов: <span style='color:{color}; font-weight:bold;'>{total}°</span> / 360°"
        )
        
        if total > 360:
            self.ui.lblYMTsumAngle.setStyleSheet("color: red;")
        else:
            self.ui.lblYMTsumAngle.setStyleSheet("color: black;")

    def block_signals(self, block):
        for spinbox in [self.ui.sbYMTalpha1, self.ui.sbYMTalpha2, self.ui.sbYMTalpha3]:
            spinbox.blockSignals(block)

    def reset_to_default_angle(self):
        self.block_signals(True)
        self.ui.sbYMTalpha1.setValue(0)
        self.ui.sbYMTalpha2.setValue(120)
        self.ui.sbYMTalpha3.setValue(240)
        self.block_signals(False)
        
        self.previous_values = [0, 120, 240]
        self.update_sum_label()
        self.field_param_changed.emit()

    def get_main_data(self, scale=1.0) -> dict:
        return {
            "field_size": self.ui.spinbSize.value() * scale,
            "mode": self.ui.cbFieldType.currentText(),
            "model": self.ui.cbModel.currentText(),
            "sizes": self.pixmap_sizes
        }
    
    def get_box_data(self, scale=1.0) -> dict:
        return {
            "small" : self.ui.spinb1.value() * scale, 
            "medium" : self.ui.spinb2.value() * scale, 
            "large" : self.ui.spinb3.value() * scale,
            "countObject": self.ui.sbBOXCountObject.value(),
            "areaInt": self.ui.sbBOXAreaInt.value() * scale,
        }
    
    def get_cross_data(self, scale=1.0) -> dict:
        return {
            "widthArms": self.ui.dsbCrossWidthArms.value() * scale,
            "lengthArms": self.ui.dsbCrossLegthArms.value() * scale,
            "center" : self.ui.checkbCenter.isChecked(), 
            "up" : self.ui.checkbUp.isChecked(), 
            "right" : self.ui.checkbRight.isChecked(),
            "down" : self.ui.checkbDown.isChecked(), 
            "left" : self.ui.checkbLeft.isChecked(), 
            "outside" : False
        }
    
    def get_morris_data(self, scale=1.0) -> dict:
        return {
            "areaInt": self.ui.sbPlatform.value() * scale,
            "space": self.ui.sbSpace.value() * scale,
            "custom_fields": np.array([spinbox.value() for _, spinbox in self.custom_fields]) * scale,
            "angle": self.ui.sbAngle.value(),
            "diam": self.ui.sbDiam.value() * scale,
            "field_size": self.ui.spinbSize.value() * scale
        }
    
    def get_ldt_data(self, scale=1.0) -> dict:
        return {
            "widthArmsLight": self.ui.dsbLDTWidthArmsLight.value() * scale,
            "lengthArmsLight": self.ui.dsbLDTLegthArmsLight.value() * scale,
            "widthArmsDark": self.ui.dsbLDTWidthArmsDark.value() * scale,
            "lengthArmsDark": self.ui.dsbLDTLegthArmsDark.value() * scale,
            "radius": self.ui.dsbLDTradius.value() * scale,
            "SizePass": self.ui.dsbLDTSizePass.value() * scale,
            "has_dark_room": self.ui.cbHasDarkRoom.isChecked()
        }
    
    def get_ymt_data(self, scale=1.0) -> dict:
        return {
            "widthArms": self.ui.dsbWidthArms.value() * scale,
            "lengthArms": self.ui.dsbLegthArms.value() * scale,
            "angleArms": self.ui.sbAngleArms.value(),
            "countObject": self.ui.sblCountObject.value(),
            "areaInt": self.ui.sblAreaInt.value() * scale,
            "alpha1": self.ui.sbYMTalpha1.value(),
            "alpha2": self.ui.sbYMTalpha2.value(),
            "alpha3": self.ui.sbYMTalpha3.value(),
        }
    
    def get_tcs_data(self, scale=1.0) -> dict:
        return {
            "width": self.ui.dsbTCSwidth.value() * scale,
            "length": self.ui.dsbTCSlenght.value() * scale,
            "length_left": self.ui.dsbTCSleftlegth.value() * scale,
            "length_right": self.ui.dsbTCSrightlegth.value() * scale,
            "countObject": self.ui.sbTCSCountObject.value(),
            "areaInt": self.ui.sbTCSAreaInt.value() * scale,
            "SizePass": self.ui.sbTCSSizePass.value() * scale
        }
    
    def collect(self) -> dict:
        data = {
            "main": self.get_main_data(),
            "mode": {
                "box": self.get_box_data(),
                "cross": self.get_cross_data(),
                "morris": self.get_morris_data(),
                "ldt": self.get_ldt_data(),
                "ymt": self.get_ymt_data(),
                "tcs": self.get_tcs_data(),
            }
        }
        return data
    
    @Slot()
    def show_warning(self, msg):
        QMessageBox.warning(self, "Error", msg)