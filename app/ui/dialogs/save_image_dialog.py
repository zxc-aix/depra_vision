from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, Slot

from app.ui.components import UI_SaveSettings

class SaveImgaeDialog(QDialog):
    def __init__(self, image, file_dir, base_name="picture"):
        super().__init__()
        self.ui = UI_SaveSettings()
        self.ui.setupUi(self)

        self.base_name = base_name
        self._setup_controls()
        self._init_variables(image, file_dir)
    
    def _setup_controls(self):
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnSave.clicked.connect(self.save_file)
        self.ui.btnInput.clicked.connect(self.browse_folder)

        self.ui.btnSave.setEnabled(False)

        self.ui.sbSizeLeft.setRange(100, 2000)
        self.ui.sbSizeLeft.setValue(1000)
        self.ui.sbSizeRight.setRange(100, 2000)
        self.ui.sbSizeRight.setValue(1000)
        self.ui.sbDPI.setRange(100, 1500)
        self.ui.sbDPI.setValue(600)


    def _init_variables(self, image, file_dir):
        self.file_dir = file_dir
        self.image = image
        self.file_path = None


    def browse_folder(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save image",
            self.file_dir + "/" + self.base_name + ".png",
            "PNG Files (*.png);;All Files (*)"
        )
        if file_path:  
            self.ui.leFilePath.setText(file_path)
            self.file_path = file_path

            self.ui.btnSave.setEnabled(True)

    def save_file(self):
        size_w = self.ui.sbSizeLeft.value()
        size_h = self.ui.sbSizeRight.value()
        dpi = self.ui.sbDPI.value()

        image_scaled = self.image.scaled(
            size_w,
            size_h,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        image_scaled.setDotsPerMeterX(int(dpi * 39.37))  
        image_scaled.setDotsPerMeterY(int(dpi * 39.37))

        if self.file_path:
            if not self.file_path.lower().endswith('.png'):
                self.file_path += '.png'
                
            success = image_scaled.save(self.file_path, "PNG")
            if success:
                self.show_info("Image saved successfully")
            else:
                self.show_error("Failed to save image")
        
        self.close()

    @Slot(str)
    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

    @Slot(str)
    def show_warning(self, msg: str):
        QMessageBox.warning(self, "Warning", msg)

    @Slot(str)
    def show_info(self, msg: str):
        QMessageBox.information(self, "Success", msg)


    